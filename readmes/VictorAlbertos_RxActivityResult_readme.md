:warning: Deprecated :warning:

This library is no longer mantained. You should use the Android Navigation component with `NavBackStackEntry` for [returning a result to the previous Destination](https://developer.android.com/guide/navigation/navigation-programmatic#returning_a_result).


[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-RxActivityResult-green.svg?style=true)](https://android-arsenal.com/details/1/3284)

[![Join the chat at https://gitter.im/VictorAlbertos/RxActivityResult](https://badges.gitter.im/VictorAlbertos/RxActivityResult.svg)](https://gitter.im/VictorAlbertos/RxActivityResult?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# RxActivityResult

The api which Android SDK exposes to retrieve the data from a 'returning system call' (camera, gallery, email...) just does not give a shit about [Don't break the chain](http://blog.danlew.net/2015/03/02/dont-break-the-chain) leitmotiv. Indeed, the [OnActivityResult](http://developer.android.com/intl/es/training/basics/intents/result.html) approach will break entirely your observable chaining. 

I did this library to not have to deal with this `OnActivityResult` pattern. Never. Ever.  

## RxActivityResult features:
* Launch the intent from any class, as long as you supply a valid `Activity` or `Fragment` instance.
* Get the `Intent` back with the data encapsulated in an `observable` and keep going crazy chaining operators. 

## Setup
Add the JitPack repository in your build.gradle (top level module):
```gradle
allprojects {
    repositories {
        jcenter()
        maven { url "https://jitpack.io" }
    }
}
```

And add next dependencies in the build.gradle of the module:
```gradle
dependencies {
    implementation 'com.github.VictorAlbertos:RxActivityResult:0.5.0-2.x'
    implementation 'io.reactivex.rxjava2:rxjava:2.2.3'
}
```

## Usage
Call `RxActivityResult.register` in your Android `Application` class, supplying as parameter the current instance.
        
```java
public class SampleApp extends Application {

    @Override public void onCreate() {
        super.onCreate();
        RxActivityResult.register(this);
    }
}
```

You can call `RxActivityResult.on(this).startIntent(intent)` supplying both, an `Activity` instance or a `Fragment` instance.
Observe the emitted [Result](https://github.com/VictorAlbertos/RxActivityResult/blob/master/rx_activity_result/src/main/java/rx_activity_result/Result.java) item to know the resultCode and retrieve the associated data if appropriate.  

**Limitation:** Your fragments need to extend from `androidx.fragment.app.Fragment` instead of `android.app.Fragment`, otherwise they won't be notified.


```java
Intent takePhoto = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);

RxActivityResult.on(this).startIntent(takePhoto)
        .subscribe(result -> {
            Intent data = result.data();
            int resultCode = result.resultCode();
            // the requestCode using which the activity is started can be received here.
            int requestCode = result.requestCode();

            if(requestCode == YourActivity.YOUR_REQUEST_CODE)
            {
                // Do Something
            }

            if (resultCode == RESULT_OK) {
                result.targetUI().showImage(data);
            } else {
                result.targetUI().printUserCanceled();
            }
        });
```

Please pay attention to the `targetUI()` method in the `Result` object emitted. 

This method returns a safety instance of the current `Activity`/`Fragment`. Because the original one may be recreated (due to configuration changes or some other system events) it would be unsafe calling it. 

Instead, you must call any method/variable of your `Activity`/`Fragment` from this instance encapsulated in the `Result` object.  

### StartIntentSenderForResult
RxActivityResult supports [startIntentSenderForResult](http://developer.android.com/intl/es/reference/android/app/Activity.html#startIntentSenderForResult) too, by calling `RxActivityResult.on(this).startIntentSender` and supplying the proper arguments. As follows: 

```java
RxActivityResult.on(this).startIntentSender(pendingIntent.getIntentSender(), new Intent(), 0, 0, 0)
        .subscribe(result -> {
            
        });
```

## Examples
There is an example of RxActivityResult using both activity and fragment in the [app module](https://github.com/VictorAlbertos/RxActivityResult/tree/2.x/app)

## Author
**Víctor Albertos**

* <https://twitter.com/_victorAlbertos>
* <https://linkedin.com/in/victoralbertos>
* <https://github.com/VictorAlbertos>

Another author's libraries using RxJava:
----------------------------------------
* [RxCache](https://github.com/VictorAlbertos/RxCache): Reactive caching library for Android and Java.
* [RxPaparazzo](https://github.com/FuckBoilerplate/RxPaparazzo): RxJava extension for Android to take images using camera and gallery.
* [RxFcm](https://github.com/VictorAlbertos/RxFcm): RxJava extension for Android Firebase Cloud Messaging (aka fcm).
