# DeepVAC
DeepVAC提供了基于PyTorch的AI项目的工程化规范。为了达到这一目标，DeepVAC包含了：
- 软件工程规范：[软件工程规范](./docs/arch.md)；
- 代码规范：[代码规范](./docs/code_standard.md)；
- deepvac库：[deepvac库](./docs/lib.md)。

诸多PyTorch AI项目的内在逻辑都大同小异，因此DeepVAC致力于把更通用的逻辑剥离出来，从而使得工程代码的准确性、易读性、可维护性上更具优势。

如果想使得AI项目符合DeepVAC规范，需要仔细阅读[DeepVAC标准](./docs/deepvac_standard.md)。
如果想了解deepvac库的设计，请阅读[deepvac库的设计](./docs/design.md)。


# 如何基于DeepVAC构建自己的PyTorch AI项目

## 1. 阅读[DeepVAC标准](./docs/deepvac_standard.md)
可以粗略阅读，建立起第一印象。

## 2. 环境准备
DeepVAC的依赖有：
- Python3。不支持Python2，其已被废弃；
- 依赖包：torch, torchvision, tensorboard, scipy, numpy, cv2, Pillow；

这些依赖使用pip命令（或者git clone）自行安装，不再赘述。

对于普通用户来说，最方便高效的方式还是使用[MLab HomePod](https://github.com/DeepVAC/MLab#mlab-homepod)作为DeepVAC的使用环境，这是一个预构建的Docker image，可以帮助用户省掉不必要的环境配置时间。
同时在MLab组织内部，我们也使用[MLab HomePod](https://github.com/DeepVAC/MLab#mlab-homepod)进行日常的模型的训练任务。
  

## 3. 安装deepvac库
可以使用pip来进行安装：  
```pip3 install deepvac```   
或者  
```python3 -m pip install deepvac```   


如果你需要使用deepvac在github上的最新代码，就需要使用如下的开发者模式：
#### 开发者模式
- 克隆该项目到本地：```git clone https://github.com/DeepVAC/deepvac ``` 
- 在你的入口文件中添加：
```python
import sys
#replace with your local deepvac directory
sys.path.insert(0,'/home/gemfield/github/deepvac')
```
或者设置PYTHONPATH环境变量：
```bash
export PYTHONPATH=/home/gemfield/github/deepvac
```

## 4. 创建自己的PyTorch项目
- 初始化自己项目的git仓库；
- 在仓库中创建第一个研究分支，比如分支名为 LTS_b1_aug9_movie_video_plate_130w；
- 切换到上述的LTS_b1分支中，开始工作；

## 5. 编写配置文件
配置文件的文件名均为 config.py，位于你项目的根目录。在代码开始处添加```from deepvac import new, AttrDict```；
所有用户的配置都存放在这个文件里。config模块提供了6个预定义的作用域：config.core,config.aug,config.cast,config.datasets,config.backbones,config.loss。使用方法如下：
- 所有和trainer相关（包括train、val、test）的配置都定义在config.core.<my_train_class>中；
- 所有和deepvac.aug中增强模块相关的配置都定义在config.aug.<my_aug_class>中；
- 所有和模型转换相关的配置都定义在config.cast.<the_caster_class>中；
- 所有和Datasets相关的配置都定义在config.datasets.<my_dataset_class>中；
- 所有和loss相关的配置都定义在config.loss.<my_loss_class>中；
- 用户可以开辟自己的作用域，比如config.my_stuff = AttrDict()，然后config.my_stuff.name = 'gemfield'；
- 用户可以使用new()来初始化config实例，使用clone()来深拷贝config配置项。

更多配置：
- 预训练模型加载；
- checkpoint加载；
- tensorboard使用；
- TorchScript使用；
- 转换ONNX；
- 转换NCNN；
- 转换CoreML；
- 转换TensorRT；
- 转换TNN；
- 转换MNN；
- 开启量化；
- 开启EMA；
- 开启自动混合精度训练(AMP)；

以及关于配置文件的更详细解释，请阅读[config说明](./docs/config.md).

项目根目录下的train.py中用如下方式引用config.py文件:

```python
from config import config as deepvac_config
from deepvac import DeepvacTrain

class MyTrain(DeepvacTrain):
    ......

my_train = MyTrain(deepvac_config)
my_train()
```

项目根目录下的test.py中用如下方式引用config.py文件:
```python
from config import config as deepvac_config
from deepvac import Deepvac

class MyTest(Deepvac)
    ......

my_test = MyTest(deepvac_config)
my_test()
```

之后，train.py/test.py代码中通过如下方式来读写config.core中的配置项
```python
print(self.config.log_dir)
print(self.config.batch_size)
......
```
此外，鉴于config的核心作用，deepvac还设计了如下的API来方便对config模块的使用：
- AttrDict
- new
- interpret
- fork
- clone
```python
from deepvac import AttrDict, new, interpret, fork
```
关于这些API的使用方法，请访问[config API 说明](./docs/design.md#config-module).
## 6. 编写synthesis/synthesis.py（可选）
编写该文件，用于产生本项目的数据集，用于对本项目的数据集进行自动化检查和清洗。
这一步为可选，如果有需要的话，可以参考Deepvac组织下Synthesis2D项目的实现。

## 7. 编写aug/aug.py（可选）
编写该文件，用于实现数据增强策略。
deepvac.aug模块为数据增强设计了特有的语法，在两个层面实现了复用：aug 和 composer。比如说，我想复用添加随机斑点的SpeckleAug：
```python
from deepvac.aug.base_aug import SpeckleAug
```

这是对底层aug算子的复用。我们还可以直接复用别人写好的composer，并且是以直截了当的方式。比如deepvac.aug提供了一个用于人脸检测数据增强的RetinaAugComposer：

```python
from deepvac.aug import RetinaAugComposer
```

以上说的是直接复用，但项目中更多的是自定义扩展，而且大部分情况下也需要复用torchvision的transform的compose，又该怎么办呢？这里解释下，composer是deepvac.aug模块的概念，compose是torchvision transform模块的概念，之所以这么相似纯粹是因为巧合。

要扩展自己的composer也是很简单的，比如我可以自定义一个composer（我把它命名为GemfieldComposer），这个composer可以使用/复用以下增强逻辑：
- torchvision transform定义的compose；
- deepvac内置的aug算子；
- 我自己写的aug算子。

更详细的步骤请访问：[deepvac.aug模块使用](./docs/design.md#aug)

## 8. 编写Dataset类
代码编写在data/dataloader.py文件中。继承deepvac.datasets类体系，比如FileLineDataset类提供了对如下train.txt这种格式的封装：
```bash
#train.txt，第一列为图片路径，第二列为label
img0/1.jpg 0
img0/2.jpg 0
...
img1/0.jpg 1
...
img2/0.jpg 2
...
```
有时第二列是字符串，并且想把FileLineDataset中使用Image读取图片对方式替换为cv2，那么可以通过如下的继承方式来重新实现：
```python
from deepvac.datasets import FileLineDataset

class FileLineCvStrDataset(FileLineDataset):
    def _buildLabelFromLine(self, line):
        line = line.strip().split(" ")
        return [line[0], line[1]]

    def _buildSampleFromPath(self, abs_path):
        #we just set default loader with Pillow Image
        sample = cv2.imread(abs_path)
        sample = self.compose(sample)
        return sample
```
哦，FileLineCvStrDataset也已经是deepvac.datasets中提供的类了。


## 9. 编写训练和验证脚本
在Deepvac规范中，train.py就代表了训练范式。模型训练的代码写在train.py文件中，继承DeepvacTrain类：
```python
from deepvac import DeepvacTrain

class MyTrain(DeepvacTrain):
    pass
```

继承DeepvacTrain的子类可能需要重新实现以下方法才能够开始训练：
| 类的方法（*号表示用户一般要重新实现） | 功能 | 备注 |
| ---- | ---- | ---- |
| preEpoch | 每轮Epoch之前的用户操作，DeepvacTrain啥也不做 | 用户可以重新定义（如果需要的话） |
| preIter | 每个batch迭代之前的用户操作，DeepvacTrain啥也不做 | 用户可以重新定义（如果需要的话） |
| postIter | 每个batch迭代之后的用户操作，DeepvacTrain啥也不做 | 用户可以重新定义（如果需要的话） |
| postEpoch | 每轮Epoch之后的用户操作，DeepvacTrain啥也不做 | 用户可以重新定义（如果需要的话） |
| doFeedData2Device | DeepvacTrain把来自dataloader的sample和target(标签)移动到device设备上  | 用户可以重新定义（如果需要的话） |
| doForward | DeepvacTrain会进行网络推理，推理结果赋值给self.config.output成员 |用户可以重新定义（如果需要的话）  |
| doLoss | DeepvacTrain会使用self.config.output和self.config.target进行计算得到此次迭代的loss| 用户可以重新定义（如果需要的话）|
| doBackward | 网络反向传播过程，DeepvacTrain会调用self.config.loss.backward()进行BP| 用户可以重新定义（如果需要的话）|
| doOptimize | 网络权重更新的过程，DeepvacTrain会调用self.config.optimizer.step() | 用户可以重新定义（如果需要的话） |
| doSchedule | 更新学习率的过程，DeepvacTrain会调用self.config.scheduler.step() | 用户可以重新定义（如果需要的话） |
| * doValAcc | 在val模式下计算模型的acc，DeepvacTrain啥也不做 | 用户一般要重新定义，写tensorboard的时候依赖于此 |

典型的写法如下：
```python
class MyTrain(DeepvacTrain):
    ...
    #因为基类不能处理list类型的标签，重写该方法
    def doFeedData2Device(self):
        self.config.target = [anno.to(self.config.device) for anno in self.config.target]
        self.config.sample = self.config.sample.to(self.config.device)

    #初始化config.core.acc
    def doValAcc(self):
        self.config.acc = your_acc
        LOG.logI('Test accuray: {:.4f}'.format(self.config.acc))


train = MyTrain(deepvac_config)
train()
```
## 10. 编写测试脚本
在Deepvac规范中，test.py就代表测试范式。测试代码写在test.py文件中，继承Deepvac类。

和train.py中的train/val的本质不同在于：
- 舍弃train/val上下文；
- 网络不再使用autograd上下文；
- 不再进行loss、反向、优化等计算；
- 使用Deepvac的*Report模块来进行准确度、速度方面的衡量；

继承Deepvac类的子类必须（重新）实现以下方法才能够开始测试：

| 类的方法（*号表示必需重新实现） | 功能 | 备注 |
| ---- | ---- | ---- |
| preIter | 每个batch迭代之前的用户操作，Deepvac啥也不做 | 用户可以重新定义（如果需要的话） |
| postIter| 每个batch迭代之后的用户操作，Deepvac啥也不做 | 用户可以重新定义（如果需要的话） |
| doFeedData2Device | Deepvac把来自dataloader的sample和target(标签)移动到device设备上  | 用户可以重新定义（如果需要的话） |
| doForward | Deepvac会进行网络推理，推理结果赋值给self.config.output成员 |用户可以重新定义（如果需要的话）  |
| doTest | 用户完全自定义的test逻辑，可以通过report.add(gt, pred)添加测试结果，生成报告 | 看下面的测试逻辑 |

典型的写法如下：
```python
class MyTest(Deepvac):
    ...
    def doTest(self):
        ...

test = MyTest(deepvac_config)
test()
#test(input_tensor)
```

当执行test()的时候，DeepVAC框架会按照如下的优先级进行测试：
- 如果用户传递了参数，比如test(input_tensor)，则将针对该input_tensor进行doFeedData2Device + doForward，然后测试结束；
- 如果用户重写了doTest()函数，则将执行doTest()，然后测试结束；
- 如果用户配置了config.my_test.test_loader，则将迭代该loader，对每个sample进行doFeedData2Device + doForward，然后测试结束；
- 以上都不符合，报错退出。


# DeepVAC的社区产品
| 产品名称 | 简介  |当前版本 | 获取方式/部署形式 |
| ---- | ---- | ---- |---- |
|[DeepVAC](https://github.com/deepvac/deepvac)|独树一帜的PyTorch工程规范  | 0.6.0 | pip install deepvac |
|[libdeepvac](https://github.com/deepvac/libdeepvac) | 独树一帜的PyTorch模型部署框架 | 1.9.0 | SDK，下载 & 解压|
|[MLab HomePod](https://github.com/DeepVAC/MLab#mlab-homepod)| 迄今为止最先进的容器化PyTorch模型训练环境 | 2.0 | docker run / k8s|
|MLab RookPod| 迄今为止最先进的成本10万人民币以下的存储解决方案 | NA | 硬件规范 + k8s yaml|
|[pyRBAC](https://github.com/DeepVAC/pyRBAC) | 基于Keycloak的RBAC python实现 |  NA | pip install(敬请期待) |
|DeepVAC版PyTorch | 为MLab HomePod pro版本定制的PyTorch包 |1.9.0 | conda install -c gemfield pytorch |
|[DeepVAC版LibTorch](https://github.com/deepvac/libdeepvac)| 为libdeepvac定制的LibTorch库 | 1.9.0 | 压缩包，下载 & 解压|
