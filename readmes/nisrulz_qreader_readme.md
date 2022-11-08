![Image](img/github_banner.png)

### Specs
[![API](https://img.shields.io/badge/API-14%2B-orange.svg?style=flat)](https://android-arsenal.com/api?level=14)

### Badges/Featured In
[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-QREader-green.svg?style=true)](https://android-arsenal.com/details/1/3478)  [![AndroidDev Digest](https://img.shields.io/badge/AndroidDev%20Digest-%23121-blue.svg)](https://www.androiddevdigest.com/digest-121/)


### Show some :heart:
[![GitHub stars](https://img.shields.io/github/stars/nisrulz/qreader.svg?style=social&label=Star)](https://github.com/nisrulz/qreader) [![GitHub forks](https://img.shields.io/github/forks/nisrulz/qreader.svg?style=social&label=Fork)](https://github.com/nisrulz/qreader/fork) [![GitHub watchers](https://img.shields.io/github/watchers/nisrulz/qreader.svg?style=social&label=Watch)](https://github.com/nisrulz/qreader) [![GitHub followers](https://img.shields.io/github/followers/nisrulz.svg?style=social&label=Follow)](https://github.com/nisrulz/qreader)
[![Twitter Follow](https://img.shields.io/twitter/follow/nisrulz.svg?style=social)](https://twitter.com/nisrulz)

Android library which makes use of Google's Mobile Vision API to enable reading QR Code.

The library is built for simplicity and ease of use. It not only eliminates most boilerplate code for dealing with setting up QR Code reading , but also provides an easy and simple API to retrieve information from QR Code quickly.

> Requires Google Play Services

# Changelog
Starting with `1.0.4`, Changes exist in the [releases tab](https://github.com/nisrulz/qreader/releases).

#Integration
QREader is available in the Jcenter, so getting it as simple as adding it as a dependency

- For gradle version < 4.0

    ```gradle
    compile 'com.github.nisrulz:qreader:{latest version}'
    ```

- For gradle 4.0+

    ```gradle
    implementation 'com.github.nisrulz:qreader:{latest version}'
    ```

where `{latest version}` corresponds to published version in [ ![Download](https://api.bintray.com/packages/nisrulz/maven/com.github.nisrulz%3Aqreader/images/download.svg) ](https://bintray.com/nisrulz/maven/com.github.nisrulz%3Aqreader/_latestVersion)


# Usage Docs

### Steps

1. Add a `SurfaceView` to your layout

  ```xml
  <SurfaceView
    android:id="@+id/camera_view"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:layout_above="@+id/info"
    />
  ```

1. Setup `SurfaceView` and `QREader` in `onCreate()`

  ```java
  // QREader
  private SurfaceView mySurfaceView;
  private QREader qrEader;
  ..

  @Override
  protected void onCreate(final Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    ..
    ..

    // Setup SurfaceView
    // -----------------
    mySurfaceView = (SurfaceView) findViewById(R.id.camera_view);

    // Init QREader
    // ------------
    qrEader = new QREader.Builder(this, mySurfaceView, new QRDataListener() {
      @Override
      public void onDetected(final String data) {
        Log.d("QREader", "Value : " + data);
        text.post(new Runnable() {
          @Override
          public void run() {
            text.setText(data);
          }
        });
      }
    }).facing(QREader.BACK_CAM)
        .enableAutofocus(true)
        .height(mySurfaceView.getHeight())
        .width(mySurfaceView.getWidth())
        .build();

  }
  ```

1. Initialize and Start in `onResume()`

  ```java
    @Override
    protected void onResume() {
      super.onResume();

      // Init and Start with SurfaceView
      // -------------------------------
      qrEader.initAndStart(mySurfaceView);
    }
  ```
1. Cleanup in `onPause()`

  ```java
    @Override
    protected void onPause() {
      super.onPause();

      // Cleanup in onPause()
      // --------------------
      qrEader.releaseAndCleanup();
    }
  ```
1. Some provided utility functions which you can use
  + To check if the camera is running

    ```java
    boolean isCameraRunning = qrEader.isCameraRunning()
    ```

  + To stop `QREader`

      ```java
      qrEader.stop();
      ```
  + To start `QREader`

      ```java
      qrEader.start();
      ```

  > ##### Check the included sample app for a working example.

# Pull Requests
I welcome and encourage all pull requests. It usually will take me within 24-48 hours to respond to any issue or request. Here are some basic rules to follow to ensure timely addition of your request:
  1. Match coding style (braces, spacing, etc.) This is best achieved using CMD+Option+L (Reformat code) on Mac (not sure for Windows) with Android Studio defaults.
  2. If its a feature, bugfix, or anything please only change code to what you specify.
  3. Please keep PR titles easy to read and descriptive of changes, this will make them easier to merge :)
  4. Pull requests _must_ be made against `develop` branch. Any other branch (unless specified by the maintainers) will get rejected.
  5. Check for existing [issues](https://github.com/nisrulz/qreader/issues) first, before filing an issue.  
  6. Have fun!

### Created & Maintained By
[Nishant Srivastava](https://github.com/nisrulz/nisrulz.github.io) ([@nisrulz](https://www.twitter.com/nisrulz))

> If you found this library helpful or you learned something from the source code and want to thank me, consider buying me a cup of :coffee:
>  + [PayPal](https://www.paypal.me/nisrulz/5)
>  + Bitcoin Address: 13PjuJcfVW2Ad81fawqwLtku4bZLv1AxCL