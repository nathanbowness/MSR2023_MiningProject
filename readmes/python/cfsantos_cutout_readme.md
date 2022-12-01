# MaxDropout

This repository contains the code for the paper [MaxDropout: Deep Neural Network RegularizationBased on Maximum Output Values](https://arxiv.org/abs/2007.13723).   

Code based on the [Cutout original repository](https://github.com/uoguelph-mlrg/Cutout)

## Introduction

MaxDropout is a regularization technique based on Dropout. While dropout removes random neurons from a given tensor, MaxDropout relies on the highest values of this tensor, changing the values according to this rule.  

| Original Image           |  Dropout(50%) |   MaxDropout(50%)   |
:-------------------------:|:-------------:|:-------------------:|
<img width="240" height="200" src="https://github.com/cfsantos/MaxDropout-torch/blob/master/images/original.png "> |  <img width="240" height="200" src="https://github.com/cfsantos/MaxDropout-torch/blob/master/images/droped.png"> |  <img width="240" height="200" src="https://github.com/cfsantos/MaxDropout-torch/blob/master/images/maxdroped.png"> |

 

Bibtex:  
```
@misc{santos2020maxdropout,
    title={MaxDropout: Deep Neural Network Regularization Based on Maximum Output Values},
    author={Claudio Filipi Goncalves do Santos and Danilo Colombo and Mateus Roder and João Paulo Papa},
    year={2020},
    eprint={2007.13723},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

## Results and Usage   
### Dependencies  
[PyTorch v0.4.0](http://pytorch.org/)  
[tqdm](https://pypi.python.org/pypi/tqdm)

### ResNet18  
Test error (%, flip/translation augmentation, mean/std normalization, mean of 5 runs) 

| **Network** | **CIFAR-10** | **CIFAR-100** |
| ----------- | ------------ | ------------- |
| ResNet18    | 4.72         | 22.46         |
| ResNet18 + cutout | 3.99   | 21.96         |
| ResNet18 + MaxDropout | 4.66   | 21.93         |
| ResNet18 + cutout + MaxDropout | **3.76**   | **21.82**         |  


To train ResNet18 on CIFAR10 with data augmentation and MaxDropout:    
`python train.py --dataset cifar10 --model resnet18 --data_augmentation `

To train ResNet18 on CIFAR100 with data augmentation and MaxDropout:    
`python train.py --dataset cifar100 --model resnet18 --data_augmentation `

To train ResNet18 on CIFAR10 with data augmentation, cutout and MaxDropout:    
`python train.py --dataset cifar10 --model resnet18 --data_augmentation --cutout --length 16`

To train ResNet18 on CIFAR100 with data augmentation, cutout and MaxDropout:    
`python train.py --dataset cifar100 --model resnet18 --data_augmentation --cutout --length 8`
### WideResNet
WideResNet model implementation from https://github.com/xternalz/WideResNet-pytorch  

Test error (%, flip/translation augmentation, mean/std normalization, mean of 5 runs)  

| **Network** | **CIFAR-10** | **CIFAR-100** | 
| ----------- | ------------ | ------------- | 
| WideResNet  | 4.00         | 19.25          | 
| WideResNet + Dropout | 3.89 | 18.89         | 
| WideResNet + MaxDropout | **3.84** | **18.81**         |

To train WideResNet 28-10 on CIFAR10 with data augmentation and MaxDropout:    
`python train.py --dataset cifar10 --model wideresnet --data_augmentation `

To train WideResNet 28-10 on CIFAR100 with data augmentation and MaxDropout:    
`python train.py --dataset cifar100 --model wideresnet --data_augmentation `



