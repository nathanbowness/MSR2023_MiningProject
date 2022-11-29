# Remnants of the Precursors

Remnants of the Precursors is a Java-based modernization of the original Master of Orion game from 1993.

# Links
Official website: https://www.remnantsoftheprecursors.com/<br/>
Community subreddit: https://www.reddit.com/r/rotp/<br/>
Download build: https://rayfowler.itch.io/remnants-of-the-precursors

# Planetary Governor

This is a fork with Planetary Governor mod 

https://remnantsoftheprecursors.com/

https://rayfowler.itch.io/remnants-of-the-precursors

https://github.com/rayfowler/rotp-public

This governor manages planet spending to:

* Balance spending between Industry and Ecology to maximize growth.
* Build all terraforming and factory upgrades when available.
* Build and upgrade defences when needed.
* Build a stargate if technology is available.
* If all above have been built, research.

It can be toggled on or off for each planet. You can basically enable it on any
planet not building ships and leave it untouched for most of the game. With new 
tech discoveries it will readjust the sliders automatically. This cuts down the
amount of micromanagement needed drastically.

In addition, Governor can:

* Auto-transport population.
* Auto-scout and Auto-colonize.
* Very simple auto-attack.

To run the mod:

* Download my distribution of rotp-${project.version}.jar (large file) and run that instead of 
original game. You are also welcome to try rotp-mini-${project.version}.jar which is smaller
as it uses better compression for game assets. 

or

* Download only the rotp-${project.version}-governor.jar
* Place it in same directory that contains original Remnants.jar
* Run rotp-${project.version}-governor.jar

Binary files are now built by github and available here: https://github.com/coder111111/rotp-public/releases/

To enable governor, use 'q' key on keyboard, or else click "Allocate Spending"
text in the planetary spending screen. Since version 1.8 Governor is on by default.

---

Additional features / changelog

* 4.04.0 Merge 1.04. Package Windows game with JRE v17 as that's the latest LTS release.

* 4.03.0 Merge 1.03. Since the change to increase minimum transport cost to 10BC was never implemented upstream, 
revamp auto-transport. Revert to transporting only organic population growth 1-2 at a time. And eco spending
will not spend on population growth when close to maximum population leaving room for natural growth. Also
update startup to be more robust when restart to increase memory size is needed. Re-enable "code only" small
jar packaging which is designed to run along with vanilla Remnants.jar

* 4.00.3 Merge 1.02a. Update Readme.

* 4.00.2 Merge 1.01. No other changes so far.

* 4.00.1 Merge 1.00. No other changes so far.

* 3.95.1 Merge 0.95. Added native packaging with launch4j. Removed code-only "governor" packaging.

* 3.91.2 Updated native-transform-maven-plugin

* 3.91.1 Merge v0.91. Change versioning scheme to follow upstream numbers more closely.

* 3.09.2 Fix/improve parallel ship range display. Thanks Elkad for the bug report.

* 3.09.1 Merge v0.9. Since we're no longer beta but march towards 1.0, there's a change in version numbers. I have
  changed Governor version numbers to be 3.xxx since I don't want numbers to decrease. Also, made a change to merge
  areas for ship range display on the map in parallel, which should result in some performance improvement if you have
  many cores.

* 2.16.3. Merge v2.16b Beta. Governor will not spend on defense (build shields) if missile base count is set to 0 
  or lower than already built on the planet. Autoattack will attack enemy planets which haven't been scouted yet.

* 2.15.2. Merge v2.15b Beta. Fix AutoColonize for games with restricted colonization option.

* 2.14.1. Merge v2.14 Beta. Fix AutoScout to send out armed ships from uncolonized systems as well if no enemy inbound.

* 2.13.3. Merge v2.13b Beta. Fix AutoScout to send out ships from uncolonized systems.

* 2.12.2. Merge v2.12a Beta. Add autoattack option. Make AutoScout, AutoColonize or AutoAttack number of ships 
  configurable. This allows sending several armed ships, not just one. Some tweaks to auto* features- now armed 
  ships won't be sent out if enemy fleet is incoming.

* 2.11.1. Merge v2.11 Beta

* 2.10.2. Fix typos and text (hopefully I got it right this time). Thanks Modnar!

* 2.10.1. Merge v2.10 Beta. Removed colonize prompt options from Governor options, as they are added in main settings.

* 2.09.2. Merge v2.09b Beta.

* 2.09.1. Merge v2.09 Beta. Fix icon loading.

* 2.08.3. Completionist button now really checks for certain conditions before it's enabled (fixed stupid bug). Added
  a game icon. Added option to disable/enable colonization prompts even after the game is started. Modnar- now I can
  really play your 2021 map. 

* 2.08.2. Fix full screen to really be full-screen. Add "Completionist" button for the endgame which allows all 
  empires to research certain techs like Irradiated colony base or Atmospheric Terraforming. This allows me to finish
  the game with entire galaxy full of gaia planets. If you don't like it- don't use it :)

