![Android Gems](http://www.android-gems.com/badge/hani-momanii/SuperNova-Emoji.svg)


[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-SuperNova--Emoji-green.svg?style=true)](https://android-arsenal.com/details/1/3319)
![emojicon on Maven Central](https://img.shields.io/badge/maven%20central-0.0.3-brightgreen.svg)
![AppVeyor branch](https://img.shields.io/appveyor/ci/gruntjs/grunt/master.svg)
[![](https://jitpack.io/v/hani-momanii/SuperNova-Emoji.svg)](https://jitpack.io/#hani-momanii/SuperNova-Emoji)

## [Release Notes](https://github.com/hani-momanii/SuperNova-Emoji/releases)
 

## SuperNova-Emoji

[SuperNova-Emoji](https://github.com/hani-momanii/SuperNova-Emoji) is a library to implement and render emojis.
Minimum SDK Level: 9 (2.3)


![image](https://github.com/hani-momanii/SuperNova-Emoji/blob/master/vid.gif)

## Contact


[![alt text][1.1]][1]
[![alt text][2.1]][2]
[![alt text][6.1]][6]


[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)
[6.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

## Java Usage

To use default colors : 
EmojIconActions(Context ctx,View rootView,EmojiconEditText emojiconEditText,ImageView emojiButton)
```
EmojIconActions  emojIcon=new EmojIconActions(this,rootView,emojiconEditText,emojiButton);
emojIcon.ShowEmojIcon();
```

![image](https://github.com/hani-momanii/SuperNova-Emoji/blob/master/ios.png)


To use custom color :
EmojIconActions(Context ctx,View rootView,EmojiconEditText emojiconEditText,ImageView emojiButton,String iconPressedColor,String tabsColor,String backgroundColor)
```
EmojIconActions  emojIcon=new EmojIconActions(this,rootView,emojiconEditText,emojiButton,"#495C66","#DCE1E2","#E6EBEF");
emojIcon.ShowEmojIcon();
```
![image](https://github.com/hani-momanii/SuperNova-Emoji/blob/master/color.png)



To Listen to keyboard status 
```
emojIcon.setKeyboardListener(new EmojIconActions.KeyboardListener() {
@Override
public void onKeyboardOpen() {
    Log.e("Keyboard","open");
  }

@Override
public void onKeyboardClose() {
  Log.e("Keyboard","close");
}
});
```
To use the device default emoji
```
emojIcon.setUseSystemEmoji(true);
emojiconEditText.setUseSystemEmoji(true);
```
![image](https://github.com/hani-momanii/SuperNova-Emoji/blob/master/def.png)



## XML Usage

```
<hani.momanii.supernova_emoji_library.Helper.EmojiconEditText
        android:id="@+id/emojicon_edit_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        emojicon:emojiconSize="28sp" />
        
        
<hani.momanii.supernova_emoji_library.Helper.EmojiconTextView
        android:id="@+id/emojicon_text_view"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" 
        emojicon:emojiconSize="28sp"/>

```



## Usage

* `EmojiconTextView`: a `TextView` which can render emojis.
* `EmojiconEditText`: a `EditText` which can render emojis.
* `EmojiconMultiAutoCompleteTextView`: a `MultiAutoCompleteTextView` which can render emojis.

## Building in IntelliJ

Via Gradle:

```

repositories {
    maven { url 'https://jitpack.io' }
}
compile 'com.github.hani-momanii:SuperNova-Emoji:1.1'
```

## Acknowledgements

Based on Hieu Rocker's [library Emojicon Github](https://github.com/rockerhieu/emojicon/).

Emojicon is using emojis graphics from [emoji-cheat-sheet.com](https://github.com/arvida/emoji-cheat-sheet.com/tree/master/public/graphics/emojis).

## License

* [Apache Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

```
Copyright 2016 Hani Al-Momani

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



[1]: https://twitter.com/hani_momanii
[2]: https://www.facebook.com/hani.momanii
[6]: https://github.com/hani-momanii
