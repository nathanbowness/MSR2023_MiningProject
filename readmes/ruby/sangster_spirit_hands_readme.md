# Spirit Hands

This repo is an improved fork with real configuration syntax, with updates and bug fixes based on [`jazz_hands`](https://github.com/nixme/jazz_hands).

Spending hours in the rails console? Spruce it up and show off those
hard-working hands!

**spirit_hands** is an opinionated set of console-related gems and a bit of glue:

* [**Pry**][pry] for a powerful shell alternative to IRB.
* [**Awesome Print**][awesome_print] for stylish pretty print.
* [**Hirb**][hirb] for tabular collection output.
* [**Hirb Unicode**][hirb-unicode-steakknife] for aligned Unicode output.
* [**Pry Rails**][pry-rails] for additional commands (`show-routes`,
  `show-models`, `show-middleware`) in the Rails console.
* [**Pry Doc**][pry-doc] to browse Ruby source, including C, directly from the
  console.
  commits on methods and classes, not just files. (non-JRuby only)
* [**Pry Remote**][pry-remote] to connect remotely to a Pry console.
* [**Pry Coolline**][pry-coolline] for syntax highlighting as you type.
* **Debugging** (`next`, `step`, ...): Ruby (MRI) [**Pry Byebug**][pry-byebug], JRuby [**Pry Nav**][pry-nav].


## Usage

### Rails or Ruby Project Integration

Ruby 2.0.0+, Rails 3, 4 or 5 Ruby project, add this to your project Gemfile:

```ruby
group :development, :test do
  gem 'spirit_hands'
end
```

### Global usage
 `[sudo] gem install spirit_hands`

That's it. Run `rails console` as usual.

Ruby compiled against a proper readline library, ideally GNU readline, is
recommended. Alternatively, [`gem install rb-readline`][rb-readline] for an
acceptible backup. Using ruby compiled against a `libedit` wrapper (primarily OS
X) will work but is not recommended.


## Options

Change the following options by creating a .pryrc  in your Rails or Ruby project

### Example `.pryrc`

```ruby
begin
  require 'spirit_hands'
  SpiritHands.colored_prompt = false
  SpiritHands.hirb = false
rescue LoadError => e
  raise unless e.message =~ /.*such file.*spirit_hands/
  puts 'no SpiritHands'  
end
```

### `awesome_print`

[**AwesomePrint**][awesome_print] is enabled by default.
`SpiritHands.awesome_print = false` to disable.

### `color`

An alias for getting and setting `Pry.color`

### `colored_prompt`

Color the console prompt? Defaults to `true` when the current ruby is compiled
against GNU readline or `rb-readline`, which don't have issues counting
characters in colored prompts. `false` for libedit.

**Note:** `Pry.color = false` trumps this setting and disables all console coloring.

### `coolline`

Control whether pry-coolline is activated.

~~Cooline is **enabled** by default.~~

**NOTE** Pry-coolline is *currently disabled* by default because it doesn't support full Readline Vi and Emacs emulation. If you really want live syntax highlighting anyhow without full Readline support, specify `SpiritHands.coolline=true` in `~/.pryrc` after `require 'spirit_hands'`. Also, consider contributing a coolline/pry-coolline PR/fork if you must have this functionality.

### `hirb`
[**Hirb**][hirb] is **enabled** by default.
`SpiritHands.hirb = false` to disable.

### `hirb_unicode`
[**Hirb-unicode**][hirb-unicode-steakknife] is enabled by default when hirb is enabled.
`SpiritHands.hirb_unicode = false` to disable.  
No effect when hirb is disabled.


### `prompt`

#### Pseudo-XML-like Syntax as follows

```
   current command number <cmd/>
   app name               <app/>

   literal less-than <    \<     ( "\\<" in Ruby strings )
   bold                   <bold>....<bold>

   Foreground color:

   black                 <black>...</black>
   and red green yellow blue magenta cyan white

   Background color:

   bgblack bgred bggreen bgyellow bgblue bgmagenta bgcyan bgwhite

   Even the frightening blink tag, where available <blink>...</blink>

More at: SpiritHands::Prompt::Render::MATCHED_TAG_CODES.keys

```

### `prompt_separator`

Separator string between the application name and line input. Defaults to `»`
for GNU readline or libedit. Defaults to `>` for `rb-readline` which fails on
mixed encodings.


[pry]:                      http://pry.github.com
[awesome_print]:            https://github.com/michaeldv/awesome_print
[hirb]:                     https://github.com/cldwalker/hirb
[hirb-unicode-steakknife]:  https://github.com/steakknife/hirb-unicode
[pry-rails]:                https://github.com/rweng/pry-rails
[pry-doc]:                  https://github.com/pry/pry-doc
[pry-remote]:               https://github.com/Mon-Ouie/pry-remote
[pry-coolline]:             https://github.com/pry/pry-coolline
[coderay]:                  https://github.com/rubychan/coderay
[rb-readline]:              https://github.com/luislavena/rb-readline
[pullrequests]:             https://github.com/steakknife/spirit_hands/pulls
[issues]:                   https://github.com/steakknife/spirit_hands/issues
[changelog]:                https://github.com/steakknife/spirit_hands/blob/master/CHANGELOG.md
[pry-nav]:                  https://github.com/nixme/pry-nav
[pry-byebug]:               https://github.com/deivid-rodriguez/pry-byebug

### Security

```
$ gem cert --add <(curl -Ls https://raw.githubusercontent.com/steakknife/spirit_hands/master/gem-public_cert.pem)
$ gem install spirit_hands -P MediumSecurity
```
