h1. Thinking Sphinx

Thinking Sphinx is a library for connecting ActiveRecord to the Sphinx full-text search tool, and integrates closely with Rails (but also works with other Ruby web frameworks). The current release is v5.4.0.

h2. Upgrading

Please refer to "the changelog":https://github.com/pat/thinking-sphinx/blob/develop/CHANGELOG.markdown and "release notes":https://github.com/pat/thinking-sphinx/releases for any changes you need to make when upgrading. The release notes in particular are quite good at covering breaking changes and more details for new features.

The documentation also has more details on what's involved for upgrading from "v4 to v5":https://freelancing-gods.com/thinking-sphinx/v5/upgrading.html, "v3 to v4":https://freelancing-gods.com/thinking-sphinx/v4/upgrading.html, and "v1/v2 to v3":https://freelancing-gods.com/thinking-sphinx/v3/upgrading.html.

h2. Installation

It's a gem, so install it like you would any other gem. You will also need to specify the mysql2 gem if you're using MRI, or jdbc-mysql if you're using JRuby:

<pre><code>gem 'mysql2',          '~> 0.4',    :platform => :ruby
gem 'jdbc-mysql',      '~> 5.1.35', :platform => :jruby
gem 'thinking-sphinx', '~> 5.4'</code></pre>

The MySQL gems mentioned are required for connecting to Sphinx, so please include it even when you're using PostgreSQL for your database.

You'll also need to install Sphinx - this is covered in "the extended documentation":https://freelancing-gods.com/thinking-sphinx/installing_sphinx.html.

h2. Usage

Begin by reading the "quick-start guide":https://freelancing-gods.com/thinking-sphinx/quickstart.html, and beyond that, "the documentation":https://freelancing-gods.com/thinking-sphinx/ should serve you pretty well.

h2. Requirements

The current release of Thinking Sphinx works with the following versions of its dependencies:

|_. Library |_. Minimum |_. Tested Against |
| Ruby | v2.4 | v2.4, v2.5, v2.6, v2.7, v3.0 |
| Sphinx | v2.2.11 | v2.2.11, v3.3.1 |
| Manticore | v2.8 | v3.5, v4.0 |
| ActiveRecord | v4.2 | v4.2..v7.0 |

It _might_ work with older versions of Ruby, but it's highly recommended to update to a supported release.

It should also work with JRuby, but the test environment for that in CI has been unreliable, hence that's not actively tested against at the moment.

h3. Sphinx or Manticore

If you're using Sphinx, v2.2.11 is recommended even though it's quite old, as it works well with PostgreSQL databases (but if you're using MySQL - or real-time indices - then v3.3.1 should also be fine).

If you're opting for Manticore instead, v2.8 or newer works, but v3 or newer is recommended as that's what is actively tested against.

h3. Rails and ActiveRecord

Currently Thinking Sphinx is built to support Rails/ActiveRecord 4.2 or newer. If you're using Sinatra and ActiveRecord instead of Rails, that's fine - just make sure you add the @:require => 'thinking_sphinx/sinatra'@ option when listing @thinking-sphinx@ in your Gemfile.

If you want ActiveRecord 3.2-4.1 support, then refer to the 4.x releases of Thinking Sphinx. Or, for ActiveRecord 3.1 support, then refer to the 3.0.x releases. Anything older than that, then you're stuck with Thinking Sphinx v2.x (for Rails/ActiveRecord 3.0) or v1.x (Rails 2.3). Please note that these older versions are no longer actively supported.

h3. Ruby

You'll need either the standard Ruby (v2.4 or newer) or JRuby (9.1 or newer).

h3. Database Versions

MySQL 5.x and Postgres 8.4 or better are supported.

h2. Contributing

Please note that this project has a "Contributor Code of Conduct":http://contributor-covenant.org/version/1/0/0/. By participating in this project you agree to abide by its terms.

To contribute, clone this repository and have a good look through the specs - you'll notice the distinction between acceptance tests that actually use Sphinx and go through the full stack, and unit tests (everything else) which use liberal test doubles to ensure they're only testing the behaviour of the class in question. I've found this leads to far better code design.

All development is done on the @develop@ branch; please base any pull requests off of that branch. Please write the tests and then the code to get them passing, and send through a pull request.

In order to run the tests, you'll need to create a database named @thinking_sphinx@:

<pre><code># Either fire up a MySQL console:
mysql -u root
# OR a PostgreSQL console:
psql
# In that console, create the database:
CREATE DATABASE thinking_sphinx;</code></pre>

You can then run the unit tests with @rake spec:unit@, the acceptance tests with @rake spec:acceptance@, or all of the tests with just @rake@. To run these with PostgreSQL, you'll need to set the @DATABASE@ environment variable accordingly:

<pre><code>DATABASE=postgresql rake</code></pre>

h2. Licence

Copyright (c) 2007-2021, Thinking Sphinx is developed and maintained by Pat Allan, and is released under the open MIT Licence. Many thanks to "all who have contributed patches":https://github.com/pat/thinking-sphinx/contributors.
