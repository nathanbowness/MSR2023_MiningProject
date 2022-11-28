# Octopus Deploy Jenkins Plugin #
Connecting [Octopus Deploy](https://octopusdeploy.com/) to the [Jenkins](https://jenkins-ci.org/) workflow.

Using Jenkins and Octopus Deploy together, you can:

  Use Jenkins to compile, test, and package your applications.
- Automatically trigger deployments in Octopus from Jenkins whenever a build completes.
- Automatically fail a build in Jenkins if the deployment in Octopus fails.
- Securely deploy your applications with Octopus Deploy across your infrastructure.
- Fully automate your continuous integration and continuous deployment processes.
Octopus Deploy will take those packages and push them to development, test, and production environments.

Please visit the Octopus Deploy [Freestyle](https://g.octopushq.com/JenkinsPluginDocumentation) or [Pipeline](https://g.octopushq.com/JenkinsPluginPipelineDocumentation) documentation for help getting started, or the [Jenkins guides](https://g.octopushq.com/GuidesJenkins) for step by step instructions on deploying applications from Jenkins to Octopus.

Support is available from the [official Octopus Deploy support channels](https://g.octopushq.com/HelpGeneral).

## Upgrading from 1.x to 2.x ##
The way the plugin interacts with Octopus changed from version 1.x to 2.x. Some additional configuration is required after upgrading to 2.x. See the documentation for the steps required to [install the Octopus CLI](https://octopus.com/docs/packaging-applications/build-servers/jenkins#octopus-cli). Once the Octopus CLI has been installed, check existing Octopus steps to ensure they are configured correctly.

## Contributing to the plugin ##

We welcome contributions; issues, bug fixes, enhancements. If you are starting to work on something more detailed please reach out to support@octopus.com to ensure it aligns with what we have going on, and that we are not doubling up efforts.

We have the following [developer focussed guidelines](./developer-guide.md) to get started working on the plugin.


