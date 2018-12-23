---
title: How to fix broken hyperlinks to equations in LaTeX
date: 2014-03-07 23:00
category: personal
---

While writing my dissertation in LaTeX, I was having a problem that
some sub-equations were not linking to the correct place. The solution
is to load the `mathtools` package before the `hyperref` package.
[This question][1] on TeX.SX showed the way, even though I'm not using
the `\numberwithin{equation}{section}` line.

[1]: http://tex.stackexchange.com/questions/65926/hyperlinking-problems-when-using-subequations-hyperref-and-cleveref