* 2.08.1. Merge v2.08 Beta. More fair autotransport. It used to take the colony with least population, and send all
  transports to it. Now if there are two colonies with 2 population, both will get some transports. This might be slow
  for large galaxies, so please let me know if you have long end of turn processing times and turning off 
  autotransport speeds things up considerably.

* 2.07.1. Merge v2.07 Beta. Don't build ships after finishing stargate. Major refactor of autoscout/autocolonize. 
  New autotransport options for Rich/Poor planets. Change option defaults- not more features are on by default.

* 2.05.3. Minified version fixed- now game start should not crash. Fixed small exercution issue on governor only jar.

* 2.05.2. Initial support for minified version. Build and packaging fixes. Fix the eco overspending bug.

* 2.04.2. Attempts at improving github build & release process

* 2.04.1. Merge v2.04 Beta.

* 2.03.1. Merge v2.03 Beta. Fix autocolonize to colonize hostile worlds if player race is silicoids.

* 2.01.1. Merge changes on top of latest Beta2 source. Some small fixes & cleanup.

* 1.13.6. Bugfixes for autoscouting, autocolonization, autotransport. Pulled in latest changes from Ray's master 
repo (mostly bugfixes by modnar_hajile). There might be savegame compatibility problems with previous versions.

* 1.13.5. Implemented automated scouting and automated colonization. Some fixes to automated
population transport to make it more efficient and less buggy. Small fixes. Some improvements to
JSON conversion (still nowhere near finished).

* 1.13.4. Bugfix release- fix the "continue" to work correctly. Start work on savegame
to JSON conversion (not yet ready).

* 1.13.3. Added shipbuilding option. If it's turned on, governor remembers that planet was building
ships (keeps 1 tick in shipbuilding), and will resume building ships once it finishes all
the IND/ECO/DEF. If planet was not spending on shipbuilding, it keeps it on research. Also fixed
the patch (-governor) version. And fixed a potential bug with game loading.

* Added default missile base number configuration. Added automated reserve spending.
It will spend only on planets that have <30% average production. It will only spend
the amount planet can use this turn. You can set a reserve it autospend will keep
unspent. Autospend will only spend on planets that have IND or ECO unfinished. It will
spend on planets with lowest production first.

* Save game compatibility fixed in 1.10.1. (it was broken in 1.10). /u/sarlok contributed 
improvements to Governor eco/industry assignments in and more.

* Population transport is now modernized to comply with the rule changes in 1.9.
Governor Options dialog is now better and has more options for population transport.
I'm now using merge to keep the project in sync with upstream not to break the changes
made by other authors forking from me.

* Governed colonies are now shown in green in colonies list. If autotransport is on,
maximum population reached message should not be shown for governed planets and 
governor won't spend production on population growth if only 1-3 population remains 
until limit. Also, my email is shown in case of error.

* ROTP-1.11-mini.jar is now provided. It uses WebP images and Ogg Vorbis sounds.
It should have all the same features as ROTP but take up less space (~193 MB). Since
WebP library uses native parts, this will only work on Windows (32 and 64 bit),
Mac OSX 64 bit, Linux 64 bit. If you have a different system, use full-size ROTP.
On Windows, please install Microsoft Visual C++ 2015 Redistributable 
(https://www.microsoft.com/en-us/download/details.aspx?id=52685).
Please report any bugs with this (especially sounds) as it needs wider testing.

* Some problems with ROTP-mini have been fixed. I also found out that to run on 
Windows, ROTP-mini needs "vcruntime140d.dll" & "ucrtbased.dll" to run. Please get
them and place them in the same directory. This issue has been raised with WebP
library authors already: https://github.com/sejda-pdf/webp-imageio/issues/1

* Since version 1.5 governor will be on by default on new colonies.

* Governor will transport population from planets that are full to planets that
are underpopulated. Population from planets with maximum population will be 
transported. Only population that will grow back in 1 turn will be transported 
(usually 1-2 pop). When choosing destination, target population and distance will
be taken into account. 

* Governor will build stargates on Rich and Ultra Rich planets when technology is 
available.

GUI has now been added to control behaviour of the governor. Please click "Options"
next to "Allocate Spending" to go to governor options. Old system properties based
options are supported for now but will be dropped in future releases.

Governor options should be saved in your save game file.

---

# Building from source

It's a maven build. Git clone the sources, then do "mvn package" and you have entire
project built and packaged in "target" directory.

Minimized build is provided on a separate branch. Minimized assets are not committed 
to git. Minimized assets are converted during the build using "cwebp" and "oggenc" tools. 
Please make sure these are in your PATH or else the build will fail. You can find them:

https://developers.google.com/speed/webp/docs/precompiled

https://www.rarewares.org/ogg-oggenc.php

Or install them using your Linux distribution package manager.
