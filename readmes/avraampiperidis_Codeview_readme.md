# Codeview
-------------
http://avraampiperidis.github.io/Codeview/ <br>
[![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-Codeview-brightgreen.svg?style=flat)](https://android-arsenal.com/details/1/3999)

Codeview is a android library tha lets you
preview code in webview very easy and simple with highlighs and colors.
With styles to chooses and language.

Also you can inject html and text into webview or any extended webview class.


This library was inspired and is working thanks to [highlight.js](https://highlightjs.org/). <br>
Apps using Codeview library.<br> 
https://play.google.com/store/apps/details?id=com.protectsoft.javatutorial   <br>
https://play.google.com/store/apps/details?id=com.protectsoft.pythontutorial  <br>

https://bintray.com/zeronerone/maven/Codeview#statistics <br>

Usage
-----

#### Codeview

#### Download/Install Gradle
--------

```groovy
repositories {
        jcenter()
    }
    
compile 'Codeview-1.0.0:webviewcode:1.0.0' 
```
##### 1) Get a reference to your WebView or any extended WebView

```java
WebView webview = (WebView) findViewById(R.id.webview);
//set settings here
```

##### 2) Basic usage. Default style is Original, and default language is java.

```java
//your string code 
String code = "public static void main(String[] args) { \n" +
                "\n" +
                "//comments\n" +
                "   for(int i =0; i < 10; i++) {\n" +
                "       addnum();\n" +
                "   }\n" +
                "\n" +
                "}\n";
								
Codeview.with(getApplicationContext())
		.withCode(code)
		.into(webview);
```
<img src="https://github.com/avraampiperidis/Codeview/blob/master/readmepics/pic2.png?raw=true" width="350">

##### 3) set style and language.

```java
MyTouchWebView webview = (MyTouchWebView) findViewById(R.id.mytouchwebview);
//set settings here
```

```java
//your string java code 
String code = "public static void main(String[] args) { \n" +
                "\n" +
                "//comments\n" +
                "   for(int i =0; i < 10; i++) {\n" +
                "       addnum();\n" +
                "   }\n" +
                "\n" +
                "}\n";
								
Codeview.with(getApplicationContext())
		.withCode(code)
		.setStyle(Settings.WithStyle.DARKULA)
        .setLang(Settings.Lang.JAVA)
		.into(webview);
```
<img src="https://github.com/avraampiperidis/Codeview/blob/master/readmepics/pic1.png?raw=true" width="350">

##### 4) Inject html head content and text.

```java
WebView webview = (WebView) findViewById(R.id.webview);
//set settings here
```

```java
//your string javascript code
        String code = "function Constructor(v1,v2,v3)\n" +
                "{\n" +
                "  this.v1 = v1;\n" +
                "  this.v2 = v2;\n" +
                "  this.funk = function()\n" +
                "  {\n" +
                "    console.log(\"Test: \"+ v3 );\n" +
                "  }\n" +
                "}\n" +
                "\n" +
                "var obj1 = new Constructor(\"par1\",\"par2\",\"par3\");\n" +
                "var arr = [\"w1\",\"w2\",\"w3\",obj1];\n" +
                "\n" +
                "function f2()\n" +
                "{            \n" +
                "  obj1.funk(); //works ok\n" +
                "  console.log(\"test \"+tablica[3].funk.call() ); //doesn't work\n" +
                "}";
                
                
        Codeview.with(getApplicationContext())
                .setHtmlHeadContent("<style> table,tr,td {" +
                        " border: 1px solid black;" +
                        " }" +
                        "" +
                        "</style>")
                .withHtml("<h1> h1 injected header</h1>")
                .withText("this text is always wrap inside pre tags")
                .withCode(code)
                .withHtml("<h1> h1 header after code </h1>")
                .withHtml("<table><tr><td> my html table </td></tr></table>")
                .setStyle(Settings.WithStyle.DARKSTYLE)
                .setLang(Settings.Lang.JAVASCRIPT)
                .setAutoWrap(true)
                .into(webView);
```
<img src="https://github.com/avraampiperidis/Codeview/blob/master/readmepics/pic3.png?raw=true" width="350">

## License
MIT License

Copyright (c) 2016 Avraam Piperidis

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


