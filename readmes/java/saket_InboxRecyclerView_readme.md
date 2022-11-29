[![](https://github.com/saket/InboxRecyclerView/blob/master/docs/images/static_thumbnail.jpg)](https://www.youtube.com/playlist?list=PLY9Ajk3MUE7UAT4rn9LO-jSPfkPm5ewrQ)

`InboxRecyclerView` is a library for building expandable descendant navigation inspired by [Google Inbox](http://androidniceties.tumblr.com/post/100872004063/inbox-by-gmail-google-play-link) and [Reply](https://material.io/design/material-studies/reply.html), and is an easy drop-in into existing projects. You can take a look at the [sample app](https://github.com/saket/InboxRecyclerView/tree/master/sample) for best practices or [download its APK](https://github.com/saket/InboxRecyclerView/releases) for trying it out on your phone. If you're interested in learning how it was created, [here's an in-depth blog post](https://saket.me/inbox-recyclerview).

```groovy
implementation 'me.saket:inboxrecyclerview:3.0.0'
```

### Usage

**Layout**

```xml
<me.saket.inboxrecyclerview.InboxRecyclerView
  android:layout_width="match_parent"
  android:layout_height="match_parent" />

<me.saket.inboxrecyclerview.page.ExpandablePageLayout
  android:layout_width="match_parent"
  android:layout_height="match_parent"
  android:background="@color/same_as_your_list_items">

  <!--
    Your expandable content will live here. Make sure that
    your page has a higher z-index than the list by giving
    it a higher view position or a higher elevation.
  -->
</me.saket.inboxrecyclerview.page.ExpandablePageLayout>
```

**Expanding content**

```kotlin
recyclerView.itemExpandAnimator = ItemExpandAnimator.scale() // or split() / none()
recyclerView.dimPainter = DimPainter.listAndPage(Color.WHITE, alpha = 0.65f)

recyclerView.expandablePage = findViewById(...).also {
  it.pushParentToolbarOnExpand(toolbar)
  it.addOnPullListener(PageCollapseEligibilityHapticFeedback(it))
}

recyclerViewAdapter.onItemClick = { clickedItem ->
  // Load or update your content inside the page here.
  recyclerView.expandItem(clickedItem.adapterId)
}
```

### How do I…

- [customize item expand animations?](docs/item_animators.md)
- [control the pull-to-collapse gesture?](docs/pull_to_collapse.md)
- [change background dimming?](docs/background_dim.md)
- [listen to state changes?](docs/page_callbacks.md)
- [expand items without using `Long` based adapter IDs?](https://github.com/saket/InboxRecyclerView/wiki/Custom-expansion-keys)

### Pull collapsible activities

To maintain consistency across your whole app, a `PullCollapsibleActivity` is also included that brings the same animations and gesture to activities with little effort.

Step 1. Extend `PullCollapsibleActivity`.

Step 2. Add these attributes to the activity’s theme:

```xml
<item name="android:windowIsTranslucent">true</item>
<item name="android:colorBackgroundCacheHint">@null</item>
```

### License
```
Copyright 2018 Saket Narayan.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
