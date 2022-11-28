# netlify-commons

[![](https://godoc.org/github.com/netlify/netlify-commons?status.svg)](https://godoc.org/github.com/netlify/netlify-commons)

> This repo is actively being decomposed. Please check the section below for where many packages have moved. The deprecation process is slow so code is removed where possible, but to stop doing major refactors, we are putting this notice

## Decomposition information
These packages have moved and will be removed in an upcoming breaking change. Please prefer making the modifications to the new repos. There will be no effort in maintaining packages that have been marked for deletion.

- `nconf` --> [go-config](https://github.com/netlify/go-config)
- `metriks`, `tracing` --> [go-observability](https://github.com/netlify/go-observability)
- `featureflags` --> [go-flags](https://github.com/netlify/go-flags)
- `testutil` --> [go-test-utils](https://github.com/netlify/go-test-utils)
- `bugsnag`, `pprof`, `util` --> [go-utils](https://github.com/netlify/go-utils)

The largest change is going to be porting `router`, `http`, and `server` to their own repos.

Things that are on the chopping block coming up (pending time mostly):
- removal of the `instrument`, `graceful`, `discovery` packages as there is minimal usage and some functionality is better supported in the stdlib
- moving `mongoclient` out
- moving `ntoml` out

This is a core library that will add common features for our services.

> The ones that have their own right now will be migrated as needed

Mostly this deals with configuring logging, messaging (rabbit && nats), and loading configuration.
