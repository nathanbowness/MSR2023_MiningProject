<div align="center">
  <img src="img/github_banner.png" />
</div>
<h1 align="center"><a href="https://twitter.com/intent/tweet?text=Checkout%20PackageHunter%3A%20Android%20library%20to%20hunt%20down%20package%20information.%F0%9F%98%8E&url=https://github.com/nisrulz/packagehunter&via=nisrulz&hashtags=AndroidDev">
        <img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"/>
    </a></h1>

<div align="center">
  <strong>Android library to hunt down package information.</strong>
  <p>The library is built for simplicity and approachability. It not only eliminates most boilerplate code for dealing with package information, but also provides an easy and simple API to retrieve them and associated data.</p>
</div>
<br/>
<div align="center">
    <!-- Bintray -->
    <a href="https://bintray.com/nisrulz/maven/com.github.nisrulz%3Apackagehunter/_latestVersion">
        <img src="https://api.bintray.com/packages/nisrulz/maven/com.github.nisrulz%3Apackagehunter/images/download.svg"/>
    </a>
    <!-- API -->
    <a href="https://android-arsenal.com/api?level=14">
        <img src="https://img.shields.io/badge/API-14%2B-orange.svg?style=flat"/>
    </a>
    <!-- Android Arsenal -->
    <a href="https://android-arsenal.com/details/1/3815">
        <img src="https://img.shields.io/badge/Android%20Arsenal-PackageHunter-green.svg?style=true"/>
    </a>
     <!-- Android Dev Digest -->
    <a href="https://www.androiddevdigest.com/digest-101/">
        <img src="https://img.shields.io/badge/AndroidDev%20Digest-%23101-blue.svg"/>
    </a>
    <!-- GitHub stars -->
    <a href="https://github.com/nisrulz/packagehunter">
        <img src="https://img.shields.io/github/stars/nisrulz/packagehunter.svg?style=social&label=Star"/>
    </a>
    <!-- GitHub forks -->
    <a href="https://github.com/nisrulz/packagehunter/fork">
        <img src="hhttps://img.shields.io/github/forks/nisrulz/packagehunter.svg?style=social&label=Fork"/>
    </a>
    <!-- GitHub watchers -->
    <a href="https://github.com/nisrulz/packagehunter">
        <img src="https://img.shields.io/github/watchers/nisrulz/packagehunter.svg?style=social&label=Watch"/>
    </a>
    <!-- Say Thanks! -->
    <a href="https://saythanks.io/to/nisrulz">
        <img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"/>
    </a>
    <a href="https://www.paypal.me/nisrulz/5">
        <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
    </a>
    <br/>
     <!-- GitHub followers -->
    <a href="https://github.com/nisrulz/packagehunter">
        <img src="https://img.shields.io/github/followers/nisrulz.svg?style=social&label=Follow%20@nisrulz"/>
    </a>
    <!-- Twitter Follow -->
    <a href="https://twitter.com/nisrulz">
        <img src="https://img.shields.io/twitter/follow/nisrulz.svg?style=social"/>
    </a>
</div>

<div align="center">
    <a href="https://android.libhunt.com/newsletter/13">
        Also featured in Awesome Android Newsletter #Issue 13
    </a>
</div>

<div align="center">
  <sub>Built with ❤︎ by
  <a href="https://twitter.com/nisrulz">Nishant Srivastava</a> and
  <a href="https://github.com/nisrulz/packagehunter/graphs/contributors">
    contributors
  </a>
</div>
<br/>
<br/>


### App in Playstore
[![playstore](https://github.com/nisrulz/packagehunter/blob/master/img/google-play-store.png)](https://play.google.com/store/apps/details?id=github.nisrulz.projectpackagehunter)

![Sc1](https://github.com/nisrulz/packagehunter/blob/master/img/sc1.png) ![Sc2](https://github.com/nisrulz/packagehunter/blob/master/img/sc2.png) ![Sc3](https://github.com/nisrulz/packagehunter/blob/master/img/sc3.png) ![Sc4](https://github.com/nisrulz/packagehunter/blob/master/img/sc4.png)

# Changelog

Starting with `1.1.0`, Changes exist in the [releases tab](https://github.com/nisrulz/packagehunter/releases).

# Including in your project
PackageHunter is available in the Jcenter, so getting it as simple as adding it as a dependency
```gradle
compile 'com.github.nisrulz:packagehunter:{latest version}'
```
where `{latest version}` corresponds to published version in [ ![Download](https://api.bintray.com/packages/nisrulz/maven/com.github.nisrulz%3Apackagehunter/images/download.svg) ](https://bintray.com/nisrulz/maven/com.github.nisrulz%3Apackagehunter/_latestVersion)

# Simple example

Create an instance of `PackageHunter`
```java
PackageHunter packageHunter = new PackageHunter(context);
```
Next call an available function on the ***packageHunter*** instance such as
```java
String appName= packageHunter.getAppNameForPkg(packageName);
```

### Get information for

+ [Specific Package](https://github.com/nisrulz/packagehunter/wiki/Usage#specific-package)
+ [All Packages in Device](https://github.com/nisrulz/packagehunter/wiki/Usage#all-packages-in-device)
+ [Search for a Package](https://github.com/nisrulz/packagehunter/wiki/Usage#search-for-a-package)

### :page_with_curl: For more info , check the **[Wiki Docs](https://github.com/nisrulz/packagehunter/wiki/Usage)**

# Pull Requests
I welcome and encourage all pull requests. It usually will take me within 24-48 hours to respond to any issue or request. Here are some basic rules to follow to ensure timely addition of your request:
  1. Match coding style (braces, spacing, etc.) This is best achieved using CMD+Option+L (Reformat code) on Mac (not sure for Windows) with Android Studio defaults. The code style used in this project is from [Grandcentrix](https://github.com/grandcentrix/AndroidCodeStyle), so please use the same when editing this project.
  2. If its a feature, bugfix, or anything please only change code to what you specify.
  3. Please keep PR titles easy to read and descriptive of changes, this will make them easier to merge :)
  4. Pull requests _must_ be made against `develop` branch. Any other branch (unless specified by the maintainers) will get rejected.
  5. Check for existing [issues](https://github.com/nisrulz/packagehunter/issues) first, before filing an issue.  
  6. Have fun!

## Author & support
This project was created by [Nishant Srivastava](https://github.com/nisrulz/nisrulz.github.io#nishant-srivastava) but hopefully developed and maintained by many others. See the [the list of contributors here](https://github.com/nisrulz/packagehunter/graphs/contributors).

> If you appreciate my work, consider buying me a cup of :coffee: to keep me recharged :metal:
>  + [PayPal](https://www.paypal.me/nisrulz/5)
>  + Bitcoin Address: 13PjuJcfVW2Ad81fawqwLtku4bZLv1AxCL
>
> I love using my work and I'm available for contract work. Freelancing helps to maintain and keep [my open source projects](https://github.com/nisrulz/) up to date!

<img src="http://forthebadge.com/images/badges/built-for-android.svg" />
