{<img src="https://travis-ci.org/onomojo/i18n_country_select.svg?branch=master" alt="Build Status" />}[https://travis-ci.org/onomojo/i18n_country_select]


== Country Code Select

A simple country code select helper with I18n translations for the countries. Works exactly the same as country_select but uses country codes instead and has i18n translations for the country names.

NOTE: The old country_code_select repository that this one was forked from is outdated and no longer maintained. This i18_country_select repository is the most current.

== Installation
Put the following in your Gemfile

  gem 'i18n_country_select'

== Example
Simple use supplying model and attribute as parameters:

  country_code_select(:user, :country)

Supplying priority countries to be placed at the top of the list:

  country_code_select(:user, :country, [[ 'US', 'United States' ], [ 'CA', 'Canada' ]])

Specifying different selected value:

  country_code_select(:user, :country, [], selected: 'CA')


Based on the deprecated country_code_select by: Russ Smith (russ@bashme.org) and Frank Wambutt (frank@mo-stud.io)


== License

MIT or GPL
