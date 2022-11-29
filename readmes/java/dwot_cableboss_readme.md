CableBoss
===========

This is a forked version of [vlcj-player](https://github.com/caprica/vlcj-player) with an embedded discord bot.

This bot listens for commands from discord messages to search for and playback 
media in a Plex library or playback a youtube video and stream this on discord.

This is done with a dedicated PC using a dedicated discord (non-bot) user and using AutoHotKey scripts to 
join channels & start / stop streaming.

It's wonky frankenstein of a thing.  It is severely limited without official support for streaming from discord bots.

To get this to work

- You'll need a Spare PC to run as your Player w/
    - Discord established, logged in and running, joined to your target server, with appropriate permissions
    - AutoHotKey installed
    - OpenJDK installed (https://adoptopenjdk.net/)
    - MouseJiggler (to keep from getting AFK'd out)

1. Establish a Bot with discord via https://discord.com/developers/applications (https://discordjs.guide/preparations/setting-up-a-bot-application.html)
2. Join your bot to a server with read/write message access (https://discordjs.guide/preparations/adding-your-bot-to-servers.html)
3. Build with maven package, grab the vlcj-player-2.0.0-SNAPSHOT-dist.zip.
4. Unzip to location on the Player PC. This will unpack the vlcj jars as well as all the dependency jars. 
5. Copy ahkScripts from source to somewhere on path (should add to build and dist)
6. Create a vlcj.properties file, see vlcj.properties.example
7.  Run VLCJ via bat file ```java "-DVLCJ_PROP_FILE=vlcj.properties" -jar "vlcj-player-2.0.0-SNAPSHOT-shaded.jar" ```
     Fully qualify the paths to the jar and properties if they give you grief.
8. VLCJ takes a minute or so to become reponsive (via GUI) this seems normal, let it do it's thing.
9. Establish a keybind in discord on the player for Toggle Screen Share, set this to Ctrl+Shift+G (hardcoded in AHK
    script, can change there).
10. Under Game Activity in Discord click "Not seeing your game? Add It!" and add vlcj-player so it is detected and the
    hot key for streaming is enabled.

Provided that all worked and I didn't miss anything you should now have a Discord Bot controlled Discord video streamer. 
