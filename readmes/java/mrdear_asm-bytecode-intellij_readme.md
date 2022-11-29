This file was created by IntelliJ IDEA 10.0.1 for binding GitHub repository

### what

为 ams-bytecode-intellij增加cfr decompile反编译选项

![cfr decompile](http://oobu4m7ko.bkt.clouddn.com/1517390920.png?imageMogr2/thumbnail/!100p)


### 使用方式

**安装**

方式1. 打来IDEA plugins, 搜索 `CFR` 关键词,下载 `CFR Decompile`

方式2: 打开[https://plugins.jetbrains.com/plugin/11035-cfr-decompile](https://plugins.jetbrains.com/plugin/11035-cfr-decompile),然后下载后手动安装


**使用**

1. 在编辑框右键,选择 show bytecode outline 


### example

**--sugarenums false**
![](http://oobu4m7ko.bkt.clouddn.com/enum.png?imageMogr2/thumbnail/!100p)


**--stringbuilder false**
![](http://oobu4m7ko.bkt.clouddn.com/string.png?imageMogr2/thumbnail/!100p)

**--decodestringswitch false**
![](http://oobu4m7ko.bkt.clouddn.com/switchcase.png)


### link

[CFR - another java decompiler](http://www.benf.org/other/cfr/)


### 附录

**CFR参数**
```

    --aexagg                         (boolean) 
    --aggressivesizethreshold        (int = 0)  default: 15000
    --allowcorrecting                (boolean)  default: true
    --analyseas                      (One of [JAR, WAR, CLASS]) 
    --arrayiter                      (boolean)  default: true if class file from version 49.0 (Java 5) or greater
    --caseinsensitivefs              (boolean)  default: false
    --clobber                        (boolean) 
    --collectioniter                 (boolean)  default: true if class file from version 49.0 (Java 5) or greater
    --commentmonitors                (boolean)  default: false
    --comments                       (boolean)  default: true
    --decodeenumswitch               (boolean)  default: true if class file from version 49.0 (Java 5) or greater
    --decodefinally                  (boolean)  default: true
    --decodelambdas                  (boolean)  default: true if class file from version 52.0 (Java 8) or greater
    --decodestringswitch             (boolean)  default: true if class file from version 51.0 (Java 7) or greater
    --dumpclasspath                  (boolean)  default: false
    --eclipse                        (boolean)  default: true
    --elidescala                     (boolean)  default: false
    --extraclasspath                 (string) 
    --forcecondpropagate             (boolean) 
    --forceexceptionprune            (boolean) 
    --forcereturningifs              (boolean) 
    --forcetopsort                   (boolean) 
    --forcetopsortaggress            (boolean) 
    --forloopaggcapture              (boolean) 
    --hidebridgemethods              (boolean)  default: true
    --hidelangimports                (boolean)  default: true
    --hidelongstrings                (boolean)  default: false
    --hideutf                        (boolean)  default: true
    --innerclasses                   (boolean)  default: true
    --j14classobj                    (boolean)  default: false if class file from version 49.0 (Java 5) or greater
    --jarfilter                      (string) 
    --labelledblocks                 (boolean)  default: true
    --lenient                        (boolean)  default: false
    --liftconstructorinit            (boolean)  default: true
    --outputdir                      (string) 
    --outputpath                     (string) 
    --override                       (boolean)  default: true if class file from version 50.0 (Java 6) or greater
    --pullcodecase                   (boolean)  default: false
    --recover                        (boolean)  default: true
    --recovertypeclash               (boolean) 
    --recovertypehints               (boolean) 
    --removebadgenerics              (boolean)  default: true
    --removeboilerplate              (boolean)  default: true
    --removedeadmethods              (boolean)  default: true
    --removeinnerclasssynthetics     (boolean)  default: true
    --rename                         (boolean)  default: false
    --renamedupmembers              
    --renameenumidents              
    --renameillegalidents           
    --renamesmallmembers             (int = 0)  default: 0
    --showinferrable                 (boolean)  default: false if class file from version 51.0 (Java 7) or greater
    --showops                        (int = 0)  default: 0
    --showversion                    (boolean)  default: true
    --silent                         (boolean)  default: false
    --stringbuffer                   (boolean)  default: false if class file from version 49.0 (Java 5) or greater
    --stringbuilder                  (boolean)  default: true if class file from version 49.0 (Java 5) or greater
    --sugarasserts                   (boolean)  default: true
    --sugarboxing                    (boolean)  default: true
    --sugarenums                     (boolean)  default: true if class file from version 49.0 (Java 5) or greater
    --tidymonitors                   (boolean)  default: true
    --help                           (string) 
```
