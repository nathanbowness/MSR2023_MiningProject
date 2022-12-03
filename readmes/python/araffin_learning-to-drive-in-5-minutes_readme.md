# Learning to Drive Smoothly in Minutes

**IMPORTANT: for an up-to-date version (using Stable-Baselines3 and PyTorch), please take a look at https://github.com/araffin/aae-train-donkeycar/releases/tag/live-twitch-2**

Learning to drive smoothly in minutes, using a reinforcement learning algorithm -- Soft Actor-Critic (SAC) -- and a Variational AutoEncoder (VAE) in the Donkey Car simulator.


Blog post on Medium: [link](https://medium.com/@araffin/learning-to-drive-smoothly-in-minutes-450a7cdb35f4)

Video: [https://www.youtube.com/watch?v=iiuKh0yDyKE](https://www.youtube.com/watch?v=iiuKh0yDyKE)


Level-0          | Level-1
:-------------------------:|:-------------------------:
![result](content/smooth.gif)  | ![result](content/level1.gif)
[Download VAE](https://drive.google.com/open?id=1n7FosFA0hALhuESf1j1yg-hERCnfVc4b) |  [Download VAE](https://drive.google.com/open?id=1hfQNAvVp2QmbmTLklWt2MxtAjrlisr2B)
[Download pretrained agent](https://drive.google.com/open?id=10Hgd5BKfn1AmmVdLlNcDll6yXqVkujoq) | [Download pretrained agent](https://drive.google.com/open?id=104tlsIrtOTVxJ1ZLoTpBDzK4-DRTA5et)

Note: the pretrained agents must be saved in `logs/sac/` folder (you need to pass `--exp-id 6` (index of the folder) to use the pretrained agent).


## Quick Start

0. Download simulator [here](https://drive.google.com/open?id=1h2VfpGHlZetL5RAPZ79bhDRkvlfuB4Wb) or build it from [source](https://github.com/tawnkramer/sdsandbox/tree/donkey)
1. Install dependencies (cf requirements.txt)
2. (optional but recommended) Download pre-trained VAE: [VAE Level 0](https://drive.google.com/open?id=1n7FosFA0hALhuESf1j1yg-hERCnfVc4b) [VAE Level 1](https://drive.google.com/open?id=1hfQNAvVp2QmbmTLklWt2MxtAjrlisr2B)
3. Train a control policy for 5000 steps using Soft Actor-Critic (SAC)

```
python train.py --algo sac -vae path-to-vae.pkl -n 5000
```

4. Enjoy trained agent for 2000 steps

```
python enjoy.py --algo sac -vae path-to-vae.pkl --exp-id 0 -n 2000
```

To train on a different level, you need to change `LEVEL = 0` to `LEVEL = 1` in `config.py`

## Train the Variational AutoEncoder (VAE)

0. Collect images using the teleoperation mode:

```
python -m teleop.teleop_client --record-folder path-to-record/folder/
```

1. Train a VAE:
```
python -m vae.train --n-epochs 50 --verbose 0 --z-size 64 -f path-to-record/folder/
```

## Train in Teleoparation Mode

```
python train.py --algo sac -vae logs/vae.pkl -n 5000 --teleop
```

## Test in Teleoparation Mode

```
python -m teleop.teleop_client --algo sac -vae logs/vae.pkl --exp-id 0
```

## Explore Latent Space

```
python -m vae.enjoy_latent -vae logs/level-0/vae-8.pkl
```

## Reproducing Results

To reproduce the results shown in the video, you have to check different values in `config.py`.

### Level 0

`config.py`:

```python
MAX_STEERING_DIFF = 0.15 # 0.1 for very smooth control, but it requires more steps
MAX_THROTTLE = 0.6 # MAX_THROTTLE = 0.5 is fine, but we can go faster
MAX_CTE_ERROR = 2.0 # only used in normal mode, set it to 10.0 when using teleoperation mode
LEVEL = 0
```

Train in normal mode (smooth control), it takes ~5-10 minutes:
```
python train.py --algo sac -n 8000 -vae logs/vae-level-0-dim-32.pkl
```

Train in normal mode (very smooth control with `MAX_STEERING_DIFF = 0.1`), it takes ~20 minutes:
```
python train.py --algo sac -n 20000 -vae logs/vae-level-0-dim-32.pkl
```

Train in teleoperation mode (`MAX_CTE_ERROR = 10.0`), it takes ~5-10 minutes:
```
python train.py --algo sac -n 8000 -vae logs/vae-level-0-dim-32.pkl --teleop
```

### Level 1

Note: only teleoperation mode is available for level 1

`config.py`:

```python
MAX_STEERING_DIFF = 0.15
MAX_THROTTLE = 0.5 # MAX_THROTTLE = 0.6 can work but it's harder to train due to the sharpest turn
LEVEL = 1
```

Train in teleoperation mode, it takes ~10 minutes:
```
python train.py --algo sac -n 15000 -vae logs/vae-level-1-dim-64.pkl --teleop
```

Note: although the size of the VAE is different between level 0 and 1, this is not an important factor.

## Record a Video of the on-board camera

You need a trained model. For instance, for recording 1000 steps with the last trained SAC agent:
```
python -m utils.record_video --algo sac --vae-path logs/level-0/vae-32-2.pkl -n 1000
```

## Citing the Project

To cite this repository in publications:

```
@misc{drive-smoothly-in-minutes,
  author = {Raffin, Antonin and Sokolkov, Roma},
  title = {Learning to Drive Smoothly in Minutes},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/araffin/learning-to-drive-in-5-minutes/}},
}
```

## Credits

Related Paper: ["Learning to Drive in a Day"](https://arxiv.org/pdf/1807.00412.pdf).

- [r7vme](https://github.com/r7vme/learning-to-drive-in-a-day) Author of the original implementation
- [Wayve.ai](https://wayve.ai) for idea and inspiration.
- [Tawn Kramer](https://github.com/tawnkramer) for Donkey simulator and Donkey Gym.
- [Stable-Baselines](https://github.com/hill-a/stable-baselines) for DDPG/SAC and PPO implementations.
- [RL Baselines Zoo](https://github.com/araffin/rl-baselines-zoo) for training/enjoy scripts.
- [S-RL Toolbox](https://github.com/araffin/robotics-rl-srl) for the data loader
- [Racing robot](https://github.com/sergionr2/RacingRobot) for the teleoperation
- [World Models Experiments](https://github.com/hardmaru/WorldModelsExperiments) for VAE implementation.
