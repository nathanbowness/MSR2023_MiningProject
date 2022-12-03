# plotpy: Python tools for curve and image plotting

<img src="http://pythonhosted.org/plotpy/_images/panorama.png">

See [documentation](http://pythonhosted.org/plotpy/) for more details on 
the library and [changelog](CHANGELOG.md) for recent history of changes.

Copyright © 2009-2018 CEA, Pierre Raybaut, licensed under the terms of the 
[CECILL License](Licence_CeCILL_V2-en.txt).


## Overview

Based on ``PythonQwt`` (a pure Python/PyQt reimplementation of the curve 
plotting Qwt C++ library, included in plotpy base source code) and on the 
scientific modules NumPy and SciPy, ``plotpy`` is a Python library providing 
efficient 2D data-plotting features (curve/image visualization and related 
tools) for interactive computing and signal/image processing application 
development. It is based on Qt graphical user interfaces library, and 
currently supports both ``PyQt4`` and ``PyQt5``.

Extension to ``PythonQwt``:

* set of tools for curve and image plotting
* GUI-based application development helpers


## Dependencies

### Requirements

- Python 2.6+ or Python 3.2+
- [PyQt4](https://pypi.python.org/pypi/PyQt4) 4.3+ or [PyQt5](https://pypi.python.org/pypi/PyQt5) 5.5+
- [NumPy](https://pypi.python.org/pypi/NumPy) 1.6+
- [SciPy](https://pypi.python.org/pypi/SciPy) 0.7+
- [Pillow](https://pypi.python.org/pypi/Pillow)

[PythonQwt](https://pypi.python.org/pypi/PythonQwt) is no longer required as it is now embedded in ``plotpy``.

### Optional modules
        
- [spyder](https://pypi.python.org/pypi/spyder) 2.1+ or 3.0+ for GUI-embedded console support
- [pydicom](https://pypi.python.org/pypi/pydicom) 0.9.3+ for DICOM I/O support


## Building/Installation

### All platforms:
        
The setup.py script supports the following extra options for 
optimizing the image scaler engine with SSE2/SSE3 processors: 
``--sse2`` or ``--sse3``.

### On GNU/Linux and MacOS platforms:

```bash
python setup.py build install
```

### On Windows platforms with Microsoft Visual C/C++:
        
```cmd
python setup.py build install
```
    
### On Windows platforms with MinGW:
        
```cmd
python setup.py build -c mingw32 install
```
