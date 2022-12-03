# jupyter-binder

This repo is a collection of my notebooks I've used to play around with some data science topics. They were mostly a place for me to explore and learn about a topic, but I've posted them here in case others find them useful! Some of them have fairly good comments, which are hopefully helpful for others!

## Running the notebooks

### 1. Run in the cloud via mybinder
Click the button below to run and play with the notebooks in this repo! (Binder [last built](http://mybinder.org/status/nhdaly/jupyter-binder) at [5985cc1](https://github.com/NHDaly/jupyter-binder/commit/5985cc1)).

The binder currently has [iJulia](https://github.com/JuliaLang/IJulia.jl) and [TensorFlow](https://www.tensorflow.org/) installed, as well as the [OpenAi Gym](https://gym.openai.com) framework.


[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master)

### 2. Run locally with docker
First, clone this repo.
Then, create the docker container and launch the notebook server by running `./start-local-binder.sh`. (This requires `docker` to be installed. It will build a docker container based on `Dockerfile`, and launch it once it finishes. The first time, this will be very, very slow.)

Note, the files will be located in the directory "binder/".

### 3. Run locally, natively
If you already have any of the requisite tools installed on your machine (`Tensorflow` or `Julia`, etc), you can simply launch a `jupyter` notebook server to run the scripts yourself, via `jupyter notebook`.


---------

## Table of Contents

NOTE: The interactive `mybinder` deep-links below each open a new mybinder session, which seems to be running very, very slowly. If you want to open multiple interactive posts (which I encourage!), I would recommend you first simply open the binder by clicking the above badge or [clicking here](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master), and then open each interactive `.ipynb` file from there.

### Recurrent Neural Networks
The following posts are reimplementations of and explanations of Karpathy's ["The Unreasonable Effectiveness of Recurrent Neural Networks"](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). I used these posts to try to get a better understanding of the concepts. Please note that I am by no means an expert on these topics, and certainly wasn't when I wrote these -- this was my first introduction to Neural Networks and ML.

`julia_rnn.ipynb` attempts to follow along with contents of Karpathy's article. In this post, we build the RNN from scratch, and hand-code its gradient (derivative), and build the training infrastructure to train it. In the end, the RNN is producing "shakespeare-ish" looking text. This is implemented in `Julia`, instead of the [python implementation](https://github.com/karpathy/char-rnn) from Karpathy's post.

*Click here to
[read as a static post](https://github.com/NHDaly/jupyter-binder/blob/master/julia_rnn.ipynb), or here for an [interactive jupyter notebook](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master?filepath=julia_rnn.ipynb).*


`TensorFlow-custom-RNN.ipynb` builds the same model, but using `TensorFlow` in `python`. This post also does a better job explaining the math, to try provide a more intuitive feel for _why_ the cost function is what it is.

*Click here to
[read as a static post](https://github.com/NHDaly/jupyter-binder/blob/master/TensorFlow-custom-RNN.ipynb), or here for an [interactive jupyter notebook](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master?filepath=TensorFlow-custom-RNN.ipynb).*

### Monte Carlo Tree Search (MCTS) tic-tac-toe

`MonteCarlo-TicTacToe.ipynb` is a `python`-only implementation of a bot that plays perfect tic-tac-toe. It's a simple implementation of the [Monte Carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search).
The only requirement is jupyter notebook, since it uses the notebook's built-in `ipython` display utilities to play.

*Click here to
[read as a static post](https://github.com/NHDaly/jupyter-binder/blob/master/MonteCarlo-TicTacToe.ipynb), or here for an [interactive jupyter notebook](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master?filepath=MonteCarlo-TicTacToe.ipynb).*

_This one is definitely worth playing with interactively!!_

### OpenAI gym: Cartpole problem (Reinforcement Learning tutorial)

The [OpenAI gym](https://gym.openai.com/) presents the Cartpole problem [as an introduction](https://openai.com/requests-for-research/#cartpole) to reinforcement learning. They suggest that you complete it with three algorithms of increasing complexity: random guessing, hill-climbing, and Policy gradient. Here, I implement all three solutions from scratch, using `python` and `numpy`. At the end of the Policy gradient post, I collect some observations.

- **random guessing**: *[read as a static post](https://github.com/NHDaly/jupyter-binder/blob/master/OpenAI-gym-cartpole-random-guessing.ipynb), or explore an [interactive jupyter notebook](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master?filepath=OpenAI-gym-cartpole-random-guessing.ipynb).*
- **hill-climbing**: *[read as a static post](https://github.com/NHDaly/jupyter-binder/blob/master/OpenAI-gym-cartpole-hill-climbing.ipynb), or explore an [interactive jupyter notebook](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master?filepath=OpenAI-gym-cartpole-hill-climbing.ipynb).*

- **Policy gradient**: *[read as a static post](https://github.com/NHDaly/jupyter-binder/blob/master/OpenAI-gym-cartpole-policy-gradient.ipynb), or explore an [interactive jupyter notebook](https://mybinder.org/v2/gh/nhdaly/jupyter-binder/master?filepath=OpenAI-gym-cartpole-policy-gradient.ipynb).*


### Karl Nearest Neighbors
A simple python program solving this goal: For each point in a list, find the set of points that are within `desired_range` of that point. This only requires `python`.

This was a demonstration for my friend Karl..


