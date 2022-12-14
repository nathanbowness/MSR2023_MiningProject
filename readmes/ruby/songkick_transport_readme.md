= Songkick::Transport {<img src="https://secure.travis-ci.org/songkick/transport.png?branch=master" />}[http://travis-ci.org/songkick/transport]

This is a transport layer abstraction for talking to our service APIs. It
provides an abstract HTTP-like interface while hiding the underlying transport
and serialization details. It transparently deals with parameter serialization,
including the following:

* Correctly CGI-escaping any data you pass in
* Nested parameters, e.g. <tt>'foo' => {'a' => 'b', 'c' => 'd'}</tt> becomes
  <tt>foo[a]=b&foo[c]=d</tt>
* File uploads and multipart requests
* Entity body for POST/PUT, query string for everything else

We currently support three backends:

* Talking HTTP with {Curb}[http://curb.rubyforge.org/]
* Talking HTTP with {HTTParty}[http://httparty.rubyforge.org/]
* Talking directly to a {Rack}[http://rack.rubyforge.org/] app with Rack::Test

If the service you're talking to returns <tt>Content-Type: application/json</tt>,
we automatically parse the response for you. You can register parsers for other
content types as described below.


== Using the transports

Let's say you're running a {Sinatra}[http://www.sinatrarb.com/] application that
exposes some JSON:

    require 'sinatra'
    
    get '/ohai' do
      headers 'Content-Type' => 'application/json'
      '{"hello":"world"}'
    end

In order to talk to this service, you select a transport to use and make the
request:

    require 'songkick/transport'
    Transport = Songkick::Transport::Curb
    
    client = Transport.new('http://localhost:4567',
                           :user_agent => 'Test Agent',
                           :timeout    => 5)
    
    response = client.get('/ohai')
    # => Songkick::Transport::Response::OK
    
    response.data
    # => {"hello" => "world"}

<tt>Songkick::Transport::Curb</tt> and <tt>Songkick::Transport::HttParty</tt>
both take a hostname on instantiation. <tt>Songkick::Transport::RackTest</tt>
takes a reference to a Rack application, for example:

    require 'songkick/transport'
    Transport = Songkick::Transport::RackTest
    
    client = Transport.new(Sinatra::Application,
                           :user_agent => 'Test Agent',
                           :timeout    => 5,
                           :basic_auth => {:username => "foo", :password => "bar"})

All transports expose exactly the same instance methods.

The client supports the +delete+, +get+, +head+, +patch+, +post+, +put+ and
+options+ methods, which all take a path and an optional +Hash+ of parameters,
for example:

    client.post('/users', :username => 'bob', :password => 'foo')

If the response is successful, meaning there are no errors caused by the server-
or client-side software or the network between them, then a response object is
returned. If the response contains data, the object's +data+ method exposes it
as a parsed data structure.

The response's headers are exposed through the +headers+ method, which is an
immutable hash-like object that normalizes various header conventions.

    response = client.get('/users')
    
    # These all return 'application/json'
    response.headers['Content-Type']
    response.headers['content-type']
    response.headers['HTTP_CONTENT_TYPE']

If there is an error caused by our software, the request returns +nil+ and an
error is logged. If there is an error caused by user input, a +UserError+
response is returned with +data+ and +errors+ attributes.


=== Response conventions

This library was primarily developed to talk to Songkick's backend services, and
as such adopts some conventions that put it at a higher level of abstraction
than a vanilla HTTP client.

A response object has the following properties:

* +body+ -- the raw response body
* +data+ -- the result of parsing the body according to its content-type
* +headers+ -- a read-only hash-like object containing response headers
* +status+ -- the response's status code

Only responses with status codes, 200 (OK), 201 (Created), 204 (No Content), and
409 (Conflict) yield response objects. All other status codes cause an exception
to be raised. We use 409 to indicate user error, i.e. input validation errors as
opposed to software/infrastructure errors. The response object is typed for the
status code; the possible types are:

* 200: <tt>Songkick::Transport::Response::OK</tt>
* 201: <tt>Songkick::Transport::Response::Created</tt>
* 204: <tt>Songkick::Transport::Response::NoContent</tt>
* 409: <tt>Songkick::Transport::Response::UserError</tt>

If the request raises an exception, it will be of one of the following types:

* <tt>Songkick::Transport::UpstreamError</tt> -- generic base error type
* <tt>Songkick::Transport::HostResolutionError</tt> -- the hostname could be
  resolved using DNS
* <tt>Songkick::Transport::ConnectionFailedError</tt> -- a TCP connection could
  not be made to the host
* <tt>Songkick::Transport::TimeoutError</tt> -- the request timed out before a
  response could be received
* <tt>Songkick::Transport::InvalidJSONError</tt> -- the response contained
  invalid JSON
* <tt>Songkick::Transport::HttpError</tt> -- we received a response with a
  non-successful status code, e.g. 404 or 500

It is possible to customise the status codes which are treated as UserError
when initializing the client. Requests responding with any of the provided 
status codes will then yield a response object with error details, rather than
raising an exception;

    client = Transport.new('http://localhost:4567',
                           :user_error_codes => [409, 422])


=== Registering response parsers

<tt>Songkick::Transport</tt> automatically sets <tt>response.data</tt> if the
content-type of the response is <tt>application/json</tt>. You can register
parsers for other content-types like so:

    Songkick::Transport.register_parser('application/yaml', YAML)

The parser object you register must respond to <tt>parse(string)</tt>.

You can also register a default parser, to handle all content types that don't have a specified parser.

    Songkick::Transport.register_default_parser(DefaultParser)


=== Nested parameters

All transports support serialization of nested parameters, for example you can
send this:

    client.post('/venues', :venue => {:name => 'HMV Forum', :city_id => 4})

and it will send this query string to the server:

    venue[name]=HMV+Forum&venue[city_id]=4

It can serialize fairly complicated data structures, within the limits of what
can represented using query strings, for example this structure:

    { "lisp" => ["define", {"square" => ["x", "y"]}, "*", "x", "x"] }

is serialized as:

    lisp[]=define&lisp[][square][]=x&lisp[][square][]=y&lisp[]=%2A&lisp[]=x&lisp[]=x

Rails and Sinatra will parse this back into the original data structure for you
on the server side.


=== Request headers, timeouts and basic auth

You can make requests with custom headers using +with_headers+. The return value
of +with_headers+ works just like a client object, so you can use it for
multiple requests:

    auth = client.with_headers('Authorization' => 'OAuth abc123')
    auth.get('/me')
    auth.put('/users/99', :username => 'bob')

Note that +with_headers+ will normalize Rack-style headers for easy forwarding
of input from the front end. For example, +HTTP_USER_AGENT+ is converted to
<tt>User-Agent</tt> in the outgoing request.

Similarly, the request timeout can be adjusted per-request:

    client.with_timeout(10).get('/slow_resource')

Likewise basic auth credentials:

    client.with_basic_auth({:username => "foo", :password => "bar"}).get('/')


=== File uploads

File uploads are handled transparently for you by the +post+ and +put+ methods.
If the value of any parameter (including parameters nested inside hashes) is of
type <tt>Songkick::Transport::IO</tt>, the whole request will be treated as
<tt>multipart/form-data</tt> and all the data will be serialized for you.

<tt>Songkick::Transport::IO</tt> must be instantiated with an IO object, a mime
type, and a filename, for example:

    file = File.open('concerts.xml')
    io = Songkick::Transport::IO.new(file, 'application/xml', 'concerts.xml')
    client.post('/inventories', :inventory => io)
    file.close

The file upload can be mixed with normal textual data, and nested hashes, for
example:

    client.post('/inventories', :inventory => {:file => io, :date => '2012-03-01'})

On Sinatra, you get a hash containing both the tempfile and some metadata. You
can use this to construct an +IO+ to forward to another service. The complete
params look like:

    {
      :inventory => {
        :file => {
          :name     => "inventory[file]",
          :filename => "concerts.xml",
          :type     => "application/xml",
          :tempfile => #<File:/tmp/RackMultipart20120301-31254-15b6o5r-0>,
          :head     => "Content-Disposition: form-data; name=\"inventory[file]\"; filename=\"concerts.xml\"\r\nContent-Length: 6694\r\nContent-Type: application/xml\r\nContent-Transfer-Encoding: binary\r\n"
        }
        :date => "2012-03-01"
      }
    }
    
    file = params[:inventory][:file]
    io = Songkick::Transport::IO.new(file[:tempfile], file[:type], file[:filename])

On Rails 2, you just get a tempfile, but it has some additional methods to get
what you need. The params look like this:

    {
      "inventory" => {
        "file" => #<File:/tmp/CGI20120301-32754-gzgzdy-0>,
        "date" => "2012-03-01"
      }
    }
    
    file = params["inventory"]["file"]
    io = Songkick::Transport::IO.new(file, file.content_type, file.original_filename)

<tt>Songkick::Transport</tt> has a helper for turning both these upload object
types into an <tt>IO</tt> for you:

    io = Songkick::Transport.io(params[:inventory][:file])

You can then use this to forward uploaded files to another service from your
Rails or Sinatra application.

=== Logging, instrumentation and reporting

You can enable basic logging by supplying a logger and switching logging on.

    Songkick::Transport.logger = Logger.new(STDOUT)
    Songkick::Transport.verbose = true

The default setting (before you set <tt>Songkick::Transport.verbose = true</tt>
is that Transport will warn you about all errors, i.e. any request that raises
an exception. With <tt>verbose = true</tt>, it also logs the details of every
request made; it logs the requests using a format you can paste into a +curl+
command, and logs the status code, data and duration of every response.

There may be params you don't want in your logs, and you can specify those:

    Songkick::Transport.sanitize 'password', /access_token/

This method accepts both strings and regexes. Any parameter name (as serialized
in a query string) that matches one of these will be logged as e.g.
<tt>password=[REMOVED]</tt>.

It also sanitizes custom headers that are put in the logs, so you might want to
exclude headers used for authentication:

    Songkick::Transport.sanitize /Authorization/i, /Cookie/i

There is also a more advanced reporting system that lets you aggregate request
statistics. During a request to a web application, many requests to backend
services may be involved. The reporting system lets you collect information
about all the backend requests that happened while executing a block. For
example you can use it to create a logging middleware:

    class Reporter
      def initialize(app)
        @app = app
      end

      def call(env)
        report = Songkick::Transport.report
        response = report.execute { @app.call(env) }
        # write report details somewhere
        response
      end
    end

The +report+ object is an array-like object that contains data for all the
requests made during the block's execution. Each request responds to the
following API:

* +endpoint+ -- The origin the request was sent to
* +verb+ -- The HTTP method of the request, e.g. <tt>"get"</tt>
* +path+ -- The requested path
* +params+ -- The hash of parameters used to make the request
* +response+ -- The response object the request returned
* +error+ -- The exception the request raised, if any
* +duration+ -- The request's duration in milliseconds

The +report+ object itself also responds to +total_duration+, which gives you
the total time spent calling backend services during the block.

To instrument transports using the `ActiveSupport::Notifications` API, pass
`{:instrumenter => ActiveSupport::Notifications}` in the options. You can also
override the default event label of `http.songkick_transport` by passing
`:instrumentation_label`.

== Writing Service classes

`Songkick::Transport::Service` is a class to make writing service clients more convenient.

Set up config globally (perhaps in a Rails initializer):

    Songkick::Transport::Service.set_endpoints("blah-service" => "of1-dev-services:2347")
    Songkick::Transport::Service.user_agent "myproject"
    Songkick::Transport::Service.timeout 60 #??optional, default is 10

Subclass to create service clients:

    class BlahService < Songkick::Transport::Service
      endpoint "blah-service"

      # these global configs can also be set at the class level, in which case they
      #??override the global config
      user_agent "myproject mainservice class"
      timeout 10

      def get_data
        http.get("/stuff", :search => "name")
      end
    end

The default transport layer for clients inheriting from `Songkick::Transport::Service`
is Curb, if you want to use something else you can override it globally or in a class
with:

    transport_layer Songkick::Transport::HttParty

You can specify extra headers to be sent with every request from a service class and
from the root class, and they are merged together:

    Songkick::Transport::Service.with_headers "rlah" => "1"

    class BlahService < Songkick::Transport::Service
      with_headers "blah" => "1"
    end

    class FlahService < BlahService
      with_headers "flah" => "1"

      def get_data
        http.get("/stuff") # will have headers "rlah", "blah" and "flah"
      end
    end

To pass extra, perhaps transport-specific, options hashes to the transport
layer on initialize, specify them with:

    class FooService < Songkick::Transport::Service
      transport_layer Songkick::Transport::Curb
      transport_layer_options :no_signal => true
    end

These are also inheritable, and merge down like extra headers do.

== License

The MIT License

Copyright (c) 2012-2015 Songkick

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
