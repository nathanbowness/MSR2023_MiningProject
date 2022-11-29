# Main improvements

This github repository is fully insperd from [TFLite in raspberry](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md), I implememt the code to visualize the video and the image of the TOLOv4 TFLite, I convert the weight from the darknet framework to the TFLite with the usage of this [github repo](https://github.com/hunglc007/tensorflow-yolov4-tflite).

I put all the weights model tested in this [drive folder](https://drive.google.com/drive/folders/1R9FvOpKk_CNUzLZpqp06GN1OENbjEbPR?usp=sharing), so you can skip the conversion and research process of model in TFLite format .

| Model                 | FPS | mAP50-coco |
|-----------------------|-----|------------|
| SSD-MobilenetV3-small | **7.1** | 0.29       |
| SSD-MobilenetV3-large | 5.2 | **0.43**       |
| SSD-MobilenetV1       | 3.2 | 0.27       |
| YOLOv4-tiny-256       | 3.2 | 0.25       |
| YOLOv4-tiny-320       | 2.3 | 0.28       |
| YOLOv4-tiny-416       | 1.5 | 0.29       |
| YOLOv4-tiny-512       | 1.1 | 0.28       |

This is a resume of the results, seems YOLO lost a lot causeof the conversione to the TFLite framework. The frame per second are calcualted on a raspeberry pi4.

I also add in the normal detection of the video for SSD video a calculation of the FPS.

## Section 1 - How to run the detector on your Linux system

Before of all check your linux system is update.

##### 1 - Clone and install requirements
Clone the repository
```
git clone https://github.com/GiorgioSgl/TFLite_Yolov4_and_SSD
```

Second create a python virtual environment to avoid confilict between the packages of your system
Install it
```
sudo pip3 install virtualenv
```

Create the virtual environment
```
cd TFLite_Yolov4_and_SSD
python3 -m venv my_environment
```

Activate the environment
```
source tflite1-env/bin/activate
```

Install all the requirements
```
bash get_pi_requirements.sh
```

##### 2 - Test it 

SSD model
```
python3 TFLite_detection_image.py --modeldir=<model directory>/ --image test1.jpg
```


YOLO model
```
python3 TFLite_detection_image_YOLO.py --modeldir=<model directory>/ --image test1.jpg
```

## Section 2 - Run Edge TPU Object Detection Models on the Raspberry Pi Using the Coral USB Accelerator

[![Link to Section 2 YouTube video!](https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/master/doc/YouTube_video2.png)](https://www.youtube.com/watch?v=qJMwNHQNOVU)

The [Coral USB Accelerator](https://coral.withgoogle.com/products/accelerator/) is a USB hardware accessory for speeding up TensorFlow models. You can buy one [here (Amazon Associate link)](https://amzn.to/2BuG1Tv). 

The USB Accelerator uses the Edge TPU (tensor processing unit), which is an ASIC (application-specific integrated circuit) chip specially designed with highly parallelized ALUs (arithmetic logic units). While GPUs (graphics processing units) also have many parallelized ALUs, the TPU has one key difference: the ALUs are directly connected to eachother. The output of one ALU can be directly passed to the input of the next ALU without having to be stored and retrieved from a memory buffer. The extreme paralellization and removal of the memory bottleneck means the TPU can perform up to 4 trillion arithmetic operations per second! This is perfect for running deep neural networks, which require millions of multiply-accumulate operations to generate outputs from a single batch of input data. 

<p align="center">
  <img src="https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/master/doc/Coral_and_EdgeTPU2.png">
</p>

My Master's degree was in ASIC design, so the Edge TPU is very interesting to me! If you're a computer architecture nerd like me and want to learn more about the Edge TPU, [here is a great article that explains how it works](https://cloud.google.com/blog/products/ai-machine-learning/what-makes-tpus-fine-tuned-for-deep-learning).

It makes object detection models run WAY faster, and it's easy to set up. These are the steps we'll go through to set up the Coral USB Accelerator:

- 2a. Install libedgetpu library
- 2b. Set up Edge TPU detection model
- 2c. Run super-speed detection!

This section of the guide assumes you have already completed [Section 1](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md#section-1---how-to-set-up-and-run-tensorflow-lite-object-detection-models-on-the-raspberry-pi) for setting up TFLite object detection on the Pi. If you haven't done that portion, scroll back up and work through it first.

### Step 2a. Install libedgetpu library
First, we'll download and install the Edge TPU runtime, which is the library needed to interface with the USB Acccelerator. These instructions follow the [USB Accelerator setup guide](https://coral.withgoogle.com/docs/accelerator/get-started/) from official Coral website.

Open a command terminal and move into the /home/pi/tflite1 directory and activate the tflite1-env virtual environment by issuing:

```
cd /home/pi/tflite1
source tflite1-env/bin/activate
```

Add the Coral package repository to your apt-get distribution list by issuing the following commands:

```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
```

Install the libedgetpu library by issuing:

```
sudo apt-get install libedgetpu1-std
```

You can also install the libedgetpu1-max library, which runs the USB Accelerator at an overclocked frequency, allowing it to achieve even faster framerates. However, it also causes the USB Accelerator to get hotter. Here are the framerates I get when running TFLite_detection_webcam.py with 1280x720 resolution for each option with a Raspberry Pi 4 4GB model:

* libedgetpu1-std: 22.6 FPS
* libedgetpu1-max: 26.1 FPS

I didn't measure the temperature of the USB Accelerator, but it does get a little hotter to the touch with the libedgetpu1-max version. However, it didn't seem hot enough to be unsafe or harmful to the electronics.

If you want to use the libedgetpu-max library, install it by using `sudo apt-get install libedgetpu1-max`. (You can't have both the -std and the -max libraries installed. If you install the -max library, the -std library will automatically be uninstalled.)

Alright! Now that the libedgetpu runtime is installed, it's time to set up an Edge TPU detection model to use it with.

### Step 2b. Set up Edge TPU detection model
Edge TPU models are TensorFlow Lite models that have been compiled specifically to run on Edge TPU devices like the Coral USB Accelerator. They reside in a .tflite file and are used the same way as a regular TF Lite model. My preferred method is to keep the Edge TPU file in the same model folder as the TFLite model it was compiled from, and name it as "edgetpu.tflite".

I'll show two options for setting up an Edge TPU model: using the sample model from Google, or using a custom model you compiled yourself.

#### Option 1. Using Google's sample EdgeTPU model
Google provides a sample Edge TPU model that is compiled from the quantized SSDLite-MobileNet-v2 we used in [Step 1e](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md#step-1e-set-up-tensorflow-lite-detection-model). Download it and move it into the Sample_TFLite_model folder (while simultaneously renaming it to "edgetpu.tflite") by issuing these commands:

```
wget https://dl.google.com/coral/canned_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite

mv mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite Sample_TFLite_model/edgetpu.tflite
```

Now the sample Edge TPU model is all ready to go. It will use the same labelmap.txt file as the TFLite model, which should already be located in the Sample_TFLite_model folder.

#### Option 2. Using your own custom EdgeTPU model
If you trained a custom TFLite detection model, you can compile it for use with the Edge TPU. Unfortunately, the edgetpu-compiler package doesn't work on the Raspberry Pi: you need a Linux PC to use it on. Section 3 of this guide will give a couple options for compiling your own model if you don't have a Linux box. While I'm working on writing it, [here are the official instructions that show how to compile an Edge TPU model from a TFLite model](https://coral.withgoogle.com/docs/edgetpu/compiler/).

Assuming you've been able to compile your TFLite model into an EdgeTPU model, you can simply copy the .tflite file onto a USB and transfer it to the model folder on your Raspberry Pi. For my "BirdSquirrelRaccoon_TFLite_model" example from [Step 1e](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md#step-1e-set-up-tensorflow-lite-detection-model), I can compile my "BirdSquirrelRaccoon_TFLite_model" on a Linux PC, put the resulting edgetpu.tflite file on a USB, transfer the USB to my Pi, and move the edgetpu.tflite file into the /home/pi/tflite1/BirdSquirrelRaccoon_TFLite_model folder. It will use the same labelmap.txt file that already exists in the folder to get its labels.

Once the edgetpu.tflite file has been moved into the model folder, it's ready to go!

### Step 2c. Run detection with Edge TPU!

Now that everything is set up, it's time to test out the Coral's ultra-fast detection speed! Make sure to free up memory and processing power by closing any programs you aren't using. Make sure you have a webcam plugged in.

Plug in your Coral USB Accelerator into one of the USB ports on the Raspberry Pi. If you're using a Pi 4, make sure to plug it in to one of the blue USB 3.0 ports.

*Insert picture of Coral USB Accelerator plugged into Raspberry Pi here!*

Make sure the tflite1-env environment is activate by checking that (tflite1-env) appears in front of the command prompt in your terminal. Then, run the real-time webcam detection script with the --edgetpu argument:

```
python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model --edgetpu
```

The `--edgetpu` argument tells the script to use the Coral USB Accelerator and the EdgeTPU-compiled .tflite file. If your model folder has a different name than "Sample_TFLite_model", use that name instead.

After a brief initialization period, a window will appear showing the webcam feed with detections drawn on each from. The detection will run SIGNIFICANTLY faster with the Coral USB Accelerator.

If you'd like to run the video or image detection scripts with the Accelerator, use these commands:

```
python3 TFLite_detection_video.py --modeldir=Sample_TFLite_model --edgetpu
python3 TFLite_detection_image.py --modeldir=Sample_TFLite_model --edgetpu
```

Have fun with the blazing detection speeds of the Coral USB Accelerator!

## Section 3 - Compile Custom Edge TPU Object Detection Models

To use a custom model on the Coral USB Accelerator, you have to run it through Coral's [Edge TPU Compiler](https://coral.ai/docs/edgetpu/compiler/) tool. Unfortunately, the compiler only works on Linux operating systems, and only on certain CPU architectures. 

The easiest way to compile the Edge TPU model is to use a Google Colab session. I created a Colab page specifically for compiling Edge TPU models. Please click the link below and follow the instructions in the Colab notebook.

https://colab.research.google.com/drive/1o6cNNNgGhoT7_DR4jhpMKpq3mZZ6Of4N?usp=sharing

## Appendix: Common Errors
This appendix lists common errors that have been encountered by users following this guide, and solutions showing how to resolve them.

**Feel free to create Pull Requests to add your own errors and resolutions! I'd appreciate any help.**

### 1. TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
The 'NoneType' error means that the program received an empty array from the webcam, which typically means something is wrong with the webcam or the interface to the webcam. Try plugging and re-plugging the webcam in a few times, and/or power cycling the Raspberry Pi, and see if that works. If not, you may need to try using a new webcam.

### 2. ImportError: No module named 'cv2'
This error occurs when you try to run any of the TFLite_detection scripts without activating the 'tflite1-env' first. It happens because Python cannot find the path to the OpenCV library (cv2) to import it. 

Resolve the issue by closing your terminal window, re-opening it, and issuing:

```
cd tflite1
source tflite1-env/bin/activate
```

Then, try re-running the script as described in [Step 1e](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md#step-1e-run-the-tensorflow-lite-model).

### 3. THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE
This error can occur when you run the `bash get_pi_requirements.sh` command in Step 1c. It occurs because the package data got corrupted while downloading. You can resolve the error by re-running the `bash get_pi_requirements.sh` command a few more times until it successfully completes without reporting that error.

### 4. Unsupported data type in custom op handler: 6488064Node number 2 (EdgeTpuDelegateForCustomOp) failed to prepare.
This error occurs when trying to use a newer version of the libedgetpu library (v13.0 or greater) with an older version of TensorFlow (v2.0 or older). It can be resolved by uninstalling your current version of TensorFlow and installing the latest version of the tflite_runtime package. Issue these commands (make sure you are inside the tflite1-env virtual environment):

```
pip3 uninstall tensorflow
pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
```

(Or, if you're using Python 3.5, use `pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp35-cp35m-linux_armv7l.whl` instead.)

Then, re-run the TFLite detection script. It should work now!

*Note: the URLs provided in these commands may change as newer versions of tflite_runtime are released. Check the [TFLite Python Quickstart page](https://www.tensorflow.org/lite/guide/python) for download URLs to the latest version of tflite_runtime.*

### 5. IndexError: list index out of range
This error usually occurs when you try using an "image classification" model rather than an "object detection" model. Image classification models apply a single label to an image, while object detection models locate and label multiple objects in an image. The code in this repository is written for object detection models.

Many people run in to this error when using models from Teachable Machine. This is because Teachable Machine creates image classification models rather than object detection models. To create an object detection model for TensorFow Lite, you'll have to follow the guide in this repository.

If you'd like to see how to use an image classification model on the Raspberry Pi, please see this example:
https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi
## Reference

My job is inspiered mainly by this two github repository:
- [TFLite in raspberry](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md)
- [Yolov4 weight to tensorflow](https://github.com/hunglc007/tensorflow-yolov4-tflite)


## License

MIT

**Free Software, Hell Yeah!**
