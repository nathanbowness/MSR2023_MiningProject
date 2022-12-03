Deprecated
===========

Please use [Pynput](https://github.com/moses-palmer/pynput) instead.

What's wrong with PyUserInput?

* Nobody is actively working on it
* Events on Windows depend on PyHook which is dead and not compatible with Python 3
* Only works with QWERTY
* Inconsistent API for non-printable characters
* Probably more

PyUserInput
===========

A module for cross-platform control of the mouse and keyboard in python that is
simple to use.

Mouse control and capture should be fairly complete and mature on all supported platforms. Any incompatabilities should be reported.

Basic keyboard handling should work, but known issues exist. Contributions welcome. For some less-common keyboard keys and layouts, you may want to look at [Pynput](https://github.com/moses-palmer/pynput)

Installation
------------

### Dependencies
Depending on your platform, you will need the following python modules for PyUserInput to function:
* Linux - Xlib (python-xlib)
* Mac - Quartz, AppKit
* Windows - pywin32, pyHook

If you don't have the dependencies appropriate for your system, the installation of PyUserInput should warn you of that fact.

### Windows Dependencies
PyUserInput on Windows depends on pywin32, a set of Windows extensions for Python. To install them, please visit http://sourceforge.net/projects/pywin32/files/pywin32/, choose the latest build, and download and run the file corresponding to your version and architecture of Python.

### Using pip
PyUserInput is registered on PyPI (Python Package Index) and updated periodically, so tools such as pip or easy_install should work.

`pip install PyUserInput`

### From Source

You can download a [zip file from Github](https://github.com/PyUserInput/PyUserInput/archive/master.zip) or a tar.gz file from PyPI that contains the source code. Once you have uncompressed the file into a directory, you should navigate a terminal session to the directory that contains setup.py. The next step is to type the following command:

`python setup.py install`

If you are on linux and have a problem with permissions, you may need to prepend the command with sudo. For any other installation problems, open an issue on GitHub.

How to get started
------------------

After installing PyUserInput, you should have pymouse and pykeyboard modules in
your python path. Let's make a mouse and keyboard object:

```python

from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
```

Here's an example of clicking the center of the screen and typing "Hello, World!":

```python

x_dim, y_dim = m.screen_size()
m.click(x_dim/2, y_dim/2, 1)
k.type_string('Hello, World!')
```

PyKeyboard allows for a range of ways for sending keystrokes:

```python

# pressing a key
k.press_key('H')
# which you then follow with a release of the key
k.release_key('H')
# or you can 'tap' a key which does both
k.tap_key('e')
# note that that tap_key does support a way of repeating keystrokes with a interval time between each
k.tap_key('l',n=2,interval=5)
# and you can send a string if needed too
k.type_string('o World!')
```


and it supports a wide range of special keys:

```python

#Create an Alt+Tab combo
k.press_key(k.alt_key)
k.tap_key(k.tab_key)
k.release_key(k.alt_key)

k.tap_key(k.function_keys[5])  # Tap F5
k.tap_key(k.numpad_keys['Home'])  # Tap 'Home' on the numpad
k.tap_key(k.numpad_keys[5], n=3)  # Tap 5 on the numpad, thrice
```

Note you can also send multiple keystrokes together (e.g. when accessing a keyboard shortcut) using the press_keys method:

```python

# Mac example
k.press_keys(['Command','shift','3'])
# Windows example
k.press_keys([k.windows_l_key,'d'])
```

Consistency between platforms is a big challenge; Please look at the source for the operating system that you are using to help understand the format of the keys that you would need to send. For example:

```python

# Windows
k.tap_key(k.alt_key)
# Mac
k.tap_key('Alternate')
```

I'd like to make a special note about using PyMouseEvent and PyKeyboardEvent.
These objects are a framework for listening for mouse and keyboard input; they
don't do anything besides listen until you subclass them. I'm still formalizing
PyKeyboardEvent, so here's an example of subclassing PyMouseEvent:

```python

from pymouse import PyMouseEvent

def fibo():
    a = 0
    yield a
    b = 1
    yield b
    while True:
        a, b = b, a+b
        yield b

class Clickonacci(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.fibo = fibo()

    def click(self, x, y, button, press):
        '''Print Fibonacci numbers when the left click is pressed.'''
        if button == 1:
            if press:
                print(self.fibo.next())
        else:  # Exit if any other mouse button used
            self.stop()

C = Clickonacci()
C.run()
```

Intended Functionality of Capturing in PyUserInput
--------------------------------------------------

For PyMouseEvent classes, the variables "capture" and "capture_move" may be
passed during instantiation. If `capture=True` is passed, the intended result
is that all mouse button input will go to your program and nowhere else. The
same is true for `capture_move=True` except it deals with mouse pointer motion
instead of the buttons. Both may be set simultaneously, and serve to prevent
events from propagating further. If you notice any bugs with this behavior,
please bring it to our attention.

A Short Todo List
-----------------

These are a few things I am considering for future development in
PyUserInput:

 * Get rid of PyHook
 * Make PyKeyboard work for less-common keys and layouts
 * Make friends with more developers, help is needed...
