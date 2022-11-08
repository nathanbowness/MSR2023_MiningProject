DEPRECATED
==========
RxAppState is deprecated. No more development will be taking place.

Use Google's [ProcessLifecycleOwner](https://developer.android.com/reference/android/arch/lifecycle/ProcessLifecycleOwner) instead
which is part of [Android Architecture Components](https://developer.android.com/topic/libraries/architecture).

An implementation can be as simple as:
```java
public class AppLifecycleListener implements LifecycleObserver {

    @OnLifecycleEvent(Lifecycle.Event.ON_START)
    public void onAppDidEnterForeground() {
        // ...
    }

    @OnLifecycleEvent(Lifecycle.Event.ON_STOP)
    public void onAppDidEnterBackground() {
       // ...
    }
}
```
Register the observer like this:
```java
ProcessLifecycleOwner.get().getLifecycle().addObserver(new AppLifecycleListener());
```

Here is a great blog post that explains it in more detail:
[Detecting when an Android app backgrounds in 2018](https://proandroiddev.com/detecting-when-an-android-app-backgrounds-in-2018-4b5a94977d5c)

RxAppState [![Build Status](https://travis-ci.org/jenzz/RxAppState.svg?branch=master)](https://travis-ci.org/jenzz/RxAppState)
==========
A simple, reactive Android library based on [RxJava](https://github.com/ReactiveX/RxJava) that monitors app state changes.  
It notifies subscribers every time the app goes into background and comes back into foreground.

A typical use case is, for example, session tracking for analytics purposes
or suppressing push notifications when the app is currently visible to the user.

Background
----------
Android has this ancient pain of not providing any type of callback to know if your app is currently in the foreground or background.
It is lacking an equivalent of the iOS [UIApplicationDelegate](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol)
which offers callbacks like [`applicationDidEnterBackground`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/#//apple_ref/occ/intfm/UIApplicationDelegate/applicationDidEnterBackground:)
and [`applicationDidBecomeActive`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/#//apple_ref/occ/intfm/UIApplicationDelegate/applicationDidBecomeActive:).

There are two popular discussions on this topic on StackOverflow:

* [How to detect when an Android app goes to the background and come back to the foreground](http://stackoverflow.com/questions/4414171/how-to-detect-when-an-android-app-goes-to-the-background-and-come-back-to-the-fo)
* [Checking if an Android application is running in the background](http://stackoverflow.com/questions/3667022/checking-if-an-android-application-is-running-in-the-background)

This library internally uses a combination of `ActivityLifecycleCallbacks` and the `onTrimMemory(int level)` callback to identify the current app state.  
Just check out the source code (mainly: [DefaultAppStateRecognizer](https://github.com/jenzz/RxAppState/blob/master/appstate/src/main/java/com/jenzz/appstate/internal/DefaultAppStateRecognizer.java)).
The implementation is dead simple.

Usage
-----
You most probably want to monitor for app state changes in your application's `onCreate()` method
in which case you also don't need to worry about unregistering your `AppStateListener`.
Remember that if you subscribe in an `Activity` or a `Fragment`, don't forget to unsubscribe to avoid memory leaks.
```java
AppStateMonitor appStateMonitor = RxAppStateMonitor.create(this);
appStateMonitor.addListener(new AppStateListener() {
    @Override
    public void onAppDidEnterForeground() {
        // ...
    }

    @Override
    public void onAppDidEnterBackground() {
        // ...
    }
});
appStateMonitor.start();
```

Example
-------
Check out the [sample project](https://github.com/jenzz/RxAppState/tree/master/sample) for an example implementation.

Download
--------
Grab it via Gradle:

```groovy
dependencies {
  compile 'com.jenzz.appstate:appstate:3.0.1'
}
```

**Note:** There are adapters available for [RxJava](https://github.com/jenzz/RxAppState/tree/master/appstate-adapters/rxjava) and [RxJava2](https://github.com/jenzz/RxAppState/tree/master/appstate-adapters/rxjava2).

License
-------
This project is licensed under the [MIT License](https://raw.githubusercontent.com/jenzz/RxAppState/master/LICENSE).