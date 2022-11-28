# AdColony Android SDK
* Modified: June 7th, 2022
* SDK Version: 4.8.0

## Overview
AdColony delivers zero-buffering, [full-screen, Instant-Play™ HD video](https://www.adcolony.com/technology/instant-play/), [interactive Aurora™ Video](https://www.adcolony.com/technology/auroravideo/), and Aurora™ Playable ads that can be displayed anywhere within your application. Our advertising SDK is trusted by the world’s top gaming and non-gaming publishers, delivering them the highest monetization opportunities from brand and performance advertisers. AdColony’s SDK can monetize a wide range of ad formats including in-stream/pre-roll, out-stream/interstitial and V4VC™, a secure system for rewarding users of your app with virtual currency upon the completion of video and playable ads.


## Release Notes

#### 4.8.0

* Added banner onShow callback
* Fixed ConcurrentModificationException

**Required update**
**Due to policy changes from Google, publishers are required to use SDK version 4.4.0 or above.**

*Note: SDK version 4.6.0 and above potentially requires Gradle Plugin version updates. See [this blog post](https://android-developers.googleblog.com/2020/07/preparing-your-build-for-package-visibility-in-android-11.html) for more information.*

Here is the link to the [release notes](https://github.com/AdColony/AdColony-Android-SDK/blob/master/CHANGELOG.md) for all the previous SDK versions.

## Getting Started 
To get started, here is the link to [Android SDK integration documentation](https://github.com/AdColony/AdColony-Android-SDK/wiki).

### Supporting 64-bit on Android
Version 3.3.7 and above no longer uses the .so libraries and these can be removed from your project. SDK 3.3.7 and above supports 64-bit without the .so libraries.

If you are using using earlier 3.x SDK versions you need to add the proper libadcolony.so and libjs.so architectures to your project to support 64-bit.

## Upgrade 
#### SDK 2.x:

Please note that updating from our 2.x SDK is not a drag and drop update, but rather includes breaking API and process changes. In order to take advantage of the 3.x SDK, a complete re-integration is necessary. Please review our [documentation](https://github.com/AdColony/AdColony-Android-SDK/wiki) to get a better idea on what changes will be necessary in your app.

#### SDK 3.x:
Update the AdColony library referenced by your project following the steps below:

**Manual**

* Drag and drop the adcolony.jar into your project.

**Via Gradle**

See our [project setup guide](https://github.com/AdColony/AdColony-Android-SDK/wiki/Project-Setup), update your 'dependencies' configuration within your module's build.gradle to point to the latest version:

```
dependencies {
  /** 
   * Any other dependencies your module has are placed in this dependency configuration
   */
  implementation 'com.adcolony:sdk:4.8.0'
}
```

## Legal Requirements
By downloading the AdColony SDK, you are granted a limited, non-commercial license to use and review the SDK solely for evaluation purposes.  If you wish to integrate the SDK into any commercial applications, you must register an account with AdColony and accept the terms and conditions on the AdColony website.

Note that U.S. based companies will need to complete the W-9 form and send it to us before publisher payments can be issued.

## Contact Us
For more information, please visit AdColony.com. For questions or assistance, please email us at support@adcolony.com.
