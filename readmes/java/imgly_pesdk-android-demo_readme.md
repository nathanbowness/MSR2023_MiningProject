<!-- ------------------------------------------------------- --|
 |-- ------------------------------------------------------- --|
 |-- ----This file is automatically generated by grovvy.---- --|
 |-- Do not modify this file -- YOUR CHANGES WILL BE ERASED! --|
 |-- ------------------------------------------------------- --|
 |-- ------------------------------------------------------- -->
<p align="center">
    <a target="_blank" href="https://img.ly/photo-sdk/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android&utm_term=Android"><img src="https://img.ly/static/logos/PE.SDK_Logo.svg" alt="PhotoEditor SDK Logo"/></a>
</p>
<p align="center">
  <a href="http://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels">
    <img src="https://img.shields.io/badge/MIN_SDK-21-B8D529.svg?style=flat">
    <img src="https://img.shields.io/badge/BUILD_SDK-31-92D230.svg?style=flat">
  </a>
  <a href="https://img.ly/docs/pesdk/android/introduction/getting_started">
    <img src="https://img.shields.io/badge/platform-android-2DC25C.svg?style=flat">
  </a>
  <a href="https://artifactory.img.ly/artifactory/imgly/ly/img/android/pesdk/">
    <img src="https://img.shields.io/badge/VERSION-10.4.2-007ec6.svg?style=flat" alt="Maven">
  </a>
  <a href="http://twitter.com/PhotoEditorSDK">
    <img src="https://img.shields.io/badge/twitter-@PhotoEditorSDK-8646E2.svg?style=flat" alt="Twitter">
  </a>
</p>



# About PhotoEditor SDK for Android

## Overview

