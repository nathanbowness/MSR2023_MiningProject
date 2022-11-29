<div align="center">
 <img src=".github/bandev-xplosion.svg" height="150" align="center" />
 <br>
 <a>
  <img src="https://bandev.uk/api/badges/app-promise.svg"/>
  <a href="https://github.com/BanDev/Xplosion/blob/main/LICENSE.md" target="_blank">
   <img src="https://img.shields.io/github/license/bandev/Xplosion"/>
  </a>
  <img src="https://img.shields.io/github/repo-size/bandev/Xplosion"/>
  <a href="https://www.buymeacoffee.com/bandev" target="_blank">
   <img src="https://img.shields.io/badge/donate-%C2%A35-orange" >
  </a>
 </a>
</div>

<h2 id="what">What is Xplosion?</h2>
<p>Xplosion is a fork of <a href="https://github.com/hanks-zyh/SmallBang">SmallBang</a> that has been converted to Kotlin and updated for the latest version of Android.</p>

<h2 id="usage">Usage</h2>
    <ul>
        <li>
            <b>Step 1.</b> Make sure <code>mavenCentral()</code> is added as a dependency in your root gradle file:
            <br>
            <br>
            <pre>
allprojects {
    repositories {
        mavenCentral()
    }
}</pre>
        </li>    
        <li>
            <b>Step 2.</b> Add the dependency to your app's project gradle file:
            <br>
            <br>
            <pre>
dependencies {
    implementation 'uk.bandev:xplosion:1.0.7'
}</pre>
        </li>   
        <li>
                <b>Step 3.</b> Add the view to your layout:
                <br>
                <br>
                <pre>
&lt;uk.bandev.xplosion.XplosionView
    android:id="@+id/xplosion"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"&gt;

    ...
    
&lt;/uk.bandev.xplosion.XplosionView&gt;</pre>
            </li>   
    </ul>

<h2 id="contributing">Contributing</h2>
<p>Looking to contribute to Xplosion? That&#39;s great! There are a couple of ways to help out. Translations, bug reports and pull requests are all greatly appreciated. Please refer to our <a href="https://github.com/BanDev/Xplosion/blob/main/CONTRIBUTING.md">contributing guidelines</a> to get started.</p>

<h2 id="license">License</h2>
<pre>
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
</pre>
