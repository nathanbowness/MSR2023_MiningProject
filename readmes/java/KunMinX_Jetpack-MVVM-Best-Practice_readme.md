![](https://images.xiaozhuanlan.com/photo/2021/b106fd65d34a4a724244e7c5b42a2372.jpg)

[《重学安卓》](https://xiaozhuanlan.com/kunminx)付费读者加微信进群：myatejx

> [免费试读](https://juejin.cn/post/7106042518457810952)，**[专栏目录](https://www.yuque.com/kunminx/fpmbc5/ghlwb5)**，**[更新动态](https://www.yuque.com/kunminx/fpmbc5/in59vu)**，[优惠政策](https://www.yuque.com/kunminx/fpmbc5/of601a)

&nbsp;

# 版权声明

我们就本项目 "被卖课" 一事，在掘金发表一期专访 [《开源项目被人拿去做课程卖了 1000 多万是什么体验》](https://juejin.im/post/5ecb4950518825431a669897)

本项目系我为方便开发者们 **无痛理解 Google 开源 Jetpack MVVM 中每个架构组件的 存在缘由、职责边界**，而 **精心设计的高频应用场景**，

与此同时，本项目是作为 [《重学安卓》](https://xiaozhuanlan.com/topic/6017825943)专栏 Jetpack MVVM 系列文章 “配套项目” 而存在，**文章内容和项目代码设计均涉及本人对 Jetpack MVVM 独家理解，本人对此享有著作权**。

任何组织或个人，未经与作者本人沟通，不得将本项目代码设计和本人对 Jetpack MVVM 独家理解用于 "**打包贩卖、引流、出书 和 卖课**" 等商业用途。

&nbsp;

# 架构图一览

![](https://images.xiaozhuanlan.com/photo/2022/3254319c497bb39d638667cb589b48c7.png)

&nbsp;

# 前言

上周我在各大 “技术社区” 发表了一篇 [《Jetpack MVVM 精讲》](https://juejin.im/post/5dafc49b6fb9a04e17209922)，原以为在 “知识网红” 唱衰 Android 的 2019 会无人问津，没想到文章一经发布，从 “国内知名公司” 架构师、技术经理，到 “世界级公司”  Android 开发都在看。

且从读者反馈来看，近期大部分 Android 开发已跳出舒适圈，开始尝试认识和应用 Jetpack MVVM 到实际项目中。

只可惜，关于 Jetpack MVVM，网上多是 **东拼西凑、人云亦云、通篇贴代码** 文章，这不仅不能提供 “完整视角” 帮助读者 首先明确背景状况，更是给还没入门 Jetpack 读者 **徒添困扰**、起 **劝退** 作用。

好消息是，这一期，我们带着 **精心打磨 Jetpack MVVM 最佳实践案例** 来了！

&nbsp;
&nbsp;


|                       爱不释手交互设计                       |                         连贯用户体验                         |                      唯一可信源统一分发                      |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![](https://upload-images.jianshu.io/upload_images/57036-0a5cdc68f003211a.gif) | ![](https://upload-images.jianshu.io/upload_images/57036-2b21db531e51ff03.gif) | ![](https://upload-images.jianshu.io/upload_images/57036-9a541148ce5bed2e.gif) |



|                   横竖屏布局无缝切换                   |
| :----------------------------------------------------: |
| ![](https://i.loli.net/2021/08/25/X9rado7AfnCEgv3.gif) |

&nbsp;
&nbsp;

# 项目简介

本人拥有 3 年 “移动端业务架构” 践行和设计经验，领导或参与团队 “重构” 中大型项目多达十数个，对 Jetpack MVVM 架构在 “确立规范化、标准化开发模式 以 **减少不可预期错误**” 所作的努力，有深入理解。



在这个案例中，我将为你展示，Jetpack MVVM 是如何 **以简驭繁** 地将原本十分容易出错、一出错就会耽搁半天的开发工作，通过寥寥几行代码 轻而易举完成。

> 👆👆👆 划重点！

&nbsp;

该项目中，

> 我们为 **横、竖屏** 场景安排两套 **截然不同布局**，且在 [生命周期](https://xiaozhuanlan.com/topic/0213584967)、[重建机制](https://xiaozhuanlan.com/topic/7692814530)、[状态管理](https://xiaozhuanlan.com/topic/7692814530)、[DataBinding](https://xiaozhuanlan.com/topic/9816742350)、[ViewModel](https://xiaozhuanlan.com/topic/6257931840)、[LiveData](https://xiaozhuanlan.com/topic/0168753249) 、[Navigation](https://xiaozhuanlan.com/topic/5860149732) 等知识点帮助下，通过寥寥几行代码，轻松做到 **在横竖屏两种布局间 无缝切换，且不产生任何 预期外错误**。


> 我们在多个 Fragment 页面 分别安排 **播放状态指示器**（包括 播放暂停按钮状态、播放列表当前索引指示 等），并向你展示 “如何” 及 “为何” 通过 [LiveData](https://xiaozhuanlan.com/topic/0168753249) **配合** 唯一可信源 [ViewModel](https://xiaozhuanlan.com/topic/6257931840) 或单例，实现 **全应用范围内 “可追溯事件” 统一分发**。


> 我们在 Fragment 和 Activity 之间分别安排 跨页面通信，从而向你展示 如何基于 **迪米特原则**（也称 最少知道原则）、通过 UnPeekLiveData 和 应用级 SharedViewModel 实现 **生命周期安全、确保消息同步可靠一致的 页面通信**。


> 我们在 `ui.page` 、`data.repository`、`domain.request` 等目录下，分别安排 视图控制器、[ViewModel](https://xiaozhuanlan.com/topic/6257931840) 、DataRepository 等 内容，从而向你展示，**单向依赖** 架构设计，是如何通过分层 数据请求和响应，**规避 “内存泄漏”** 等问题。


> 本项目代码一律采用 经过 ISO 认证 标准化工业级语言 Java 来编写。且在上述类中，我们大都 **提供丰富注释**，助你理解 “骨架代码” 为何要如此设计、如此设计能 **在软件工程背景下** 避免哪些不可预期错误。

&nbsp;
&nbsp;

除了 **在 "以简驭繁" 代码中 掌握 MVVM 最佳实践**，你还可从该项目中获得内容包括：

1. 整洁代码风格 和 标准资源命名规范。
2. 对 “视图控制器” 知识点的 深入理解 和 正确使用。
3. AndroidX 和 Material Design 2 全面使用。
4. ConstraintLayout 约束布局最佳实践。
5. **优秀的 用户体验 和 交互设计**。
6. 绝不使用 Dagger，绝不使用奇技淫巧、编写艰深晦涩代码。
7. The one more thing is：

即日起，可在 "应用商店" 下载体验！

[![google-play1.png](https://upload-images.jianshu.io/upload_images/57036-f9dbd7810d38ae95.png)](https://www.coolapk.com/apk/247826) [![coolapk1.png](https://upload-images.jianshu.io/upload_images/57036-6cf24d0c9efe8362.png)](https://www.coolapk.com/apk/247826)


&nbsp;
&nbsp;

# Thanks to

[AndroidX](https://developer.android.google.cn/jetpack/androidx)

[Jetpack](https://developer.android.google.cn/jetpack/)

[material-components-android](https://github.com/material-components/material-components-android)

[轻听](https://play.google.com/store/apps/details?id=com.tencent.qqmusiclocalplayer)

[AndroidSlidingUpPanel](https://github.com/umano/AndroidSlidingUpPanel)

项目中使用 图片素材 来自 [UnSplash](https://unsplash.com/) 提供 **免费授权图片**。

项目中使用 音频素材 来自 [BenSound](https://www.bensound.com/) 提供 **免费授权音乐**。

&nbsp;
&nbsp;

# Who is using

根据小伙伴们 “开源库使用情况” 匿名调查问卷参与，截至 2022年5月28日，我们了解到

包括 “腾讯音乐、网易、BMW、TCL” 在内诸多知名厂商软件，都参考过我们开源的此架构模式，或正在使用我们维护的 [UnPeek-LiveData](https://github.com/KunMinX/UnPeek-LiveData) 等框架。

目前已将统计数据更新到 相关开源库 ReadMe 中，错过本次问卷调查的小伙伴也不用担心，我们继续对此保持开放，不定期将小伙伴们登记的公司和产品更新到表格，

以便吸纳更多小伙伴参与对 “架构组件” 的使用和反馈，集众人所长，让组件得以不断演化和升级。

https://wj.qq.com/s2/8362688/124a/

| 集团 / 公司 / 品牌 / 团队                             | 产品           |
| ----------------------------------------------------- | -------------- |
| 腾讯音乐                                              | QQ 音乐        |
| 网易                                                  | 网易云音乐     |
| TCL                                                   | 内置文件管理器 |
| 贵州广电网络                                          | 乐播播         |
| 上海亿保健康管理有限公司                              | 安诺保         |
|                                                       | 小辣椒         |
| ezen                                                  | Egshig音乐     |
| BMW                                                   | Speech         |
| 上海互教信息有限公司                                  | 知心慧学教师   |
| 美术宝                                                | 弹唱宝         |
|                                                       | 网安           |
| 字节跳动直播                                          | 直播 SDK       |
| 一加手机                                              | OPNote         |

&nbsp;
&nbsp;


# My Pages

Email：[kunminx@gmail.com](mailto:kunminx@gmail.com)

Juejin：[KunMinX 在掘金](https://juejin.im/user/58ab0de9ac502e006975d757/posts)

[《重学安卓》 专栏](https://xiaozhuanlan.com/kunminx)

付费读者加微信进群：myatejx

[![重学安卓小专栏](https://images.xiaozhuanlan.com/photo/2021/d493a54a32e38e7fbcfa68d424ebfd1e.png)](https://xiaozhuanlan.com/kunminx)

&nbsp;
&nbsp;

# License

```
Copyright 2019-present KunMinX

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

