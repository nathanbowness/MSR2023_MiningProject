= asciidoctor-bibtex: bibtex integration for AsciiDoc
// Settings:
:idprefix:
:idseparator: -
ifndef::env-github[:icons: font]
ifdef::env-github,env-browser[]
:toc: macro
:toclevels: 1
endif::[]
ifdef::env-github[]
:!toc-title:
:status:
endif::[]
// URLs:
:url-asciidoctor: http://asciidoctor.org
:url-asciidoctor-mathematical: https://github.com/asciidoctor/asciidoctor-mathematical
:url-asciidoctor-pdf: https://github.com/asciidoctor/asciidoctor-pdf
:url-asciidoctor-latex: https://github.com/asciidoctor/asciidoctor-latex
:url-asciidoc-bib: https://github.com/petercrlane/asciidoc-bib
:url-gem: https://rubygems.org/gems/asciidoctor-bibtex

ifdef::status[]
image:https://github.com/asciidoctor/asciidoctor-bibtex/workflows/CI/badge.svg[GitHub Actions Status,link=https://github.com/asciidoctor/asciidoctor-bibtex/actions]
image:https://img.shields.io/gem/v/asciidoctor-bibtex.svg[Latest Release, link=https://rubygems.org/gems/asciidoctor-bibtex]
endif::[]

asciidoctor-bibtex adds bibtex integration to AsciiDoc documents by introducing three new macros: `cite:[KEY]`, `bibitem:[KEY]` and `bibliography::[]`. Citations are parsed and replaced with formatted inline texts, and reference lists are automatically generated and inserted into where `bibliography::[]` is placed. `bibitem:[KEY]` will insert a rendered bibliography item directly into the text.

asciidoctor-bibtex is designed to be used as an extension to {url-asciidoctor}[Asciidoctor]. Thus this extension can be used together with other asciidoctor extensions such as {url-asciidoctor-mathematical}[asciidoctor-mathematical] and {url-asciidoctor-pdf}[asciidoctor-pdf] to enrich your AsciiDoc experience.

NOTE: asciidoctor-bibtex no longer supports AsciiDoc-to-AsciiDoc conversion.

== History

asciidoctor-bibtex starts as a fork of {url-asciidoc-bib}[asciidoc-bib] and goes along a different path.
The major reason for the fork at the time was the differences in citation and bibliography macros.
asciidoc-bib failed to follow the grammar of macros in AsciiDoc and thus caused problems with existing documents and extensions.
Thus, a fork was needed.
Another reason was the inability to pass configuration via AsciiDoc attributes.

While {url-asciidoc-bib}[asciidoc-bib] focuses on replacing citations in the original documents and produces new AsciiDoc documents, asciidoctor-bibtex focuses on compatibility with Asciidoctor and other Asciidoctor extensions at the very beginning.
As time passes, asciidoctor-bibtex diverges significantly from its ancesstor.
For example, asciidoctor-bibtex now supports generating real bibtex citations and bibliography, so it can be used together with {url-asciidoctor-latex}[asciidoctor-latex] for native bibtex support.

== Install

 $ gem install asciidoctor-bibtex

asciidoctor-bibtex depends on https://github.com/inukshuk/bibtex-ruby[bibtex-ruby], https://github.com/inukshuk/citeproc-ruby[citeproc-ruby], and https://github.com/inukshuk/csl-styles[csl-styles].
Ensure the `ruby-dev` and `libxslt1-dev` packages are installed on your machine so the dependencies will compile properly.

{url-asciidoctor}[Asciidoctor] must also be installed for 'asciidoctor-bibtex' to work.
Asciidoctor version 2.0.0 or higher is required.

== Usage

First, you need to have a valid bibtex file.
You specify the location to this file using the `bibtex-file` document attribute.

=== Macros

Syntax for inserting a citation is the following inline macro:

 cite|citenp:[ref(pages), ...]

where '(pages)' is optional.

Examples of "chicago-author-date" style:

* `cite:[Lane12]` becomes "(Lane 2012)"
* `citenp:[Lane12]` becomes "Lane (2012)"
* `cite:[Lane12(59)]` becomes "(Lane 2012, 59)"

For *apa* (Harvard-like) style:

* `cite:[Lane12]` becomes "(Lane, 2012)"
* `citenp:[Lane12]` becomes "Lane (2012)"
* `cite:[Lane12(59)]` becomes "(Lane, 2012, p.59)"

For *ieee*, a numeric style:

`cite:[Lane12,Lane11]` becomes "[1, 2]"

To add a list of formatted references, place `bibliography::[]` on a line by itself.

One can use `bibitem:[Lane12]` to insert a rendered bibliography item inline, maybe to generate a cv. For example:

[source, asciidoc]
----
= My CV

== Publications

=== 2019

- bibitem:[Me2019a]
- bibitem:[Me2019b]
- bibitem:[Me2019c]
----

=== Configuration

Configuration is applied in the form of AsciiDoc document attributes, which must be defined in the document header.

|===
| Attribute Name | Description | Valid Values | Default Value

| bibtex-file
| Bibtex database file
| any string, or empty
| Automatic searching

| bibtex-style
| Reference formatting style
| any style supported by csl-styles
| ieee

| bibtex-order
| Order of citations
| `appearance` or `alphabetical`
| `appearance`

| bibtex-format
| Formatting of citations and bibliography
| `asciidoc`, `bibtex` or `biblatex`
| `asciidoc`

| bibtex-locale
| Locale used to render the bibliography
| strings supported by CSL
| `en-US`

| bibtex-throw
| Throw an error on unknown references
| `true` or `false`
| `false`

| bibtex-citation-template
| Custom citation template for numeric style
| Any string matching `/(.+?)\$id(.+)/`
| `[$id]`
|===

=== Commandline

Use asciidoctor-bibtex as an extension with the CLI:

 $ asciidoctor -r asciidoctor-bibtex sample.adoc

== License

The files within this project may be distributed under the terms of the http://owl.apotheon.org[Open Works License].

== Links

See {url-asciidoc-bib} for the original asciidoc-bib source.
