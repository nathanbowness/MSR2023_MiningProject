# gochimp3
[![GoDoc][godoc-img]][godoc-url] [![Build Status][travis-img]][travis-url] [![Gitter chat][gitter-img]][gitter-url]

## Introduction
Golang client for [MailChimp API 3.0](http://developer.mailchimp.com/documentation/mailchimp/).

## Install
Install with `go get`:

```bash
$ go get github.com/hanzoai/gochimp3
```

## Usage
```go
package main

import (
	"fmt"
	"os"

	"github.com/hanzoai/gochimp3"
)

const (
	apiKey = "YOUR_API_KEY_HERE"
)

func main() {
	client := gochimp3.New(apiKey)

	// Audience ID
	// https://mailchimp.com/help/find-audience-id/
	listID := "7f12f9b3fz"

	// Fetch list
	list, err := client.GetList(listID, nil)
	if err != nil {
		fmt.Printf("Failed to get list %s", listID)
		os.Exit(1)
	}

	// Add subscriber
	req := &gochimp3.MemberRequest{
		EmailAddress: "test@mail.com",
		Status:       "subscribed",
	}

	if _, err := list.CreateMember(req); err != nil {
		fmt.Printf("Failed to subscribe %s", req.EmailAddress)
		os.Exit(1)
	}
}
```

### Set Timeout
``` go
client := gochimp3.New(apiKey)
client.Timeout = (5 * time.Second)
```

[godoc-img]:      https://godoc.org/github.com/hanzoai/gochimp3?status.svg
[godoc-url]:      https://godoc.org/github.com/hanzoai/gochimp3
[travis-img]:     https://img.shields.io/travis/hanzoai/gochimp3.svg
[travis-url]:     https://travis-ci.org/hanzoai/gochimp3
[gitter-img]:     https://badges.gitter.im/join-chat.svg
[gitter-url]:     https://gitter.im/hanzoai/chat

<!-- not used -->
[coveralls-img]:    https://coveralls.io/repos/hanzoai/gochimp3/badge.svg?branch=master&service=github
[coveralls-url]:    https://coveralls.io/github/hanzoai/gochimp3?branch=master
