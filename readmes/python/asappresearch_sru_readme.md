
## News
SRU++, a new SRU variant, is released. [[tech report](https://arxiv.org/pdf/2102.12459.pdf)] [[blog](https://www.asapp.com/blog/reducing-the-high-cost-of-training-nlp-models-with-sru/)]

The experimental code and SRU++ implementation are available on [the dev branch](https://github.com/asappresearch/sru/tree/3.0.0-dev/experiments/srupp_experiments) which will be merged into master later.

## About

**SRU** is a recurrent unit that can run over 10 times faster than cuDNN LSTM, without loss of accuracy tested on many tasks. 
<p align="center">
<img width=620 src="https://raw.githubusercontent.com/taolei87/sru/master/imgs/speed.png"><br>
<i>Average processing time of LSTM, conv2d and SRU, tested on GTX 1070</i><br>
</p>
For example, the figure above presents the processing time of a single mini-batch of 32 samples. SRU achieves 10 to 16 times speed-up compared to LSTM, and operates as fast as (or faster than) word-level convolution using conv2d.

#### Reference:
Simple Recurrent Units for Highly Parallelizable Recurrence [[paper](https://arxiv.org/abs/1709.02755)]
```
@inproceedings{lei2018sru,
  title={Simple Recurrent Units for Highly Parallelizable Recurrence},
  author={Tao Lei and Yu Zhang and Sida I. Wang and Hui Dai and Yoav Artzi},
  booktitle={Empirical Methods in Natural Language Processing (EMNLP)},
  year={2018}
}
```

When Attention Meets Fast Recurrence: Training Language Models with Reduced Compute [[paper](https://arxiv.org/pdf/2102.12459)]
```
@article{lei2021srupp,
  title={When Attention Meets Fast Recurrence: Training Language Models with Reduced Compute},
  author={Tao Lei},
  journal={arXiv preprint arXiv:2102.12459},
  year={2021}
}
```
<br>

## Requirements
 - [PyTorch](http://pytorch.org/) >=1.6 recommended
 - [ninja](https://ninja-build.org/)

Install requirements via `pip install -r requirements.txt`.

<br>

## Installation

#### From source:
SRU can be installed as a regular package via `python setup.py install` or `pip install .`.

#### From PyPi:
`pip install sru`


#### Directly use the source without installation:
Make sure this repo and CUDA library can be found by the system, e.g. 
```
export PYTHONPATH=path_to_repo/sru
export LD_LIBRARY_PATH=/usr/local/cuda/lib64
```

<br>

## Examples
The usage of SRU is similar to `nn.LSTM`. SRU likely requires more stacking layers than LSTM. We recommend starting by 2 layers and use more if necessary (see our report for more experimental details).
```python
import torch
from sru import SRU, SRUCell

# input has length 20, batch size 32 and dimension 128
x = torch.FloatTensor(20, 32, 128).cuda()

input_size, hidden_size = 128, 128

rnn = SRU(input_size, hidden_size,
    num_layers = 2,          # number of stacking RNN layers
    dropout = 0.0,           # dropout applied between RNN layers
    bidirectional = False,   # bidirectional RNN
    layer_norm = False,      # apply layer normalization on the output of each layer
    highway_bias = -2,        # initial bias of highway gate (<= 0)
)
rnn.cuda()

output_states, c_states = rnn(x)      # forward pass

# output_states is (length, batch size, number of directions * hidden size)
# c_states is (layers, batch size, number of directions * hidden size)

```
  
<br>

## Contributing
Please read and follow the [guidelines](CONTRIBUTING.md).


### Other Implementations

[@musyoku](https://github.com/musyoku) had a very nice [SRU implementaion](https://github.com/musyoku/chainer-sru) in chainer.

[@adrianbg](https://github.com/adrianbg) implemented the first [CPU version](https://github.com/taolei87/sru/pull/42).

<br>

  
