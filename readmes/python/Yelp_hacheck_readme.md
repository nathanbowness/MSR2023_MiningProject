[![Build Status](https://travis-ci.org/Yelp/hacheck.png)](https://travis-ci.org/Yelp/hacheck)

**hacheck** is a healthcheck-proxying service. It listens on port 3333, speaks HTTP, and has the following API:

    GET /<protocol>/<service_name>/<port>/<query>

This will check the following locations for service state:

 * `/var/spool/hacheck/all`
 * `/var/spool/hacheck/<service_name>`
 * Depending on the value of `<protocol>`:
  * if `http`: `http://localhost:<port>/<query>`
  * if `tcp`: will attempt to connect to port `<port>` on localhost. `<query>` is currently ignored
  * if `spool`: will only check the spool state
  * if `mysql` and the `mysql_username` and `mysql_password` are set, will do a login and quit on the requested mysql port; `<query>` is ignored and no logical database is selected.

When it does query the actual service check endpoint, **hacheck** MAY cache the value of that query for some amount of time

**hacheck** also comes with the command-line utilities `haup`, `hadown`, and `hastatus`. These take a service name and manipulate the spool files, allowing you to pre-emptively mark a service as "up" or "down".

### Yelp/hacheck versus uber/hacheck

This software was originally developed by [Uber](https://github.com/uber/hacheck).
This version has several features not present in the upstream version:

* By setting the `allow_remote_spool_changes` flag in the config file, it becomes possible to POST changes to spool
  status remotely.
  This is useful if there is some software, like [Paasta](https://github.com/Yelp/paasta), making decisions centrally about when
  to kill tasks.
* If the client sends the header `X-Haproxy-Server-State`, then we use the port specified in that header and ignore the
  port in the URL. We also use the host address specified in this header instead of localhost.
  This is useful for configurations where an HAProxy has a backend with many servers running on different ports, such
  as when your tasks are running under [Marathon](https://github.com/mesosphere/marathon). Or if the backends have different
  IPs such as Pods running on Kubernetes.
* If the client sends `X-Nerve-Check-IP`, then we use the IP specified here to check against (rather than the default
  of localhost). This is again useful for Kubernetes Pods where we want to healthcheck with [Nerve](https://github.com/airbnb/nerve)
  from the hosts network namespace but each Pod runs with its own IP.
* Spool files(downtimes) can optionally have expirations, and store information about when they were created.
* Spool files(downtimes) can apply to a service on a specific port - useful if you have multiple copies of a service on
  the same box.
* It is possible to specify (via `http_headers_to_copy` in the config file) a set of headers that should be forwarded
  to the service being checked.

### Dependencies

**hacheck** is written in Python and makes extensive use of the [tornado](http://www.tornadoweb.org/en/stable/) asynchronous web framework (specifically, it uses the coroutine stuff in Tornado 3). Unit tests use nose and mock.

It runs on Python 2.6 and above, as well as Python 3.3 and above.

### Use cases

Imagine you want to take down the server `web01` for maintenance. Just SSH to it, then (as root) run `hadown all` and wait however long your HAproxy healthchecking interval is. Do your maintenance, then run `haup all` to put it back in service. So easy!

### Configuration

`hacheck` accepts a `-c` flag which should point to a YAML-formatted configuration file. Some notable properties of this file:
* `cache_time`: The duration for which check results may be cached
* `service_name_header`: If set, the name of a header which will be populated with the service name on HTTP checks
* `log_path`: Either the string `"stdout"`, the string `"stderr"`, or a fully-qualified path to a file to write logs to. Uses a [WatchedFileHandler](http://docs.python.org/2/library/logging.handlers.html#watchedfilehandler) and ought to play nicely with logrotate
* `mysql_username`: username to use when logging into mysql for checks
* `mysql_password`: password to use when logging into mysql for checks
* `rlimit_nofile`: set the NOFILE rlimit. If the string "max", will set the rlimit to the hard rlimit; otherwise, will be interpreted as an integer and set to that value.
* `allow_remote_spool_changes`: whether to allow remote control of spool files.
* `http_headers_to_copy`: List of headers to copy
* `http_header_service_identity`: Header to check for service identity, if set and environment variable `MESH_REGISTRATIONS` is set, value is checked.

### Monitoring

`hacheck` exports some useful monitoring stuff at the `/status` endpoint. It also exports a count of requests by source-IP and service name on the `/status/count` endpoint.

If the [mutornadomon](https://github.com/uber/mutornadomon) package is available, `hacheck` will import and use it, exposing standard stats about tornado to localhost at `/mutornadomon`

### License

This work is licensed under the [MIT License](http://opensource.org/licenses/MIT), the contents of which can be found at [LICENSE.txt](LICENSE.txt).
