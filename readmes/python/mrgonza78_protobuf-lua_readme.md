protobuf-lua
============

Lua library for Google's [Protocol Buffers](http://code.google.com/p/protobuf/).

## Instalation and usage

Make sure you have `pip` installed (`sudo easy_install pip`) and install `protobuf` package (`sudo pip install protobuf`)

If you wanna use this fork in luarocks, user following command:

```
luarocks install https://raw.githubusercontent.com/mrgonza78/protobuf-lua/master/protobuf-scm-1.rockspec
```

Make a link to the protoc plugin, for example:

```ln -s $(luarocks config --lua-libdir)/luarocks/rocks/protobuf/scm-1/protoc-plugin/protoc-gen-lua /usr/local/bin/```

proto files can then be compiled using: ```protoc --lua_out=./ foo.proto```

The API is similar to Google's protobuf python library. An example can be found in the example directory.
