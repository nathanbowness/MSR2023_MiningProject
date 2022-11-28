# Dockerfile Maven

[![Build Status](https://travis-ci.com/spotify/dockerfile-maven.svg?branch=master)](https://travis-ci.com/spotify/dockerfile-maven)
[![Maven Central](https://img.shields.io/maven-central/v/com.spotify/dockerfile-maven.svg)](https://search.maven.org/#search%7Cga%7C1%7Cg%3A%22com.spotify%22%20dockerfile-maven)
[![License](https://img.shields.io/github/license/spotify/dockerfile-maven.svg)](LICENSE)

## Status: mature

**At this point, we're not developing or accepting new features or even fixing non-critical bugs.**

This Maven plugin integrates Maven with Docker.

The design goals are:

  - Don't do anything fancy.  `Dockerfile`s are how you build
    Docker projects; that's what this plugin uses.  They are
    mandatory.
  - Make the Docker build process integrate with the Maven build
    process.  If you bind the default phases, when you type `mvn
    package`, you get a Docker image.  When you type `mvn deploy`,
    your image gets pushed.
  - Make the goals remember what you are doing.  You can type `mvn
    dockerfile:build` and later `mvn dockerfile:tag` and later `mvn
    dockerfile:push` without problems.  This also eliminates the need
    for something like `mvn dockerfile:build -DalsoPush`; instead you
    can just say `mvn dockerfile:build dockerfile:push`.
  - Integrate with the Maven build reactor.  You can depend on the
    Docker image of one project in another project, and Maven will
    build the projects in the correct order.  This is useful when you
    want to run integration tests involving multiple services.

This project adheres to the [Open Code of Conduct][code-of-conduct].
By participating, you are expected to honor this code.

See the [changelog for a list of releases][changelog]

[code-of-conduct]: https://github.com/spotify/code-of-conduct/blob/master/code-of-conduct.md
[changelog]: CHANGELOG.md

## Set-up

This plugin requires Java 7 or later and Apache Maven 3 or later (dockerfile-maven-plugin <=1.4.6 needs
Maven >= 3, and for other cases, Maven >= 3.5.2). To run the integration tests or to use the plugin in practice, a working
Docker set-up is needed.

## Example

For more examples, see the [integration test](./plugin/src/it) directory.

In particular, the [advanced](./plugin/src/it/advanced) test showcases a
full service consisting of two micro-services that are integration
tested using `helios-testing`.

This configures the actual plugin to build your image with `mvn
package` and push it with `mvn deploy`.  Of course you can also say
`mvn dockerfile:build` explicitly.

```xml
<plugin>
  <groupId>com.spotify</groupId>
  <artifactId>dockerfile-maven-plugin</artifactId>
  <version>${dockerfile-maven-version}</version>
  <executions>
    <execution>
      <id>default</id>
      <goals>
        <goal>build</goal>
        <goal>push</goal>
      </goals>
    </execution>
  </executions>
  <configuration>
    <repository>spotify/foobar</repository>
    <tag>${project.version}</tag>
    <buildArgs>
      <JAR_FILE>${project.build.finalName}.jar</JAR_FILE>
    </buildArgs>
  </configuration>
</plugin>
```

A corresponding `Dockerfile` could look like:

```
FROM openjdk:8-jre
MAINTAINER David Flemström <dflemstr@spotify.com>

ENTRYPOINT ["/usr/bin/java", "-jar", "/usr/share/myservice/myservice.jar"]

# Add Maven dependencies (not shaded into the artifact; Docker-cached)
ADD target/lib           /usr/share/myservice/lib
# Add the service itself
ARG JAR_FILE
ADD target/${JAR_FILE} /usr/share/myservice/myservice.jar
```

**Important note**

The most Maven-ish way to reference the build artifact would probably
be to use the `project.build.directory` variable for referencing the
'target'-directory. However, this results in an absolute path, which
is not supported by the ADD command in the Dockerfile. Any such source
must be inside the *context* of the Docker build and therefor must be
referenced by a *relative path*. See https://github.com/spotify/dockerfile-maven/issues/101

*Do **not** use `${project.build.directory}` as a way to reference your
build directory.*

## What does it give me?

There are many advantages to using this plugin for your builds.

### Faster build times

This plugin lets you leverage Docker cache more consistently, vastly
speeding up your builds by letting you cache Maven dependencies in
your image.  It also encourages avoiding the `maven-shade-plugin`,
which also greatly speeds up builds.

### Consistent build lifecycle

You no longer have to say something like:

    mvn package
    mvn dockerfile:build
    mvn verify
    mvn dockerfile:push
    mvn deploy

Instead, it is simply enough to say:

    mvn deploy

With the basic configuration, this will make sure that the image is
built and pushed at the correct times.

### Depend on Docker images of other services

You can depend on the Docker information of another project, because
this plugin attaches project metadata when it builds Docker images.
Simply add this information to any project:

```xml
<dependency>
  <groupId>com.spotify</groupId>
  <artifactId>foobar</artifactId>
  <version>1.0-SNAPSHOT</version>
  <type>docker-info</type>
</dependency>
```

Now, you can read information about the Docker image of the project
that you depended on:

```java
String imageName = getResource("META-INF/docker/com.spotify/foobar/image-name");
```

This is great for an integration test where you want the latest
version of another project's Docker image.

Note that you have to register a Maven extension in your POM (or a
parent POM) in order for the `docker-info` type to be supported:

```xml
<build>
  <extensions>
    <extension>
      <groupId>com.spotify</groupId>
      <artifactId>dockerfile-maven-extension</artifactId>
      <version>${version}</version>
    </extension>
  </extensions>
</build>
```

## Use other Docker tools that rely on Dockerfiles

Your project(s) look like so:

```
a/
  Dockerfile
  pom.xml
b/
  Dockerfile
  pom.xml
```

You can now use these projects with Fig or docker-compose or some
other system that works with Dockerfiles.  For example, a
`docker-compose.yml` might look like:

```yaml
service-a:
  build: a/
  ports:
  - '80'

service-b:
  build: b/
  links:
  - service-a
```

Now, `docker-compose up` and `docker-compose build` will work as
expected.

## Usage

See [usage docs](https://github.com/spotify/dockerfile-maven/blob/master/docs/usage.md).

## Authentication

See [authentication docs](https://github.com/spotify/dockerfile-maven/blob/master/docs/authentication.md).

## Releasing

To cut the Maven release:

```
mvn clean [-B -Dinvoker.skip -DskipTests -Darguments='-Dinvoker.skip -DskipTests'] \
  -Dgpg.keyname=<key ID used for signing artifacts> \
  release:clean release:prepare release:perform
```

We use [`gren`](https://github.com/github-tools/github-release-notes#installation) to create Releases in Github:

```
gren release
```