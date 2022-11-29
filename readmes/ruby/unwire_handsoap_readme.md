Handsoap
===

Install
---

    gem sources -a http://gemcutter.org
    sudo gem install handsoap curb nokogiri

What
---
Handsoap is a library for creating SOAP clients in Ruby.

[Watch a tutorial](http://www.vimeo.com/4813848), showing how to use Handsoap. The final application can be found at: [http://github.com/troelskn/handsoap-example/tree/master](http://github.com/troelskn/handsoap-example/tree/master)

API docs are at [http://rdoc.info/projects/unwire/handsoap/](http://rdoc.info/projects/unwire/handsoap/)

Some usage information is to be found in [the wiki](http://wiki.github.com/unwire/handsoap).

![Handsoap](http://ny-image0.etsy.com/il_430xN.68558416.jpg)

Why
---

Ruby already has a SOAP-client library, [soap4r](http://dev.ctor.org/soap4r), so why create another one?

> Let me summarize SOAP4R: it smells like Java code built on a Monday morning by an EJB coder.
>
> -- [Ruby In Practice: REST, SOAP, WebSphere MQ and SalesForce](http://blog.labnotes.org/2008/01/28/ruby-in-practice-rest-soap-websphere-mq-and-salesforce/)

OK, not entirely fair, but soap4r has problems. It's incomplete and buggy. If you try to use it for any real-world services, you quickly run into compatibility issues. You can get around some of them, if you have control over the service, but you may not always be that lucky. In the end, even if you get it working, it has a bulky un-Rubyish feel to it.

Handsoap tries to do better by taking a minimalistic approach. Instead of a full abstraction layer, it is more like a toolbox with which you can write SOAP bindings. You could think of it as a [ffi](http://c2.com/cgi/wiki?ForeignFunctionInterface) targeting SOAP.

This means that you generally need to do more manual labor in the cases where soap4r would have automated the mapping. It also means that you need to get your hands dirty with wsdl, xsd and other heavyweight specifications. However, it does give you some tools to help you stay sane.

There are several benefits of using Handsoap:

* It supports the entire SOAP specification, all versions (because you have to implement it your self).
* You actually get a sporting chance to debug and fix protocol level bugs.
* It's much faster than soap4r, because it uses fast low-level libraries for xml-parsing and http-communication.

To summarise, soap4r takes an optimistic approach, where Handsoap expects things to fail. If soap4r works for you today, it's probably the better choice. If you find your self strugling with it, Handsoap will offer a more smooth ride. It won't magically fix things for you though.

Handsoap vs. soap4r benchmark
---

Benchmarks are always unfair, but my experiments has placed Handsoap at being approximately double as fast as soap4r. I'd love any suggestions for a more precise measure.

    $ ruby tests/benchmark_test.rb 1000
    Benchmarking 1000 calls ...
                    user     system      total        real
    handsoap    0.750000   0.090000   0.840000 (  1.992437)
    soap4r      2.240000   0.140000   2.380000 (  3.605836)
    ---------------
    Legend:
    The user CPU time, system CPU time, the sum of the user and system CPU times,
    and the elapsed real time. The unit of time is seconds.

SOAP basics
---

SOAP is a protocol that is tunneled through XML over HTTP. Apart from using the technology for transportation, it doesn't have much to do with HTTP. Some times, it hasn't even got much to do with XML either.

A SOAP client basically consists of three parts:

* A http-connectivity layer,
* a mechanism for marshalling native data types to XML,
* and a mechanism for unmarshalling XML to native data types.

The protocol also contains a large and unwieldy specification of how to do the (un)marshalling, which can be used as the basis for automatically mapping to a rich type model. This makes the protocol fitting for .net/Java, but is a huge overhead for a very dynamically typed language such as Ruby. Much of the complexity of clients such as soap4r, is in the parts that tries to use this specification. Handsoap expects you to manually write the code that marshals/unmarshals, thereby bypassing this complexity (or rather - pass it to the programmer)

Handsoap only supports RPC-style SOAP. This seems to be the most common style. It's probably possible to add support for Document-style with little effort, but until I see the need I'm not going there.

API documentation
---

In addition to this guide, there's autogenerated API documentation available at [http://rdoc.info/projects/unwire/handsoap/](http://rdoc.info/projects/unwire/handsoap/)

Getting started
---

For getting started with Handsoap, you should read [the guide in the wiki](http://wiki.github.com/unwire/handsoap/recommendations).

The toolbox
---

The Handsoap toolbox consists of the following components.

Handsoap can use either [curb](http://curb.rubyforge.org/), [Net::HTTP](http://www.ruby-doc.org/stdlib/libdoc/net/http/rdoc/index.html) or [httpclient](http://dev.ctor.org/http-access2) for HTTP-connectivity. The former is recommended, and default, but for portability you might choose one of the latter. You usually don't need to interact at the HTTP-level, but if you do (for example, if you have to use SSL), you can do so through a thin abstraction layer.

For parsing XML, Handsoap defaults to use [Nokogiri](http://github.com/tenderlove/nokogiri/tree/master). Handsoap has an abstraction layer, so that you can switch between REXML, Nokogiri and ruby-libxml. Besides providing portability between these parsers, Handsoap also gives some helper functions that are meaningful when parsing SOAP envelopes.

Finally, there is a library for generating XML, which you'll use when mapping from Ruby to SOAP. It's quite similar to [Builder](http://builder.rubyforge.org/), but is tailored towards being used for writing SOAP-messages. The name of this library is `XmlMason` and it is included/part of Handsoap.

Maintainers & Contributors
---

Handsoap is maintained by [Unwire A/S](http://www.unwire.dk), namely [Troels Knak-Nielsen](http://github.com/troelskn) and [Jimmi Westerberg](http://github.com/jimmiw), with the help of many other contributors.

Use the git command below to see a list of them all. (GIT command was found at formtastic)

  git shortlog -n -s --no-merges

License
---

Copyright: [Unwire A/S](http://www.unwire.dk), 2009

License: [Creative Commons Attribution 2.5 Denmark License](http://creativecommons.org/licenses/by/2.5/dk/deed.en_GB)
or: [LGPL 3](http://www.gnu.org/copyleft/lesser.html)
___

troelskn@gmail.com - April, 2009