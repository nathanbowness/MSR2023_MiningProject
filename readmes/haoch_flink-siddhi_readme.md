flink-siddhi
============

[![Travis CI](https://api.travis-ci.org/haoch/flink-siddhi.svg)](https://travis-ci.org/haoch/flink-siddhi)
[![Clojars Project](https://img.shields.io/clojars/v/com.github.haoch/flink-siddhi_2.11.svg)](https://clojars.org/com.github.haoch/flink-siddhi_2.11)

> A light-weight library to run [Siddhi CEP](https://github.com/wso2/siddhi) within [Apache Flink](https://github.com/apache/flink) streaming application.

Siddhi CEP is a lightweight and easy-to-use Open Source Complex Event Processing Engine (CEP) released as a Java Library under `Apache Software License v2.0`. 
Siddhi CEP processes events which are generated by various event sources, analyses them and notifies appropriate complex events according to the user specified queries. 

This project is mainly to provide a light-weight library to easily run Siddhi CEP within flink streaming application.

## Features

* Integrate Siddhi CEP as an stream operator (i.e. `TupleStreamSiddhiOperator`), supporting rich CEP features like
  * Filter
  * Join
  * Aggregation
  * Group by
  * Having
  * Window
  * Conditions and Expressions
  * Pattern processing
  * Sequence processing
  * Event Tables
  * ...
* Provide easy-to-use Siddhi CEP API to integrate Flink DataStream API (See `SiddhiCEP` and `SiddhiStream`)
  * Register Flink DataStream associating native type information with Siddhi Stream Schema, supporting POJO,Tuple, Primitive Type, etc.
  * Connect with single or multiple Flink DataStreams with Siddhi CEP Execution Plan
  * Return output stream as DataStream with type intelligently inferred from Siddhi Stream Schema
* Integrate siddhi runtime state management with Flink state (See `AbstractSiddhiOperator`)
* Support siddhi plugin management to extend CEP functions. (See `SiddhiCEP#registerExtension`)

## Development

### Prerequisites

* Java (Version: `1.8`)
* Apache Maven
* Apache Flink (Version: `1.7.0`)

### Clone

	git clone git@github.com:haoch/flink-siddhi.git

### Building

   	mvn clean install -DskipTests
   
### Testing

   	mvn clean test

## Usage and API

* Add [`com.github.haoch:flink-siddhi`](https://clojars.org/com.github.haoch/flink-siddhi_2.11) in project dependencies:

        <dependencies>
                <dependency>
                        <groupId>com.github.haoch</groupId>
                        <artifactId>flink-siddhi_2.11</artifactId>
                        <version>LATEST</version>
                </dependency>
        </dependencies>
        
        <repositories>
                <repository>
                        <id>clojars</id>
                        <url>http://clojars.org/repo/</url>
                </repository>
        </repositories>
 
* Execute [`SiddhiQL`](https://docs.wso2.com/display/CEP300/Introduction+to+Siddhi+Query+Language) with `SiddhiCEP` API, for example:

        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        SiddhiCEP cep = SiddhiCEP.getSiddhiEnvironment(env);
        
        cep.registerExtension("custom:plus",CustomPlusFunctionExtension.class);
        
        cep.registerStream("inputStream1", input1, "id", "name", "price","timestamp");
        cep.registerStream("inputStream2", input2, "id", "name", "price","timestamp");
        
        DataStream<Tuple5<Integer,String,Integer,String,Double>> output = cep
             .from("inputStream1").union("inputStream2")
             .cql( 
             "from every s1 = inputStream1[id == 2] "
             + " -> s2 = inputStream2[id == 3] "
             + "select s1.id as id_1, s1.name as name_1, s2.id as id_2, s2.name as name_2 , custom:plus(s1.price,s2.price) as price"
             + "insert into outputStream")
            .returns("outputStream");
        
        env.execute();
     
  > For more examples, please see [`org.apache.flink.contrib.siddhi.SiddhiCEPITCase`](https://github.com/haoch/flink-siddhi/blob/master/core/src/test/java/org/apache/flink/streaming/siddhi/SiddhiCEPITCase.java)
  

## Documentations
* Site: https://haoch.github.io/flink-siddhi/
* Wiki: https://github.com/haoch/flink-siddhi/wiki
* Siddhi Query Language: https://docs.wso2.com/display/CEP300/Introduction+to+Siddhi+Query+Language
* Apache Flink: http://flink.apache.org/

## Support and Contact
* Issues: https://github.com/haoch/flink-siddhi/issues
* Documents: https://github.com/haoch/flink-siddhi/wiki

## Contributors

* Hao Chen [@haoch](https://github.com/haoch) (Author, hao AT apache DOT org)
* Aparup Banerjee [@aparup](https://github.com/aparup)
* Blues Zheng [@kisimple](https://github.com/kisimple)
* [@aagupta1](https://github.com/aagupta1)
* [@wittyameta](https://github.com/wittyameta)
* Jinhu Wu [@wujinhu](https://github.com/wujinhu)
* Pi Jing [@tammypi](https://github.com/tammypi)
* Jayant Ameta [@wittyameta](https://github.com/wittyameta)
* Drona [@Dr0na](https://github.com/Dr0na)

## Contribution

Welcome to make contribution to code or document by [sending a pull request](https://github.com/haoch/flink-siddhi/pulls), or [reporting issues or bugs](https://github.com/haoch/flink-siddhi/issues).

## License

Licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). More details, please refer to [LICENSE](LICENSE) file.