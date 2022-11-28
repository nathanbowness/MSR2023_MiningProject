English [Français](README-fr.md)

# Fanfix

Fanfix is a small Java program that can download stories from some supported websites and render them offline.

## 🔴 This is the command line and server program

You can also use:
- the graphical client [Fanfix-swing](https://github.com/nikiroo/fanfix-swing/)
- the TUI client [Fanfix-jexer](https://github.com/nikiroo/fanfix-jexer/)

## Synopsis

- ```fanfix``` --import [*URL*]
- ```fanfix``` --export [*id*] [*output_type*] [*target*]
- ```fanfix``` --convert [*URL*] [*output_type*] [*target*] (+info)
- ```fanfix``` --read [*id*] ([*chapter number*])
- ```fanfix``` --read-url [*URL*] ([*chapter number*])
- ```fanfix``` --search
- ```fanfix``` --search [*where*] [*keywords*] (page [*page*]) (item [*item*])
- ```fanfix``` --search-tag
- ```fanfix``` --search-tag [*index 1*]... (page [*page*]) (item [*item*])
- ```fanfix``` --list
- ```fanfix``` --server [*key*] [*port*]
- ```fanfix``` --stop-server [*key*] [*port*]
- ```fanfix``` --remote [*key*] [*host*] [*port*]
- ```fanfix``` --help

## Description

(If you are interested in the recent changes, please check the [Changelog](changelog.md) -- note that starting from version 1.4.0, the changelog is checked at startup.)

This program will convert from a (supported) URL to an .epub file for stories or a .cbz file for comics (a few other output types are also available, like Plain Text, LaTeX, HTML...).

To help organize your stories, it can also work as a local library so you can:

- Import a story from its URL (or just from a file)
- Export a story to a file (in any of the supported output types)
- Display a story from the local library in text format in the console
- Via [fanfix-swing](https://github.com/nikiroo/fanfix-swing/): Display a story from the local library graphically **by itself** ([fanfix-swing](https://github.com/nikiroo/fanfix-swing/)) or **by calling a native program to handle it** (potentially converted into HTML before hand, so any browser can open it)

### Supported websites

Currently, the following websites are supported:

- http://FimFiction.net/: fan fictions devoted to the My Little Pony show
- http://Fanfiction.net/: fan fictions of many, many different universes, from TV shows to novels to games
- http://mangahub.io/: a well filled repository of mangas (English)
- https://e621.net/: a Furry website supporting comics, including MLP
- https://sofurry.com/: same thing, but story-oriented
- https://e-hentai.org/: done upon request (so, feel free to ask for more websites!)
- http://mangas-lecture-en-ligne.fr/: a website offering a lot of mangas (in French)

### Support file types

We support a few file types for local story conversion (both as input and as output):

- epub: .epub files created by this program (we do not support "all" .epub files, at least for now)
- text: local stories encoded in plain text format, with a few specific rules:
	- the title must be on the first line
	- the author (preceded by nothing, ```by ``` or ```©```) must be on the second line, possibly with the publication date in parenthesis (i.e., ```By Unknown (3rd October 1998)```)
	- chapters must be declared with ```Chapter x``` or ```Chapter x: NAME OF THE CHAPTER```, where ```x``` is the chapter number
	- a description of the story must be given as chapter number 0
	- a cover image may be present with the same filename as the story, but a .png, .jpeg or .jpg extension
- info_text: contains the same information as the text format, but with a companion .info file to store some metadata (the .info file is supposed to be created by Fanfix or compatible with it)
- cbz: .cbz (collection of images) files, preferably created with Fanfix (but any .cbz file is supported, though without most of Fanfix metadata, obviously)
- html: HTML files that you can open with any browser; note that it will create a directory structure with ```index.html``` as the main file -- we only support importing HTML files created by Fanfix

### Supported platforms

Any platform with at lest Java 1.6 on it should be ok.

It has been tested on Linux (Debian, Slackware, Ubuntu), MacOS X and Windows for now, but feel free to inform us if you try it on another system.

If you have any problems to compile it with a supported Java version (1.6+), please contact us.

## Options

You can start the program in two ways:

- ```java -jar fanfix.jar```
- ```fanfix``` (if you used *make install*)

The following arguments are allowed:

- ```--import [URL]```: import the story at URL into the local library
- ```--export [id] [output_type] [target]```: export the story denoted by ID to the target file
- ```--convert [URL] [output_type] [target] (+info)```: convert the story at URL into target, and force-add the .info and cover if +info is passed
- ```--read [id] ([chapter number])```: read the given story denoted by ID from the library
- ```--read-url [URL] ([chapter number])```: convert on the fly and read the story at URL, without saving it
- ```--search```: list the supported websites (```where```)
- ```--search [where] [keywords] (page [page]) (item [item])```: search on the supported website and display the given results page of stories it found, or the story details if asked
- ```--tag [where]```: list all the tags supported by this website
- ```--tag [index 1]... (page [page]) (item [item])```: search for the given stories or subtags, tag by tag, and display information about a specific page of results or about a specific item if requested
- ```--list```: list the stories present in the library and their associated IDs
- ```--server [key] [port]```: start a story server on this port
- ```--stop-server [key] [port]```: stop the remote server running on this port (key must be set to the same value)
- ```--remote [key] [host] [port]```: contact this server instead of the usual library (key must be set to the same value)
- ```--help```: display the available options
- ```--version```: return the version of the program

### Environment

Some environment variables are recognized by the program:

- ```LANG=en```: force the language to English
- ```CONFIG_DIR=$HOME/.fanfix```: use the given directory as a config directory (and copy the default configuration if needed)
- ```NOUTF=1```: try to fallback to non-unicode values when possible (can have an impact on the resulting files, not only on user messages)
- ```DEBUG=1```: force the ```DEBUG=true``` option of the configuration file (to show more information on errors)

## Compilation

```./configure.sh && make```

You can also import the java sources into, say, [Eclipse](https://eclipse.org/), and create a runnable JAR file from there.

There are some unit tests you can run, too:

```./configure.sh && make build test run-test```

If you run the unit tests, note that some flag files can impact them:

- ```test/VERBOSE```      : enable verbose mode
- ```test/OFFLINE```      : to forbid any downloading
- ```test/URLS```         : to allow testing URLs
- ```test/FORCE_REFRESH```: to force a clear of the cache

Note that ```test/CACHE``` can be kept, as it will contain all internet related files you need (if you allow URLs, run the test once which will populate the CACHE then go OFFLINE, it will still work).

The test files will be:

- ```test/*.url```  : URL to download in text format, content = URL
- ```test/*.story```: text mode story, content = story


### Dependant libraries (included)

Required:

- ```libs/nikiroo-utils-sources.jar```: some shared utility functions
- [```libs/unbescape-sources.jar```](https://github.com/unbescape/unbescape): a nice library to escape/unescape a lot of text formats; used here for HTML
- [```libs/jsoup-sources.jar```](https://jsoup.org/): a library to parse HTML
- [```libs/JSON-java-20190722-sources.jar```](https://github.com/stleary/JSON-java): a library to parse JSON

Optional:

- [```libs/jexer-sources.jar```](https://github.com/klamonte/jexer): a small library that offers TUI widgets
- [```pandoc```](http://pandoc.org/): to generate the man pages from the README files

Nothing else but Java 1.6+.

Note that calling ```make libs``` will export the libraries into the src/ directory.

## Author

Fanfix was written by Niki Roo <niki@nikiroo.be>

