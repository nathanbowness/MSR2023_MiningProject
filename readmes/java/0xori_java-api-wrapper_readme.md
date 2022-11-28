# Important notice
Unfortunately, we decided to discontinue support for this project; SoundCloud will no longer accept pull requests or make public releases of java-api-wrapper. If you're using java-api-wrapper in one of your projects, we suggest you fork the project in order to perform any necessary maintenance.

# java-api-wrapper [![Build Status](https://secure.travis-ci.org/soundcloud/java-api-wrapper.png?branch=master)](http://travis-ci.org/soundcloud/java-api-wrapper)

OAuth2 SoundCloud API wrapper written in Java ([javadoc][]).

It is simple to use and requires a minimum of external dependencies (compared to
the OAuth1 wrapper) so should be easily embeddable in both desktop and
mobile applications.

## Android

The wrapper works well on Android (although it has no dependencies on it)
since it is an extraction from our [SoundCloud Android][] codebase. However, if
all you want is to share sounds from your own application we recommend to check out the
[Android Sharing Kit][] which delegates all the hard work to the SoundCloud
app and makes use of Android's [intent][] framework.

## Usage

Create a wrapper instance:

```java
ApiWrapper wrapper = new ApiWrapper("client_id", "client_secret", null, null);
```

Obtain a token:

```java
wrapper.login("username", "password");
```

Execute a request:

```java
HttpResponse resp = wrapper.get(Request.to("/me"));
```

Update a resource:

```java
HttpResponse resp =
      wrapper.put(Request.to("/me")
             .with("user[full_name]", "Che Flute",
                   "user[website]",   "http://cheflute.com")
             .withFile("user[avatar_data]", new File("flute.jpg")));
```

## Refresh tokens

OAuth2 access tokens are only valid for a certain amount of time (usually 1h)
and need to be refreshed when they become stale. The wrapper automatically
refreshes the token and retries the request so an API client usually does not
need to care about this fact. If the client is interested (possibly to persist
the updated token) it can register a listener with the wrapper.

## Non-expiring access tokens (only applies to version 1.0.1+)

Expiring access tokens provide more security but also add more complexity to
the authentication process. If you don't want to use them you can request
non-expiring tokens by specifying the scope "non-expiring" when exchanging the
tokens:

```java
Token token = wrapper.login("username", "password", Token.SCOPE_NON_EXPIRING);
```

The resulting token will be valid until revoked manually.

For the `authorization_code` grant type you need to request the scope like so:

```java
URI uri = wrapper.authorizationCodeUrl(Endpoints.CONNECT, Token.SCOPE_NON_EXPIRING);
// open uri in browser / WebView etc.
```

## Login via Facebook

Please see [FacebookConnect][] for an example of this login flow.

## Requirements

The wrapper depends on [Apache HttpClient][] (including the [HttpMime][]
module) and [json-java][]. The Android SDK already comes with these two
libraries so you don't need to include them when using the wrapper there.

## Build + Test

The project uses the groovy-based build system [gradle][] (version 1.x):

    $ brew update && brew install gradle (OSX+homebrew, check website for other OS)
    $ git clone git://github.com/soundcloud/java-api-wrapper.git
    $ cd java-api-wrapper
    $ gradle jar  # build jar file (build/libs/java-api-wrapper-1.x.x.jar)
    $ gradle test # run tests

You don't have to use gradle - the repo also contains a `pom.xml` file which
can be used to build and test the project with [Apache Maven][] (`mvn install`).

Jar files are available in the Github [download section][downloads] and on
sonatype.org / maven ([snapshots][], [releases][], [maven-central][]).

## Examples

The wrapper ships with a few examples in `src/examples/java`:

  * [CreateWrapper][] creates a wrapper and obtains an access token using
  login / password.
  * [GetResource][] performs a GET request for a resource and prints the
  JSON result.
  * [PostResource][] performs a POST request to create a resource and prints the
  JSON result
  * [PutResource][] performs a PUT request to update a resource and prints the
  JSON result
  * [UploadFile][] uploads a file to SoundCloud.
  * [FacebookConnect][] obtain an access token via Facebook login

You can use gradle tasks to compile and run these examples with one command.

First create a wrapper and remember to substitute all credentials with real ones
([register an app][register-app] if you need client_id/secret):

    # with gradle
    $ gradle createWrapper -Pclient_id=my_client_id \
        -Pclient_secret=mys3cr3t \
        -Plogin=api-testing \
        -Ppassword=testing

    # with plain java
    $ java -classpath java-api-wrapper-1.x.y-all.jar \
        com.soundcloud.api.examples.CreateWrapper \
        my_client_id mys3cr3t api-testing testing

Output:

    got token from server: Token{
      access='0000000KNYbSTHKNZC2tq7Epkgxvgmhu',
      refresh='0000000jd4YCL0vCuKf6UtPsS6Ahd0wc', scope='null',
      expires=Mon May 02 17:35:15 CEST 2011}

    wrapper serialised to wrapper.ser

