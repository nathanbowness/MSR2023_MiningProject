# Streaming multipart/form-data parser

[![image](https://github.com/siddhantgoel/streaming-form-data/workflows/streaming-form-data/badge.svg)](https://github.com/siddhantgoel/streaming-form-data/workflows/streaming-form-data/badge.svg)

[![image](https://img.shields.io/pypi/v/streaming-form-data.svg)](https://pypi.python.org/pypi/streaming-form-data)

[![image](https://img.shields.io/pypi/pyversions/streaming-form-data.svg)](https://pypi.python.org/pypi/streaming-form-data)

[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


`streaming_form_data` provides a Python parser for parsing `multipart/form-data`
input chunks (the encoding used when submitting data over HTTP through HTML
forms).

## Testimonials

> "[_this speeds up file uploads to my Flask app by **more than factor 10**_](https://github.com/pallets/werkzeug/issues/875#issuecomment-429287766)"

> "[_Thanks a lot for your fix with streaming-form-data. I can finally upload gigabyte sized files at good speed and without memory filling up!_](https://github.com/pallets/werkzeug/issues/875#issuecomment-530020990)"

## Installation

```bash
$ pip install streaming-form-data
```

In case you prefer cloning the Github repository and installing manually, please
note that `master` is the development branch, so `stable` is what you should be
working with.

## Usage

```python
>>> from streaming_form_data import StreamingFormDataParser
>>> from streaming_form_data.targets import ValueTarget, FileTarget, NullTarget
>>>
>>> headers = {'Content-Type': 'multipart/form-data; boundary=boundary'}
>>>
>>> parser = StreamingFormDataParser(headers=headers)
>>>
>>> parser.register('name', ValueTarget())
>>> parser.register('file', FileTarget('/tmp/file.txt'))
>>> parser.register('discard-me', NullTarget())
>>>
>>> for chunk in request.body:
...     parser.data_received(chunk)
...
>>>
```

## Documentation

Up-to-date documentation is available on [Read the Docs].

## Development

Please make sure you have Python 3.6+ and [pip-tools] installed.

Since this package includes a C extension, please make sure you have a working C
compiler available. On Debian-based distros this usually means installing the
`build-essentials` package.

1. Git clone the repository:
   `git clone https://github.com/siddhantgoel/streaming-form-data`

2. Install the packages required for development:
   `make pip-sync`

3. That's basically it. You should now be able to run the test suite:
   `make test`.

[pip-tools]: https://pypi.org/project/pip-tools/
[Read the Docs]: https://streaming-form-data.readthedocs.io/
