## Amazon Kinesis Video Streams Producer SDK Java

## License

This library is licensed under the Apache License, 2.0. 

## Introduction

Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), and other processing.

The Amazon Kinesis Video Streams Producer SDK Java makes it easy to build an on-device application that securely connects to a video stream, and reliably publishes video and other media data to Kinesis Video Streams. It takes care of all the underlying tasks required to package the frames and fragments generated by the device's media pipeline. The SDK also handles stream creation, token rotation for secure and uninterrupted streaming, processing acknowledgements returned by Kinesis Video Streams, and other tasks.

## Resources

* [Developer Guide](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-javaapi.html) - For in-depth getting started and usage information.
* [Release Notes](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/releases) - To see the latest features, bug fixes, and changes in the SDK
* [Issues](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/issues) - Report issues and submit pull requests 


### Prerequisites

* You can find available pre-built KinesisVideoProducerJNI library in [src/main/resources/lib/](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/tree/master/src/main/resources/lib) for Mac (x64), Ubuntu (x64) and Raspian (x86) and Windows 10. If pre-built libraries did not work for you, ["KinesisVideoProducerJNI"](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp) native library needs to be built first before running the Java demo application. Please follow the steps  in the section **Build the native library (KinesisVideoProducerJNI) to run Java Demo App** in Producer SDK CPP [readme](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp).

### Building from Source

Import the Maven project to your IDE, it will find dependency packages from Maven and build.

### Examples

#### Launching Demoapp sample application

Run `DemoAppMain.java` in `./src/main/demo` with JVM arguments set to
```
-Daws.accessKeyId=<YourAwsAccessKey> -Daws.secretKey=<YourAwsSecretKey> -Dkvs-stream=<YourKinesisVideoStreamName> -Djava.library.path=<NativeLibraryPath> -Dlog4j.configurationFile=log4j2.xml
```
for **non-temporary** AWS credential.

```
-Daws.accessKeyId=<YourAwsAccessKey> -Daws.secretKey=<YourAwsSecretKey> -Daws.sessionToken=<YourAwsSessionToken> -Dkvs-stream=<YourKinesisVideoStreamName> -Djava.library.path=<NativeLibraryPath> -Dlog4j.configurationFile=log4j2.xml
```
for *temporary* AWS credential.

