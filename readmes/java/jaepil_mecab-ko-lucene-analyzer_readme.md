# mecab-ko-lucene-analyzer

## 소개

[mecab-ko-lucene-analyzer](https://bitbucket.org/eunjeon/mecab-ko-lucene-analyzer)는 [mecab-ko](https://bitbucket.org/eunjeon/mecab-ko), [mecab-ko-dic](https://bitbucket.org/eunjeon/mecab-ko-dic)을 사용한 lucene/solr용 한국어 형태소 분석기입니다.

다음과 같은 기능들을 제공합니다.

- 명사추출
- 복합명사 분해
- 원어절 추출

[ElasticSearch](http://www.elasticsearch.org/)용 형태소 분석기의 사용 설명서는 [mecab-ko analysis for ElasticSearch](https://bitbucket.org/eunjeon/mecab-ko-lucene-analyzer/raw/master/elasticsearch-analysis-mecab-ko/)에서 보실 수 있습니다.

## 특징

- '무궁화꽃이피었습니다.'와 같이 띄어 쓰기가 잘못된 오류를 교정하여 형태소 분석이 가능합니다.
- StandardTokenizer의 경우, 명사뿐 아니라 품사가 결합된 어절도 Token으로 뽑아냅니다.

        철수가 학교에 간다. -> 철수가, 철수, 학교에, 학교, 간다

- 문장의 끝에 문장의 끝을 알리는 기호 "`.!?`"가 있으면 더 자연스럽게 형태소 분석이 됩니다.
- 분석된 token의 형태소를 구체적으로 볼 수 있습니다.

        박보영이(NNP+JKS), 박보영(NNP), 서울에(NNP+JKB), 서울(NNP), 갔다(VV+EP+EF), 가/VV(VV)

- Apache Lucene/Solr 6.3.0 버전 기준으로 작성되었습니다. (Apache Lucene/Solr 6.3.0에서 사용 가능)

## 설치

### mecab-ko(형태소 분석기 엔진)과 mecab-ko-dic(사전 파일) 설치

mecab-ko와 mecab-ko-dic의 설치는 [mecab-ko-dic 설명](https://bitbucket.org/eunjeon/mecab-ko-dic)을 참조하시기 바랍니다.

### MeCab.jar와 libMeCab.so 설치

설치 문서는 [Solr Quick Start](http://lucene.apache.org/solr/quickstart.html) 문서 기준으로 작성되었습니다.

[mecab-java-0.996.tar.gz](https://bitbucket.org/eunjeon/mecab-java/downloads/mecab-java-0.996.tar.gz) 를 다운받아 설치합니다.

    $ tar zxvf mecab-java-0.996.tar.gz
    $ cd mecab-java-0.996
    $ vi Makefile
        # java path 설정.               ; INCLUDE=/usr/lib/jvm/java-7-oracle/include
        # OpenJDK 사용시 "-O1" 로 변경. ; $(CXX) -O1 -c -fpic $(TARGET)_wrap.cxx  $(INC)
        # "-cp ." 추가.                 ; $(JAVAC) -cp . test.java
    $ make
    $ cp MeCab.jar [solr 디렉터리]/server/lib/ext # JNI 클래스는 System classpath에 위치해야 합니다. Jetty는 기본값으로 $jetty.home/lib/ext에 추가적인 jar를 넣을 수 있습니다.
    $ sudo cp libMeCab.so /usr/local/lib

__주의 사항__

- mecab-ko의 버전에 맞는 mecab-java-0.996.tar.gz를 선택해야 합니다. mecab-0.996-ko.0.9.0 버전에서는 mecab-java-0.996을 사용해야 합니다.
- Makefile에서 INCLUDE 값을 자신의 환경에 맞게 변경해야 합니다.
- OpenJDK를 사용하시는 경우, 최적화 옵션을 -O나 -O1로 고쳐야 합니다. [mecab-ko-lucene-analyzer OpenJDK에서 사용하기](http://eunjeon.blogspot.kr/2013/04/mecab-ko-lucene-analyzer-openjdk.html) 참조

### mecab-ko-lucene-analyzer 다운로드 및 설치
[mecab-ko-lucene-analyzer 다운로드 페이지](https://bitbucket.org/eunjeon/mecab-ko-lucene-analyzer/downloads)에서 `mecab-ko-lucene-analyzer-XX.tar.gz`의 최신 버전을 다운 받아 압축을 풀면 두개의 jar파일이 있습니다. 

- mecab-ko-mecab-loader-XX.jar: System classpath에 복사합니다. (ex: `[solr 디렉터리]/server/lib/ext`)
- mecab-ko-lucene-analyzer-XX.jar: Solr contrib 디렉터리에 디렉터리를 생성후 복사합니다. (ex: `[solr 디렉터리]/contrib/eunjeon/lib`)

#### mecab-ko-lucene-analyzer 버전별 mecab-ko-dic, Lucene/Solr, elasticsearch 지원 버전

| mecab-ko-lucene-analyzer | mecab-ko-dic                 | Lucene/Solr                 | elasticsearch               |
| ------------------------ | ---------------------------- | --------------------------- | --------------------------- |
| **0.21.0 or higher**     | mecab-ko-dic-2.0.0 or higher | Lucene/Solr 6.3.0 or higher | [mecab-ko analysis for ElasticSearch](https://bitbucket.org/eunjeon/mecab-ko-lucene-analyzer/raw/master/elasticsearch-analysis-mecab-ko/) 참조 |
| **0.18.x - 0.20.x**      | mecab-ko-dic-2.0.0 or higher | Lucene/Solr 5.3.x           | [mecab-ko analysis for ElasticSearch](https://bitbucket.org/eunjeon/mecab-ko-lucene-analyzer/raw/master/elasticsearch-analysis-mecab-ko/) 참조 |
| **0.17.x**               | mecab-ko-dic-2.0.0 or higher | Lucene/Solr 4.9.x - 4.10.x  | 1.3.x or higher             |
| **0.16.x**               | mecab-ko-dic-1.6.0 - 1.6.1   | Lucene/Solr 4.9.x - 4.10.x  | 1.3.x or higher             |
| **0.15.x**               | mecab-ko-dic-1.6.0 - 1.6.1   | Lucene/Solr 4.3.x - 4.8.x   | 0.90.x - 1.2.x              |
| **0.14.x**               | mecab-ko-dic-1.5.0 - 1.6.1   | Lucene/Solr 4.3.x - 4.8.x   | 0.90.x - 1.2.x              |
| **0.13.x**               | mecab-ko-dic-1.4.0           | Lucene/Solr 4.3.x - 4.8.x   | 0.90.x - 1.2.x              |
| **0.12.x**               | mecab-ko-dic-1.4.0           | Lucene/Solr 4.3.x           |                             |
| **0.11.x**               | mecab-ko-dic-1.3.0 - 1.4.0   | Lucene/Solr 4.3.x           |                             |
| **0.10.x**               | mecab-ko-dic-1.3.0 - 1.4.0   | Lucene/Solr 4.1.x - 4.2.x   |                             |
| **0.9.x**                | mecab-ko-dic-1.1.0 - 1.4.0   | Lucene/Solr 4.1.x - 4.2.x   |                             |

## 사용법

### solr 설정

#### solrconfig.xml 설정
`server/solr/configsets/data_driven_schema_configs/conf/solrconfig.xml`에 `mecab-ko-lucene-analyzer-XX.jar`가 있는 경로를 설정합니다.

    <lib dir="${solr.install.dir:../../../..}/contrib/eunjeon/lib" regex=".*\.jar" />

#### managed-schema 설정
`server/solr/configsets/data_driven_schema_configs/conf/managed-schema` 에 `fieldType` 을 설정합니다.

##### Tokenizer 옵션 속성

| 세팅                              |  설명                                                                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **mecabArgs**                     | mecab 실행옵션. 디폴트 값은 '-d /usr/local/lib/mecab/dic/mecab-ko-dic'<br />다른 옵션은 http://taku910.github.io/mecab/mecab.html 참조 |
| **compoundNounMinLength**         | 분해를 해야하는 복합명사의 최소 길이. 기본 값은 3                                                                                      |
| **useAdjectiveAndVerbOriginForm** | 동사와 형용사 원형을 사용하여 검색할지 여부. 디폴트 값은 true                                                                          |

##### managed-schema 설정 예
###### query에서는 복합명사 분해를 하지 않는 경우

    <!-- Korean -->
    <dynamicField name="*_txt_ko" type="text_ko" indexed="true" stored="true"/>
    <fieldType name="text_ko" class="solr.TextField" positionIncrementGap="100">
      <analyzer type="index">
        <tokenizer class="org.bitbucket.eunjeon.mecab_ko_lucene_analyzer.StandardTokenizerFactory"/>
      </analyzer>
      <analyzer type="query">
        <tokenizer class="org.bitbucket.eunjeon.mecab_ko_lucene_analyzer.StandardTokenizerFactory" compoundNounMinLength="100"/>
      </analyzer>
    </fieldType>

###### index, query 모두 복합명사 분해를 하는 경우

    <!-- StandardTokenizerFactory는 compoundNounMinLength를 속성으로 받을 수 있습니다.
         분해를 하는 복합명사의 최소 길이를 뜻하며 기본 값은 3입니다. 이 경우, 길이가 3미만인 복합명사는 분해하지 않습니다.
    -->
    <!-- Korean -->
    <dynamicField name="*_txt_ko" type="text_ko" indexed="true" stored="true"/>
    <fieldType name="text_ko" class="solr.TextField" positionIncrementGap="100">
      <analyzer> 
        <tokenizer class="org.bitbucket.eunjeon.mecab_ko_lucene_analyzer.StandardTokenizerFactory" compoundNounMinLength="3"/>
      </analyzer>
    </fieldType>


mecab-ko-dic을 디폴트 경로\(`/usr/local/lib/mecab/dic/mecab-ko-dic`\)에 설치하지 않은 경우에는 `mecabArgs` 속성을 사용하여 사전 경로를 지정해야 합니다.
mecab 다른 옵션은 다음의 URL을 참조하십시오. http://taku910.github.io/mecab/mecab.html

    <!-- Korean -->
    <dynamicField name="*_txt_ko" type="text_ko" indexed="true" stored="true"/>
    <fieldType name="text_ko" class="solr.TextField" positionIncrementGap="100">
      <analyzer>
        <tokenizer class="org.bitbucket.eunjeon.mecab_ko_lucene_analyzer.StandardTokenizerFactory" compoundNounMinLength="3" mecabArgs="-d /my/mecab-ko-dic/directory"/>
      </analyzer>
    </fieldType>

### solr 실행
`libMeCab.so` 파일이 있는 라이브러리 경로를 지정해 주면서 solr를 실행합니다.

    $ ./bin/solr start -e cloud -noprompt -Djava.library.path=/usr/local/lib

### 분석 결과
![Alt 박보영이 서울에 갔다.](solr_demo.png)

## 라이센스
Copyright 2013 Yongwoon Lee, Yungho Yu.
`mecab-ko-lucene-analyzer`는 아파치 라이센스 2.0에 따라 소프트웨어를 사용, 재배포 할 수 있습니다. 더 자세한 사항은 [Apache License Version 2.0](https://bitbucket.org/eunjeon/mecab-ko-lucene-analyzer/raw/master/LICENSE)을 참조하시기 바랍니다.
