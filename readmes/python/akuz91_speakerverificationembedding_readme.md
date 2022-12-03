# SpeakerVerificationEmbedding


Implementation of speech embedding net and loss (described [here](https://arxiv.org/pdf/1710.10467.pdf)). Original implementation by HarryVolek utilizes the [TIMIT dataset](https://github.com/philipperemy/timit) for training the speech embedder and an outline to build dvector-embeddings around. We add the [ICSI database](http://groups.inf.ed.ac.uk/ami/icsi/license.shtml) to the speech embedding net training and convert the Supreme Court of the United States (SCOTUS) oral arguments and [LibriSpeech](http://www.openslr.org/12/) readings into d-vector embeddings for the [UIS-RNN](https://github.com/google/uis-rnn) speaker diarization model. 

Adapted by Jeffrey Tumminia, Sophia Tsilerides, Amanda Kuznecov, Ilana Weinstein as part of NYU Center for Data Science Capstone Project. Research mentored by Prof. Aaron Kaufman. Computational resources provided by NYU Prince HPC.  


# Dependencies

* PyTorch 0.4.1
* python 3.5+
* numpy 1.15.4
* librosa 0.6.1
* webrtcvad 2.0.10


# Outline

## Datasets

We utilize the following datasets

    - [TIMIT](https://github.com/philipperemy/timit)
    - [ICSI](http://groups.inf.ed.ac.uk/ami/icsi/license.shtml)
    - [SCOTUS Oyez](https://www.oyez.org/)
    - [LibriSpeech](http://www.openslr.org/12/)
    
TIMIT and ISCI are used to train `SpeechEmbedder` model. SCOTUS and Libre are datasets represented as dvectors and aligned with their diarization times to make labelled datasets for the UISRNN. Details for data preprocessing & handling are in dataset level readmes found in the folders.
    
## Performance 

Model trained on TIMIT and fine-tuned on ICSI. Test set is held-out TIMIT data with unknown speakers.

```
EER across # epochs: .0578
```

## D-vector Embedding

Inference scripts are present for the SCOTUS and Libre dataset. The preprocessing for these datasets is outlined ...


Calling `dvector_SCOTUS` outputs a folder for each case processed, each containing a numpy array of dvector embeddings which are unaligned with the sequence of the case audio. Calling `align_SCOTUS.py` will process these unaligned cases into a numpy array of dvectors (`case_sequence.npy`) and a numpy array of labels (`case_cluster_id.npy`) which are both the same length, as well as a csv of a list of files which were not embedded (usually do to being too short). These are formatted for [our fork of the uisrnn](https://github.com/JeffT13/LegalUISRNN)