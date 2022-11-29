### Overview

![sample2](images/sample2.png "MapViewer Sample2")
![sample2](images/sample5.png "MapViewer Sample5")

This project is based on the JXMapViewer component of SwingX-WS.

The project was hosted at SwingLabs.org, but has been discontinued. We extracted the JXMapViewer part from the latest SwingX-WS version available and continue developing it.

The JXMapViewer Tutorial by Joshua Marinacci provided a good overview over the functionality of the component, which is now gone from java.net but available on [archive.org](https://web.archive.org/web/20100309081606/http://today.java.net/pub/a/today/2007/10/30/building-maps-into-swing-app-with-jxmapviewer.html). Please have a look at the [examples section](https://github.com/msteiger/jxmapviewer2/tree/master/examples/src) in addition.

The content of this project are also available at [Maven Central](https://mvnrepository.com/artifact/org.jxmapviewer/jxmapviewer2) and can be referenced in your `pom.xml` with the following coordinates:

```xml
<dependency>
    <groupId>org.jxmapviewer</groupId>
    <artifactId>jxmapviewer2</artifactId>
    <version>2.5</version>
</dependency>
```

### Examples

You can find some examples as part of this source code repository. You can open them as a separate project in your IDE and run them there.
Alternatively, they can be run from the command line after creating a Maven package from them.

```bash
$ mvn clean package
$ java -cp target/jxmapviewer2-examples-2.5.jar sample1_basics.Sample1
```

### GeoPackage data

An example on how to integrate GeoPackage data has been implemented here: https://github.com/msteiger/jxmapviewer2/pull/122

### History

This source code used in this project is based on: 

 * SwingX-ws-2009_06_14.jar formerly hosted at java.net/projects/swingx
 * SwingX 1.6.3 (released Feb 2012) formerly hosted at java.net/projects/swingx-ws

This is what we have done so far ...

 * Extract the JXMapViewer part from the full package
 * Upgrade to Java 6 (version 2.1)
 * Upgrade to Java 7 (version 2.5)
 * Fixed javadoc
 * Replaced `system.out.println()` with `apache.commons.logging` 
 * Removed broken TileProviders
 * Remove dependencies to SwingX (and its indirect dependencies)
 * Fixed tile caching so that only tiles are cached, not everything
 * Extract user interaction from the viewer
 * Make CompoundPainter use Lists instead of Arrays
 * Find out what the "Java One" hack is and replace it with proper implementation
 * Improved zooming in - images of coarser resolution are used until new images are loaded
 * Fixed thread leak when setting new TileFactory
 * Supports OSGi bundles (contains MANIFEST.MF)
 * Supports Maven dependency management
 * Fixed use of deprecated code
 * Fix bugs that were posted on java.net/jira/browse/SWINGX_WS

### License
This project has been licensed under the GNU Lesser General Public License (LGPL)

