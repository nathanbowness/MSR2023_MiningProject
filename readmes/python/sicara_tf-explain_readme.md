# tf-explain

[![Pypi Version](https://img.shields.io/pypi/v/tf-explain.svg)](https://pypi.org/project/tf-explain/)
[![DOI](https://zenodo.org/badge/196956879.svg)](https://zenodo.org/badge/latestdoi/196956879)
[![Build Status](https://github.com/sicara/tf-explain/actions/workflows/ci.yml/badge.svg)](https://github.com/sicara/tf-explain/actions)
[![Documentation Status](https://readthedocs.org/projects/tf-explain/badge/?version=latest)](https://tf-explain.readthedocs.io/en/latest/?badge=latest)
![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-%23EBBD68.svg)
![Tensorflow Versions](https://img.shields.io/badge/tensorflow-2.x-blue.svg)

__tf-explain__ implements interpretability methods as Tensorflow 2.x callbacks to __ease neural network's understanding__.
See [Introducing tf-explain, Interpretability for Tensorflow 2.0](https://blog.sicara.com/tf-explain-interpretability-tensorflow-2-9438b5846e35)

__Documentation__: https://tf-explain.readthedocs.io

## Installation

__tf-explain__ is available on PyPi. To install it:

```bash
virtualenv venv -p python3.8
pip install tf-explain
```

tf-explain is compatible with Tensorflow 2.x. It is not declared as a dependency
to let you choose between full and standalone-CPU versions. Additionally to the previous install, run:

```bash
# For CPU or GPU
pip install tensorflow==2.6.0
```
Opencv is also a dependency. To install it, run:
```bash
# For CPU or GPU
pip install opencv-python
```

## Quickstart

tf-explain offers 2 ways to apply interpretability methods. The full list of methods is the [Available Methods](#available-methods) section.

### On trained model

The best option is probably to load a trained model and apply the methods on it.

```python
# Load pretrained model or your own
model = tf.keras.applications.vgg16.VGG16(weights="imagenet", include_top=True)

# Load a sample image (or multiple ones)
img = tf.keras.preprocessing.image.load_img(IMAGE_PATH, target_size=(224, 224))
img = tf.keras.preprocessing.image.img_to_array(img)
data = ([img], None)

# Start explainer
explainer = GradCAM()
grid = explainer.explain(data, model, class_index=281)  # 281 is the tabby cat index in ImageNet

explainer.save(grid, ".", "grad_cam.png")
```

### During training

If you want to follow your model during the training, you can also use it as a Keras Callback,
and see the results directly in [TensorBoard](https://www.tensorflow.org/tensorboard/).

```python
from tf_explain.callbacks.grad_cam import GradCAMCallback

model = [...]

callbacks = [
    GradCAMCallback(
        validation_data=(x_val, y_val),
        class_index=0,
        output_dir=output_dir,
    )
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```


## Available Methods

1. [Activations Visualization](#activations-visualization)
1. [Vanilla Gradients](#vanilla-gradients)
1. [Gradients*Inputs](#gradients-inputs)
1. [Occlusion Sensitivity](#occlusion-sensitivity)
1. [Grad CAM (Class Activation Maps)](#grad-cam)
1. [SmoothGrad](#smoothgrad)
1. [Integrated Gradients](#integrated-gradients)

### Activations Visualization

> Visualize how a given input comes out of a specific activation layer

```python
from tf_explain.callbacks.activations_visualization import ActivationsVisualizationCallback

model = [...]

callbacks = [
    ActivationsVisualizationCallback(
        validation_data=(x_val, y_val),
        layers_name=["activation_1"],
        output_dir=output_dir,
    ),
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```

<p align="center">
    <img src="./docs/assets/activations_visualisation.png" width="400" />
</p>


### Vanilla Gradients

> Visualize gradients importance on input image

```python
from tf_explain.callbacks.vanilla_gradients import VanillaGradientsCallback

model = [...]

callbacks = [
    VanillaGradientsCallback(
        validation_data=(x_val, y_val),
        class_index=0,
        output_dir=output_dir,
    ),
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```

<p align="center">
    <img src="./docs/assets/vanilla_gradients.png" width="200" />
</p>


### Gradients*Inputs

> Variant of [Vanilla Gradients](#vanilla-gradients) ponderating gradients with input values

```python
from tf_explain.callbacks.gradients_inputs import GradientsInputsCallback

model = [...]

callbacks = [
    GradientsInputsCallback(
        validation_data=(x_val, y_val),
        class_index=0,
        output_dir=output_dir,
    ),
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```

<p align="center">
    <img src="./docs/assets/gradients_inputs.png" width="200" />
</p>


### Occlusion Sensitivity

> Visualize how parts of the image affects neural network's confidence by occluding parts iteratively

```python
from tf_explain.callbacks.occlusion_sensitivity import OcclusionSensitivityCallback

model = [...]

callbacks = [
    OcclusionSensitivityCallback(
        validation_data=(x_val, y_val),
        class_index=0,
        patch_size=4,
        output_dir=output_dir,
    ),
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```

<div align="center">
    <img src="./docs/assets/occlusion_sensitivity.png" width="200" />
    <p style="color: grey; font-size:small; width:350px;">Occlusion Sensitivity for Tabby class (stripes differentiate tabby cat from other ImageNet cat classes)</p>
</div>

### Grad CAM

> Visualize how parts of the image affects neural network's output by looking into the activation maps

From [Grad-CAM: Visual Explanations from Deep Networks
via Gradient-based Localization](https://arxiv.org/abs/1610.02391)

```python
from tf_explain.callbacks.grad_cam import GradCAMCallback

model = [...]

callbacks = [
    GradCAMCallback(
        validation_data=(x_val, y_val),
        class_index=0,
        output_dir=output_dir,
    )
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```


<p align="center">
    <img src="./docs/assets/grad_cam.png" width="200" />
</p>

### SmoothGrad

> Visualize stabilized gradients on the inputs towards the decision

From [SmoothGrad: removing noise by adding noise](https://arxiv.org/abs/1706.03825)

```python
from tf_explain.callbacks.smoothgrad import SmoothGradCallback

model = [...]

callbacks = [
    SmoothGradCallback(
        validation_data=(x_val, y_val),
        class_index=0,
        num_samples=20,
        noise=1.,
        output_dir=output_dir,
    )
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```

<p align="center">
    <img src="./docs/assets/smoothgrad.png" width="200" />
</p>

### Integrated Gradients

> Visualize an average of the gradients along the construction of the input towards the decision

From [Axiomatic Attribution for Deep Networks](https://arxiv.org/pdf/1703.01365.pdf)

```python
from tf_explain.callbacks.integrated_gradients import IntegratedGradientsCallback

model = [...]

callbacks = [
    IntegratedGradientsCallback(
        validation_data=(x_val, y_val),
        class_index=0,
        n_steps=20,
        output_dir=output_dir,
    )
]

model.fit(x_train, y_train, batch_size=2, epochs=2, callbacks=callbacks)
```

<p align="center">
    <img src="./docs/assets/integrated_gradients.png" width="200" />
</p>


## Roadmap

- [ ] Subclassing API Support
- [ ] Additional Methods
  - [ ] [GradCAM++](https://arxiv.org/abs/1710.11063)
  - [x] [Integrated Gradients](https://arxiv.org/abs/1703.01365)
  - [x] [Guided SmoothGrad](https://arxiv.org/abs/1706.03825)
  - [ ] [LRP](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0130140)
- [ ] Auto-generated API Documentation & Documentation Testing

## Contributing

To contribute to the project, please read the [dedicated section](./CONTRIBUTING.md).

## Citation

A [citation file](./CITATION.cff) is available for citing this work. Click the "Cite this repository" button on the right-side panel of Github to get a BibTeX-ready citation.
