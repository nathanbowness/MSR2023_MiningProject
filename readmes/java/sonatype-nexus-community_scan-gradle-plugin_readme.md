<!--

    Copyright (c) 2020-present Sonatype, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

-->

<p align="center">
    <img src="https://github.com/sonatype-nexus-community/scan-gradle-plugin/blob/main/docs/images/sherlocktrunks.png" width="350"/>
</p>

# Sonatype Scan Gradle Plugin - AKA Sherlock Trunks #
[![Maven Central](https://img.shields.io/maven-central/v/org.sonatype.gradle.plugins/scan-gradle-plugin.svg?label=Maven%20Central)](https://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22org.sonatype.gradle.plugins%22%20AND%20a%3A%22scan-gradle-plugin%22)

[![Gradle Plugins Portal](https://img.shields.io/maven-metadata/v/https/plugins.gradle.org/m2/org/sonatype/gradle/plugins/scan/org.sonatype.gradle.plugins.scan.gradle.plugin/maven-metadata.xml.svg?colorB=007ec6&label=Gradle%20Plugins%20Portal)](https://plugins.gradle.org/plugin/org.sonatype.gradle.plugins.scan)

[![CircleCI Build Status](https://circleci.com/gh/sonatype-nexus-community/scan-gradle-plugin.svg?style=shield "CircleCI Build Status")](https://circleci.com/gh/sonatype-nexus-community/scan-gradle-plugin) 

Gradle plugin that scans the dependencies of a Gradle project using Sonatype platforms: OSS Index and Nexus IQ Server.

## Compile and Publish to Local Maven Cache

> ./gradlew clean publishToMavenLocal

If you want to save some time, skip integration tests:

> ./gradlew clean publishToMavenLocal -x integrationTest

## Run Integration Tests

> ./gradlew integrationTest

## Compatibility
The plugin can be used on projects with Gradle 3.3 or higher (local installation or wrapper) and Java 8 installed locally.

## Supported Programming Languages
Gradle can be used to build projects developed in various programming languages. This plugin supports:
- Java
- Kotlin
- Scala
- Groovy

## How to Use
- Create/Clone/Download any Gradle project.
- Edit its `build.gradle` file adding this:

```
plugins {
  id 'org.sonatype.gradle.plugins.scan' version '2.5.3' // Update the version as needed
}
```

- Or `build.gradle.kts`:
```
plugins {
    id ("org.sonatype.gradle.plugins.scan") version "2.5.3" // Update the version as needed
}
```

Some basic examples will be provided next, which we strongly advice to read :)

After doing so, specific usage on CI tools can be found at https://github.com/guillermo-varela/example-scan-gradle-plugin

### OSS Index
OSS Index can be used without any extra configuration, but to avoid reaching the limit for anonymous queries every user
is encouraged to create a free account on [OSS Index](https://ossindex.sonatype.org/user/signin) and use the credentials
on this plugin. Cache can also be configured optionally.

If you are using Groovy (build.gradle file):
```groovy
ossIndexAudit {
    username = 'email' // if not provided, an anonymous query will be made
    password = 'pass'
    allConfigurations = false // if true includes the dependencies in all resolvable configurations. By default is false, meaning only 'compileClasspath', 'runtimeClasspath', 'releaseCompileClasspath' and 'releaseRuntimeClasspath' are considered
    useCache = true // true by default
    cacheDirectory = 'some/path' // by default it uses the user data directory (according to OS)
    cacheExpiration = 'PT12H' // 12 hours if omitted. It must follow the Joda Time specification at https://www.javadoc.io/doc/joda-time/joda-time/2.10.4/org/joda/time/Duration.html#parse-java.lang.String-
    proxyConfiguration { // extra configuration when running behind a proxy without direct internet access
        protocol = 'http' // can be 'http' (default) or 'https'
        host = 'proxy-host' // hostname for the proxy
        port = 8080 // port for the proxy
        authConfiguration.username = 'username' // username for the proxy (if credentials are required)
        authConfiguration.password = 'password' // password for the proxy (if credentials are required)
    }
    modulesIncluded = ['module-1', 'module-2'] // Optional. For multi-module projects, the names of the sub-modules to include for auditing. If not specified all modules are included.
    modulesExcluded = ['module-1', 'module-2'] // Optional. For multi-module projects, the names of the sub-modules to exclude from auditing. If not specified no modules are excluded. This value is processed after 'modulesIncluded' if both are specified.

    // ossIndexAudit can be configured to exclude vulnerabilities from matching
    excludeVulnerabilityIds = ['39d74cc8-457a-4e57-89ef-a258420138c5'] // list containing ids of vulnerabilities to be ignored
    excludeCoordinates = ['commons-fileupload:commons-fileupload:1.3'] // list containing coordinate of components which if vulnerable should be ignored

    // Output options
    outputFormat = 'DEFAULT' // Optional, other values are: 'DEPENDENCY_GRAPH' prints dependency graph showing direct/transitive dependencies, 'JSON_CYCLONE_DX_1_4' prints a CycloneDX 1.4 SBOM in JSON format.
    cycloneDxComponentType = 'LIBRARY' // Optional, only used when outputFormat = 'JSON_CYCLONE_DX_1_4' to define the type of component this project is for the BOM metadata with possible values: 'LIBRARY' (default), 'APPLICATION', 'FRAMEWORK', 'CONTAINER', 'OPERATING_SYSTEM', 'DEVICE', 'FIRMWARE' and 'FILE'.
    isColorEnabled = false // if true (and outputFormat = "DEFAULT") prints vulnerability description in color. By default is true.
    showAll = false // if true prints all dependencies. By default is false, meaning only dependencies with vulnerabilities will be printed.
    printBanner = true // if true will print ASCII text banner. By default is true.
}
```

Or if you are using Kotlin (build.gradle.kts file):
```kotlin
ossIndexAudit {
    username = "email" // if not provided, an anonymous query will be made
    password = "pass"
    isAllConfigurations =
        false // if true includes the dependencies in all resolvable configurations. By default is false, meaning only "compileClasspath", "runtimeClasspath", "releaseCompileClasspath" and "releaseRuntimeClasspath" are considered
    isUseCache = true // true by default
    cacheDirectory = "some/path" // by default it uses the user data directory (according to OS)
    cacheExpiration =
        "PT12H" // 12 hours if omitted. It must follow the Joda Time specification at https://www.javadoc.io/doc/joda-time/joda-time/2.10.4/org/joda/time/Duration.html#parse-java.lang.String-
    proxyConfiguration { // extra configuration when running behind a proxy without direct internet access
        protocol = "http" // can be "http" (default) or "https"
        host = "proxy-host" // hostname for the proxy
        port = 8080 // port for the proxy
        authConfiguration.username = "username" // username for the proxy (if credentials are required)
        authConfiguration.password = "password" // password for the proxy (if credentials are required)
    }
    modulesIncluded = listOf("module-1", "module-2") // Optional. For multi-module projects, the names of the sub-modules to include for auditing. If not specified all modules are included.
    modulesExcluded = listOf("module-1", "module-2") // Optional. For multi-module projects, the names of the sub-modules to exclude from auditing. If not specified no modules are excluded. This value is processed after 'modulesIncluded' if both are specified.

    // ossIndexAudit can be configured to exclude vulnerabilities from matching
    excludeVulnerabilityIds =
        listOf("39d74cc8-457a-4e57-89ef-a258420138c5") // list containing ids of vulnerabilities to be ignored
    excludeCoordinates =
        listOf("commons-fileupload:commons-fileupload:1.3") // list containing coordinate of components which if vulnerable should be ignored

    // Output options
    outputFormat = "DEFAULT" // Optional, other values are: "DEPENDENCY_GRAPH" prints dependency graph showing direct/transitive dependencies, "JSON_CYCLONE_DX_1_4" prints a CycloneDX 1.4 SBOM in JSON format.
    cycloneDxComponentType = "LIBRARY" // Optional, only used when outputFormat = "JSON_CYCLONE_DX_1_4" to define the type of component this project is for the BOM metadata with possible values: "LIBRARY" (default), "APPLICATION", "FRAMEWORK", "CONTAINER", "OPERATING_SYSTEM", "DEVICE", "FIRMWARE" and "FILE".
    isColorEnabled = false // if true (and outputFormat = "DEFAULT") prints vulnerability description in color. By default is true.
    isShowAll = false // if true prints all dependencies. By default is false, meaning only dependencies with vulnerabilities will be printed.
    isPrintBanner = true // if true will print ASCII text banner. By default is true.
}
```

- Open Terminal on the project's root and run `./gradlew ossIndexAudit`
- You should see the audit result on Terminal.

### Nexus IQ Server Scan and Evaluate
- Start a local instance of IQ Server, or get the URL and credentials of a remote one.
- Configure IQ Server settings inside the `nexusIQScan` configuration on the file `build.gradle` e.g.

Groovy:
```
nexusIQScan {
    username = 'admin' // Make sure to use an user with the role 'Application Evaluator' in the given IQ Server application
    password = 'pass'
    serverUrl = 'http://localhost:8070'
    applicationId = 'app'
    organizationId = 'orgId' // Optional. If provided, a validation will be done to check if the given application ID exists under the organization ID (please note this is different than the organization name). If the application doesn't exists, then it will be created under the organization.
    stage = 'build' // build is used if omitted
    allConfigurations = false // if true includes the dependencies in all resolvable configurations. By default is false, meaning only 'compileClasspath', 'runtimeClasspath', 'releaseCompileClasspath' and 'releaseRuntimeClasspath' are considered
    resultFilePath = 'results.json' // Optional. JSON file containing results of the evaluation
    modulesExcluded = ['module-1', 'module-2'] // Optional. For multi-module projects, the names of the sub-modules to exclude from scanning and evaluation.
    dirExcludes = 'some-ant-pattern' // Optional. Comma separated ant-like glob patterns to select directories/archives that should be excluded. For Android projects we suggest using '**/classes.jar,**/annotations.zip,**/lint.jar,**/internal_impl-*.jar'
    dirIncludes = 'some-ant-pattern' // Optional. Comma separated ant-like glob patterns to select directories/archives that should be examined
}
```

Kotlin:
```
nexusIQScan {
    username = "admin" // Make sure to use an user with the role "Application Evaluator" in the given IQ Server application
    password = "pass"
    serverUrl = "http://localhost:8070"
    applicationId = "app"
    organizationId = "orgId" // Optional. If provided, a validation will be done to check if the given application ID exists under the organization ID (please note this is different than the organization name). If the application doesn"t exists, then it will be created under the organization.
    stage = "build" // build is used if omitted
    isAllConfigurations = false // if true includes the dependencies in all resolvable configurations. By default is false, meaning only "compileClasspath", "runtimeClasspath", "releaseCompileClasspath" and "releaseRuntimeClasspath" are considered
    resultFilePath = "results.json" // Optional. JSON file containing results of the evaluation
    modulesExcluded = listOf("module-1", "module-2") // Optional. For multi-module projects, the names of the sub-modules to exclude from scanning and evaluation.
    dirExcludes = "some-ant-pattern" // Optional. Comma separated ant-like glob patterns to select directories/archives that should be excluded. For Android projects we suggest using "**/classes.jar,**/annotations.zip,**/lint.jar,**/internal_impl-*.jar"
    dirIncludes = "some-ant-pattern" // Optional. Comma separated ant-like glob patterns to select directories/archives that should be examined
}
```

- Open Terminal on the project's root and run `./gradlew nexusIQScan`
- You should see the scan report URL report on Terminal.

### Nexus IQ Index
Allows you to save information about the dependencies of a project into module information (`module.xml`) files that Sonatype CI tools can use to include these dependencies in a scan.

- Open Terminal on the project's root and run `./gradlew nexusIQIndex`

For multi-module projects, you can configure a list of sub-modules to exclude from indexing.
Groovy:
```
nexusIQIndex {
     modulesExcluded = ['module-1', 'module-2'] // Optional. For multi-module projects, the names of the sub-modules to exclude from indexing.
}
```

Kotlin:
```
nexusIQIndex {
     modulesExcluded = listOf("module-1", "module-2") // Optional. For multi-module projects, the names of the sub-modules to exclude from indexing.
}
```

### Sensitive Data
Sometimes it's not desirable to keep sensitive data stored on `build.gradle`. For such cases it's possible to use project properties (-P arguments) or system properties (-D arguments or injected from a tool) from command line or environment variables when running the `nexusIQScan` or `ossIndexAudit` tasks.

Here is an example using project properties for the credentials, Groovy
```
nexusIQScan {
    username = project['username']
    password = project['password']
    serverUrl = 'http://localhost:8070'
    applicationId = 'app'
}

ossIndexAudit {
    username = project['username']
    password = project['password']
}
```

Kotlin:

```
nexusIQScan {
    username = project["username"]
    password = project["password"]
    serverUrl = "http://localhost:8070"
    applicationId = "app"
}

ossIndexAudit {
    username = project["username"]
    password = project["password"]
}
```

On command line:
```
./gradlew nexusIQScan -Pusername=admin -Ppassword=pass
```

```
./gradlew ossIndexAudit -Pusername=admin -Ppassword=pass
```

Each property name can be set as needed.

Here is an example using system properties for the credentials (Groovy):

```
nexusIQScan {
    username = System.properties['username']
    password = System.properties['password']
    serverUrl = 'http://localhost:8070'
    applicationId = 'app'
}

ossIndexAudit {
    username = System.properties['username']
    password = System.properties['password']
}
```

As mentioned above the values can be set on command line using -D arguments or injected via a tool (CI/CD for instance).

Finally this is how environment variables can be used (usually values are injected from the local environment or by a CI tool, Groovy):
```
nexusIQScan {
    username = System.getenv('username')
    password = System.getenv('password')
    serverUrl = 'http://localhost:8070'
    applicationId = 'app'
}

ossIndexAudit {
    username = System.getenv('username')
    password = System.getenv('password')
}
```

Kotlin version:
```
nexusIQScan {
    username = System.getenv("username")
    password = System.getenv("password")
    serverUrl = "http://localhost:8070"
    applicationId = "app"
}

ossIndexAudit {
    username = System.getenv("username")
    password = System.getenv("password")
}
```

### Multi-module projects
Just apply the plugin on the root project and all sub-modules will be processed and the output will be a single report
with all components found in each module. This includes Android projects.

## Contributing

We care a lot about making the world a safer place, and that's why we created this `scan-gradle-plugin`. If you as well want to speed up the pace of software development by working on this project, jump on in! Before you start work, create a new issue, or comment on an existing issue, to let others know you are!

Check the full contrubuting guidelines at: [CONTRIBUTING.md](./.github/CONTRIBUTING.md)

## The Fine Print

It is worth noting that this is **NOT SUPPORTED** by Sonatype, and is a contribution of ours
to the open source community (read: you!)

Remember:

* Use this contribution at the risk tolerance that you have
* Do NOT file Sonatype support tickets related to `scan-gradle-plugin` support in regard to this project
* DO file issues here on GitHub, so that the community can pitch in

Phew, that was easier than I thought. Last but not least of all:

Have fun creating and using `scan-gradle-plugin`, we are glad to have you here!

## Getting help

Looking to contribute to our code but need some help? There's a few ways to get information:

* Chat with us on [Gitter](https://gitter.im/sonatype/nexus-developers)
