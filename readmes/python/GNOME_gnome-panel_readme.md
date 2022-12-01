# About

This repository contains the GNOME Panel of the GNOME Flashback project. It consists of the `gnome-panel` binary, 
the `libpanel-applet` library and several applets.

  * The GNOME panel is the area on your desktop from which you can run
    applications and applets, and perform other tasks.

  * The `libpanel-applet` library allows to develop small applications
    which may be embedded in the panel. These are called applets.
    Documentation for the API is available on developer.gnome.org
    (see [stable](https://developer.gnome.org/libpanel-applet/stable/) 
    and [unstable](https://developer.gnome.org/libpanel-applet/unstable/) versions).

  * The applets supplied here include the Workspace Switcher, the Window
    List, the Window Selector, the Notification Area, the Clock and the
    infamous 'Wanda the Fish'. Further applets are available in the `gnome-applets`
    repository.

# Releases

You may download gnome-panel releases and updates from the [release server](http://download.gnome.org/sources/gnome-panel/)

# Discussions

To discuss gnome-panel, you may use the [gnome-flashback-list](http://mail.gnome.org/mailman/listinfo/gnome-flashback-list) mailing list.

# Installation

See the file 'INSTALL'. If you are not using a released version of
gnome-panel (for example, if you checked out the code from git), you
first need to run './autogen.sh'.

# How to report bugs

Bugs should be reported in the issue section of [GNOME Gitlab](https://gitlab.gnome.org/GNOME/gnome-panel/issues)

You will need to create an account for yourself.

Please read the HACKING file for information on where to send changes or
bugfixes for this package.
