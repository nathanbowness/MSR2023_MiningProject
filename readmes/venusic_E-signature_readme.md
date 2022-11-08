（安卓电子签名简介）E-signature for Android V0.2
============================
* 支持签名边缘裁剪
* 根据速度进行了插值改变宽度。


[![](https://jitpack.io/v/venusic/E-signature.svg)](https://jitpack.io/#venusic/E-signature)

Gradle 添加：
```
	allprojects {
		repositories {
			...
			maven { url 'https://jitpack.io' }
		}
	}
	
	dependencies {
    	        compile 'com.github.venusic:E-signature:${last_version}'
    	}
```
### 使用
- 添加View

```
     <com.venusic.handwrite.view.HandWriteView
               android:id="@+id/view"
               android:layout_width="match_parent"
               app:paintMaxWidth="20px" //最大宽度
               app:paintMinWidth="10px" //最小宽度
               app:paintColor="#FF0000" //颜色
               android:layout_height="match_parent"/>
```
- 保存
 

```
if (view.isSign()) {
    try {
        //路径
        //是否清除边缘空白
        //边缘保留多少像素空白
        //是否加密存储 如果加密存储会自动在路径后面追加后缀.sign
        view.save(MainActivity.path1, true, 10,true);
    } catch (IOException e) {
        e.printStackTrace();
    }
} else {
    Toast.makeText(context, "您没有签名~", Toast.LENGTH_SHORT).show();
}

```

 
- 清除

```
view.clear();
```
- 修改背景、笔宽、颜色

```
    //最小宽度、最大宽度
  view.setPaintWidth(10,20);
  view.setPaintColor(Color.WHITE);
  view.clear();
```

- 加密存储
使用`SignFileInputStream`和`SignFileOutputStream`进行读写操作即可。如果使用Glide加载图片，可以在AndroidManifest.xml注册GlideModel：
```
   <application>
       
        <meta-data
            android:name="com.venusic.handwrite.glide.SignFileModel"
            android:value="GlideModule"/>
   </application>
```

然后即可使用Glide正常加载加密之后的签名文件。

### 效果图

![Logo](webimage/img1.png)

![Logo](webimage/img2.png)

  
