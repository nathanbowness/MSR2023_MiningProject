[![GoDoc](https://godoc.org/github.com/couchbase/sg-bucket?status.png)](https://godoc.org/github.com/couchbase/sg-bucket) [![Sourcegraph](https://sourcegraph.com/github.com/couchbase/sg-bucket/-/badge.svg)](https://sourcegraph.com/github.com/couchbase/sg-bucket?badge)  [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


# sg-bucket

This repo contains:

- Interfaces needed by all concrete implementations of the `sgbucket.Bucket` interface, as well as by Sync Gateway itself.
- Common code used by certain sg-bucket concrete implementations ([walrus](https://github.com/couchbaselabs/walrus), [forestdb-bucket](https://github.com/couchbaselabs/forestdb-bucket/)) and to a lesser extent by Sync Gateway itself.
