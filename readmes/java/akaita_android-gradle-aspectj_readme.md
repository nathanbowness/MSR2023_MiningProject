# GradleAspectJ-Android
[![AspectJ](https://img.shields.io/badge/AspectJ-4.1.0-brightgreen.svg)](http://www.eclipse.org/aspectj/) [![Kotlin](https://img.shields.io/badge/Kotlin-1.3.72-blue.svg)](http://kotlinlang.org) [![Download](https://api.bintray.com/packages/akaita/android/android-gradle-aspectj/images/download.svg)](https://bintray.com/akaita/android/android-gradle-aspectj/_latestVersion)<br />
[![GitHub license](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg?style=flat)](http://www.apache.org/licenses/LICENSE-2.0)


***
*This is a temporary fork of https://github.com/Archinamon/android-gradle-aspectj , created just to quickly distribute v4.3.0* 
***

A Gradle plugin which enables AspectJ for Android builds.
Supports writing code with AspectJ-lang in `.aj` files and in java-annotation style.
Full support of Android product flavors and build types.
Support Kotlin, Groovy, Scala and any other languages that compiles into java bytecode.

Current version supporting of AGP 4.1.+: `com.akaita.android:android-gradle-aspectj:4.3.0`.<br />
<br />
Friendly with <a href="https://zeroturnaround.com/software/jrebel-for-android/" target="_blank">jRebel for Android</a>!

This plugin is completely friendly with <a href="https://bitbucket.org/hvisser/android-apt" target="_blank">APT</a> (Android Annotation Processing Tools) and <a href="https://github.com/evant/gradle-retrolambda/" target="_blank">Retrolambda</a> project (but Java 8 not supported in .aj files).
<a href="https://github.com/excilys/androidannotations" target="_blank">AndroidAnnotations</a>, <a href="https://github.com/square/dagger" target="_blank">Dagger</a> are also supported and works fine.

This plugin has many ideas from the others similar projects, but no one of them grants full pack of features like this one.
Nowadays it has been completely re-written using Transform API.

Key features
-----

Augments Java, Kotlin, Groovy bytecode simultaneously!<br />
Works with background mechanics of jvm-based languages out-of-box!<br />
[How to teach Android Studio to understand the AspectJ!](IDE)<br />
May not work properly for AS 3.0 :(

It is easy to isolate your code with aspect classes, that will be simply injected via cross-point functions, named `advices`, into your core application. The main idea is — code less, do more!

AspectJ-Gradle plugin provides supply of all known JVM-based languages, such as Groovy, Kotlin, etc. That means you can easily write cool stuff which may be inject into any JVM language, not only Java itself! :)

To start from you may look at my <a href="https://github.com/Archinamon/AspectJExampleAndroid" target="_blank">example project</a>. And also you may find useful to look at <a href="https://eclipse.org/aspectj/doc/next/quick5.pdf" target="_blank">reference manual</a> of AspectJ language and simple <a href="https://eclipse.org/aspectj/sample-code.html" target="_blank">code snippets</a>. In case aspectj-native not supported by Android Studio (even with IDE-plugin it's using is complicated), you may write a java-classes with aspectj annotations.

Two simple rules you may consider when writing aspect classes.
- Do not write aspects outside the `src/$flavor/aspectj` source set! These aj-classes will be excluded from java compiler.
- Do not try to access aspect classes from java/kotlin/etc. In case java compiler doesn't know anything about aspectj, it will lead to compile errors on javac step.

These rules affects only in case you're writing in native aj-syntax.
You may write aspects in java-annotation style and being free from these limitations.

Usage
-----

First add a maven repo link into your `repositories` block of module build file:
```kotlin
mavenCentral()
```
Don't forget to add `mavenCentral()` due to some dependencies inside AspectJ-gradle module.

Add the plugin to your `buildscript`'s `dependencies` section:
<details open><summary>Kotlin</summary>

```kotlin
classpath("com.akaita.android:android-gradle-aspectj:4.3.0")
```

</details>
<details><summary>Groovy</summary>

```groovy
classpath 'com.akaita.android:android-gradle-aspectj:4.3.0'
```

</details>

<br />
Apply the `aspectj` plugin:

<details open><summary>Kotlin</summary>

```kotlin
plugins {
    id("com.android.application")
    id("com.archinamon.aspectj")
}
```

</details>
<details><summary>Groovy</summary>

```groovy
plugins {
    id 'com.android.application'
    id 'com.archinamon.aspectj'
}
```

</details>

<br />
Now you can write aspects using annotation style or native (even without IntelliJ IDEA Ultimate edition).
Let's write simple Application advice:

```java
import android.app.Application;
import android.app.NotificationManager;
import android.content.Context;
import android.support.v4.app.NotificationCompat;

aspect AppStartNotifier {

    pointcut postInit(): within(Application+) && execution(* Application+.onCreate());

    after() returning: postInit() {
        Application app = (Application) thisJoinPoint.getTarget();
        NotificationManager nmng = (NotificationManager) app.getSystemService(Context.NOTIFICATION_SERVICE);
        nmng.notify(9999, new NotificationCompat.Builder(app)
            .setTicker("Hello AspectJ")
            .setContentTitle("Notification from aspectJ")
            .setContentText("privileged aspect AppAdvice")
            .setSmallIcon(R.drawable.ic_launcher)
            .build());
    }
}
```

Tune extension
-------
<details open><summary>Kotlin</summary>

```kotlin
aspectj {
    compileTests = true // default value

    ajc = "1.9.4" // default value
    java = JavaVersion.VERSION_1_7 // default value

    /* @see Ext plugin config **/
    includeAllJars = false // default value
    includeJar.addAll(arrayOf("design", "support-v4", "dagger")) // default is empty
    excludeJar.addAll(arrayOf("support-v7", "joda")) // default is empty
    extendClasspath = true // default value

    includeAspectsFromJar.addAll(arrayOf("my-aj-logger-lib", "any-other-libs-with-aspects")) // default is empty
    ajcArgs.apply {
        add("-warn:deprecation")
        add("-referenceInfo")
    }

    weaveInfo = true // default value
    debugInfo = false // default value
    addSerialVersionUID = false // default value
    noInlineAround = false // default value
    ignoreErrors = false // default value
    
    breakOnError = true // default value
    experimental = false // default value
    buildTimeLog = true // default value

    transformLogFile = "ajc-transform.log" // default value
    compilationLogFile = "ajc-compile.log" // default value
}
```

</details>
<details><summary>Groovy</summary>

```groovy
aspectj {
    dryRun false // default value
    compileTests true // default value

    ajc '1.9.4' // default value
    java = JavaVersion.VERSION_1_7 // default value

    /* @see Ext plugin config **/
    includeAllJars false // default value
    includeJar 'design', 'support-v4', 'dagger' // default is empty
    excludeJar 'support-v7', 'joda' // default is empty
    extendClasspath true // default value

    includeAspectsFromJar 'my-aj-logger-lib', 'any-other-libs-with-aspects'  // default is empty
    ajcArgs << '-referenceInfo' << '-warn:deprecation'

    weaveInfo true // default value
    debugInfo false // default value
    addSerialVersionUID false // default value
    noInlineAround false // default value
    ignoreErrors false // default value
    
    breakOnError true // default value
    experimental false // default value
    buildTimeLog true // default value

    transformLogFile 'ajc-transform.log' // default value
    compilationLogFile 'ajc-compile.log' // default value
}
```

</details>

<br />
Note that you may not include all these options!

All the extension parameters are have default values (all of them are described above, except of includeJar/Aspects/ajcArgs options).
So no need to define them manually.

- `compileTests` Workaround to disable `compileDebugUnitTestAspectJ` for unitTest variant

- `ajc` Allows to define the aspectj runtime jar version manually (1.8.12 current)
- `java` What jvmTarget will ajc use to compile bytecode into
- `extendClasspath` Explicitly controls whether plugin should mutate the classpath with aspectj-runtime itself

- `includeAllJars` Explicitly include all available jar-files into -inpath to proceed by AJ-compiler
- `includeJar` Name filter to include any jar/aar which name or path satisfies the filter
- `excludeJar` Name filter to exclude any jar/aar which name or path satisfies the filter
- `includeAspectsFromJar` Name filter to include any jar/aar with compiled binary aspects you wanna affect your project
- `ajcExtraArgs` Additional parameters for aspectj compiler

- `weaveInfo` Enables printing info messages from Aj compiler
- `debugInfo` Adds special debug info in aspect's bytecode
- `addSerialVersionUID` Adds serialVersionUID field for Serializable-implemented aspect classes
- `noInlineAround` Strict ajc to inline around advice's body into the target methods
- `ignoreErrors` Prevent compiler from aborting if errors occurs during processing the sources

- `breakOnError` Allows to continue project building when ajc fails or throws any errors
- `experimental` Enables experimental ajc options: `-XhasMember` and `-Xjoinpoints:synchronization,arrayconstruction`. More details in <a href="https://github.com/Archinamon/GradleAspectJ-Android/issues/18" target="_blank">issue #18</a>

- `buildTimeLog` Appends a BuildTimeListener to current module that prints time spent for every task in build flow, granularity in millis

- `transformLogFile` Defines name for the log file where all Aj compiler info writes to, new separated for Transformer
- `compilationLogFile` Defines name for the log file where all Aj compiler info writes to, new separated for CompileTask

Extended plugin config
-----------------
<details open><summary>Kotlin</summary>

```kotlin
plugins {
    id("com.android.application")
    id("com.archinamon.aspectj-ext")
}
```

</details>
<details><summary>Groovy</summary>

```groovy
plugins {
    id 'com.android.application'
    id 'com.archinamon.aspectj-ext'
}
```

</details>

<br />
Ext config:
- allows usage of `includeJar` and `includeAllJars` parameters, with workaround to avoid `Multiple dex files exception`
- supports `multiDex`
- supports `Instrumented tests`

Currently it has some limitations:
- `InstantRun` must be switched off (Plugin detects IR status and fails build if IR will be found).

Provider plugin config
-----------------
<details open><summary>Kotlin</summary>

```kotlin
plugins {
    id("com.android.application")
    id("com.archinamon.aspectj-provides")
}
```

</details>
<details><summary>Groovy</summary>

```groovy
plugins {
    id 'com.android.application'
    id 'com.archinamon.aspectj-provides'
}
```

</details>

<br />
Plugin-provider may be useful for that cases when you need to extract aspect-sources into separate module and include it on demand to that modules where you only need it.
Therefor this behavior will save you build-time due to bypassing aspectj-transformers in provide-only modules.

You ain't limited to describe as much provider-modules as you need and then include them using `includeAspectsFromJar` parameter in the module which code or dependencies you may want to augment.

With <a href="https://github.com/Archinamon/AspectJExampleAndroid" target="_blank">example project</a> you could learn how to write such provider-module.

DryRun plugin config
-----------------
<details open><summary>Kotlin</summary>

```kotlin
plugins {
    id("com.android.application")
    id("com.archinamon.aspectj-dryRun")
}
```

</details>
<details><summary>Groovy</summary>

```groovy
plugins {
    id 'com.android.application'
    id 'com.archinamon.aspectj-dryRun'
}
```

</details>

<br />
Disables aspectj-compiler and transformation task for the hole project.

Working tests
-------
<details open><summary>Kotlin</summary>

```kotlin
plugins {
    id("com.android.application")
    id("com.archinamon.aspectj-junit")
}
```

</details>
<details><summary>Groovy</summary>

```groovy
plugins {
    id 'com.android.application'
    id 'com.archinamon.aspectj-junit'
}
```

</details>

<br />
Test scope overloads JUnit compilation flow with AJC instead of JavaC. So any aspects has been written within `test` directory will be compiled with all java sources and aspects will weave them if need. 

ProGuard
-------
Correct tuning will depends on your own usage of aspect classes. So if you declares inter-type injections you'll have to predict side-effects and define your annotations/interfaces which you inject into java classes/methods/etc. in proguard config.

Basic rules you'll need to declare for your project:
```
-adaptclassstrings
-keepattributes InnerClasses, EnclosingMethod, Signature, *Annotation*

-keepnames @org.aspectj.lang.annotation.Aspect class * {
    ajc* <methods>;
}
```

If you will face problems with lambda factories, you may need to explicitly suppress them. That could happen not in aspect classes but in any arbitrary java-class if you're using Retrolambda.
So concrete rule is:
```
-keep class *$Lambda* { <methods>; }
-keepclassmembernames public class * {
    *** lambda*(...);
}
```

Changelog
---------
#### 4.3.0 -- Support AGP 4.1.+
* this release supports agp 4.1.+ but earlier versions not;

#### 4.2.1 -- Improve jar archives
* better api for AGP 4.0.+;
* fix java.lang.NoClassDefFoundError: Failed resolution of: Landroidx/appcompat/R$drawable;

#### 4.2.0 -- Support AGP 4.0.+
* this release supports agp 4.0.+ but earlier versions not;

#### 4.1.0 -- Support AGP 3.6.+
* this release supports agp 3.6.+ but earlier versions not;

#### 4.0.1 -- Fix synchronous run
* fixed async running of ajc (which is not supporting async compiling);

#### 4.0.0 -- Support AGP 3.5.+
* this release supports agp 3.5.+ but earlier versions not;

#### 3.4.5 -- Fix for Gradle 6.0
* create task explicitly instead of `project.task()`;

#### 3.4.3 -- Once more fix :(
* hotfixed provides plugin mode — transformation should not starts;

#### 3.4.2 -- Hotfix provides
* hotfixed provides plugin mode — transformation should not starts;

#### 3.4.1 -- Fix provides
* fixed aspectj-provides plugin mode — do not cleanup destination dir;

#### 3.4.0 -- Better DryRun mode
* fixed support of 3.5.0 Android Gradle Plugin — thanks to @superafroman;
* remove aj runtime check;
* standalone DryRun plugin mode to avoid transformation and compilation steps;

#### 3.3.12 -- Fix 'Dependencies resolution fail'
* fixed rare bug — 'failed to attach configuration after dependencies has been resolved';
* better properties extraction within kts script; 

#### 3.3.11 -- Fix legacy AGP support
* better legacy support — fixed AGP 3.1.4 compatibility;

#### 3.3.10 -- Update AJC
* bump aspectj compiler version;

#### 3.3.9 -- Small fix dryRun
* to prevent aj transformation with empty outputs — use `-PdryRunAjc=true`;

#### 3.3.8 -- Fix unitTest variant
* added workaround to disable unitTest aj compile step if classpath is broken;

#### 3.3.7 -- Fixes ext plugin
* fixed `aspectj-ext` plugin to work properly with transform api;
* added transform output dir to inPath;
* fix ajc inPath for compilation step;

#### 3.3.6 -- Fixes
* fix dryRun option for transformer;
* better readme;

#### 3.3.5 -- Dry run
* fix classpath resolving;
* implement dry run to disable compiler/transformation in gradle;

#### 3.3.3 -- Support AGP 3.3.+
* fixed support AGP 3.3.+ api;
* added legacy compatibility fallbacks;
* added java bytecode target version for ajc;
* upgrade bundled ajc runtime and tools jars to 1.9.2;
* upgrade default aspectj runtime library to 1.9.2;

#### 3.3.0 -- JUnit tests support
* implementing `com.archinamon.aspectj-junit` plugin supporting weaving unit tests;
* `com.archinamon.aspectj-test` has been removed as not working legacy sh$t;
* updated android-gradle-plugin to 3.2.0 inside (might be a breaking change);
* migration to Kotlin-DSL;
* new plugin tests allows to check does it weaves android's junit source code;

#### 3.2.0 -- Gradle 3.0.0 support
* added support of stable gradle plugin 3.0.0;
* updated internal ajc and provided aj runtime library versions to the latest 1.8.12;

#### 3.1.1 -- Useful improvements
* added an extension trigger to append BuildTime logger for current module;
* back from grave — added exclude-filter for `aspectj-ext` plugin;

#### 3.1.0 -- Provider
* implemented `provides` plugin split to effectively extract aspects to external/sub modules;
* small code improvements and cleanups;

#### 3.0.3 -- Minor fixes
* fixed aar detecting mechanism;
* registered plugin in mavenCentral!

#### 3.0.0 -- Grand refactoring in Kotlin
* all groovy classes was obsolete;
* new code-base in Kotlin 1.1.1 stable;

#### 2.4.3 -- Hot-fixed  two-step compilation
* compiled in first step aspect classes have not been copied to final output;

#### 2.4.2 -- Hot-fix
* fixed missed variable;
* fixed imports;

#### 2.4.0 -- Added aspectj-ext plugin
* `includeJar` parameter now able to read aar's manifest file to exactly detect required library;
* `com.archinamon.aspectj-ext` plugin added to properly weave inpath jars, in this mode InstantRun doesn't allowed;
* small fixes and package/name refactoring;

#### 2.3.1 -- New two-step build mechanic
* renamed extension parameter: ajcExtraArgs -> ajcArgs;
* split parameter: logFileName -> [transformLogFile, compilationLogFile];
* added separate compile task to build all sources under `/aspectj` folder;
* aj-transformer now looks into `/build/aspectj/$variantName` folder for aspects class';
* updated ajc-version to 1.8.10;
* fixed issue with missing error printing to Messages when failing;
* added inpath/aspectpath clearance before emitting transform inputs (by @philippkumar);

#### 2.3.0 -- Major fixes
* InstantRun support;
* fails androidTest hot launch;
* ZipException within augmenting third party libraries via AspectJ;
* more clear logging and errors emitting;

#### 2.2.2 -- Improvements
* fixed build config namings;
* re-designed work with log file and errors handling;
* pretty formatting ajc arguments for build stdout;
* implemented handling custom ajc arguments via build.gradle config;

#### 2.2.1 -- Hot-fix
* fixed illegal 'return' statement;
* change included in `updated` 2.2.0 artifacts;

#### 2.2.0 -- Ajc fixes and improvements
* fixed problem with -aspectPath building project with multidex;
* fixed scope problems with Transform API;
* removed Java 8 support;
* implemented clear and easy way to attach compiled aspects via jar/aar;
* implemented more easy way to weave by aspects any library (jar/aar);
* implemented breaking build on errors occurring to prevent runtime issues;
* implemented ajc experimental features: -XhasMember and -Xjoinpoints:synchronization,arrayconstruction;
* implemented more logic way to detect the plugin placement in build file to support retrolambda correctly;
* code cleanups and improvements;

#### 2.1.0 -- Transform api fix
* finally fixed errors with multidex;
* fixed jar merge errors;
* fixed errors with new gradle plugin;
* fixed Java 8 support;
* fixed Retrolambda compatibility;

#### 2.0.4 -- Small fix
* fixed error with mandatory default aj-directory;

#### 2.0.3 -- Gradle instant run
* merged pull request with the latest gradle plugin update;
* fixed errors after update;

#### 2.0.2 -- Fixed filters
* problem with empty filters now fixed;

#### 2.0.1 -- Hotfix :)
* proper scan of productFlavors and buildTypes folders for aj source sets;
* more complex selecting aj sources to compile;
* more precise work with jars;
* changed jar filter policy;
* optimized weave flags;

#### 2.0.0 -- Brand new mechanics
* full refactor on Transform API;
* added new options to aspectj-extension;

#### 1.3.3 -- Rt qualifier
* added external runtime version qualifier;

#### 1.3.2 -- One more fix
* now correctly sets destinationDir;

#### 1.3.1 -- Hot-fixes
* changed module name from `AspectJ-gradle` to `android-gradle-aspectj`;
* fixed couple of problems with test flavours processing;
* added experimental option: `weaveTests`;
* added finally post-compile processing for tests;

#### 1.3.0 -- Merging binary processing and tests
* enables binary processing for test flavours;
* properly aspectpath and after-compile source processing for test flavours;
* corresponding sources processing between application modules;

#### 1.2.1 -- Hot-fix of Gradle DSL
* removed unnecessary parameters from aspectj-extension class;
* fixed gradle dsl-model;

#### 1.2.0 -- Binary weaving
* plugin now supports processing .class files;
* supporting jvm languages — Kotlin, Groovy, Scala;
* updated internal aj-tools and aj runtime to the newest 1.8.9;

#### 1.1.4 -- Experimenting with binary weaving
* implementing processing aars/jars;
* added excluding of aj-source folders to avoid aspects re-compiling;

#### 1.1.2 -- Gradle Instant-run
* now supports gradle-2.0.0-beta plugin and friendly with slicer task;
* fixed errors within collecting source folders;
* fixed mixing buildTypes source sets;

#### 1.1.1 -- Updating kernel
* AspectJ-runtime module has been updated to the newest 1.8.8 version;
* fixed plugin test;

#### 1.1.0 -- Refactoring
* includes all previous progress;
* updated aspectjtools and aspectjrt to 1.8.7 version;
* now has extension configuration;
* all logging moved to the separate file in `app/build/ajc_details.log`;
* logging, log file name, error ignoring now could be tuned within the extension;
* more complex and correct way to detect and inject source sets for flavors, buildTypes, etc;

#### 1.0.17 -- Cleanup
* !!IMPORTANT!! now correctly supports automatically indexing and attaching aspectj sources within any buildTypes and flavors;
* workspace code refactored;
* removed unnecessary logging calls;
* optimized ajc logging to provide more info about ongoing compilation;

#### 1.0.16 -- New plugin routes
* migrating from corp to personal routes within plugin name, classpath;

#### 1.0.15 -- Full flavor support
* added full support of build variants within flavors and dimensions;
* added custom source root folder -- e.g. `src/main/aspectj/path.to.package.Aspect.aj`;

#### 1.0.9 -- Basic flavors support
* added basic support of additional build variants and flavors;
* trying to add incremental build //was removed due to current implementation of ajc-task;

#### 1.0 -- Initial release
* configured properly compile-order for gradle-Retrolambda plugin;
* added roots for preprocessing generated files (needed to support Dagger, etc.);
* added MultiDex support;
 
#### Known limitations
* You can't speak with sources in aspectj folder due to excluding it from java compiler;
* Doesn't support gradle-experimental plugin;

All these limits are fighting on and I'll be glad to introduce new build as soon as I solve these problems.

License
-------

    Copyright 2015 Eduard "Archinamon" Matsukov.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
