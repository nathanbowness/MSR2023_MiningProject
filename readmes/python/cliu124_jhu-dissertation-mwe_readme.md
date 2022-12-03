Johns Hopkins University-compliant dissertation template  
Minimal working example using `LaTeX`
==========

# Background

When I was writing my dissertation back in 2010, I was peripherally aware of `LaTeX` but not so much that I felt like investing the time required to learn how to make a complex document with it, so I ultimately wrote my dissertation in `MS-Word` and compiled it in a very ugly and sloppy way into what was ultimately reduced to a single file called `old-dissertation.doc`, written in the old `MS-Word` document format before they were XML-based. This archive is intended to simplify the process of creating a dissertation using `LaTeX` that complies with the JHU formatting requirements found
[here](https://www.library.jhu.edu/library-services/electronic-theses-dissertations/formatting-requirements/).

## Project aims:

1. to make a `LaTeX` conversion of my `MS-Word` dissertation (produced in 2010), along with all the `LaTeX` bells and whistles of internal document links and references as well as integrated bookmarks in the final PDF file.

2. to produce **the template I wish I had available to me when I was writing my dissertation** back in 2010; a more or less complete minimal working example (mwe) of a JHU-compliant dissertation using `LaTeX` with all the required parts in the required order.

# Quick Start

1. Install a major `LaTeX` distribution such as `TeX Live` (multi-platform), `MiKTeX` (Windows) or `MacTeX` (Mac OS). The output produced by these files contains dummytext by default from the `lipsum` package provided in most `LaTeX` distributions.

2. To compile the included sample document, type `latex mwe`.  If you want to test the references and everything, use the usual magic sequence of commands:

```sh
pdflatex mwe
biber mwe # or bibtex mwe
pdflatex mwe
pdflatex mwe
```
Extra compiles may be needed for and accurate Table of Contents, List of Figures, etc.

# `latexmk` version

I use the outstanding  `latexmk` (Version 4.65) program by by John Collins which can be obtained from [CTAN](http://www.ctan.org/pkg/latexmk) or from the [author's website](http://www.personal.psu.edu/jcc8/latexmk) to automate the process of compiling `.tex` files and cleaning up the unwanted files produced in the compilation process.

I added a `bash` function to my `~/.bash_profile` dotfile of the form

```sh
latex-make-and-clean () {
  time latexmk -pdf -pdflatex='pdflatex -file-line-error -synctex=1' "$@" && latexmk -c
  rm *.bbl pdfa.xmpi text/*.aux
  }
```

which will run `pdflatex` and `biber` (or `bibtex`) as many times as necessary to properly compile the file with references, a table of contents, appendices and so forth. `Synctex` is incorporated as well. Finally, the current directory and subdirectory `text/` are cleaned of superfluous files, while reporting the time elapsed at the end.

As single commands, this looks like

```
time latexmk -pdf -pdflatex='pdflatex -file-line-error -synctex=1' mwe
latexmk -c
rm *.bbl pdfa.xmpi text/*.aux
```

# What's Included?

I opted for a reductionist approach, seeking to minimize the number and type of files required to produce a document of the desired complexity that compiles without modification, mainly because I remember feeling overwhelmed by the apparent complexity of some `LaTeX` repos I came across when I was trying to put my own dissertation together. Bearing that in of mind, we have

* `mwe.tex` – The root `LaTeX` file containing the `LaTeX` preamble as well as the "include" statements for each part of the dissertation

* `mwe.pdf` – A compiled version of the sample document

* `classics.bib` – A sample `BibTeX` file containing references to a number of classic scientific works

* `figures/` – directory for figure images

* `text/` – directory for content files

* `jrc-dissertation.pdf` - the `LaTeX` version of John Clayton's dissertation (upon which the mwe was modeled)

* `README.md` - this document

# Figures

Figures should be generated as such:

```tex
\begin{figure}[p]
  \centering
  \includegraphics[width=\columnwidth]{myfigure}
  \caption{My caption}
  \label{fig:myfig}
\end{figure}
```

Where the figure `myfigure.EXT` can be located in the directory designated by the `\graphicspath` command in the `mwe.tex` file.

Note that no file extension is given in the `includegraphicx` command; this makes the code maximally portable for different graphics drivers. For `pdflatex`, there are many allowable extensions, including `.pdf` and `.jpg` among others. For plain `LaTeX`, you generally have to use `.eps` files. But, if you hard-code the extension in your `LaTeX` code, then you will not be able to switch between latex and `pdflatex`.

# Overview of document conversion workflow from `MS-Word`

I started with `old-dissertation.doc`, an old 2009-ish `MS-Word` file (26MB or so) and converted it first to `old-dissertation.htm` (along with a directory of extracted images `figures`) with the native Word Version in which it was created. The resulting `html` file was converted to rich text with `textutil -convert rtf` and the resulting `old-dissertation.rtf` file was converted to a `LaTeX` file with the `rtf2latex2e` command line tool. Finally, the contents of `old-dissertation.tex` were split according to line number with `sed`, as in:

```sh
sed -n '47,94p' old-dissertation.tex > abstract.tex
sed -n '97,121p' old-dissertation.tex > thesis-readers.tex
sed -n '122,200p' old-dissertation.tex > preface.tex
sed -n '201,441p' old-dissertation.tex > contents.tex
sed -n '443,582p' old-dissertation.tex > list-of-figures.tex
sed -n '584,599p' old-dissertation.tex > list-of-appendices.tex
sed -n '601,1108p' old-dissertation.tex > chapter-1.tex
sed -n '1110,1779p' old-dissertation.tex > chapter-2.tex
sed -n '1781,2380p' old-dissertation.tex > chapter-3.tex
sed -n '2382,2921p' old-dissertation.tex > chapter-4.tex
sed -n '2923,3020p' old-dissertation.tex > general-discussions-conclusions.tex
sed -n '3022,4122p' old-dissertation.tex > references.tex
sed -n '4124,4523p' old-dissertation.tex > appendix-i.tex
sed -n '4525,5010p' old-dissertation.tex > appendix-ii.tex
sed -n '5012,10950p' old-dissertation.tex > appendix-iii.tex
sed -n '10953,11342p' old-dissertation.tex > cv.tex
sed -n '11344,11373p' old-dissertation.tex > biographical-sketch.tex
```
The line numbers were manually derived from `old-dissertation.tex` in `vim`

# Major changes from the previous template

* Added each `.tex` file split from `old-dissertation.tex` to `text/` directory

* These files were then integrated into the project and modified as necessary to compile

* Added `bib` file generated from the `BibDesk` reference manager and tweaked as necessary

* removed `rnw_chapter` directory

* removed color profile

* incorporated link color from `RJournal_nogeom.sty`

* removed RJournal style file

* adjusted title page to [JHU specifications](https://www.library.jhu.edu/library-services/electronic-theses-dissertations/formatting-requirements/) based on example files and pointsize while removing most `vspace` calls in favor of adding space after forced line breaks as a multiple of `baselineskip`.

* incorporated thesis readers into `abstract.tex`

# JHU `LaTeX` dissertation template version history

* The original `thesis.cls` class file was authored by Ian Goh (in 1999, based on the `.clo` files) and primarily based on the `UCTHESIS` document class for LaTeX version 2e by [Blaise B. Frederick](https://www.mcleanhospital.org/profile/blaise-frederick) and [Ethan Munson](https://uwm.edu/engineering/people/munson-ph-d-ethan/) from 1994 
* `format.tex` was created independently of `thesis.cls` by Chuanfa Guo in the Biostatistics department of JHPSH on October 26, 1998
* The `thesis.cls` class file for JHU was updated by Matt Clapp on November 11, 2005
* The report-class based template was created by [R. Jacob Vogelstein](https://www.linkedin.com/in/r-jacob-vogelstein-65821b4/) in May, 2007
  * Updated by [Noah J. Cowan](https://limbs.lcsr.jhu.edu/people/cowan/) on March 1, 2010
  * Updated by [Brian D. Weitzner](https://github.com/weitzner) on April 29, 2014 as available at [GitHub](https://github.com/weitzner/jhu-thesis-template)
  * Updated by [John Muschelli](https://github.com/muschellij2) on January 29, 2016 and now uses a makefile as available [here](https://github.com/muschellij2/PhD_Thesis)
  * Updated by [Leonardo Collado Torres](https://github.com/lcolladotor) on April 13, 2016 as available at this [repo](https://github.com/weitzner/jhu-thesis-template)
  * Forked by [John Clayton](http://github.com/jrclayton) in December, 2019 as available at this [repo](https://github.com/jrclayton/jhu-dissertation-mwe) 