**Note**: NativeLibraryPath must contain your ["KinesisVideoProducerJNI"](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp#build-the-native-library-kinesisvideoproducerjni-to-run-java-demo-app) library. File name depends on your Operating System:
* `libKinesisVideoProducerJNI.so` for Linux
* `libKinesisVideoProducerJNI.dylib` for Mac OS
* `KinesisVideoProducerJNI.dll` for Windows

If you are using pre-built libraries, please specify the path of library. Take pre-build library for Mac as example, you can specify `src/resources/lib/mac` as <NativeLibraryPath>.

Demo app will start running and putting sample video frames in a loop into Kinesis Video Streams. You can change your stream settings in `DemoAppMain.java` before you run the app.

##### Run the demo application from command line

If you want to run the `DemoAppMain`, follow the [steps](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/issues/14) below. See [Prerequisites](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java#prerequisites) to find available native library needed to run `DemoAppMain`.

Change the current working directory to

```
$ cd /<YOUR_FOLDER_PATH_WHERE_SDK_IS_DOWNLOADED>/amazon-kinesis-video-streams-producer-sdk-java/
```

Compile and assemble Java SDK, Java Demoapp and the Maven dependencies
```
$ mvn clean compile assembly:single
```

Start the demo app
```
$ java -classpath target/amazon-kinesis-video-streams-producer-sdk-java-1.12.1-jar-with-dependencies.jar -Daws.accessKeyId=<ACCESS_KEY> -Daws.secretKey=<SECRET_KEY> -Dkvs-stream=<KINESIS_VIDEO_STREAM_NAME> -Djava.library.path=<NativeLibraryPath> -Dlog4j.configurationFile=log4j2.xml com.amazonaws.kinesisvideo.demoapp.DemoAppMain

```
##### Run API and functionality tests
```
$ mvn clean test -DargLine="-Daws.accessKeyId=<YourAwsAccessKey> -Daws.secretKey=<YourAwsSecretKey> -Daws.sessionToken=<YourAwsSessionToken> -Djava.library.path=<NativeLibraryPath> -Dlog4j.configurationFile=log4j2.xml"
```

##### Run the demo application from Docker

Refer the **README.md** file in the  *dockerscripts* folder for running the build and demo app within Docker container.

#### Launching PutMediaDemo sample application

 Run `PutMediaDemo.java` to send sample mkv stream to Kinesis Video Streams. **Note:** ACCESS_KEY, SECRET_KEY, and a KINESIS_VIDEO_STREAM are required for running this sample application as well. However, this demo application does not require JNI.

```
-Daws.accessKeyId=<YourAwsAccessKey> -Daws.secretKey=<YourAwsSecretKey> -Dkvs-stream=<YourKinesisVideoStreamName>
```
for **non-temporary** AWS credential.

```
-Daws.accessKeyId=<YourAwsAccessKey> -Daws.secretKey=<YourAwsSecretKey> -Daws.sessionToken=<YourAwsSessionToken> -Dkvs-stream=<YourKinesisVideoStreamName>
```
#### Pre-built KinesisVideoProducerJNI library supported platforms
* Mac OS X (El capitan 10.11 or above)
* Ubuntu (14.04 or above)
* Raspian (9 stretch or above)

#### Additional Examples

For additional examples on using Kinesis Video Streams Java SDK and  Kinesis Video Streams Parsing Library refer:

##### [Kinesis Video Streams Producer SDK CPP](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/README.md)
##### [Kinesis Video Streams Parser Library](https://github.com/aws/amazon-kinesis-video-streams-parser-library/blob/master/README.md)

##### [Kinesis Video Streams Android](https://github.com/awslabs/aws-sdk-android-samples/tree/master/AmazonKinesisVideoDemoApp)

#### Troubleshooting

If you notice error in loading the native library (JNI), then check the output of `ldd` or `otool`

```
$ ldd libKinesisVideoProducerJNI.so
```
or in MacOS
```
$ otool -L libKinesisVideoProducerJNI.dylib
```

This will provide details on missing libraries during linking; If the output shows missing shared libraries, then run the following commands to link:

Run the following from the build directory in CPP producer SDK:
```
cmake .. -DBUILD_JNI=TRUE 
make
```

Then, provide the path to the libKinesisVideoProducerJNI.dylib library.

This should resolve native library loading issues.

## Development

The repository is using `develop` branch as the aggregation and all of the feature development is done in appropriate feature branches. The PRs (Pull Requests) are cut on a feature branch and once approved with all the checks passed they can be merged by a click of a button on the PR tool. The master branch should always be build-able and all the tests should be passing. We are welcoming any contribution to the code base. The master branch contains our most recent release cycle from `develop`.

## Release Notes

### Release 1.12.1 (May 2022)
* Allow updating automaticStreamingFlags (default: AUTOMATIC_STREAMING_INTERMITTENT_PRODUCER) in ClientInfo
* Allow updating storePressurePolicy (default: CONTENT_STORE_PRESSURE_POLICY_DROP_TAIL_ITEM) in StreamInfo

### Release 1.12.0 (February 2022)
* Update guice from 4.2.3 to 5.1.0
* Update junit from 4.13.1 to 4.13.2
* Update mockito-core from 2.18.3 to 4.3.1
* Update annotations from 2.0.3 to 3.0.1
* Update commons-lang3 from 3.4 to 3.12.0
* Update gson from 2.8.2 to 2.9.0
* Update jsr-275 from 1.0.0 to 0.9.1 (artifact moved)
* Update commons-io from 2.7 to 2.11.0
* Update httpasyncclient from 4.1.4 to 4.1.5
* Replace custom logger with log4j2
* Obtain PIC logs in Java with JNI
* Add ProducerFunctionalityTests and ProducerApiTests

### Release 1.11.0 (11 September 2020)
* Improve TLS validation by implementing hostname verification

### Release 1.10.0 (29 May 2020)
* Updated docker scripts to incorporate the changes in producer SDK
* Provision of `CachedInfoMultiAuthServiceCallbacks` which implements caching layer and per-stream auth. Useful in the following scenarios:
  - A single client object is used for multiple streams that are intended for different accounts
  - For service proxy type of scenarios

### Release 1.9.5 (16 Jan 2020)
* Remove finalized() function and require explicit call on free() to avoid dangling finalized() causing memory leak.
* Performance improvement on sending data in multiple ongoing stream in one client.
* Fix stream information mis-alignment due to missing retention in describeStreamResult

### Release 1.9.4 (9 July 2019)
* License update: KVS SDK is under Apache 2.0 license now.
* Stablization updates in C layer.
* Added internal retry logic to handle error case that SDK can recover, i.e. network unstability.
* Skip over error fragments - SDK will continue skip any invalid fragments are ingested through SDK earlier and continue streaming.
* Automatic CPD (codec private data) extraction from the stream when CPD is part of the first H264 AnnexB frame.

### Release 1.9.3 (12 March 2019)
* Bug fix to avoid crash due to access to freed native stream object.

### Release 1.9.2 (21 Feburary 2019)
* Bug fix for broken MKV generated due to difference between trackInfoType in Java and C layer.

### Release 1.9.1 (19 Feburary 2019)
* Bug fix for credentials not rotating issue when given credentials expire in less than 40 minutes.
* Add audio video sample to support injesting multiple track data into Kinesis Video.

### Release 1.9.0 (8 Feburary 2019)
* Bug fix for KinesisVideoClient.unregisterMediaSource() accessing to freed native object issue.
* Add KinesisVideoClient.freeMediaSource() clean-up function to handle async behavior.

### Release 1.8.0 (25 January 2019)
* Fix duplicate stream error after unregistering media source when service call failed
* Fix inputstream not closing after stopSync issue
* Updating the name and description of Java SDK to publish in maven

### Release 1.7.0 (3 December 2018)
* Added support for uploading files(offline mode) to Kinesis Video Stream
* Additional fixes

### Release 1.6.0 (3 December 2018)
* Remove streamName parameter from KinesisVideoClient.registerMediaSource() as MediaSource already has the stream name in StreamInfo.
* Add KinesisVideoClient.unregisterMediaSource() to remove MediaSource to KinesisVideoProducerStream binding from KinesisVideoClient. Customers can use unregisterMediaSource() after they stop streaming, so MediaSource data will not to be sent to Kinesis Video Streams.
* Add getStreamInfo() to MediaSource instead of MediaSourceConfiguration. If customers have implemented their own MediaSource and MediaSourceConfiguration, they would need to provide stream information via MediaSource.getStreamInfo(). The MediaSourceConfiguration.getStreamInfo() will not work.
* The following classes are no longer publicly available.
 * MediaSource
 * MediaSourceConfiguration
 * MediaSourceSink
 * AbstractKinesisVideoClient
 * NativeKinesisVideoClient
 * BytesGenerator
 * BytesMediaSource
 * BytesMediaSourceConfiguration
 * ProducerStreamSink
 * KinesisVideoServiceClient
 * NativeKinesisVideoProducerJni
 * NativeKinesisVideoProducerStream
 * NativeLibraryLoader
 * KinesisVideoMetrics
 * KinesisVideoProducer
 * KinesisVideoProducerStream
 * KinesisVideoStreamMetrics
 * ReadResult
 * ServiceCallbacks
 * com.amazonaws.kinesisvideo.service.exception.AccessDeniedException
 * com.amazonaws.kinesisvideo.service.exception.AmazonServiceException
 * com.amazonaws.kinesisvideo.service.exception.ResourceInUseException
 * com.amazonaws.kinesisvideo.service.exception.ResourceNotFoundException
 * AckConsumer
 * BlockingAckConsumer
 * DefaultServiceCallbacksImpl

### Release 1.5.0 (24 August 2018)
* Windows native library available for Producer SDK
* Intermittent producer support
* Per-stream customized callback support

### Release 1.3.1 (23 July 2018)

* Add reset connection function.
* Fix key frame data-flag matching issue which could cause parsing issue in decoding process.

### Release 1.3.0 (15 March 2018)

* Provide pre-built KinesisVideoProducerJNI library for Mac (x64), Ubuntu (x64) and Raspian (x86).
* Remove Lombok dependency on Java Producer SDK.
* Update instruction in README about KinsisVideoProducerJNI build.
* Compatible changes in Java Adapter to work with latest changes in [Kinesis Video Streams Producer SDK CPP](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/README.md).

### Release 1.2.1 (February 2018)

* Remove some unit tests relying on native library to avoid mvn package build (without -skipTests=true) failure.

### Release 1.2.0 (February 2018)

* Bug fixes and performance enhancement.
* There are some interface changes to be compatible with native library changes.

### Release 1.1.0 (December 2017)

* Updated JNI code to expose ACKs as callbacks so developer can get more information about how the streaming is going.
* The version of JNI is bumped to 1.2, this will require corresponding ["KinesisVideoProducerJNI"](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp) with same version.

### Release 1.0.0 (November 2017)

* First release of the Amazon Kinesis Video Producer SDK Java.
