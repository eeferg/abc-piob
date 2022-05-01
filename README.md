# abc-piob
Examples, templates, and utilities to typeset bagpipe tunes using ABC, including Piobaireachd settings

## Introduction

I've been using ABC to typeset my pipe tunes for years but wanted a way to include them into a nicely formatted book.  I decided on using Latex for it's flexability and ability to be run via command line.  

While creating an entire book might be more than you need, I have also included a number of custom Piobaireachd PostScript add-ons that can be used directly from abcm2ps.  


## Prerequisites

I have historically compiled abcm2ps but it's available in Ubuntu 20.04LTS using apt.  This has been tested using Windows WSL2 with no issues.

abcm2ps >= 7.8.14
texlive
texlive-extra
dvips
ps2pdf

## Using

bin/abc2eps.sh - creates EPS files from ABC
bin/makepdf.sh [filename.tex] - creates a PDF of your tune collection. Note: EPS must exist first.  Running a second time will set the table of contents.
bin/cleantex.sh - removes unneeded files after creating the PDF

There are a set of keyboard shortcuts for SublimeText that makes writing bagpipe embelishments much easier

## My typical workflow

1) Add ABC tune to the tunes directory.  Do no use spaces in file names.
2) Add the tune/eps section to the TEX document.  Note that abcm2ps adds 001..002..etc. at the end of each EPS file, this needs to be reflected in these lines
2) run bin/abc2eps.sh
3) run bin/makepdf.sh [filename.tex]
4) run bin/makepdf.sh [filename.tex] a second time when I've added new tunes or am starting without a .toc file, to reset the table of contents.
5) bin/cleantex.sh (optional) to clean up the Tex log, dvi, toc, etc files.


## Work to do

I'm not very well versed with PostScript and still have to find a way to fix some of the decoration placement in the piobaireachd settings.  

The page numbering is not exact, which I am sure is because of the way I'm placing tunes as EPS.  Likewise, the PDF bookmark feature will only take you to the top of the tune section, not the tune itself.