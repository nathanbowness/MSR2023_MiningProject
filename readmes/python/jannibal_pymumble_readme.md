# PYMUMBLE python library

## Description
This library acts as a mumble client, connecting to a murmur server, exchanging states and audio.

[![Build Status](https://ci.azlux.fr/api/badges/azlux/pymumble/status.svg)](https://ci.azlux.fr/azlux/pymumble)

The wiki/API explanation is [HERE](https://github.com/azlux/pymumble/blob/pymumble_py3/API.md).

## Installing/Getting started

### Requirements

**`libopus` is a mandatory OS library**. Please refer to your package manager to install it.

### With pip

- `pip install pymumble`
- You need to `import pymumble_py3 as pymumble` into your code.

[![PyPI version](https://badge.fury.io/py/pymumble.svg)](https://badge.fury.io/py/pymumble)   Deployment script is available [here](https://packages.azlux.fr/scripts/pymumble.txt)

### With git

- `git clone https://github.com/azlux/pymumble.git`
- `pip3 install -r requirements.txt`
- You need to `import pymumble.pymumble_py3 as pymumble` into your code.
- It's will be the same if you use a git sub-module

## CHANGELOG

The changelog is available on the release note.

## Applications list using `pymumble`

For client application examples, you can check this list :
- [Botamusique](https://github.com/azlux/botamusique)
- [MumbleRadioPlayer](https://github.com/azlux/MumbleRadioPlayer) (archived)
- [Abot](https://github.com/ranomier/pymumble-abot)
- [MumbleRecbot](https://github.com/Robert904/mumblerecbot) (deprecated)

## Features

### Currently implemented:
- Compatible with Mumble 1.3 and normally until 1.2.2
- Support OPUS. Speex is not supported
- Receive and send audio, get users and channels status
- Set properties for users (mute, comments, etc.) and go to a specific channel
- Kick and ban users
- Callback mechanism to react on server events
- Manage the blobs (images, long comments, etc.)
- Can send text messages to user and channel
- Ping statistics
- Audio targets (whisper, etc.)
- Read ACL groups

### What is missing:

>  I don't need these features, so if you want one, open an issue and I will work on it.

- UDP media. Currently it works only in TCP tunneling mode (the standard fallback of Mumble when UDP is not working)
- Some server management features (user creation, editing ACLs, etc.)
- Positioning is not managed, but it should be easy to add
- Probably a lot of other small features
- **WONTFIX** The **Python 2** version is available in the [master branch](https://github.com/azlux/pymumble/tree/master). It's working! But since we have moved on to Python 3, the Python 2 version will not receive future improvements.

## Architecture

The library is based on the Mumble object, which a thread. When started, it will try
to connect to the server and start exchanging the connection messages.
This thread implements a loop which takes care of the pings, sends commands to the server,
checks for incoming messages including audio, and checks for audio to be sent out.
The rate of this loop is controlled by how long it will wait for an incoming message before continuing.

You can check if the thread is alive with `mumble_object.is_alive()`.
The Mumble thread will stop if it disconnects from the server.
This can be useful if you need to restart the thread when using a supervisor.


## Thanks

- [@raylu](https://github.com/raylu) for making `pymumble` speak into channels
- [@schlarpc](https://github.com/schlarpc) for fixes on buffer
- [@Robert904](https://github.com/Robert904) for the inital pymumble implementation

This library is a fork of a fork of a fork (initial from https://github.com/Robert904/pymumble).
But we will try to make `pymumble` better.
So I consider this fork (the [@Azlux](https://github.com/azlux/pymumble) one) the current live fork of `pymumble`.
