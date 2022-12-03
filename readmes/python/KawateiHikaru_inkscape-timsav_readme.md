TimSav G-Code Output for Inkscape
===========================================

This is an Inkscape extension that allows you to save your Inkscape drawings as
G-Code files suitable for needle cutting with the [ERC TimSav](https://www.thingiverse.com/thing:3951161).

Disclaimer
===========================================
I am not responsible for any damanage or harm that may have caused by this extension, do so at your own risk

* Modified by: [Brian Ho](http://github.com/kawateihikaru)
* Original Author: [Marty McGuire](http://github.com/martymcguire)

Credits
=======

* Brian Ho modified this extension to generate compatible g-code for TimSav (Robotini GRBL)  
* Marty McGuire pulled this all together into an Inkscape extension.
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.

Install
=======

Copy the contents to your Inkscape `extensions/` folder.

Typical locations include:

* OS X - `/Applications/Inkscape.app/Contents/Resources/extensions`
* Linux - `/usr/share/inkscape/extensions`
* Windows - `C:\Program Files\Inkscape\share\extensions`

you should have 2 files directly under the extensions folder (unicorn.inx, unicorn.py) and the unicorn folder as well.

Usage
=====

* Create a document with the size of your foam board (eg. 20x30 in)  and **SAVE THE DOCUMENT **
    ![Document Property](doc/image1.png)
* Create some objects and convert all to paths:
	* Select all text objects.
	* Choose **Path | Object to Path**.
* The path cutting orders are generated based on the svg document hierarchy, you can organize your paths with the XML editor.
    ![Document Property](doc/image2.png)
    * For score cuts make the path strike **RED** #ff0000 (mind the lower case ff)
    * For marking cuts make the path strike **BLUE** #0000ff (mind the lower case ff)
    * The id of the path can be set with the editor and will be retained in the gcode's comment (helps with gcode troubleshooting)
* Save as G-Code:
    ![Document Property](doc/image3.png)
	* **File | Save a Copy**.
	* Select **TimSav G-Code (\*.gcode)**.
	* Save your file and load the new gcode
	![Document Property](doc/image4.png)

TODOs
=====
* Draw arrow for the direction of path for view
* Rename `*PolyLine` stuff to `*Path` to be less misleading.
* Parameterize smoothness for curve approximation.
* Use native curve G-Codes instead of converting to paths?
