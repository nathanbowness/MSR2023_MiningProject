# MassiveSitemap [![](http://travis-ci.org/rngtng/massive_sitemap.png)](http://travis-ci.org/rngtng/massive_sitemap) [![massive_sitemap Documentation](https://www.omniref.com/ruby/gems/massive_sitemap.png)](https://www.omniref.com/ruby/gems/massive_sitemap)

Build painfree sitemaps for websites with millions of pages

MassiveSitemap is a successor project of [BigSitemap](https://github.com/alexrabarts/big_sitemap), a [Sitemap](http://sitemaps.org) generator for websites with millions of pages.
It implements various generation stategies, e.g. to split large Sitemaps into multiple files, gzip files to minimize bandwidth usage, or incremental updates. Its API is very similar to _BigSitemap_, can be set up with just a few lines of code and is compatible with just about any framework.


## Usage

A simple usecase which fits most of the standard scenarios. This example adds `http://test.com/about` to the sitemap.


```ruby
require 'massive_sitemap'

index_url = MassiveSitemap.generate(:url => 'test.com') do
  add "/about"
end
MassiveSitemap.ping(index_url)

```

### Using Rails  (ActiveRecord)

This example itterates of the `User` resource and adds each with a `change_frequency`, `last_modified` and `priority` to the sitemap. In case there are more than 50.000 users, the sitemap will be auto-split in multiple files.

```ruby
require 'massive_sitemap'

index_url = MassiveSitemap.generate(:url => 'test.com') do
  User.all do |user|
    add "/users/#{user.id}", :change_frequency => 'weekly', :last_modified => user.updated_at, :priority => 0.9
  end
end
MassiveSitemap.ping(index_url)

```

## Structure

MassiveSitemap is structured in two major parts: `Builder` and `Writer`. Both offer an abstract interface which is tailored to the specific needs.

### Builder
`Builder` keeps all the sitemap structure related logic to build the XML data. `Builder::Index` does the similar for the index structure. `Builder::Rotation` is an extension to make sure no more than 50k urls are written per files, according to sitemap specs.


### Writer
The `Writer` takes care of the storage. At top level, that's just a string (`Writer::String`), however `Writer::File` stores to files, `Writer::GzipFile` gzips it as well. `Writer` keeps the state of the files and implements various strategies how to update the files.


Further extension and customization can easily be done, e.g. a `Writer::S3` [extenstion](https://github.com/rngtng/massive_sitemap-writer-s3) stores the sitemap files to Amazon S3 .

## Contributing

We'll check out your contribution if you:

- Provide a comprehensive suite of tests for your fork.
- Have a clear and documented rationale for your changes.
- Package these up in a pull request.

We'll do our best to help you out with any contribution issues you may have.


## License

The license is included as LICENSE in this directory.
