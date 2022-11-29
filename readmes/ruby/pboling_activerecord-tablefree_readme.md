ActiveRecord Tablefree
======================

| Project                 |  ActiveRecord Tablefree |
|------------------------ | ----------------------- |
| gem name                |  [activerecord-tablefree](https://rubygems.org/gems/activerecord-tablefree) |
| license                 |  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)                    |
| download rank           |  [![Downloads Today](https://img.shields.io/gem/rd/activerecord-tablefree.svg)](https://github.com/pboling/activerecord-tablefree) |
| version                 |  [![Version](https://img.shields.io/gem/v/activerecord-tablefree.svg)](https://rubygems.org/gems/activerecord-tablefree) |
| dependencies            |  [![Depfu](https://badges.depfu.com/badges/96a4d507f1a61a9368655f60fa3cb70f/count.svg)](https://depfu.com/github/pboling/activerecord-tablefree?project=Bundler) |
| continuous integration  |  [![Build Status](https://travis-ci.org/pboling/activerecord-tablefree.svg?branch=master)](https://travis-ci.org/pboling/activerecord-tablefree) |
| test coverage           |  [![Test Coverage](https://api.codeclimate.com/v1/badges/9354ad73daf12d480e81/test_coverage)](https://codeclimate.com/github/pboling/activerecord-tablefree/test_coverage) |
| maintainability         |  [![Maintainability](https://api.codeclimate.com/v1/badges/9354ad73daf12d480e81/maintainability)](https://codeclimate.com/github/pboling/activerecord-tablefree/maintainability)
| code triage             |  [![Open Source Helpers](https://www.codetriage.com/pboling/activerecord-tablefree/badges/users.svg)](https://www.codetriage.com/pboling/activerecord-tablefree) |
| homepage                |  [http://www.railsbling.com/tags/activerecord-tablefree/][homepage] |
| documentation           |  [http://rdoc.info/github/pboling/activerecord-tablefree/frames][documentation] |
| Spread ~♡ⓛⓞⓥⓔ♡~      |  [🌏](https://about.me/peter.boling), [👼](https://angel.co/peter-boling), [:shipit:](http://coderwall.com/pboling), [![Tweet Peter](https://img.shields.io/twitter/follow/galtzo.svg?style=social&label=Follow)](http://twitter.com/galtzo), [🌹](https://nationalprogressiveparty.org) |

A simple implementation of the ActiveRecord Tableless pattern for any
Rails project or other Ruby project that uses ActiveRecord.

Why, why, why
-------------

Why would you ever consider this gem as opposed to ActiveModel?

ActiveModel::Model does not support relations and nested attributes.


Installation
------------

ActiveRecord Tablefree is distributed as a gem, which is how it should
be used in your app.

Include the gem in your Gemfile:

    gem "activerecord-tablefree", "~> 3.0"


Supported Versions
------------------

Supported ruby version are

  * **2.2.x** series higher than 2.2.2 (a Rails 5 requirement)
  * **2.3.x** series
  * **2.4.x** series
  * **2.5.x** series

Supported ActiveRecord versions are

  * **5.0.x** series
  * **5.1.x** series
  * **5.2.x** series

If you are using an older ActiveRecord version you can use the gem [`activerecord-tableless`](https://github.com/softace/activerecord-tableless)

This gem tries to maintain the same API as the older `activerecord-tableless` gem.

Usage
-----

Define a model like this:

    class ContactMessage < ActiveRecord::Base
      has_no_table
      column :name, :string
      column :email, :string
      column :message, :string
      validates_presence_of :name, :email, :message
    end

You can now use the model in a view like this:

    <%= form_for :contact_message, @contact_message do |f| %>
      Your name: <%= f.text_field :name %>
      Your email: <%= f.text_field :email %>
      Your message: <%= f.text_field :message %>
    <% end %>

And in the controller:

    def contact_message
      @contact_message = ContactMessage.new
      if request.post?
        @contact_message.attributes = params[:contact_message]
        if @contact_message.valid?
          # Process the message...
        end
      end
    end

If you wish (this is not recommended), you can pretend you have a succeeding database by using

    has_no_table :database => :pretend_success

Associations
------------

Some model as before, but with an association to a real DB-backed model.

```
    class ContactMessage < ActiveRecord::Base
      has_no_table
      column :message, :string
      column :email, :string
      validates_presence_of :name, :email
      belongs_to :contact, foreign_key: :email, primary_key: :email
    end

    class Contact < ActiveRecord::Base
      validates_presence_of :name, :email
      has_one :contact_message, foreign_key: :email, primary_key: :email, dependent: nil
    end
```

Obviously the association is not full-fledged, as some traversals just won't make sense with one side not being loadable from the database.  From the `ContactMessage` you can get to the `Contact`, but not vice versa.

```
>> contact = Contact.new(name: 'Boo', email: 'boo@example.com')
>> contact_message = ContactMessage.new(contact: contact)
>> contact_message.email
=> 'boo@example.com'
```

Development
-----------

To start developing, please download the source code

    git clone git://github.com/pboling/activerecord-tablefree.git

Install development libraries

    sudo apt-get install -y libsqlite3-dev libxml2-dev libxslt-dev

When downloaded, you can start issuing the commands like

    bundle install
    bundle update
    bundle exec appraisal generate
    bundle exec appraisal install
    bundle exec appraisal rake all

Or you can see what other options are there:

    bundle exec rake -T

Publishing gem
--------------

```
gem bump -v pre
```

Verify everything is OK.

```
gem build activerecord-tablefree.gemspec
```

Verify everything is OK.

```
gem release -t
```


History
-------

Originally this code was implemented for Rails 2 by Kenneth
Kalmer. For Rails 3 the need for this functionality was reduced
dramatically due to the introduction of ActiveModel. But because the
ActiveModel does not support relations and nested attributes the
existence of this gem is still justified.

Rails 3 and 4 support is provided in the [activerecord-tableless gem](https://github.com/softace/activerecord-tableless), by [Jarl Friis](https://github.com/jarl-dk).

This gem is a Rails 5+ compatible update, and renaming of that gem.

For a history of technical implementation details feel free to take a
look in the git log :-)

## Versioning

This library aims to adhere to [Semantic Versioning 2.0.0][semver].
Violations of this scheme should be reported as bugs. Specifically,
if a minor or patch version is released that breaks backward
compatibility, a new version should be immediately released that
restores compatibility. Breaking changes to the public API will
only be introduced with new major versions.

As a result of this policy, you can (and should) specify a
dependency on this gem using the [Pessimistic Version Constraint][pvc] with two digits of precision.

For example:

```ruby
spec.add_dependency 'activerecord-tablefree', '~> 3.0'
```

Copyright
---------

* Copyright (c) 2008 - 2009 Kenneth Kalmer
* Copyright (c) 2012 - 2017 Jarl Friis
* Copyright (c) 2017 - 2018 [Peter H. Boling][peterboling] of [Rails Bling][railsbling]

The license is MIT.  See [LICENSE.txt][license] for further details.

[license]: LICENSE.txt
[semver]: http://semver.org/
[pvc]: http://guides.rubygems.org/patterns/#pessimistic-version-constraint
[railsbling]: http://www.railsbling.com
[peterboling]: http://www.peterboling.com
[documentation]: http://rdoc.info/github/pboling/activerecord-tablefree/frames
[homepage]: http://www.railsbling.com/tags/activerecord-tablefree/
