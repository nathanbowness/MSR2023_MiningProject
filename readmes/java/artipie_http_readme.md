<a href="http://artipie.com"><img src="https://www.artipie.com/logo.svg" width="64px" height="64px"/></a>

[![Join our Telegramm group](https://img.shields.io/badge/Join%20us-Telegram-blue?&logo=telegram&?link=http://right&link=http://t.me/artipie)](http://t.me/artipie)

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![DevOps By Rultor.com](http://www.rultor.com/b/artipie/http)](http://www.rultor.com/p/artipie/http)
[![We recommend IntelliJ IDEA](https://www.elegantobjects.org/intellij-idea.svg)](https://www.jetbrains.com/idea/)

[![Javadoc](http://www.javadoc.io/badge/com.artipie/http.svg)](http://www.javadoc.io/doc/com.artipie/http)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/artipie/http/blob/master/LICENSE.txt)
[![codecov](https://codecov.io/gh/artipie/maven-adapter/branch/master/graph/badge.svg)](https://codecov.io/gh/artipie/maven-adapter)
[![Hits-of-Code](https://hitsofcode.com/github/artipie/http)](https://hitsofcode.com/view/github/artipie/http)
[![Maven Central](https://img.shields.io/maven-central/v/com.artipie/http.svg)](https://maven-badges.herokuapp.com/maven-central/com.artipie/http)
[![PDD status](http://www.0pdd.com/svg?name=artipie/http)](http://www.0pdd.com/p?name=artipie/http)

# HTTP

Artipie HTTP base interfaces.  

If you have any question or suggestions, do not hesitate to [create an issue](https://github.com/artipie/http/issues/new) or contact us in
[Telegram](https://t.me/artipie).  
Artipie [roadmap](https://github.com/orgs/artipie/projects/3).

To install add this dependency to `pom.xml` file:
```xml
<dependency>
  <groupId>com.artipie</groupId>
  <artifactId>http</artifactId>
  <version><!-- use latest version --></version>
</dependency>
```

This module tends to be reactive and provides these interfaces:
 - `Slice` - Arti-pie slice, should be implemented by adapter interface
 or Artipie application, it can receive request data and return reactive response;
 - `Response` - returned by `Slice` from adapters, can be sent to `Connection`;
 - `Connection` - response asks connection to accept response data, `Connection`
 should be implemented by HTTP web server implementation to accept HTTP responses.

Each artipie adapter has to implement `Slice` interface with single method `response`.
This method should process the request and return reactive response object:
```java
class Maven implements Slice {
  @Override
  public Response response(String line, Iterable<Map.Entry<String, String>> headers,
      Flow.Publisher<Byte> body) {
      this.upload(body);
      return new RsWithStatus(200);
  }
}
```

Response is reactive object with single method `send`. This method is called by
server implementation, server provides connection implementation as `send` parameter
which can accept response data: the server asks response to send itself to connection.

```java
class MavenResponse implements Response {

    @Override
    void send(final Connection con) {
        con.accept(200, headers, empty);
    }
}
```

HTTP server implements `Connection` interface which can accept response data:
server asks response to send itself to connection, response asks connection
to accept the data. Artipie adapters are not supposed to implement this interface,
it should be done by HTTP server implementation, e.g. vertex-server module.

## Some useful examples for different objects

### Routing

You can do routing in the following style:

```java
class Repo extends Slice.Wrap {
  Repo(Storage storage) {
    super(
      new SliceRoute(
        new SliceRoute.Path(new RtRule.ByMethod(RqMethod.PUT), new SliceUpload(storage)),
        new SliceRoute.Path(new RtRule.ByMethod(RqMethod.GET), new SliceDownload(storage)),
        new SliceRoute.Path(RtRule.FALLBACK, new SliceSimple(new RsWithStatus(RsStatus.METHOD_NOT_ALLOWED)))
      )
    );
}
```

### Authentication

Authentication protocol is specified by `AuthScheme` interface
which parses user identity from request head (line and headers).

Possible implementations are:
 - Basic - from HTTP <ins>Basic</ins> authentication
 - Bearer - from <ins>Bearer</ins> token
 - Token - from <ins>token</ins> 

### Authorization

Authorization is specified by `Permissions` interface which checks user permissions
for `Action`. It can be encapsulated by `AuthSlice` wrapper to perform authorization checks:
```java
final Slice slice = new AuthSlice(
  new SliceUpload(storage),
  new BasicAuthScheme(authentication),
  new Permission.ByName(permissions, Action.Standard.READ)
);
```
This slice reads user authentication by authentication decoder (`AuthScheme` implementation),
if the identity was not found, then 401 error will be returned. Then the identity will be passed
to authorization check (`Permissions` class) with specified permission (`Action.Standard.READ` in the example).
If user is not authorized to perform this action 403 error will be returned. If all checks passed
successfully, then request will be redirected to underlying `Slice` implementation (`SliceUpload`
in the example).

### Main components of request

```java
final RequestLineFrom request = new RequestLineFrom(line);
final Uri uri = request.uri();
final RqMethod method = request.method();
final String httpVersion = request.version();
```

### Specific header

```java
new RqHeaders.Single(headers, "x-header-name");
```

### Returning of async responses

```java
return new AsyncResponse(
    CompletableFuture.supplyAsync(
        /**
         * Business logic here
        **/
    ).thenApply(
        rsp -> new RsWithBody(
            new RsWithStatus(RsStatus.OK), body
        )
    )
)
```

## How to contribute

Please read [contributing rules](https://github.com/artipie/artipie/blob/master/CONTRIBUTING.md).  

Fork repository, make changes, send us a pull request. We will review
your changes and apply them to the `master` branch shortly, provided
they don't violate our quality standards. To avoid frustration, before
sending us your pull request please run full Maven build:

```
$ mvn clean install -Pqulice
```

To avoid build errors use Maven 3.3+.
