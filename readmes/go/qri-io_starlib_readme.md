<h1 align="center">Starlib - Starlark's Missing standard Library.</h1>

[![Qri](https://img.shields.io/badge/made%20by-qri-magenta.svg?style=flat-square)](https://qri.io) [![GoDoc](https://godoc.org/github.com/qri-io/starlib?status.svg)](http://godoc.org/github.com/qri-io/starlib) [![License](https://img.shields.io/github/license/qri-io/starlib.svg?style=flat-square)](./LICENSE) [![Codecov](https://img.shields.io/codecov/c/github/qri-io/starlib.svg?style=flat-square)](https://codecov.io/gh/qri-io/starlib) [![CI](https://img.shields.io/circleci/project/github/qri-io/starlib.svg?style=flat-square)](https://circleci.com/gh/qri-io/starlib)

<div align="center">
  <h3>
    <a href="https://qri.io">
      Website
    </a>
    <span> | </span>
    <a href="#packages">
      Packages
    </a>
    <span> | </span>
    <a href="https://github.com/qri-io/starlib/CONTRIBUTOR.md">
      Contribute
    </a>
    <span> | </span>
    <a href="https://github.com/qri-io/starlib/issues">
      Issues
    </a>
     <span> | </span>
    <a href="https://qri.io/docs/starlark/starlib">
      Docs
    </a>
  </h3>
</div>

<div align="center">
  <!-- Build Status -->
</div>

## Welcome

This is a community-driven project to bring a standard library to the starlark programming dialect. We here at Qri need a standard library, and we thought it might benefit others to structure this library in a reusable way. We are a little biased towards our needs, and will be shaping the library primarily toward's Qri's use case.

| Question                                     | Answer                                                                                                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| "What's starlark?"                           | It's a python-like scripting language open-sourced by Google. [Here are the docs](https://docs.bazel.build/versions/master/skylark/language.html) |
| "What's the use-case for this?"              | [We're building it for Qri ('query')](https://qri.io)                                                                                             |
| "I want to play with starlib outside of Qri" | [Checkout the starlark playground](https://github.com/qri-io/skypg)                                                                               |
| "I have a question"                          | [Create an issue](https://github.com/qri-io/starlib/issues)                                                                                       |
| "I found a bug"                              | [Create an issue](https://github.com/qri-io/starlib/issues)                                                                                       |
| "I would like to propose a new package"      | You should think about [creating an RFC](https://github.com/qri-io/rfcs)                                                                          |

## Packages

The following is a list of the packages currently in the standard library

| Package                                                                            | Go Docs                                                                                                                                                           | Description                                     |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| [`bsoup`](https://github.com/qri-io/starlib/tree/master/bsoup)                     | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/bsoup?status.svg)](https://godoc.org/github.com/qri-io/starlib/bsoup)                     | a beautiful-soup-like API for working with HTML |
| [`encoding/base64`](https://github.com/qri-io/starlib/tree/master/encoding/base64) | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/encoding/base64?status.svg)](https://godoc.org/github.com/qri-io/starlib/encoding/base64) | base64 de/serialization                         |
| [`encoding/csv`](https://github.com/qri-io/starlib/tree/master/encoding/csv)       | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/encoding/csv?status.svg)](https://godoc.org/github.com/qri-io/starlib/encoding/csv)       | csv de/serialization                            |
| [`encoding/json`](https://github.com/qri-io/starlib/tree/master/encoding/json)     | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/encoding/json?status.svg)](https://godoc.org/github.com/qri-io/starlib/encoding/json)     | alias for [go.starlark.net/starlarkjson](https://github.com/google/starlark-go/blob/master/starlarkjson/json.go)                           |
| [`encoding/yaml`](https://github.com/qri-io/starlib/tree/master/encoding/yaml)     | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/encoding/yaml?status.svg)](https://godoc.org/github.com/qri-io/starlib/encoding/yaml)     | yaml de/serialization                           |
| [`geo`](https://github.com/qri-io/starlib/tree/master/geo)                         | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/geo?status.svg)](https://godoc.org/github.com/qri-io/starlib/geo)                         | 2d geographic operations                        |
| [`hash`](https://github.com/qri-io/starlib/tree/master/hash)                       | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/hash?status.svg)](https://godoc.org/github.com/qri-io/starlib/hash)                       | hash operations (md5/sha1/sha256)               |
| [`html`](https://github.com/qri-io/starlib/tree/master/html)                       | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/html?status.svg)](https://godoc.org/github.com/qri-io/starlib/html)                       | html text processing                            |
| [`http`](https://github.com/qri-io/starlib/tree/master/http)                       | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/http?status.svg)](https://godoc.org/github.com/qri-io/starlib/http)                       | http client operations                          |
| [`math`](https://pkg.go.dev/go.starlark.net/lib/math)                       | <img width=190/>[![Go Docs](https://godoc.org/github.com/go.starlark.net/lib/math?status.svg)](https://pkg.go.dev/go.starlark.net/lib/math)                       | mathematical functions & values [upstreamed into go-starlark](https://github.com/google/starlark-go/pull/357)                |
| [`re`](https://github.com/qri-io/starlib/tree/master/re)                           | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/re?status.svg)](https://godoc.org/github.com/qri-io/starlib/re)                           | regular expressions                             |
| [`time`](https://github.com/google/starlark-go/blob/master/lib/time/time.go)                       | <img width=190/>[![Go Docs](https://godoc.org/go.starlark.net/lib/time?status.svg)](https://pkg.go.dev/go.starlark.net/lib/time)                       | time operations, [upstreamed into go-starlark](https://github.com/google/starlark-go/pull/327)                                 |
| [`xlsx`](https://github.com/qri-io/starlib/tree/master/xlsx)                       | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/xlsx?status.svg)](https://godoc.org/github.com/qri-io/starlib/xlsx)                       | xlsx file format reading                        |
| [`zipfile`](https://github.com/qri-io/starlib/tree/master/zipfile)                 | <img width=190/>[![Go Docs](https://godoc.org/github.com/qri-io/starlib/zipfile?status.svg)](https://godoc.org/github.com/qri-io/starlib/zipfile)                 | support for zip archives                        |

###### This documentation has been adapted from the [Cycle.js](https://github.com/cyclejs/cyclejs) documentation.
