<div align="center">
  <img src="img/github_banner.png" />
</div>
<h1 align="center"><a href="https://twitter.com/intent/tweet?text=Checkout%20RecyclerViewHelper%3A%20Android%20library%20giving%20powers%20to%20RecyclerView%20%F0%9F%98%8E&url=https://github.com/nisrulz/recyclerviewhelper&via=nisrulz&hashtags=AndroidDev">
        <img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social"/>
    </a></h1>

<div align="center">
  <strong>Android library that provides most common functions around recycler-view like Swipe to dismiss, Drag and Drop, Divider in the ui, events for when item selected and when not selected, on-click listener for items.</strong>
</div>
<br/>
<div align="center">
    <!-- Bintray -->
    <a href="https://bintray.com/nisrulz/maven/com.github.nisrulz%3Arecyclerviewhelper/_latestVersion">
        <img src="https://api.bintray.com/packages/nisrulz/maven/com.github.nisrulz%3Arecyclerviewhelper/images/download.svg"/>
    </a>
    <!-- API -->
    <a href="https://android-arsenal.com/api?level=14">
        <img src="https://img.shields.io/badge/API-14%2B-orange.svg?style=flat"/>
    </a>
    <!-- Android Arsenal -->
    <a href="https://android-arsenal.com/details/1/3572">
        <img src="https://img.shields.io/badge/Android%20Arsenal-RecyclerViewHelper-green.svg?style=true"/>
    </a>
     <!-- Android Dev Digest -->
    <a href="https://www.androiddevdigest.com/digest-99/">
        <img src="https://img.shields.io/badge/AndroidDev%20Digest-%2399-blue.svg"/>
    </a>
      <!-- Android Weekly -->
    <a href="http://androidweekly.net/issues/issue-221">
        <img src="https://img.shields.io/badge/Android%20Weekly-%23221-blue.svg"/>
    </a>
    <!-- GitHub stars -->
    <a href="https://github.com/nisrulz/recyclerviewhelper">
        <img src="https://img.shields.io/github/stars/nisrulz/recyclerviewhelper.svg?style=social&label=Star"/>
    </a>
    <!-- GitHub forks -->
    <a href="https://github.com/nisrulz/recyclerviewhelper/fork">
        <img src="hhttps://img.shields.io/github/forks/nisrulz/recyclerviewhelper.svg?style=social&label=Fork"/>
    </a>
    <!-- GitHub watchers -->
    <a href="https://github.com/nisrulz/recyclerviewhelper">
        <img src="https://img.shields.io/github/watchers/nisrulz/recyclerviewhelper.svg?style=social&label=Watch"/>
    </a>
    <!-- Say Thanks! -->
    <a href="https://saythanks.io/to/nisrulz">
        <img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"/>
    </a>
    <a href="https://www.paypal.me/nisrulz/5usd">
        <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
    </a>
    <br/>
     <!-- GitHub followers -->
    <a href="https://github.com/nisrulz/recyclerviewhelper">
        <img src="https://img.shields.io/github/followers/nisrulz.svg?style=social&label=Follow%20@nisrulz"/>
    </a>
    <!-- Twitter Follow -->
    <a href="https://twitter.com/nisrulz">
        <img src="https://img.shields.io/twitter/follow/nisrulz.svg?style=social"/>
    </a>
</div>

<div align="center">
    <a href="https://android.libhunt.com/newsletter/21">
        Also featured in Awesome Android Newsletter #Issue 21
    </a>
</div>

<div align="center">
  <sub>Built with ❤︎ by
  <a href="https://twitter.com/nisrulz">Nishant Srivastava</a> and
  <a href="https://github.com/nisrulz/recyclerviewhelper/graphs/contributors">
    contributors
  </a>
</div>
<br/>
<br/>


