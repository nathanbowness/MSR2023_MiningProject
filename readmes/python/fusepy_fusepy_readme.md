fusepy
======

    **NOTE**: *This project has moved to be under a GitHub organization and can
    be found at https://github.com/fusepy/fusepy. The project has new
    maintainers and will be looking to incorporate pull requests in a more
    timely manner. If you would like to help maintain this package please open
    a pull request and demonstrate willingness to help (we will leave
    maintainer criteria up to the current maintainers).*

``fusepy`` is a Python module that provides a simple interface to FUSE_ and
MacFUSE_. It's just one file and is implemented using ctypes.

The original version of ``fusepy`` was hosted on `Google Code`_, but is now
`officially hosted on GitHub`_.

``fusepy`` is written in 2x syntax, but trying to pay attention to bytes and
other changes 3x would care about.

examples
--------
See some examples of how you can use fusepy:

:memory_: A simple memory filesystem
:loopback_: A loopback filesystem
:context_: Sample usage of fuse_get_context()
:sftp_: A simple SFTP filesystem (requires paramiko)

To get started download_ fusepy or just browse the source_.

fusepy requires FUSE 2.6 (or later) and runs on:

- Linux (i386, x86_64, PPC, arm64, MIPS)
- Mac OS X (Intel, PowerPC)
- FreeBSD (i386, amd64)


.. _FUSE: http://fuse.sourceforge.net/
.. _MacFUSE: http://code.google.com/p/macfuse/
.. _`Google Code`: http://code.google.com/p/fusepy/

.. _officially hosted on GitHub: source_
.. _download: https://github.com/fusepy/fusepy/zipball/master
.. _source: http://github.com/fusepy/fusepy

.. examples
.. _memory: http://github.com/fusepy/fusepy/blob/master/examples/memory.py
.. _loopback: http://github.com/fusepy/fusepy/blob/master/examples/loopback.py
.. _context: http://github.com/fusepy/fusepy/blob/master/examples/context.py
.. _sftp: http://github.com/fusepy/fusepy/blob/master/examples/sftp.py
