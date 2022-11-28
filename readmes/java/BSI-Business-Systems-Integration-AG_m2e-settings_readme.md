# Eclipse Settings maven-plugin
Provide consistent Eclipse IDE settings for your team from a Maven POM.
The eclipse-settings-maven-plugin will copy formatting, findbugs and other plugin
settings from a centrally maintained settings JAR to your checked out workspace and
configure each project to use those settings.

 - configure once, set everywhere
 - version control your settings

Many thanks to [Olivier Nouguier](https://github.com/cheleb) for the
[first version of this plugin](https://github.com/cheleb/m2e-settings).
And many thanks to [Martijn Dashorst](https://github.com/dashorst) for the
[second version of this plugin](https://github.com/topicusonderwijs/m2e-settings).

This project is licensed under the [MIT license](https://github.com/BSI-Business-Systems-Integration-AG/eclipse-settings-maven-plugin/blob/bsi_release/LICENSE.txt).

### Table of Contents

 - [Configuration](#configuration)
 - [Building a release](https://github.com/BSI-Business-Systems-Integration-AG/eclipse-settings-maven-plugin/blob/bsi_release/readme.markdown#releasing)

## Configuration

There are three steps to configure the *Eclipse Settings maven-plugin*:

1. Create (and deploy) your own settings jar
2. Configure the *Eclipse Settings maven-plugin* in your project
3. Re-import the Maven projects in Eclipse

### Create your own settings jar

Create a project for your own settings jar. This project will only
contain the relevant Eclipse settings files for your plugins.

#### Create a Maven project

First create an empty Maven project, and put this in the POM to build
your settings jar (adjust the values for your own settings jar).

``` xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <prerequisites>
        <maven>3.3.1</maven>
    </prerequisites>
    <groupId>com.example.settings</groupId>
    <artifactId>eclipse-settings</artifactId>
    <packaging>jar</packaging>
    <build>
        <defaultGoal>package</defaultGoal>
        <resources>
            <resource>
                <directory>files</directory>
                <filtering>false</filtering>
                <includes>
                    <include>**/*</include>
                </includes>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

This configures Maven to look in the `files` folder for resources and
package them into the resulting jar.

#### Add your settings to the JAR

Now you can copy the various Eclipse settings from the `.settings`
folders into the files folder:

``` bash
$ ls settings-project/files
-rw-r--r--   1 dashorst  staff     55 Jul  7 17:52 edu.umd.cs.findbugs.plugin.eclipse.prefs
-rw-r--r--   1 dashorst  staff    529 Jul  7 17:52 org.eclipse.core.resources.prefs
-rw-r--r--   1 dashorst  staff    175 Jul  7 17:52 org.eclipse.jdt.apt.core.prefs
-rw-r--r--   1 dashorst  staff  31543 Jul  7 17:52 org.eclipse.jdt.core.prefs
-rw-r--r--   1 dashorst  staff  11723 Jul  7 17:52 org.eclipse.jdt.ui.prefs
-rw-r--r--   1 dashorst  staff     86 Jun 29 23:47 org.eclipse.m2e.core.prefs
-rw-r--r--   1 dashorst  staff    411 Jun 29 23:52 org.eclipse.wst.common.component
-rw-r--r--   1 dashorst  staff    167 Jun 29 23:52 org.eclipse.wst.common.project.facet.core.xml
-rw-r--r--   1 dashorst  staff    382 Jul  7 17:52 org.eclipse.wst.validation.prefs
-rw-r--r--   1 dashorst  staff    232 Jul  7 17:52 org.maven.ide.eclipse.prefs
```

You can repeat this every time a new version of Eclipse comes out, and
update all settings to new defaults.

#### Deploy to a Maven repository

Now you can upload the jar to a Maven repository using `mvn deploy`. Or
use the Maven release plugin to create releases of your settings jar.

### Configure Eclipse Settings maven-plugin in your project

The eclipse-settings-maven-plugin retrieves the Eclipse workspace settings from
its configuration which is similar to the [Maven Eclipse Plugin][1] configuration.
The easiest way to provide these settings is to create a resource JAR file and distribute that
from a Maven repository.

You then specify your 'settings JAR' file as a dependency to the
*eclipse-settings-maven-plugin*:

``` xml
<build>
    <pluginManagement>
        <plugins>
            ...
            <plugin>
                <groupId>org.eclipse.scout</groupId>
                <artifactId>eclipse-settings-maven-plugin</artifactId>
                <version>3.0.3</version>
                <dependencies>
                    <dependency>
                        <groupId>com.example.settings</groupId>
                        <artifactId>eclipse-settings</artifactId>
                        <version>1.0</version>
                    </dependency>
                </dependencies>
            </plugin>
            ...
        </plugins>
    </pluginManagement>
</build>
```

This is not specific to this plugin at all, but do not forget that maven uses all declared `pluginRepository` entries to fetch dependencies for plugins. If the JAR you are getting the pref files from is not present in maven central (which is used by default), then you will need to add a `<pluginRepositories>..</pluginRepositories>` section in your POM or in your `settings.xml` file. 

As the plugin needs to be bound to a Maven lifecycle you also need to
specify the eclipse-settings-maven-plugin in your build. At the minimum you'll
need:

``` xml
<build>
    <plugins>
        ...
        <plugin>
            <groupId>org.eclipse.scout</groupId>
            <artifactId>eclipse-settings-maven-plugin</artifactId>
            <executions>
              <execution>
                <id>attach-eclipse-settings</id>
                <goals>
                  <goal>eclipse-settings</goal>
                </goals>
              </execution>
            </executions>
        </plugin>
        ...
    </plugins>
</build>
```

#### Putting the settings in the right place

The *eclipse-settings-maven-plugin* allows you to [move settings files from one
location to another][2]. You use that to put each configuration file
from your settings JAR in the right location:

``` xml
<build>
    <pluginManagement>
        <plugins>
            ...
            <plugin>
            <...>
            <configuration>
                <additionalConfig>
                    <file>
                        <name>.settings/org.eclipse.jdt.core.prefs</name>
                        <location>/org.eclipse.jdt.core.prefs</location>
                    </file>
                    <file>
                        <name>.settings/org.eclipse.jdt.ui.prefs</name>
                        <location>/org.eclipse.jdt.ui.prefs</location>
                    </file>
                    <!-- and more... -->
                </additionalConfig>
            </configuration>
            </plugin>
            ...
        </plugins>
    </pluginManagement>
</build>
```

#### Skipping the plugin execution

The plugin has a 'skip' configuration parameter to block the configuration of a project.
This can be useful to disable a configuration made in the the parent pom at child pom level.
Example:

``` xml
<build>
  <plugins>
    ...
    <plugin>
      <groupId>org.eclipse.scout</groupId>
      <artifactId>eclipse-settings-maven-plugin</artifactId>
      <configuration>
        <skip>true</skip>
      </configuration>
    </plugin>
    ...
  </plugins>
</build>
```

### Re-import projects in Eclipse

Now we have modified the projects, you have to re-import the projects
in Eclipse. Typically this is done by:

 - selecting all projects,
 - right-clicking on the selection and
 - clicking "Maven → Update project"

## Releasing __(TODO)__

If you are a developer of this project and have made some modifications use
this guide to build a release to distribute it to the users.

### Building a release

Run the release shell script from the root folder of the m2e-settings
project:

``` bash
./release.sh
```

This script performs the following steps:

- assign a new release version number to the current workspace
- create a new distribution of the new version in the current workspace
- create an updated P2 repository in the current workspace
- commit all these results into the git repository

This doesn't push the intermediate results to github, this is a manual
step you have to do to release a new version.

## Uploading a release

When you have checked the release and it is found OK, then you can
upload the new version to github and instruct your team to perform an
update:

```
git push
```

This will push the changes to github and publish a new update site to
the update site URL.


[1]: http://maven.apache.org/plugins/maven-eclipse-plugin
[2]: http://maven.apache.org/plugins/maven-eclipse-plugin/eclipse-mojo.html#additionalConfig
