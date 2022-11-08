# reminder
[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-reminder-green.svg?style=true)](https://android-arsenal.com/details/1/3709)

reminder lets you persist the state of your views to recover them later in order to display old data until fresh data arrives.

Usage
--------

### Initialize Reminder:

```java
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        ...
        Reminder.init(this);
    }
}

```

### Implement Remindable:

```java
public class MainActivity extends AppCompatActivity implements Remindable {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ...
        // This call results in either a call to onSnapshotAvailable() or onSnapshotNotFound().
        Reminder.remind(this);
    }

    @Override
    public void saveSnapshot(ReminderBundle snapshot) {
        // Save the current state of this Remindable into the snapshot.
        // The snapshot is used as follows: snapshot.put(KEY, object);
        // Information inside ReminderBundle is saved as key-value pairs.
        // This method will be called automatically (if this is an Activity) by the 
        // time onStop() is called.
        // In case your Remindable is not an Activity, an explicit call to 
        // Reminder.save(this) should be made by the time the Remindable is about
        // to be stopped/destroyed.
    }

    @Override
    public void onSnapshotAvailable(ReminderBundle snapshot) {
        // A snapshot for this Remindable is available.
        // The snapshot is used as follows: snapshot.get(KEY, clazz).
        // KEY is a String and clazz the Class<> instance of that particular object.
        // snapshot.isMillisecondsOld(N) returns true if the snapshot is at
        // least N milliseconds old.
        
        // This snapshot can be used to populate this Remindable and
        // decide according to some criteria (e.g: snapshot.isMillisecondsOld(TIME_LIMIT))
        // if newer data should be fetched
    }

    @Override
    public void onSnapshotNotFound() {
        // No snapshot was available for this Remindable.
        // Time to fetch new data!
    }
}

```

### RemindableWithId

If you want to persist the same Remindable multiple times according to some id value, you can implement RemindableWithId instead, which will make you implement one extra method called remindableId().

```java
public class ItemDetailFragment extends Fragment implements RemindableWithId {

    @Override
    public void onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ...
        // This call results in either a call to onSnapshotAvailable() or onSnapshotNotFound().
        Reminder.remind(this);
    }
    
    @Override
    public String remindableId() {
        // return something that identifies this item.
    }
    
    @Override
    public void onStop() {
        // Since this is not an Activity, an explicit call to Reminder.save(this) must be made.
        Reminder.save(this);
        super.onStop();
    }

    @Override
    public void saveSnapshot(ReminderBundle snapshot) {
        // Same as before.
    }

    @Override
    public void onSnapshotAvailable(ReminderBundle snapshot) {
        // Same as before.
    }

    @Override
    public void onSnapshotNotFound() {
        // Same as before.
    }
}

```

### Persistance Modes

Reminder can be configured to use SharedPreferences or SQLite as persistence modes. SQLite is the default mode. This is an example of how to configure it to use SharedPreferences:

```java
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        ...
        ReminderConfig config = new ReminderConfig.Builder()
                .useSharedPreferences()
                .build();
        Reminder.init(this, config);
    }
}

```

### Data clearing

If you made an update to your data model or want to delete the saved information for whatever reason, there's a simple way to do so:

```java
public class MyApplication extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        Reminder.init(this);
        ...
        Reminder.deleteAll();
    }
}

```

Download
--------
Add the JitPack repository to your root build.gradle:

```groovy
	allprojects {
		repositories {
			...
			maven { url "https://jitpack.io" }
		}
	}
```
Add the Gradle dependency:
```groovy
	dependencies {
		compile 'com.github.OneCodeLabs:reminder:x.y.z@aar'
	}
```

### License

    The MIT License (MIT)
    
    Copyright (c) 2016 
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

