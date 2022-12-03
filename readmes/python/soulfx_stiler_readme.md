stiler.py is a simple python script which does tiling on any X window-manager.

stiler.py is known to work with pekwm, openbox, metacity, and compiz.

Requirements:

wmctrl          - used to get the window and desktop information and manage the windows

Usage: stiler.py layout_option [flags]

Standard layout_options:
simple          - The basic tiling layout . 1 Main + all other at the side.
swap            - Will swap the active window to master column
cycle           - Cycle all the windows in the master pane
vertical        - Simple vertical tiling
horizontal 	    - Simple horizontal tiling
maximize        - Maximize the active window/ for openbox which doesn't permit resizing of max windows
max_all         - Maximize all windows

Grid layout_options:

The following grid options mimic the functionality of compiz's grid plugin which in turn mimics the functionality of winsplit revolution.

top_left        - Place the active window in the top left corner of the screen
top             - Place the active window along the top of the screen
top_right       - Place the active window in the top right corner of the screen
left,right      - Does the new windows7 ish style of sticking to the sides.
middle          - Place the active window in the middle of the screen
bottom_left     - Place the active window in the bottom left corner of the screen
bottom          - Place the active window along the bottom of the screen
bottom_right    - Place the active window in the bottom right corner of the screen
swap_grid       - Swap the active window with the largest window


Multiple calls to any of the grid options on the same active window will select different widths.

On first run stiler will create a config file ~/.stilerrc. Modify the values to suit your window decorations/Desktop padding.  The two most influential values are the winborder and wintitle values.

Flags:

-v              - Enable INFO level verbosity
-vv             - Enable DEBUG level verbosity
-h              - Display usage information

~/.stilerrc file options:

leftpadding     - pads the left hand side of the screen the given number of pixels
toppadding      - pads the top of the screen the given number of pixels
bottompadding   - pads the bottom of the screen the given number of pixels
rightpadding    - pads the right hand side of the screen the given number of pixels

window padding options:

winborder       - pads the given number of pixels around each window
wintitle        - pads the given number of pixels above each window

miscellaneous options 

tempfile        - cache file for holding window positions
windowfilter    - exclude minimized and UTILITY windows from being tiled

simple layout options:

mwfactor        - width of the bigger window in the simple layout

grid layout options:

monitors        - for a dual monitor setup set this to 2
gridwidths      - a list of locations on the screen at which to place the borders of the grid.  Each location is mirrored across 1/2 the screen.  For example, a gridwidths list of 0.17,0.33,0.50 creates grid borders at 0.17,0.33,0.50,0.67,0.83
widthadjustment - sometimes the gridwidths end up being rounded too high or low which can be common in a dual monitor setup.  Use the widthadjustment to account for rounding error.

If you need other layouts modify get_simple_tile 

Known Issues:

compiz          - compiz says it has a single desktop even if there are 4 virtual desktops, which means all the windows you have will be tiled.
firefox         - firefox get a little stubborn when resized below a certain point

See Also:
xbindkeys       - map keyboard keys to stiler.py options.  a sample xbindkeysrc is provided.
