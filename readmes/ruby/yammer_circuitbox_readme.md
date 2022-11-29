# Circuitbox

![Tests](https://github.com/yammer/circuitbox/workflows/Tests/badge.svg) [![Gem Version](https://badge.fury.io/rb/circuitbox.svg)](https://badge.fury.io/rb/circuitbox)

Circuitbox is a Ruby circuit breaker gem. It protects your application from failures of its service dependencies. It wraps calls to external services and monitors for failures in one minute intervals. Once more than 10 requests have been made with a 50% failure rate, Circuitbox stops sending requests to that failing service for one minute. This helps your application gracefully degrade.
Resources about the circuit breaker pattern:
* [http://martinfowler.com/bliki/CircuitBreaker.html](http://martinfowler.com/bliki/CircuitBreaker.html)
* [https://github.com/Netflix/Hystrix/wiki/How-it-Works#CircuitBreaker](https://github.com/Netflix/Hystrix/wiki/How-it-Works#CircuitBreaker)

## Usage

```ruby
Circuitbox.circuit(:your_service, exceptions: [Net::ReadTimeout]) do
  Net::HTTP.get URI('http://example.com/api/messages')
end
```

Circuitbox will return nil for failed requests and open circuits.
If your HTTP client has its own conditions for failure, you can pass an `exceptions` option.

```ruby
class ExampleServiceClient
  def circuit
    Circuitbox.circuit(:yammer, exceptions: [Zephyr::FailedRequest])
  end

  def http_get
    circuit.run(exception: false) do
      Zephyr.new("http://example.com").get(200, 1000, "/api/messages")
    end
  end
end
```

Using the `run` method will throw an exception when the circuit is open or the underlying service fails.

```ruby
  def http_get
    circuit.run do
      Zephyr.new("http://example.com").get(200, 1000, "/api/messages")
    end
  end
```

## Global Configuration
Circuitbox has defaults for circuit_store and notifier.
This can be configured through ```Circuitbox.configure```.
The circuit cache used by ```Circuitbox.circuit``` will be cleared after running ```Circuitbox.configure```.
This means when accessing the circuit through ```Circuitbox.circuit``` any custom configuration options should always be given.

Any circuit created manually through ```Circuitbox::CircuitBreaker``` before updating the configuration
will need to be recreated to pick up the new defaults.

```ruby
  Circuitbox.configure do |config|
    config.default_circuit_store = Circuitbox::MemoryStore.new
    config.default_notifier = Circuitbox::Notifier::Null.new
  end
```


## Per-Circuit Configuration

```ruby
class ExampleServiceClient
  def circuit
    Circuitbox.circuit(:your_service, {
      # exceptions circuitbox tracks for counting failures (required)
      exceptions:       [YourCustomException],

      # seconds the circuit stays open once it has passed the error threshold
      sleep_window:     300,

      # length of interval (in seconds) over which it calculates the error rate
      time_window:      60,

      # number of requests within `time_window` seconds before it calculates error rates (checked on failures)
      volume_threshold: 10,

      # the store you want to use to save the circuit state so it can be
      # tracked, this needs to be Moneta compatible, and support increment
      # this overrides what is set in the global configuration
      cache: Circuitbox::MemoryStore.new,

      # exceeding this rate will open the circuit (checked on failures)
      error_threshold:  50,

      # Customized notifier
      # overrides the default
      # this overrides what is set in the global configuration
      notifier: Notifier.new
    })
  end
end
```

You can also pass a Proc as an option value which will evaluate each time the circuit breaker is used. This lets you configure the circuit breaker without having to restart the processes.

```ruby
Circuitbox.circuit(:yammer, {
  sleep_window: Proc.new { Configuration.get(:sleep_window) },
  exceptions: [Net::ReadTimeout]
})
```

## Circuit Store (:cache)

Holds all the relevant data to trip the circuit if a given number of requests
fail in a specified period of time. Circuitbox also supports
[Moneta](https://github.com/minad/moneta). As moneta is not a dependency of circuitbox
it needs to be loaded prior to use. There are a lot of moneta stores to choose from but
some pre-requisits need to be satisfied first:

- Needs to support increment, this is true for most but not all available stores.
- Needs to support expiry.
- Needs to support concurrent access if you share them. For example sharing a
  KyotoCabinet store across process fails because the store is single writer
  multiple readers, and all circuits sharing the store need to be able to write.


## Notifications

Circuitbox has two built in notifiers, null and active support.
The active support notifier is used if `ActiveSupport::Notifications` is defined when circuitbox is loaded.
If `ActiveSupport::Notifications` is not defined the null notifier is used.
The null notifier does not send notifications anywhere.

The default notifier can be changed to use a specific built in notifier or a custom notifier when [configuring circuitbox](#global-configuration).

### ActiveSupport
Usage example:

**Circuit open/close:**

```ruby
ActiveSupport::Notifications.subscribe('open.circuitbox') do |_name, _start, _finish, _id, payload|
  circuit_name = payload[:circuit]
  Rails.logger.warn("Open circuit for: #{circuit_name}")
end
ActiveSupport::Notifications.subscribe('close.circuitbox') do |_name, _start, _finish, _id, payload|
  circuit_name = payload[:circuit]
  Rails.logger.info("Close circuit for: #{circuit_name}")
end
```

**Circuit run:**

```ruby
ActiveSupport::Notifications.subscribe('run.circuitbox') do |*args|
  event = ActiveSupport::Notifications::Event.new(*args)
  circuit_name = event.payload[:circuit_name]
  
  Rails.logger.info("Circuit: #{circuit_name} Runtime: #{event.duration}")
end
```

**Circuit Warnings:**
In case of misconfiguration, circuitbox will fire a `warning.circuitbox`
notification.

```ruby
ActiveSupport::Notifications.subscribe('warning.circuitbox') do |_name, _start, _finish, _id, payload|
  circuit_name = payload[:circuit]
  warning      = payload[:message]
  Rails.logger.warning("Circuit warning for: #{circuit_name} Message: #{warning}")
end

```

## Faraday

Circuitbox ships with [Faraday HTTP client](https://github.com/lostisland/faraday) middleware.

```ruby
require 'faraday'
require 'circuitbox/faraday_middleware'

conn = Faraday.new(:url => "http://example.com") do |c|
  c.use Circuitbox::FaradayMiddleware
end

response = conn.get("/api")
if response.success?
  # success
else
  # failure or open circuit
end
```

By default the Faraday middleware returns a `503` response when the circuit is
open, but this as many other things can be configured via middleware options

* `default_value` value to return for open circuits, defaults to 503 response
  wrapping the original response given by the service and stored as
  `original_response` property of the returned 503, this can be overwritten
  with either
  * a static value
  * a `lambda` which is passed the `original_response` and `original_error`.
    `original_response` will be populated if Faraday returns an error response,
    `original_error` will be populated if an error was thrown before Faraday
    returned a response.

```ruby
c.use Circuitbox::FaradayMiddleware, default_value: lambda { |response, error| ... }
```

* `identifier` circuit id, defaults to request url

```ruby
c.use Circuitbox::FaradayMiddleware, identifier: "service_name_circuit"
```

* `circuit_breaker_options` options to initialize the circuit with defaults to
  `{ exceptions: Circuitbox::FaradayMiddleware::DEFAULT_EXCEPTIONS }`.
  Accepts same options as Circuitbox:CircuitBreaker#new

```ruby
c.use Circuitbox::FaradayMiddleware, circuit_breaker_options: {}
```

* `open_circuit` lambda determining what response is considered a failure,
  counting towards the opening of the circuit

```ruby
c.use Circuitbox::FaradayMiddleware, open_circuit: lambda { |response| response.status >= 500 }
```

## Installation

Add this line to your application's Gemfile:

    gem 'circuitbox'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install circuitbox

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
