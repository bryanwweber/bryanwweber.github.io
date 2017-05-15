title: Using the same font for numbers in math mode in LaTeX
date: 2014-03-25 13:00
category: personal

It really bugs me when numbers are typeset with two different fonts
on the same line, say in MS Word if you type 0.01 in the text and
then the same in an equation field, they won't look the same because
they use different fonts. For my dissertation (written in LaTeX), I
wanted to be sure to avoid this pitfall. Unfortunately, it is rather
more complicated than it seems on the face. First, you must use XeLaTeX
(which I am). Second, the packages [`fontspec`][1] and [`unicode-math`][2] are
necessary. `fontspec` lets you set the main body font, while `unicode-math`
lets you control the fonts used in math environments (between `$`, or in
an equation environment, etc.). However, by default, `unicode-math` will
typeset all of the numbers in whatever font you choose with that package
so the default must be changed. <!--more--> For instance, in  my dissertation, I have

```latex
\usepackage{fontspec}
\setmainfont[Ligatures=TeX]{Times New Roman}

\usepackage{unicode-math}
\unimathsetup{math-style=TeX}
\setmathfont[range=\mathup/{num}]{Times New Roman}
\setmathfont[range=\mathit/{greek,Greek,latin,Latin}]{Cambria Math}
\setmathfont[range=\mathup/{greek,Greek,latin,Latin}]{Cambria Math}
\setmathfont[range={"2212,"002B,"003D,"0028,"0029,"005B,
"005D,"221A,"2211,"2248,"222B,"007C,"2026,"2202,"00D7,"0302,
"2261,"0025,"22C5,"00B1,"2194,"21D4}]{Cambria Math}
```

The lines starting `\setmathfont` are what control the font for different
characters. The option `\mathup` means the upright math style, while the `\mathit`
option means the italic math style. The `/{num}` means to use the given
font for all the numbers in the style given immediately prior and the `/{greek,Greek,latin,Latin}`
means to use the given font for all the lower- and upper-case Greek and Latin
letters in the given style. The last two lines are required because the
`/{num}` option also includes a bunch of characters like square brackets
`[`, the integral symbol, etc., but Times New Roman does not have definitions
of these symbols. The following table shows the characters that did not
print for me:

 Unicode | Character
---------|-----------
  2212   |    `−`    
  002B   |    `+`    
  003D   |    `=`    
  0028   |    `(`    
  0029   |    `)`    
  005B   |    `[`    
  005D   |    `]`    
  221A   |    `√`    
  2211   |    `∑`    
  2248   |    `≈`    
  222B   |    `∫`    
  007C   |    `|`    
  2026   |    `…`    
  2202   |    `∂`    
  00D7   |    `×`    
  0302   |    `̂`     
  2261   |    `≡`    
  0025   |    `%`    
  22C5   |    `⋅`    
  00B1   |    `±`    
  2194   |    `↔`    
  21D4   |    `⇔`    
  2260   |    `≠`    

These lines reset these characters to use the Cambria Math font. Now, all
of my numerals are set in Times New Roman, no matter where they're used.

Finally, note that `unicode-math` should be loaded after any other packages
that mess with the math functionality, such as `amsmath` or `mathtools`.

[1]: http://ctan.org/pkg/fontspec
[2]: http://ctan.org/pkg/unicode-math
