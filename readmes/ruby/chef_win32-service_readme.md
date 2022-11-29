# win32-service

[![Gem Version](https://badge.fury.io/rb/win32-service.svg)](https://badge.fury.io/rb/win32-service)

The win32-service library allows you to control or create MS Windows services.

## Installation

gem install win32-service

## Usage

```ruby
require 'win32/service'

# Iterate over the available services
Win32::Service.services do |service|
  p service
end
```

## More Documentation

Please see the documentation in the 'doc' directory, or the gem documentation that was installed when you installed this library as a gem.

## Known Issues

### Problem:

Service.delete causes "Unable to delete: The specified service has been marked for deletion."

### Troubleshooting:

This can be caused by one of two things. Either you attempted to delete a running service without stopping it first, or you have the Services Administrative Tool (GUI) open. In the former case, the solution is to first stop the service if it's running. In the latter, close the Services GUI admin tool before deleting.

### Problem:

Service.start causes, "The service did not respond to the start or control request in a timely fashion."

### Troubleshooting:

The best way to debug your services is to wrap your entire Daemon subclass in a begin/end block and send error messages to a file. That should give a good clue as to the nature of the problem. The most probable culprits are:

- You forgot to require 'win32/daemon' in your Daemon code.

- You've tried to require a library that's not in your $LOAD_PATH. Make sure that your require statements are inside the begin/rescue block so that you can easily find those mistakes.

- Your have a bad binary path name. Be sure to use an absolute path name for the binary path name, including the full path to the Ruby interpreter, e.g. 'c:\ruby\bin\ruby' instead of just 'ruby'.

- You've got a syntax error in your code somewhere.

## See Also

ruby-wmi

## Future Plans

Add service_session_change hook

## Copyright

(C) 2003-2018, Daniel J. Berger, All Rights Reserved

## License

Artistic 2.0

## Warranty

This package is provided "as is" and without any express or implied warranties, including, without limitation, the implied warranties of merchantability and fitness for a particular purpose.

## Authors

- Daniel J. Berger
- Park Heesob