The [PhotoEditor SDK](https://img.ly/photo-sdk/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android-Demo&utm_term=Android) is a powerful and multifaceted tool which enables you to equip your Android application with high-performant photo editing capabilities. The PhotoEditor SDK is written in Java and can easily be customized to entirely blend with your CI and provide your users with the exact feature set your use-case requires.

The SDK ships with a large variety of filters, covering all state of the art style- and mood settings that can be previewed in real-time. Unlike other apps that allow a live preview of filters, the [PhotoEditor SDK](https://img.ly/photo-sdk/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android-Demo&utm_term=Android) even provides a live preview when using high-resolution images.

All operations are non-destructive which allows for fast and uncomplicated revision of the creatives at any given time and creates an intuitive and creative workflow for your users. Please see Features for a detailed list of the photo editing tools included in the [PhotoEditor SDK](https://img.ly/photo-sdk/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android-Demo&utm_term=Android).



<a href="https://play.google.com/store/apps/details?id=com.photoeditorsdk.android.app&utm_source=global_co&utm_medium=prtnr&utm_content=Mar2515&utm_campaign=PartBadge&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1">
    <img height="60" alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/generic/en-play-badge-border.png" >
</a>

## License
The PhotoEditorSDK is a product of img.ly GmbH. Please make sure that you have a commercial [license](https://img.ly/pricing/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android-Demo&utm_term=Android) before releasing your app. A commercial license is required if you would like to integrate the SDK into any app, regardless of whether you monetize directly (paid app, subscription, service fee), indirectly (advertising, etc.) or are developing a free app. Every license for the PhotoEditor SDK is valid for one product only unless the products are closely related.

If you’d like to use the PhotoEditor SDK for a charitable project, you can do so free of charge. However, please contact us anyway, so we can evaluate whether you qualify for a non-commercial license or not and handle your request accordingly.

Please [get in touch](https://img.ly/pricing/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android-Demo&utm_term=Android) if you’d like to purchase a commercial license or require further information on our pricing and services. Please see the included [LICENSE.md](./LICENSE.md) for licensing details.


## Features

* Over 60 handcrafted **Filters** covering all state of the art style- and mood settings to choose from.
* Design custom filters in Photoshop and other apps: The API of the PhotoEditor SDK enables you to expand the filter library with your own set of custom filters to define a unique visual language. Custom filters can easily be created by anyone using LUTs (Lookup Tables) from popular apps like Photoshop, GIMP or Lightroom. Design your filter and apply it onto the provided identity image. That will 'record' the filter response, now simply save it and add it as a new filter. Done.
* An **Overlay** Tool that can be used to create neat lighting effects like lens flare or bokeh but also to furnish pictures with textures like crumpled paper or plaster. You can easily expand the library by importing your own set of overlay assets.
* An **Adjustment section** that holds both essential and advanced photo editing features like brightness, contrast, saturation, clarity etc. that help tweak and fine tune images to create stunning creatives.
* A **Transform section** that unifies cropping, flipping and rotation in one feature.
* The robust **Text Feature** provides all necessary functions for quickly adding text to any picture or creative. The corresponding font library can easily be exchanged, reduced, or expanded.
* A categorized **Sticker library** whose UI is optimized for exploration and discovery. You can easily complement the library with your own custom sticker packages.
* A **Frame Tool** that works with any given photo size or ratio.
* A high performant **Brush Engine** optimized for touch screen that supports different brush strokes.
* A **Photo Roll** equipped with a wide range of stock photography and templates with presorted categories. The API allows for easy expansion, reduction and rearrangement of the assets.
* A clean and intuitive **UI** that ensures an unhindered flow of creativity and a seamless experience while composing creatives. The UI is designed to be customized to completely match your CI and blend with your app.
* You can strip out every feature you deem unnecessary to provide your users with the exact feature set your use case requires.

* __Android API Level 21+__ Covers nearly 98% of all Android devices with touchscreen.
* __Fast image export up to 4294 MegaPixel__
* __Generic camera support__ for most Android phones.
* __Tablet support__: The PhotoEditor SDK uses auto layout for its views and adapts to each screen size.
* **Non/destructive features and effects:** Quickly revise, redo or even discard your work.


## SDK Core

__ACS Component__ <br/>
A generic Android Camera Stack library which is based on the [android.hardware.Camera](http://developer.android.com/reference/android/hardware/Camera.html) API. Supports front and rear cam, HDR, flash modes and much more.

__SDK Component__ <br/>
The PhotoEditor core library for Android. Containing the OpenGL and toolkit implementation.

__UI Component__ <br/>
The default UI components consisting of LivePreview and Editor Activity.


## Documentation

For a detailed documentation, please take a look [here](https://img.ly/docs/pesdk/android/introduction/getting_started/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android-Demo&utm_term=Android).


## Author

img.ly GmbH, [@imgly](https://twitter.com/imgly), [img.ly](https://img.ly/?utm_campaign=Projects&utm_source=Github&utm_medium=PESDK&utm_content=Android-Demo&utm_term=Android)


## Installation

> The PhotoEditor SDK supports Android 5.0+ API 21 as the `minSdkVersion`, but it must be compiled with `compileSdkVersion` 31+.

## Add your license file

Before using any components of the PhotoEditor SDK, you have to add your license file to your applications assets folder.
The expected default name of the license file is "LICENSE". In order to change this, see licencePath option of PESDKConfig in your gradle file.

The license is digitally signed and can't be altered without becoming invalid. Our sample app comes with its own license, so you can try that right away. To try our SDK in your own app, you need to request a trial license that's bound to your bundle identifier. You can start a trial [here](https://img.ly/docs/pesdk) and download your license file from your [dashboard](https://img.ly/login).

Once the license file has been added the application will validate its presence upon launch.

## Setting up the workspace

Please ensure that our artifactory repository is listed in your repositories in the project’s build.gradle file:

```groovy
// Add the PESDK repository and plugin dependency
buildscript {
    repositories {
        jcenter()
        google()
        maven { url "https://artifactory.img.ly/artifactory/imgly" }
    }
    dependencies {
        classpath 'ly.img.android.pesdk:plugin:10.4.2'
    }
}

```

Apply the img.ly plugin and add the imglyConfig block into your module's `build.gradle` file:

```groovy
// Apply the Android Plugin
apply plugin: 'com.android.application'

// Apply the IMGLYPlugin
apply plugin: 'ly.img.android.sdk'

// Configure the PESDKPlugin
imglyConfig {

    // Optional: Enable the VideoEditor SDK
    vesdk {
        enabled true
        licencePath 'vesdk_android_license'
    }

    // Optional: Enable the PhotoEditor SDK
    pesdk {
        enabled true
        licencePath 'pesdk_android_license'
    }

    // Define the modules you are need
    modules {
        // Add all the UI modules you are need
        include 'ui:core'
        include 'ui:text'
        include 'ui:focus'
        include 'ui:frame'
        include 'ui:brush'
        include 'ui:filter'
        include 'ui:camera'
        include 'ui:sticker'
        include 'ui:overlay'
        include 'ui:transform'
        include 'ui:adjustment'

        // Add the serializer if you need
        include 'backend:serializer'

        // Add asset packs if you need
        include 'assets:font-basic'
        include 'assets:frame-basic'
        include 'assets:filter-basic'
        include 'assets:overlay-basic'
        include 'assets:sticker-shapes'
        include 'assets:sticker-emoticons'
    }
}

// Do your Android Configurations... ex.
android {
    /* Set the compileSdkVersion at 31 or greater and set the buildToolsVersion at '31.0.0' or greater.
     * We can't provide support for bugs, that are the result of older SDK versions.
     */
    compileSdkVersion 31
    buildToolsVersion '31.0.0'

    defaultConfig {
        /*
         * Replace with your App-ID and keep sure that it match with your license!
         * @see http://tools.android.com/tech-docs/new-build-system/applicationid-vs-packagename
         */
        applicationId "my.domain.application"

        /* Set the minimum supported SDK Version to 21 (Android 5.0) or higher */
        minSdkVersion 21

        /* Set the target SDK Version at minimum to 29 or higher */
        targetSdkVersion 29

        /* Set your own Version Code and Version Name */
        versionCode 1
        versionName "1.0"
    }

    /* Set Java Language level to Java 1.8+ */
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

```

__Sync your project with the Gradle files after every edit!__
For more information about Gradle, please take a look at the [Android Developer Documentation](http://developer.android.com/tools/building/configuring-gradle.html)

## Android Permissions

The PhotoEditor SDK requires two permissions: The "_Write access to external storage_" and the "_Camera_" permission (if you include the Camera module).
You can grant this permissions yourself otherwise the SDK will automatically grant these permissions

__Please take a look at the hint in the next step in order to integrate the Android 6.0 permission request correct!__

## Integration

### Start Editor standalone

If you want to open the editor directly with an existing image look at this example:

```kotlin
class KEditorDemoActivity : Activity() {

    companion object {
        const val PESDK_RESULT = 1
        const val GALLERY_RESULT = 2
    }

    // Create a empty new SettingsList and apply the changes on this reference.
    // If you include our asset Packs and use our UI you also need to add them to the UI Config,
    // otherwise they are only available for the backend (like Serialisation)
    // See the specific feature sections of our guides if you want to know how to add your own Assets.
    private fun createPESDKSettingsList() =
        PhotoEditorSettingsList(true)
            .configure<UiConfigFilter> {
                it.setFilterList(FilterPackBasic.getFilterPack())
            }
            .configure<UiConfigText> {
                it.setFontList(FontPackBasic.getFontPack())
            }
            .configure<UiConfigFrame> {
                it.setFrameList(FramePackBasic.getFramePack())
            }
            .configure<UiConfigOverlay> {
                it.setOverlayList(OverlayPackBasic.getOverlayPack())
            }
            .configure<UiConfigSticker> {
                it.setStickerLists(
                    StickerPackEmoticons.getStickerCategory(),
                    StickerPackShapes.getStickerCategory()
                )
            }
            .configure<PhotoEditorSaveSettings> {
                it.setOutputToGallery(Environment.DIRECTORY_DCIM)
            }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        openSystemGalleryToSelectAnImage()
    }

    fun openSystemGalleryToSelectAnImage() {
        val intent = Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI)
        try {
            startActivityForResult(intent, GALLERY_RESULT)
        } catch (ex: ActivityNotFoundException) {
            Toast.makeText(
                this,
                "No Gallery APP installed",
                Toast.LENGTH_LONG
            ).show()
        }
    }

    fun openEditor(inputImage: Uri?) {
        val settingsList = createPESDKSettingsList()

        settingsList.configure<LoadSettings> {
            it.source = inputImage
        }

        PhotoEditorBuilder(this)
            .setSettingsList(settingsList)
            .startActivityForResult(this, PESDK_RESULT)
        
        settingsList.release()
    }


    override fun onActivityResult(requestCode: Int, resultCode: Int, intent: Intent) {
        super.onActivityResult(requestCode, resultCode, intent)

        if (resultCode == RESULT_OK && requestCode == GALLERY_RESULT) {
            // Open Editor with some uri in this case with an image selected from the system gallery.
            openEditor(intent.data)

        } else if (resultCode == RESULT_OK && requestCode == PESDK_RESULT) {
            // Editor has saved an Image.
            val data = EditorSDKResult(intent)

            Log.i("PESDK", "Source image is located here ${data.sourceUri}")
            Log.i("PESDK", "Result image is located here ${data.resultUri}")

            // TODO: Do something with the result image

            // OPTIONAL: read the latest state to save it as a serialisation
            val lastState = data.settingsList
            try {
                IMGLYFileWriter(lastState).writeJson(File(
                    getExternalFilesDir(null),
                    "serialisationReadyToReadWithPESDKFileReader.json"
                ))
            } catch (e: IOException) {
                e.printStackTrace()
            }
            
            lastState.release()

        } else if (resultCode == RESULT_CANCELED && requestCode == PESDK_RESULT) {
            // Editor was canceled
            val data = EditorSDKResult(intent)

            val sourceURI = data.sourceUri
            // TODO: Do something with the source...
        }
    }
}
```

### Start Editor (with camera)

In order to open the camera preview and pass the resulting image to the editor, create a
[`CameraPreviewBuilder`](https://img.ly/docs/pesdk/apidocs/android/v10/pesdk-mobile_ui-camera/ly.img.android.pesdk.ui.activity/-camera-preview-builder/index.html) and start the [`CameraPreviewActivity`](https://img.ly/docs/pesdk/apidocs/android/v10/pesdk-mobile_ui-camera/ly.img.android.pesdk.ui.activity/-camera-preview-activity/index.html) with [`startActivityForResult(android.app.Activity, int)`](https://img.ly/docs/pesdk/apidocs/android/v10/pesdk-mobile_ui-camera/ly.img.android.pesdk.ui.activity/-camera-preview-builder/index.html#1501569930%2FFunctions%2F-594191830):

The camera module requires two permissions: The "_Write access to external storage_" and the "_Camera_" permission.
You can grant these permissions yourself otherwise the SDK will automatically grant these permissions.

> **Please make sure you delegate the [`onRequestPermissionsResult()`](https://developer.android.com/reference/android/app/Activity#onRequestPermissionsResult(int,%20java.lang.String[],%20int[])) to [`PermissionRequest.onRequestPermissionsResult()`](https://img.ly/docs/pesdk/apidocs/android/v10/pesdk-backend-core/ly.img.android.pesdk.ui.utils/-permission-request/index.html#-390511216%2FFunctions%2F-68773581)
> as demonstrated in the following example. This ensures correct behavior on Android 6.0 and above.**

```kotlin
class KCameraDemoActivity : Activity(), PermissionRequest.Response {

    companion object {
        const val PESDK_RESULT = 1
    }

    // Important permission request for Android 6.0 and above, don't forget to add this!
    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<String>, grantResults: IntArray) {
        PermissionRequest.onRequestPermissionsResult(requestCode, permissions, grantResults)
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    }

    override fun permissionGranted() {}

    override fun permissionDenied() {
        /* TODO: The Permission was rejected by the user. The Editor was not opened,
         * Show a hint to the user and try again. */
    }

    // Create a empty new SettingsList and apply the changes on this reference.
    // If you have included our asset Packs and you want to use our default UI you also need to add them to the UI config,
    // otherwise they are only available for the backend link serialisation.
    // See the specific feature sections of our guides if you want to know how to add your own assets.
    private fun createPESDKSettingsList() = PhotoEditorSettingsList(true)
        .configure<UiConfigFilter> {
            it.setFilterList(FilterPackBasic.getFilterPack())
        }
        .configure<UiConfigText> {
            it.setFontList(FontPackBasic.getFontPack())
        }
        .configure<UiConfigFrame> {
            it.setFrameList(FramePackBasic.getFramePack())
        }
        .configure<UiConfigOverlay> {
            it.setOverlayList(OverlayPackBasic.getOverlayPack())
        }
        .configure<UiConfigSticker> {
            it.setStickerLists(
                StickerPackEmoticons.getStickerCategory(),
                StickerPackShapes.getStickerCategory()
            )
        }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        openCamera()
    }

    private fun openCamera() {
        val settingsList = createPESDKSettingsList()

        CameraPreviewBuilder(this)
            .setSettingsList(settingsList)
            .startActivityForResult(this, PESDK_RESULT)

        settingsList.release()
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, intent: Intent) {
        super.onActivityResult(requestCode, resultCode, intent)

        if (resultCode == RESULT_OK && requestCode == PESDK_RESULT) {
            // Editor has saved an Image.
            val data = EditorSDKResult(intent)

            Log.i("PESDK", "Source image is located here ${data.sourceUri}")
            Log.i("PESDK", "Result image is located here ${data.resultUri}")

            // TODO: Do something with the result image

            // OPTIONAL: read the latest state to save it as a serialisation
            val lastState = data.settingsList
            try {
                IMGLYFileWriter(lastState).writeJson(File(
                    getExternalFilesDir(null),
                    "serialisationReadyToReadWithPESDKFileReader.json"
                ))
            } catch (e: IOException) {
                e.printStackTrace()
            }

            lastState.release()

        } else if (resultCode == RESULT_CANCELED && requestCode == PESDK_RESULT) {
            // Editor was canceled
            val data = EditorSDKResult(intent)

            val sourceURI = data.sourceUri
            // TODO: Do something...
        }
    }
}
```