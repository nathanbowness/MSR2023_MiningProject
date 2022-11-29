# Compact Language Detection 2.0

[![Gem Version](https://badge.fury.io/rb/cld2.svg)](http://badge.fury.io/rb/cld2)

![image](https://circleci.com/gh/BanjoInc/cld2.png?circle-token=6e9c5831521447a5005be3f4d33a221e9d2ae1d4)

Based on Jason Toy's CLD v1.0.
Blazing-fast language detection for Ruby provided by Google Chrome's [Compact Language Detector v2.0](https://github.com/CLD2Owners/cld2)

## How to Use

```ruby
CLD.detect_language("plus ça change, plus c'est la même chose")
# => {:lang_id=>4, :code=>"fr", :name=>"FRENCH", :reliable=>true}

Summary result: also return up to 3 top languages detected for the document and their respective scores, as well as individual results for each chunk from the input text.
CLD.detect_language_summary("How much wood would a woodchuck chuck")
# => {:lang_id=>0, :name=>"ENGLISH", :code=>"en", :reliable=>true, :top_langs=>[{:lang_id=>0, :code=>"en", :name=>"ENGLISH", :percent=>97, :score=>943.0}], :chunks=>[{:lang_id=>26, :code=>"un", :name=>"Unknown", :content=>"How much wood would a woodchuck chuck"}]}

CLD.detect_language_summary("हैदराबाद उच्चार ऐका सहाय्य माहिती तेलुगू హైదరాబాదు حیدر آباد")
# => {:lang_id=>64, :name=>"MARATHI", :code=>"mr", :reliable=>true, :top_langs=>[{:lang_id=>64, :code=>"mr", :name=>"MARATHI", :percent=>69, :score=>387.0}, {:lang_id=>44, :code=>"te", :name=>"TELUGU", :percent=>18, :score=>1024.0}], :chunks=>[{:lang_id=>64, :code=>"mr", :name=>"MARATHI", :content=>"हैदराबाद उच्चार ऐका सहाय्य माहिती तेलुगू "}, {:lang_id=>44, :code=>"te", :name=>"TELUGU", :content=>"హైదరాబాదు "}, {:lang_id=>26, :code=>"un", :name=>"Unknown", :content=>"حیدر آباد"}]}}
```

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'cld2', require 'cld'
```

And then execute:

```sh
$ bundle
```

## Thanks

Thanks to the Chrome authors, and to Mike McCandless for writing a Python version.
Thanks to Jason Toy for the original cld v1.0 ruby port.

Licensed the same as Chrome.
