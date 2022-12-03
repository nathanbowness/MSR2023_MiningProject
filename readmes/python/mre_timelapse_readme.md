![timelapse logo](timelapse/resources/logo.svg)

...a little macOS app that records your screen to make a timelapse.

![CI](https://github.com/mre/timelapse/workflows/CI/badge.svg)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/mre/timelapse)

## Features

- Simple
- Open Source
- Easy to access
- Low memory and CPU usage
- Follows the cursor across screens while recording

## Getting started

1. Make sure that you have `ffmpeg` installed (e.g. run `brew install ffmpeg`).
2. [Download timelapse](https://github.com/mre/timelapse/releases/latest/download/timelapse.zip)
3. Unzip and start the app. If you get a warning about the app being unsigned,
   go to `System Preferences > Security & Privacy` and allow the app to run.
4. A new icon appears in your menubar; start and stop the screen recording from
   there.
   ![A demonstration of starting and stopping a recording from the menubar](timelapse.gif)

timelapse will create a video for you **in your `Movies` folder**.

## Development

If you like to help improve this app, make sure you have at least Python 3.6
installed. First, install the project's dependencies:

```shell
make install
```

Now make changes and run the main application from the commandline:

```shell
make run
```

## License

Licensed under either of

- Apache License, Version 2.0, (LICENSE-APACHE or
  http://www.apache.org/licenses/LICENSE-2.0)
- MIT license (LICENSE-MIT or http://opensource.org/licenses/MIT)

at your option.

App icon by [gstudioimagen -
www.freepik.com](https://www.freepik.com/free-photos-vectors/people).
