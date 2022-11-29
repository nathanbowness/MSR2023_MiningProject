# StaticMatic: Build and Deploy

1: Build static websites using modern dynamic tools:

- [Haml](http://haml-lang.com/)
- [Sass](http://sass-lang.com/)
- [Coffeescript](http://jashkenas.github.com/coffee-script/)
- [Compass](compass-style.org)
- [Amazon S3 Websites](http://aws.typepad.com/aws/2011/02/host-your-static-website-on-amazon-s3.html)
- [And many, many more!](https://github.com/rtomayko/tilt#readme)

2: Deploy to Amazon S3:

    $ staticmatic s3_deploy

3: Profit (due to low hosting fees :P)

## In other words:

                    StaticMatic build                   StaticMatic deploy
    src/                    ==>           build/                ==>           mywebsite.com/
      index.haml            ==>             index.html          ==>             index.html
      style.sass            ==>             style.css           ==>             style.css
      js/                   ==>             js/                 ==>             js/
        app.coffee          ==>               app.js            ==>               app.js
      img/                  ==>             img/                ==>             img/
        logo.png            ==>               logo.png          ==>               logo.png

# Getting Started

    $ gem install staticmatic2

## Quick Start

Setup a new project:

    $ staticmatic init my-project

This will give you a basic skeleton:

    my-project/
      src/
        _layouts/
          default.haml
        _partials/
          example.haml
        index.haml

Preview your static website:

    $ cd my-project
    $ staticmatic preview
    Site root is: .
    StaticMatic Preview Server
    Ctrl+C to exit
    ...

Visit http://localhost:4000 to view your website in action.

To build & convert your haml/sass/whatever files into plain html, css, and javascript:

    $ staticmatic build
    
This will convert everything into a freshly generated `build/` folder, 100% static.

If you have an [Amazon S3 account](http://aws.amazon.com/s3/) and want to deploy to your bucket, run the following command:

    # NOTE: You must be in the root folder of your project
    $ staticmatic s3_deploy

If you haven't deployed your current project to Amazon yet, it will prompt you to create a config file. Edit this file to include your credentials, run the command again, and you're set.

## Super Special Awesome Quick Start Booster

Want to use a [Javascript App Starter](https://github.com/mindeavor/staticmatic-js-app-starter) or a skeleton of your own? Check this out!

    $ staticmatic add js-app git://github.com/mindeavor/staticmatic-js-app-starter.git
    $ staticmatic init my-new-project --skeleton=js-app

The first line stores a named reference to a repository of your choosing. You only need to do this once.

The second line clones the referenced repository into a freshly created `my-new-project` folder, as well as removes the `.git/` folder so you can do your own `git init`. Convenient!

## Special Folders

    <my-project>/
      src/
        _helpers/
        _layouts/
        _partials/

- The `_helpers` folder is where you place your custom Haml helpers

- The `_layouts` folder is where layout files will be searched for. These files must contain a `yield` statement.

- The `_partials` folder is the last place partial files will be searched for. Any partial in this folder should not be prefixed with an underscore _

*USEFUL:* Any file or folder prefixed with an underscore _ will not be copied into the generated `site/` folder, nor will they be converted by haml, coffeescript, etc

## Partials

Partials are searched for in the following order:

- The file's current directory (the file must be prefixed with an underscore in this case)
- `src/_partials/`

Examples:

    # Searches for the default rendering engine file type (by default, it is haml)
    = partial 'sidebar'
    
    # Equivalent to the above statement
    = partial 'sidebar.haml'
    
    # Directly inserts html file
    = partial 'help-content.html'
    
    # Use your own directory structure
    = partial 'blog-content/2011/vacation.markdown'

## Anti-Cache

Force the browser to ignore its cache whenever you damn well feel like it:

    # Creates a query string based on the current unix time
    stylesheets :menu, :form, :qstring => true
    
    <link href="/css/menu.css?_=1298789103" media="all" rel="stylesheet" type="text/css"/>
    <link href="/css/form.css?_=1298789103" media="all" rel="stylesheet" type="text/css"/>
    
    
    # Or, use your own qstring
    javascripts :app, :qstring => '2.0.6'

    <script language="javascript" src="js/app.js?_=2.0.6" type="text/javascript"></script>

## SSL support

To enable SSL support, add the following lines to configuration/site.rb file:
    
    require 'webrick/https'
    configuration.ssl_enable = true
    configuration.ssl_private_key_path = "/path/to/key.pem"
    configuration.ssl_certificate_path = "/path/to/cert.pem"

# Roadmap / TODO list

- Fix slowness of executable (built on [Thor](https://github.com/wycats/thor); maybe reconsider?)
- Create a cache that monitors what files have changed in between Amazon S3 uploads to reduce unnecessary uploads
- Integrate sprockets both for building and for previewing (probably as an option flag)
- Change rendering and yielding syntax to rails syntax
- Create a command that converts a staticmatic project to a rails project

[![endorse](http://api.coderwall.com/mindeavor/endorse.png)](http://coderwall.com/mindeavor)
