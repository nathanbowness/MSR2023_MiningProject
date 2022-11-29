# ![HAProxy](assets/images/haproxy-weblogo-210x49.png "HAProxy")

## HAProxy configuration parser

[![Contributors](https://img.shields.io/github/contributors/haproxytech/config-parser?color=purple)](https://github.com/haproxy/haproxy/blob/master/CONTRIBUTING)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

### autogenerated code
if you change types/types.go you need to run
```bash
make generate
```
### Contributing

For commit messages and general style please follow the haproxy project's [CONTRIBUTING guide](https://github.com/haproxy/haproxy/blob/master/CONTRIBUTING) and use that where applicable.

Please use `golangci-lint run` from [github.com/golangci/golangci-lint](https://github.com/golangci/golangci-lint) for linting code.

### Example

```go
package main

import (
    "github.com/haproxytech/config-parser/v4"
    "github.com/haproxytech/config-parser/v4/options"
    "github.com/haproxytech/config-parser/v4/parsers/http/actions"
    // ...
)
// ...

func main() {
    p, err := parser.New(options.Path("config.cfg"))
    /* p, err := parser.New(
        options.UseMd5Hash,
        options.Path("config.cfg")
    )*/
    if err != nil {
        log.Panic(err)
    }

    {
        data, _ := p.Get(parser.Comments, parser.CommentsSectionName, "# _version", true)
        if err == errors.ErrFetch {
            log.Panicln("we have an fetch error !!")
        }
        ver, _ := data.(*types.Int64C)
        ver.Value = ver.Value + 1
    }

    {
        p.Set(parser.Frontends, "http", "option forwardfor", types.OptionForwardFor{})
    }

    {
        // for options that can exists multiple times in config Insert is preffered
        //
        // setting http-request & http-response is a bit different
        // since they accept multiple structs
        httpRequestActionDeny := &actions.Deny{
            DenyStatus: "0",
            Cond:       "unless",
            CondTest:   "{ src 127.0.0.1 }",
        }
        err = p.Insert(parser.Backends, "web_servers", "http-request", httpRequestActionDeny)
        // you can also choose index where action should be inserted
        err = p.Insert(parser.Backends, "web_servers", "http-request", httpRequestActionDeny, 2)
    }

    {
        data, err := p.Get(parser.Global, parser.GlobalSectionName, "stats socket")
        if err != nil {
            log.Panicln(err)
        }
        val, _ := data.([]types.Socket)
        log.Println(val[0])
        val[0].Path = "$PWD/haproxy-runtime-api.1.sock"
        log.Println(val[0])
    }

    {
        data, err := p.Get(parser.Global, parser.GlobalSectionName, "daemon")
        log.Println(data, err)
        if err == errors.ErrFetch {
            log.Panicln("we have an fetch error !!")
        }
        //remove it
        p.Set(parser.Global, parser.GlobalSectionName, "daemon", nil)
    }

    {
        datar, err := p.Get(parser.Resolvers, "ns1", "nameserver")
        if err == nil {
            ns := datar.([]types.Nameserver)
            log.Println(ns[0].Name, ns[0].Address)
            log.Println(ns[1].Name, ns[1].Address)
            ns[1].Name = "hahaha"
            ns[0].Address = "0.0.0.0:8080"
        }
        datar, err = p.Get(parser.Resolvers, "ns1", "nameserver")
        if err == nil {
            ns := datar.([]types.Nameserver)
            log.Println(ns[0].Name, ns[0].Address)
            log.Println(ns[1].Name, ns[1].Address)
        }
    }

    {
        log.Println("nbproc ==================================================")
        data, err := p.Get(parser.Global, parser.GlobalSectionName, "nbproc")
        if err != nil {
            log.Println(err)
        } else {
            d := data.(*types.Int64C)
            log.Println(d.Value)
            d.Value = 5
        }
    }

    p.Save(configFilename)
}

```

## License

[Apache License 2.0](LICENSE)