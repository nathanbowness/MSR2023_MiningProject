# DeepXplore++, An extension of DeepXplore
See the SOSP'17 paper [DeepXplore: Automated Whitebox Testing of Deep Learning Systems](http://www.cs.columbia.edu/~suman/docs/deepxplore.pdf) for more details.

DeepXplore++ fixes discrepancies in the implementation of Neuron Coverage between the description in the paper and in the implementation found on github. In addition, DeepXplore is extended to include SNAC (Strong Neuron Activation Coverage) as a coverage criteria to be tracked as well as targetted.

# Building DeepXplore++
We've provided a Dockerfile which you can use to build and run DeepXplore++. The steps for running are the following:

1. Install [Docker](https://www.docker.com/)
2. Clone this repository to your machine
3. cd to the repository main directory
4. Run `docker build .` which will start building the image
5. Run `docker run -it [IMAGE ID]` where image ID is the hash of the image

For instructions on setting up the project locally, please see the original implementation. 

# Running DeepXplore++

At this point, you can enter any of the model directories which DeepXplore++ supports, (PDF, MNIST, Driving) and you can run the `gen_diff.py` file to generate adversarial examples and track coverage. 

`gen_diff.py` takes as input model specific arguments such as the type of input modification, lambda parameters, the number of gradient ascent iterations, and a coverage criteria that is being targetted. Examples for the supported models are shown below. See the `gen_diff.py` file for the specific model if you have any more questions.

The coverage metrics which are currently supported are Neuron Coverage (from DeepXplore) and Strong Neuron Activation Coverage (from DeepGauge). The parameter `nc` specifies the coverage target as Neuron Coverage, and `snac` specifies the coverage target as Strong Neuron Activation Coverage.

PDF - `python gen_diff.py 2 0.1 0.1 2000 20 0 nc`

MNIST - `python gen_diff.py light 1 0.1 10 20 20 0 snac`

Driving - `python gen_diff.py light 1 0.1 10 20 20 0 nc`

# Experimental Data

Experimental data for our project can be found in the `official_report_results` directory. Files are named according to the model, the number of seed inputs, the target coverage criteria, and any input modification that is specified.  

Results for the comparison of DeepXplore's neuron coverage vs. corrected neuron coverage can be found in the `original` branch under the same directory.

