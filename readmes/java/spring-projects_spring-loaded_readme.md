# Welcome to Spring-Loaded

## What is Spring Loaded?

Spring Loaded is a JVM agent for reloading class file changes whilst a JVM is running.  It transforms
classes at loadtime to make them amenable to later reloading. Unlike 'hot code replace' which only allows
simple changes once a JVM is running (e.g. changes to method bodies), Spring Loaded allows you
to add/modify/delete methods/fields/constructors. The annotations on types/methods/fields/constructors
can also be modified and it is possible to add/remove/change values in enum types.

Spring Loaded is usable on any bytecode that may run on a JVM, and is actually the reloading system
used in Grails 2,3,4 (on java 8).

# Installation

1.3.0 has now been released!

1.3.0 Enables support for Grails 4.0.4+ Running on Java 8 (Java 11 is not yet supported and is in Development)

1.2.6 snapshots are in this repo area (grab the most recently built .jar):
<a href="https://repo.spring.io/webapp/#/artifacts/browse/tree/General/libs-snapshot-local/org/springframework/springloaded/1.2.6.BUILD-SNAPSHOT">repo.spring.io</a>

The download is the agent jar and needs no further unpacking before use.




# Running with reloading

	java -javaagent:<pathTo>/springloaded-{VERSION}.jar -noverify SomeJavaClass

The verifier is being turned off because some of the bytecode rewriting stretches the meaning of
some of the bytecodes - in ways the JVM doesn't mind but the verifier doesn't like.  Once up and
running what effectively happens is that any classes loaded from jar files (dependencies) are not
treated as reloadable, whilst anything loaded from .class files on disk is made reloadable. Once
loaded the .class file will be watched (once a second) and should a new version appear
SpringLoaded will pick it up. Any live instances of that class will immediately see the new form
of the object, the instances do not need to be discarded and recreated.

No doubt that raises a lot of questions and hopefully a proper FAQ will appear here shortly! But in
the meantime, here are some basic Qs and As:

Q. Does it reload anything that might change in a class file?
A. No, you can't change the hierarchy of a type. Also there are certain constructor patterns of
usage it can't actually handle right now.

Q. With objects changing shape, what happens with respect to reflection?
A. Reflection results change over time as the objects are reloaded.  For example, modifying a class
with a new method and calling `getDeclaredMethods()` after reloading has occurred will mean you see
the new method in the results. *But* this does mean if you have existing caches in your system
that stash reflective information assuming it never changes, those will need to be cleared
after a reload.

Q. How do I know when a reload has occurred so I can clear my state?
A. You can write a plugin that is called when reloads occur and you can then take the appropriate
action.  Create an implementation of `ReloadEventProcessorPlugin` and then register it via
`SpringLoadedPreProcessor.registerGlobalPlugin(plugin)`. (There are other ways to register plugins,
which will hopefully get some documentation!)

Q. What's the state of the codebase?
A. The technology is successfully being used by Grails for reloading. It does need some performance
work and a few smacks with a refactoring hammer. It needs upgrading here and there to tolerate
the invokedynamic instruction and associated new constant pool entries that arrived in Java 7.

# Working with the code

	git clone https://github.com/spring-projects/spring-loaded

Once cloned there will be some projects suitable for import into eclipse. The main project and
some test projects. One of the test projects is an AspectJ project (containing both Java
and AspectJ code), and one is a Groovy project. To compile these test projects
in Eclipse you will need the relevant eclipse plugins:

AJDT: update site: `https://download.eclipse.org/tools/ajdt/42/dev/update`
Groovy-Eclipse: update site: `https://dist.springsource.org/snapshot/GRECLIPSE/e4.2/`

After importing them you can run the tests.  There are two kinds of tests, hand crafted and
generated.  Running all the tests including the generated ones can take a while.
To run just the hand crafted ones supply this to the JVM when launching the tests:

    -Dspringloaded.tests.generatedTests=false

NOTE: When running the tests you need to pass `-noverify` to the JVM also.

Two launch configurations are already included if you are importing these projects into eclipse,
which run with or without the generated tests.

A gradle build script is included, run './gradlew build' to rebuild the agent - it will be created
as something like: `springloaded/build/libs/springloaded-1.3.0.BUILD-SNAPSHOT.jar`

# Can I contribute?

Sure! This is based on the original Spring Source Project work done by Andy Clement. As Spring was moving away from spring-loaded in favor of spring-dev-tools (a more basic alternative), Community efforts were made to update spring-loaded to work in more recent builds of Grails.
