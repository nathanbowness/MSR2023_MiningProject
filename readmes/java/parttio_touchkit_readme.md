# TouchKit for Vaadin

The easiest way of building a cross-platform mobile user interface for a Java application. Add support for smartphones and tablets in days instead of months, with the tools you are already using.

The master branch contains a Framework 8 compatible version which is not maintained by Vaadin Ltd, but just by community members.

To see how to set up a project using TouchKit and Vaadin 8, refer to this [TouchKit example project](https://github.com/parttio/touchkit-example).

## Features

 * Components designed for mobile usage
 * mobile optimized theme, built with GWT
 * Tools to compress widgetset better
 * home screen web app support (both for iOS and in "Google PWA" style manifest.json, which is now a W3 standard)
 * strong caching and offline mode support (must be developed with GWT), using cache manifest and service worker on Android

## Releases

Official releases for versions 3.x and 4.x are available at http://vaadin.com/addon/vaadin-touchkit

5.0 (V8 compatible) and forward available at https://vaadin.com/directory/component/touchkit

## Building TouchKit

    git clone https://github.com/parttio/touchkit.git
    cd touchkit
    mvn install

## Issue tracking & Contributions

This project is no longer maintained by Vaadin Ltd, but lives as a community effort here. Use this repository for tickets, pull requests and enhancement ideas.

## License

Version 5.x is distributed under [Apache 2](http://www.apache.org/licenses/LICENSE-2.0).
