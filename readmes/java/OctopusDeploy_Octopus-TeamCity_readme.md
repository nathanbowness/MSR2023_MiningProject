This plug-in allows TeamCity builds to trigger deployments in Octopus Deploy.

## Get the plugin

Download the plugin from [the Octopus Deploy downloads page](http://octopusdeploy.com/downloads) or
the [JetBrains plugins downloads](<https://plugins.jetbrains.com/plugin/9038-octopus-deploy>).

Installation and usage instructions are available
in [the Octopus Deploy documentation](http://octopusdeploy.com/documentation/integration/teamcity).

## Building

To build the plugin from code:

1. Install the latest version of the JDK (plugin is build/runnable in Java-8 and above)
2. Install TeamCity
4. Run `gradlew clean distZip`  
   The `gradlew` script will download Gradle for you if it is not already installed.
5. The plugin is available at `build/distributions/Octopus.TeamCity.<X.Y.Z>.zip` (where X.Y.Z is the
   SemVer of the release, potentially including 'SNAPSHOT').

## Editing and debugging in IntelliJ

1. Set the following environment variables to enable debug into Server/Agent and also enable
   "devMode" in the server, which expedites development by allowing 'hot-reload' of both plugins and
   Java Server Pages (JSP files). It also ensures the new Octopus Step Vnext is available
   (feature flagged).
    1. TEAMCITY_SERVER_OPTS=-Dteamcity.development.mode=true -agentlib:
       jdwp=transport=dt_socket,server=y,suspend=n,address=*:5011 -Denable.step.vnext=true
    1. TEAMCITY_AGENT_OPTS=-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5010
1. Install TeamCity locally to `C:\TeamCity`. Allow the service to start for the first time, and add
   an admin user. Then stop the service so it is not running.
1. Give yourself full permissions to the Teamcity Data folder (usually
   `C:\ProgramData\JetBrains\TeamCity`). This folder may be hidden.
1. Import the Gradle project into IntelliJ.
1. Two Run Configurations 'AttachToServer' and 'AttachToAgent' should already exist - and allow the
   IDE to connect to running, debug-enabled

Start a Teamcity server and agent manually, then install the built plugin via the administration->
plugins menu option.

You can then attach to the server/agent via the provided run-configurations, and step through the
plugin code when build steps are configured (on server) or executed (on agent).

## Build Server
The TeamCity Plugin uses Github actions for all CI/CD/Release operations.

## Updating the version of Octopus CLI we embed

If the Octopus CLI has changed such that we need to update the version we embed with the plugin the
steps are as follows:

- Locate the build in TeamCity and navigate to the Artifacts tab
- Expand the OctopusTools.*version*.nupkg file
- Download `octo.exe` from the `tools` directory. Also download the OctopusTools.*version*
  .portable.zip file
  ![Artifacts](artifacts.png)
- Rename the latter to `OctopusTools.portable.zip` and then copy them into
  the `\octopus-agent\src\main\resources\resources\3\0` folder, over the existing files

## Using Docker

Some docker files have been provided to assist development for users who may not have all the
prerequisite tooling available on their local machine for development. This process will currently
be slower and does not provide the benefits of debugging at this point in time.

1. Run `docker-compose -f docker-compose.teamcity.yml up -d` to allow the TeamCity server and agent
   spin up. This will take some time to initialize and will store the configuration files
   under `./docker-files`. This will allow for both restarting the server without the full
   initialization and to pass in the Octopus plugin.
2. Once the server has started navigate, to the instance via http://localhost:8111 and create an
   admin login (this setup only needs to take place once due to the configuration mount). Once the
   server starts up, navigate to `Agents`->`Unauthorized` and authorise the agent that was started
   in a container alongside the server.
3. Build the plugin by running `docker-compose -f docker-compose.build.yml up`. This will use a
   gradle image, mount the current directory and invoke the `gradlew` command described above. At
   the end of the build the plugin will be copied into the TeamCity plugins directory created by the
   container in the previous step.
4. Once the plugin has been built, you will need to restart the server by running (depending on your
   environment) `docker restart octopus-teamcity_teamcity-server_1`.
5. When testing with a connection to an Octopus Server instance on your local host instance, you can
   use the special `host.docker.internal` route. e.g. http://host.docker.internal:8065

## End-2-End Tests

An E-2-E testing suite has been created and can be executed by running `./gradlew e2eTest`.

The test suite starts a (clean) OctopusDeploy server, then starts a TeamCity Server using a
pre-canned data directory, populated with a project containing build configurations.

The teamcity-rest-client is then used to trigger a specific build in the project, and the test
runner monitors the OctopusDeploy instance (via the java-sdk) to ensure expected resources are
created - thus, the test-code understands the content of the pre-canned project/build being
executed.

To create a new test the following must be performed:

* In Teamcity, create a project/build containing necessary build step(s)
* In Teamcity, export the project to zip file (from Project->Actions->Export) and add the file to
  the e2etest resources
* Write a junit test which loads the newly created project file into the team-city data directory,
  executes the build, then queries OctopusDeploy for outcomes.

## Versioning, Releasing and Publishing
### Versioning
The `gradle.properties` specifies the version of the TeamCity plugin - typically with a
"SNAPSHOT" postfix (which gives all local builds a SNAPSHOT version).

To create a release version:
1. Update the version in `gradle.properties` to remove "-SNAPSHOT" postfix
1. Create a PR in github for version increment, and merge once approved
1. Create a Release in github
    - Create a new tag as part of release - tag name should match version in gradle.properties
    - The release/tag must reference the commit created in prior bullet point
    - Populate the 'Description' field of the release with changes since last
    - Save the release (do NOT check pre-release checkbox)
1. Increment the version in `gradle.properties`, adding "-SNAPSHOT" postfix
1. Create a PR in github for the increments, and merge once approved
1. ... Develop features, then rinse and repeat.

### Publishing
Creating the release in github will trigger
the [release](https://raw.githubusercontent.com/OctopusDeploy/Octopus-TeamCity/master/.github/workflows/release.yml)
github action, which will build and test the release, before sending the built plugin zip file and
creating a release in OctopusDeploy.

The created package can be published to the JetBrains Marketplace via [Octopus Deploy]
(https://deploy.octopus.app).
Specifically, when the [TeamCity Plugin](https://deploy.octopus.
app/app#/Spaces-62/projects/teamcity-plugin/deployments) is promoted from "Components - 
Internal" to 'Components External', a script is executed which pushes the package to Jetbrains.
