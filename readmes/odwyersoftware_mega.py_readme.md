Mega.py
=======

[![Build
Status](https://travis-ci.org/odwyersoftware/mega.py.png?branch=master)](https://travis-ci.org/odwyersoftware/mega.py)
[![Downloads](https://pypip.in/d/mega.py/badge.png)](https://crate.io/packages/mega.py/)  [![PyPI version](https://badge.fury.io/py/mega.py.svg)](https://pypi.org/project/mega.py/)

Python library for the [Mega.co.nz](https://mega.nz/aff=Zo6IxNaHw14)
API, currently supporting:

-   login
-   uploading
-   downloading
-   deleting
-   searching
-   sharing
-   renaming
-   moving files

This is a work in progress, further functionality coming shortly.

For more detailed information see API\_INFO.md

How To Use
----------

### Create a Mega account

First, [create an account with Mega](https://mega.nz/aff=Zo6IxNaHw14) .

### Install mega.py package

Run the following command, or run setup from the latest github source.

```python
pip install mega.py
```

### Import mega.py

```python
from mega import Mega
```

### Create an instance of Mega.py

```python
mega = Mega()
```

### Login to Mega

```python
m = mega.login(email, password)
# login using a temporary anonymous account
m = mega.login()
```

### Get user details

```python
details = m.get_user()
```

### Get account balance (Pro accounts only)

```python
balance = m.get_balance()
```

### Get account disk quota

```python
quota = m.get_quota()
```

### Get account storage space

```python
# specify unit output kilo, mega, gig, else bytes will output
space = m.get_storage_space(kilo=True)
```

### Get account files

```python
files = m.get_files()
```

### Upload a file, and get its public link

```python
file = m.upload('myfile.doc')
m.get_upload_link(file)
# see mega.py for destination and filename options
```

### Export a file or folder

```python
public_exported_web_link = m.export('myfile.doc')
public_exported_web_link = m.export('my_mega_folder/my_sub_folder_to_share')
# e.g. https://mega.nz/#F!WlVl1CbZ!M3wmhwZDENMNUJoBsdzFng
```

### Find a file or folder

```python
folder = m.find('my_mega_folder')
# Excludes results which are in the Trash folder (i.e. deleted)
folder = m.find('my_mega_folder', exclude_deleted=True)
```

### Upload a file to a destination folder

```python
folder = m.find('my_mega_folder')
m.upload('myfile.doc', folder[0])
```

### Download a file from URL or file obj, optionally specify destination folder

```python
file = m.find('myfile.doc')
m.download(file)
m.download_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc')
m.download(file, '/home/john-smith/Desktop')
# specify optional download filename (download_url() supports this also)
m.download(file, '/home/john-smith/Desktop', 'myfile.zip')
```

### Import a file from URL, optionally specify destination folder

```python
m.import_public_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc')
folder_node = m.find('Documents')[1]
m.import_public_url('https://mega.co.nz/#!utYjgSTQ!OM4U3V5v_W4N5edSo0wolg1D5H0fwSrLD3oLnLuS9pc', dest_node=folder_node)
```

### Create a folder

```python
m.create_folder('new_folder')
m.create_folder('new_folder/sub_folder/subsub_folder')
```

Returns a dict of folder node name and node\_id, e.g.

```python
{
  'new_folder': 'qpFhAYwA',
  'sub_folder': '2pdlmY4Z',
  'subsub_folder': 'GgMFCKLZ'
}
```

### Rename a file or a folder

```python
file = m.find('myfile.doc')
m.rename(file, 'my_file.doc')
```

## Contact Support

For paid priority support contact [mega@odwyer.software](mailto:mega@odwyer.software).

**[UK Python Development Agency](https://odwyer.software/)**
