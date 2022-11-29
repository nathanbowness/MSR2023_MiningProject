### PyZ3950

This is a fork of the [PyZ3950] (https://github.com/asl2/PyZ3950) library with modifications.

See the original [README] (https://github.com/asl2/PyZ3950/blob/master/README.txt) for license information.

See the project [HISTORY] (https://github.com/asl2/PyZ3950/network).

- pip install ply
- pip uninstall PyZ3950   # or if not supported manually remove older version dist-packages/PyZ3950
- git clone https://github.com/zvolsky/PyZ3950.git
- cd PyZ3950/
- python setup.py sdist   # will create dist/ folder
- pip install PyZ3950 --no-index --no-cache-dir --find-links file:///home/.../dist/
