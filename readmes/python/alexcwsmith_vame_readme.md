![VAME](https://github.com/LINCellularNeuroscience/VAME/blob/master/Images/VAME_Logo-1.png)
![workflow](https://github.com/LINCellularNeuroscience/VAME/blob/master/Images/workflow.png)

# Release notes for this fork of VAME:
* 09-10-21 - Merged in VAME 1.0 release. Main updates from the parent repository are a video writer at vame/custom/ACWS_videowriter.py that creates motif videos from the longest sequences for each motif, rather than the first frames of the motif. Also adds scheduler_stepsize, scheduler_gamma, and scheduler_threshold for torch ReduceLROnPlateau function.
* 02-05-21 - Fixed the manual learning rate descent (see 12-8-20 update). To turn this feature on, set 'scheduler' in config.yaml to 0. Also added 'suffix' optional parameter to evaluate_model, allowing you to add a suffix to the future_reconstruction plots so as not to overwrite previously created plots, if they exist.
* 12-10-20 - Added TimeSeriesKMeans cluster method. Also added a plot_transitions function to segment_behavior.py, to create .svg file with transition matrix plot. This adds the dependencies 'tslearn' and 'seaborn', both of which can be installed from conda-forge.
* 02-05-21 - Fixed the manual learning rate descent (see 12-8-20 update). To turn this feature on, set 'scheduler' in config.yaml to 0. Also added 'suffix' optional parameter to evaluate_model, allowing you to add a suffix to the future_reconstruction plots so as not to overwrite previously created plots, if they exist.
* 12-10-20 - Added TimeSeriesKMeans cluster method. Also added a plot_transitions function to segment_behavior.py, to create .svg file with transition matrix plot. This adds the dependencies 'tslearn' and 'seaborn', both of which can be installed from conda-forge.
* 12-8-20 - Added 'step_size' and 'gamma' parameters to config file. The 'step_size' parameter determines how many training epochs occur between each decrease in learning rate. The gamma parameter is the multiplicative reduction in learning rate after every step_size iterations. Step_size defaults to 100, and gamma defaults to 0.2. In the main VAME repository these are the values used in the model.
* 11-30-20 - Minor updates include changing legend location in evaluation result figures. Also sets the nan_policy for t-test in extractResults function to 'omit', so nan clusters will be ignored rather than the t-test result being nan. In a future update empty clusters will likely be set to 0.
* 11-24-20 - Added vame/custom/alignVideos.py to produce egocentric alignment CSV files in accordance with update to main VAME repository.
* 11-2-20 - Added vame/custom/helperFunctions.py - These functions help with pre-processing of DLC data, e.g. dropping bodyparts if you don't want to include all in model. Also includes functions for extracting and concatenating results, performing statistics on motif usage between groups, and writing human-readable result CSV files.

# VAME in a Nutshell
VAME is a framework to cluster behavioral signals obtained from pose-estimation tools. It is a [PyTorch](https://pytorch.org/) based deep learning framework which leverages the power of recurrent neural networks (RNN) to model sequential data. In order to learn the underlying complex data distribution we use the RNN in a variational autoencoder setting to extract the latent state of the animal in every step of the input time series.

![behavior](https://github.com/LINCellularNeuroscience/VAME/blob/master/Images/behavior_structure_crop.gif)

The workflow of VAME consists of 5 steps and we explain them in detail [here](https://github.com/LINCellularNeuroscience/VAME/wiki/1.-VAME-Workflow).

## Installation
To get started we recommend using [Anaconda](https://www.anaconda.com/distribution/) with Python 3.6 or higher. 
Here, you can create a [virtual enviroment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to store all the dependencies necessary for VAME. (you can also use the VAME.yaml file supplied here, byt simply openning the terminal, running `git clone https://github.com/LINCellularNeuroscience/VAME.git`, then type `cd VAME` then run: `conda env create -f VAME.yaml`).

* Go to the locally cloned VAME directory and run `python setup.py install` in order to install VAME in your active conda environment.
* Install the current stable Pytorch release using the OS-dependent instructions from the [Pytorch website](https://pytorch.org/get-started/locally/). Currently, VAME is tested on PyTorch 1.5. (Note, if you use the conda file we supply, PyTorch is already installed and you don't need to do this step.)

## Getting Started
First, you should make sure that you have a GPU powerful enough to train deep learning networks. In our paper, we were using a single Nvidia GTX 1080 Ti to train our network. A hardware guide can be found [here](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/). Once you have your hardware ready, try VAME following the [workflow guide](https://github.com/LINCellularNeuroscience/VAME/wiki/1.-VAME-Workflow).

If you want to follow an example first you can download [video-1](https://drive.google.com/file/d/1w6OW9cN_-S30B7rOANvSaR9c3O5KeF0c/view?usp=sharing) here and find the .csv file in our [example](https://github.com/LINCellularNeuroscience/VAME/tree/master/examples) folder. 

## News
* March 2021: We are happy to release VAME 1.0 with a bunch of improvements and new features! These include the community analysis script, a model allowing generation of unseen datapoints, new visualization functions, as well as the much requested function to generate GIF sequences containing UMAP embeddings and trajectories together with the video of the behaving animal. Big thanks also to [@MMathisLab](https://github.com/MMathisLab) for contributing to the OS compatibility and usability of our code.
* November 2020: We uploaded an egocentric alignment [script](https://github.com/LINCellularNeuroscience/VAME/blob/master/examples/align_demo.py) to allow more researcher to use VAME
* October 2020: We updated our manuscript on [Biorxiv](https://www.biorxiv.org/content/10.1101/2020.05.14.095430v2)
* May 2020: Our preprint "Identifying Behavioral Structure from Deep Variational Embeddings of Animal Motion" is out! [Read it on Biorxiv!](https://www.biorxiv.org/content/10.1101/2020.05.14.095430v1)

### Authors and Code Contributors
VAME was developed by Kevin Luxem and Pavol Bauer.

The development of VAME is heavily inspired by [DeepLabCut](https://github.com/DeepLabCut/DeepLabCut/).
As such, the VAME project management codebase has been adapted from the DeepLabCut codebase.
The DeepLabCut 2.0 toolbox is © A. & M.W. Mathis Labs [deeplabcut.org](http:\\deeplabcut.org), released under LGPL v3.0.
The implementation of the VRAE model is partially adapted from the [Timeseries clustering](https://github.com/tejaslodaya/timeseries-clustering-vae) repository developed by [Tejas Lodaya](https://tejaslodaya.com).

### References
VAME preprint: [Identifying Behavioral Structure from Deep Variational Embeddings of Animal Motion](https://www.biorxiv.org/content/10.1101/2020.05.14.095430v2) <br/>
Kingma & Welling: [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) <br/>
Pereira & Silveira: [Learning Representations from Healthcare Time Series Data for Unsupervised Anomaly Detection](https://www.joao-pereira.pt/publications/accepted_version_BigComp19.pdf)

### License: GPLv3
See the [LICENSE file](../master/LICENSE) for the full statement.
