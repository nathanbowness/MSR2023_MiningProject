# Arquillian Liberty Server Containers [![Maven Central Latest](https://maven-badges.herokuapp.com/maven-central/io.openliberty.arquillian/arquillian-parent-liberty-jakarta/badge.svg)](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22io.openliberty.arquillian%22%20AND%20a%3A%22arquillian-parent-liberty-jakarta%22) [![Build Status](https://github.com/OpenLiberty/liberty-arquillian/actions/workflows/maven.yml/badge.svg?branch=main)](https://github.com/OpenLiberty/liberty-arquillian/actions?branch=main) [![Maven Central 1.x](https://maven-badges.herokuapp.com/maven-central/io.openliberty.arquillian/arquillian-parent-liberty/badge.svg)](http://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22io.openliberty.arquillian%22%20AND%20a%3A%22arquillian-parent-liberty%22) [![Build Status 1.x](https://github.com/OpenLiberty/liberty-arquillian/actions/workflows/maven.yml/badge.svg?branch=1.x-maintenance)](https://github.com/OpenLiberty/liberty-arquillian/actions?branch=1.x-maintenance)

[Arquillian](http://arquillian.org/) is a testing framework to develop automated functional, integration and acceptance tests for your Java applications. Arquillian container adapters allow Arquillian to bind to and manage the lifecycle of a runtime. There are two types of Arquillian container adapters for Liberty: [Liberty Managed](#Arquillian-Liberty-Managed-Container) and [Liberty Remote](#Arquillian-Liberty-Remote-Container).

### Arquillian Liberty Managed Container

An Arquillian container adapter (`DeployableContainer` implementation) that can start and stop a local Liberty process and run tests on it over a remote protocol (effectively in a different JVM). For an introduction to testing microservices with the Arquillian Liberty Managed container and [Open Liberty](https://openliberty.io/), check out the [this guide](https://openliberty.io/guides/arquillian-managed.html).

**Jakarta EE 9:** for Arquillian Liberty Managed container documentation with Jakarta EE 9, click [here](liberty-managed/JakartaEE9_README.md).

**Java EE 8 or below:** for Arquillian Liberty Managed container documentation with Java EE 8 or below, click [here](liberty-managed/README.md).

### Arquillian Liberty Remote Container

An Arquillian container adapter (`DeployableContainer` implementation) that can connect and run against a remote (different JVM, different machine) Liberty server and run tests on it over a remote protocol (effectively in a different JVM).

**Jakarta EE 9:** for Arquillian Liberty Remote container documentation with Jakarta EE 9, click [here](liberty-remote/JakartaEE9_README.md).

**Java EE 8 or below:** for Arquillian Liberty Remote container documentation with Java EE 8 or below, click [here](liberty-remote/README.md).

### Testing

To run tests, you will need to specify the following parameters:

| Parameter        | Description |
| ---------------- | ----------- |
| runtime          | The runtime to use. Specify `ol` for Open Liberty, `olbeta` for Open Liberty beta, and `wlp` for WebSphere Liberty. |
| runtimeVersion   | Version of the specified runtime to use. |

For example, to run tests on version 22.0.0.6 of the Open Liberty runtime, use the following command:

```
mvn verify -Druntime=ol -DruntimeVersion=22.0.0.6
```
