This is an experimental build system for media drivers.
All files on this tree are covered by GPLv2, as stated at COPYING file.

Usage:

Just call the build utility:
	$ ./build

Then, install the drivers as root, with:
	# make install

In order to test, unload old drivers with:
	# make rmmod

Then modprobe the driver you want to test. For example, to load driver 'foo':
	# modprobe foo


If you're developing a new driver or patch, it is better to use:
	$ ./build --main-git

Then, install the drivers as root, with:
	# make install

In order to test, unload old drivers with:
	# make rmmod

Then modprobe the driver you want to test. For example:
	# modprobe bttv

In this case, in order to modify something, you should edit the file at
the media/ subdir.

For example, a typical procedure to develop a new patch would be:

	~/media_build $ cd media
	~/media $ gedit drivers/media/video/foo.c
	~/media $ make -C ../v4l
	~/media $ make -C .. rmmod
	~/media $ modprobe foo
	(some procedure to test the "foo" driver)
	~/media $ git diff >/tmp/my_changes.patch
	(email /tmp/my_changes.patch inlined to linux-media@vger.kernel.org)
