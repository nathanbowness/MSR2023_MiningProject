Android Lint Plugin
===================
[![Build Status](https://api.travis-ci.org/SonarQubeCommunity/sonar-android.svg)](https://travis-ci.org/SonarQubeCommunity/sonar-android)

<img src="https://raw.github.com/SonarSource/sonar-android/master/logo-sonar-android-lint-plugin.png" width="300" height="359"/>

**Contributions are welcome. Join the effort !**

## Description
This plugin enhances the Java Plugin by providing the ability to import the Android Lint reports.
The idea is to visualize Android Lint errors directly in Sonar.

## Usage
* Most Android projects are compiled with Gradle, so if this is the case use the [SonarQube Scanner for Gradle](https://plugins.gradle.org/plugin/org.sonarqube) to analyse your Android project
* Tune the SonarQube quality profile by activating the Android Lint rules on which you'd like to see some issues reported into SonarQube
* Configure the Gradle project to execute the Android Lint engine before launching the SonarQube analysis
* Define in the Gradle project the property sonar.android.lint.report (default value points to : build/outputs/lint-results.xml) to specify the path to the Android Lint report
* Run your Analyzer command from the project root dir
* Follow the link provided at the end of the analysis to browse your project's quality in SonarQube UI (see: Browsing SonarQube)

A sample project is available on GitHub, can be [browsed](https://github.com/SonarSource/sonar-examples/tree/master/projects/languages/android/android-sonarqube-scanner) an be [downloaded](https://github.com/SonarSource/sonar-examples/zipball/master): /projects/languages/android/android-sonarqube-runner

## Compiling and Installing the plugin:
 - Install maven
 - Clone the repository
 - Compile and test the code, then generate the jar:
	-> run "mvn clean install" command in your terminal
 - copy the jar (in the new generated target folder) in <path_to_your_sonar_install>/extensions/plugins folder,
 - restart sonar

## Running an analyse:
1. On a Maven project
 - mvn sonar:sonar -Dsonar.profile="Android Lint" in your project

2. On another project using sonar-runner
 - Add this property to your sonar-project.properties
  -> sonar.profile=Android Lint

