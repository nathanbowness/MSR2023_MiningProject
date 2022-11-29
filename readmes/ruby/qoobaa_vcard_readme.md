# Vcard [![CI](https://github.com/qoobaa/vcard/actions/workflows/ci.yml/badge.svg)](https://github.com/qoobaa/vcard/actions/workflows/ci.yml)

Vcard gem extracts Vcard support from Vpim gem.

## Installation

Add this line to your application's Gemfile:

    gem "vcard"

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install vcard

## Configuration

You can configure how to deal with invalid lines. The gem supports three behaviours:

1. `raise_on_invalid_line = true`

 Vcard::InvalidEncodingError will be raised if any invalid line is found.

2. `raise_on_invalid_line = false, ignore_invalid_vcards = true`

 If the vcard source has an invalid line, this vcard object will be ignored.
 If you have only one vcard object in your source string, an empty array will be returned from `Vcard.decode`.

3. `raise_on_invalid_line = false, ignore_invalid_vcards = false`

 If the vcard is marked as invalid, invalid fields will be ignored, but the vcard will be present in the results of `Vcard#decode`.

```
Vcard.configure do |config|
  config.raise_on_invalid_line = false # default true
  config.ignore_invalid_vcards = false # default true
end
```

## Upgrade Notes

We are no longer testing against Ruby 1.8.7.