With the wrapper and all tokens serialised to `wrapper.ser` you can run the
other examples.

GET a resource:

    $ gradle getResource -Presource=/me
    (java -classpath java-api-wrapper-1.x.y-all.jar \
        com.soundcloud.api.examples.GetResource /me)

Output:

    GET /me
    {
        "username": "testing",
        "city": "Berlin"
        ...
    }

PUT a resource:

    $ gradle putResource -Presource=/me -Pcontent='{ "user": { "city": "Testor" } }' -PcontentType=application/json

Output:

    PUT /me
    {
        "username": "testing",
        "city": "Testor"
        ...
    }

POST a resource:

    $ gradle postResource -Presource=/playlists -Pcontent='{ "playlist": { "title": "Test" } }' -PcontentType=application/json

Output:

    POST /playlists
    {
        "title": "Test",
        "artwork_url": null,
        ...
    }

Upload a file:

    $ gradle uploadFile \
            -Pfile=src/test/resources/com/soundcloud/api/hello.aiff
      (java -classpath java-api-wrapper-1.x.y-all.jar \
        com.soundcloud.api.examples.UploadFile ...)

Output:

    Uploading src/test/resources/com/soundcloud/api/hello.aiff
    .............................................
    201 Created https://api.sandbox-soundcloud.com/tracks/2100052
    {
        "artwork_url": null,
        ...
    }

You can add the debug flag (`-d`) to gradle to get some extra HTTP logging:

    $ gradle getResource -Presource=/me -d

    [DEBUG] DefaultClientConnection - Sending request: GET /me HTTP/1.1
    [DEBUG] headers - >> GET /me HTTP/1.1
    [DEBUG] headers - >> Authorization: OAuth 0000000ni3Br147FO7Cj5XotAy
    ...

Note that while the example code uses standard Java serialization to persist
state across calls you should probably use a different mechanism in your app.

## Note on Patches/Pull Requests

  * Fork the project.
  * Make your feature addition or bug fix.
  * Add tests for it.
  * Commit, do not mess with buildfile, version, or history.
  * Send a pull request. Bonus points for topic branches.

If you want to work on the code in an IDE instead of a text editor you can
easily create project files with gradle:

    $ gradle idea     # Intellij IDEA
    $ gradle eclipse  # Eclipse

## Credits / License

The API is based on [urbanstew][]'s [soundcloudapi-java][] project.

Includes portions of code (c) 2010 Xtreme Labs and Pivotal Labs and (c) 2009 urbanSTEW.

See LICENSE for details.


[gradle]: http://www.gradle.org/
[urbanstew]: http://urbanstew.org/
[Apache HttpClient]: http://hc.apache.org/httpcomponents-client-ga/
[HttpMime]: http://hc.apache.org/httpcomponents-client-ga/httpmime
[json-java]: http://json.org/java/
[javadoc]: http://soundcloud.github.com/java-api-wrapper/javadoc/1.3.1/com/soundcloud/api/package-summary.html
[soundcloudapi-java]: http://code.google.com/p/soundcloudapi-java/
[soundcloudapi-java-annouce]: http://blog.soundcloud.com/2010/01/08/java-wrapper/
[CreateWrapper]: https://github.com/soundcloud/java-api-wrapper/blob/master/src/examples/java/com/soundcloud/api/examples/CreateWrapper.java
[GetResource]: https://github.com/soundcloud/java-api-wrapper/blob/master/src/examples/java/com/soundcloud/api/examples/GetResource.java
[PutResource]: https://github.com/soundcloud/java-api-wrapper/blob/master/src/examples/java/com/soundcloud/api/examples/PutResource.java
[PostResource]: https://github.com/soundcloud/java-api-wrapper/blob/master/src/examples/java/com/soundcloud/api/examples/PostResource.java
[UploadFile]: https://github.com/soundcloud/java-api-wrapper/blob/master/src/examples/java/com/soundcloud/api/examples/UploadFile.java
[FacebookConnect]: https://github.com/soundcloud/java-api-wrapper/blob/master/src/examples/java/com/soundcloud/api/examples/FacebookConnect.java
[SoundCloud Android]: https://play.google.com/store/apps/details?id=com.soundcloud.android
[register-app]: http://soundcloud.com/you/apps/new
[Apache Maven]: http://maven.apache.org/
[downloads]: https://github.com/soundcloud/java-api-wrapper/archives/master
[snapshots]: https://oss.sonatype.org/content/repositories/snapshots/com/soundcloud/java-api-wrapper/
[releases]: https://oss.sonatype.org/content/repositories/releases/com/soundcloud/java-api-wrapper/
[maven-central]: http://repo1.maven.org/maven2/com/soundcloud/java-api-wrapper/
[Android Sharing Kit]: https://github.com/soundcloud/android-intent-sharing/wiki
[android-token-sharing]: https://github.com/soundcloud/android-token-sharing
[intent]: http://developer.android.com/reference/android/content/Intent.html
