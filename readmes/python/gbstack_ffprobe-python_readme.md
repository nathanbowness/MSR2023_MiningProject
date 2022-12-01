ffprobe-python module
=====================

A wrapper around the ffprobe command to extract metadata from media files or streams.

Usage:

```python
#!/usr/bin/env python

from ffprobe import FFProbe

# Local file
metadata=FFProbe('test-media-file.mov')

# Video stream
# metadata=FFProbe('http://some-streaming-url.com:8080/stream')

for stream in metadata.streams:
    if stream.is_video():
        print('Stream contains {} frames.'.format(stream.frames()))

```

This software is now maintained by Mark Ma <519329064@qq.com>.

---

(The MIT License)

Copyright 2013 Simon Hargreaves <simon@simon-hargreaves.com>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the Software), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
