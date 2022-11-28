# nds

[![Build Status](https://travis-ci.org/qedus/nds.svg?branch=master)](https://travis-ci.org/qedus/nds) [![Coverage Status](https://coveralls.io/repos/github/qedus/nds/badge.svg?branch=master)](https://coveralls.io/github/qedus/nds?branch=master) [![GoDoc](https://godoc.org/github.com/qedus/nds?status.png)](https://godoc.org/github.com/qedus/nds)

Package `github.com/qedus/nds` is a datastore API for the Google App Engine (GAE) [Go Runtime Environment](https://developers.google.com/appengine/docs/go/) that uses memcache to cache all datastore requests. It is compatible with both Classic and Managed VM products. This package guarantees strong cache consistency when using `nds.Get*` and `nds.Put*`, meaning you will never get data from a stale cache.

Exposed parts of this API are the same as the official one distributed by Google ([`google.golang.org/appengine/datastore`](https://godoc.org/google.golang.org/appengine/datastore)). However, underneath `github.com/qedus/nds` uses a caching stategy similar to the GAE [Python NDB API](https://developers.google.com/appengine/docs/python/ndb/). In fact the caching strategy used here even fixes one or two of the Python NDB [caching consistency bugs](http://goo.gl/3ByVlA).

You can find the API documentation at [http://godoc.org/github.com/qedus/nds](http://godoc.org/github.com/qedus/nds).

One other benefit is that the standard `datastore.GetMulti`, `datastore.PutMulti` and `datastore.DeleteMulti` functions only allow you to work with a maximum of 1000, 500 and 500 entities per call respectively. The `nds.GetMulti`, `nds.PutMulti` and `nds.DeleteMulti` functions in this package allow you to work with as many entities as you need (within timeout limits) by concurrently calling the appropriate datastore function until your request is fulfilled.

## How To Use

You can use this package in *exactly* the same way you would use [`google.golang.org/appengine/datastore`](https://godoc.org/google.golang.org/appengine/datastore). However, it is important that you use `nds.Get*`, `nds.Put*`, `nds.Delete*` and `nds.RunInTransaction` entirely within your code. Do not mix use of those functions with the `google.golang.org/appengine/datastore` equivalents as you will be liable to get stale datastore entities from `github.com/qedus/nds`.

Ultimately all you need to do is find/replace the following in your codebase:

- `datastore.Get` -> `nds.Get`
- `datastore.Put` -> `nds.Put`
- `datastore.Delete` -> `nds.Delete`
- `datastore.RunInTransaction` -> `nds.RunInTransaction`

## Versions

Versions are specified using [Go Modules](https://github.com/golang/go/wiki/Modules).

- Version 1.x.x: Can be found on branch [`master`](https://github.com/qedus/nds/tree/master) and uses the `google.golang.org/appengine` package.
- Version 2.x.x: Can be found on branch [`v2`](https://github.com/qedus/nds/tree/v2). This is a major update and takes advantage of the new `cloud.google.com/go/datastore` package provided by Google. It currently in an experimental state and we welcome contributions.
