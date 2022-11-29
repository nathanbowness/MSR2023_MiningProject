= minitest-ci

{<img src="https://circleci.com/gh/circleci/minitest-ci.svg?style=svg" alt="Circle CI" />}[https://circleci.com/gh/circleci/minitest-ci]

* https://github.com/circleci/minitest-ci

== DESCRIPTION:

Minitest reporter plugin for CircleCI[https://circleci.com/].

This gem was made possible by YP.com

Records test results and generates XML files at the end of the test run.

These results can be plugged into, for example, Hudson or Jenkins.
This format is also the default used by CircleCI.

== USAGE:

In order to use this gem, add it to your Gemfile:

    gem "minitest-ci"

To make integration with CircleCI easier, make sure you have a ":test" task defined.
You can do this by simply adding the following to your Rakefile:

    require 'rake/testtask'

    Rake::TestTask.new do |t|
      t.pattern = "test/test_*.rb"
    end

    task :default => :test

You should be on your way to continuous testing with Minitest and CircleCI!

For more complicated setups, see below.

=== Custom setup

To configure the test output folder, use the "--ci-dir=" option, setting it in
TESTOPTS.  On CircleCI, you might want to use something like this in your
circle.yml:

    machine:
      environment:
        TESTOPTS: "--ci-dir=$CIRCLE_TEST_REPORTS/reports"
    test:
      override:
        - bundle exec rake test:
            parallel: true
            files:
              - test/**/*.rb

Alternatively, you can add the following code to your test runner setup:

    # test/helper.rb
    require 'minitest'
    require 'minitest/autorun'
    require 'minitest/ci'

    if ENV["CIRCLECI"]
      Minitest::Ci.report_dir = "#{ENV["CIRCLE_TEST_REPORTS"]}/reports"
    end

    class MiniTest::Test
      # include other helpers, etc
    end


**NOTE**: The report directory is cleaned between test runs. To disable:

    # test/helper.rb
    Minitest::Ci.clean = false

    # Rakefile (optional, but recommended)
    task :ci_cleanup do
      require 'minitest/ci'
      Minitest::Ci.new.start
    end
    task :test => %w[ci_cleanup test:one test:two]

To configure report filename, use the `report_name` option like

    Minitest::Ci.new $ci_io, { :report_name => :sha1 }

or like

    machine:
      environment:
        TESTOPTS: "--report-name=sha1"

Supported options are: `:test_name` (default), `:sha1`, or a `Proc` (not supported through ENV var)

== REQUIREMENTS:

* Minitest > version 5