> Note: Development for pre-androidx version of this library has stopped. If you are looking for [pre-androidx version, then checkout this branch.](https://github.com/nisrulz/recyclerviewhelper/tree/archive/pre-androidx)
> Library is compatible with AndroidX version only.

# Integration
RecyclerViewHelper is available in the Jcenter, so getting it as simple as adding it as a dependency
```gradle
def recyclerViewVersion="{latest version}"
// Required
implementation "androidx.recyclerview:recyclerview:${recyclerViewVersion}"

// RecyclerViewHelper
implementation "com.github.nisrulz:recyclerviewhelper:x${recyclerViewVersion}"
```
where `{latest version}` corresponds to published version in [ ![Download](https://api.bintray.com/packages/nisrulz/maven/com.github.nisrulz%3Arecyclerviewhelper/images/download.svg) ](https://bintray.com/nisrulz/maven/com.github.nisrulz%3Arecyclerviewhelper/_latestVersion) without the prepended `x`.
 This is done to distinguish between library using andoirdx vs pre-androidx.

Usage Example:
```gradle
def recyclerViewVersion="1.1.0"
// Required
implementation "androidx.recyclerview:recyclerview:${recyclerViewVersion}"

// RecyclerViewHelper
implementation "com.github.nisrulz:recyclerviewhelper:x${recyclerViewVersion}"
```

> NOTE : The version here corresponds to the version of recyclerview dependency.

##### Make sure that the google's maven repo is declared in your projects `build.gradle` file as below

  ```gradle
  allprojects {
    repositories {
      google()
      jcenter()
    }
  }
  ```

# Usage
+ Implement the `RHVAdapter` in your recycler view adapter and `RHVViewHolder` in your ItemViewHolder 
```java

    public class MyAdapter extends RecyclerView.Adapter<MyAdapter.ItemViewHolder> implements RVHAdapter {
    
         ...
    
        @Override
        public boolean onItemMove(int fromPosition, int toPosition) {
            swap(fromPosition, toPosition);
            return false;
        }
    
        @Override
        public void onItemDismiss(int position, int direction) {
            remove(position);
        }
    
        public class ItemViewHolder extends RecyclerView.ViewHolder implements RVHViewHolder {
            ...
               
            @Override
            public void onItemSelected(int actionstate) {
                System.out.println("Item is selected");
            }
    
            @Override
            public void onItemClear() {
                System.out.println("Item is unselected");
    
            }
        }
    
        // Helper functions you might want to implement to make changes in the list as an event is fired
        private void remove(int position) {
            dataList.remove(position);
            notifyItemRemoved(position);
        }
    
        private void swap(int firstPosition, int secondPosition) {
            Collections.swap(dataList, firstPosition, secondPosition);
            notifyItemMoved(firstPosition, secondPosition);
        }
    }

```

+ Then implement your recycler view
```java

   public class MainActivity extends AppCompatActivity {
   
   
       RecyclerView myrecyclerview;
       ArrayList<String> data;
       MyAdapter adapter;
   
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
   
           myrecyclerview = (RecyclerView) findViewById(R.id.rv_fruits);
   
           data = new ArrayList<>();
           data.add("Apple");
           ...
           data.add("Fig");
   
           // Setup your adapter
           adapter = new MyAdapter(data);
           // Setup 
           myrecyclerview.hasFixedSize();
           myrecyclerview.setLayoutManager(new LinearLayoutManager(this));
           myrecyclerview.setAdapter(adapter);
   
   
           // Setup onItemTouchHandler to enable drag and drop , swipe left or right
           ItemTouchHelper.Callback callback = new RVHItemTouchHelperCallback(adapter, true, true,
                   true);
           ItemTouchHelper helper = new ItemTouchHelper(callback);
           helper.attachToRecyclerView(myrecyclerview);
   
           // Set the divider in the recyclerview
           myrecyclerview.addItemDecoration(new RVHItemDividerDecoration(this, LinearLayoutManager.VERTICAL));
   
           // Set On Click Listener
           myrecyclerview.addOnItemTouchListener(new RVHItemClickListener(this, new RVHItemClickListener.OnItemClickListener() {
               @Override
               public void onItemClick(View view, int position) {
                   String value = "Clicked Item " + data.get(position) + " at " + position;
   
                   Log.d("TAG", value);
                   Toast.makeText(MainActivity.this, value, Toast.LENGTH_SHORT).show();
               }
           }));
   
       }
   }


```

### Demo

![Walkthrough](img/walkthrough1.gif)

# Pull Requests
I welcome and encourage all pull requests. It usually will take me within 24-48 hours to respond to any issue or request. Here are some basic rules to follow to ensure timely addition of your request:
  1. Match coding style (braces, spacing, etc.) This is best achieved using CMD+Option+L (Reformat code) on Mac (not sure for Windows) with Android Studio defaults. This project uses a [modified version of Grandcentrix's code style](https://github.com/nisrulz/AndroidCodeStyle/tree/nishant-config), so please use the same when editing this project.
  2. If its a feature, bugfix, or anything please only change code to what you specify.
  3. Please keep PR titles easy to read and descriptive of changes, this will make them easier to merge :)
  4. Pull requests _must_ be made against `develop` branch. Any other branch (unless specified by the maintainers) will get rejected.
  5. Check for existing [issues](https://github.com/nisrulz/recyclerviewhelper/issues) first, before filing an issue.
  6. Have fun!


## License
Licensed under the Apache License, Version 2.0, [click here for the full license](/LICENSE.txt).

## Author & support
This project was created by [Nishant Srivastava](https://github.com/nisrulz/nisrulz.github.io#nishant-srivastava) but hopefully developed and maintained by many others. See the [the list of contributors here](https://github.com/nisrulz/recyclerviewhelper/graphs/contributors).

>Special Credits to Paul Burke and his [article](https://medium.com/@ipaulpro/drag-and-swipe-with-recyclerview-b9456d2b1aaf) which got me thinking
>
>This library contains a modified version of his implementations of ItemTouchHelper.
<br/>

If you appreciate my work, consider [buying me](https://www.paypal.me/nisrulz/5usd) a cup of :coffee: to keep me recharged :metal: [[PayPal](https://www.paypal.me/nisrulz/5usd)]

<img src="http://forthebadge.com/images/badges/built-for-android.svg" />