title: Various tricks for using the LaTeX packages caption and floatrow
date: 2014-03-24 18:00
category: personal

Today I had two problems with clashes between the [`floatrow`](http://www.ctan.org/pkg/floatrow) and
[`caption`](http://www.ctan.org/pkg/caption) packages. The first was regarding hyperlinks and the other
was regarding spacing of the subcaption of subfigures.<!--more-->

For the first, using the `\autoref` command would print the wrong type of float. The
problem occurs when using multiple types of floats in a `floatrow`,
for instance a `table` and a `figure`. If a `table` box in a `figure` environment
is referenced, `\autoref` will print the type of the environment (i.e. `figure`)
instead of the correct type (`table`). This only occurs when using the `caption`
package. The solution is to explicitly tell the caption what type it is
with a `\captionsetup{type=table}` statement:

```latex
\documentclass{article}
\usepackage{floatrow}
\usepackage{caption}
\usepackage[demo]{graphicx}
\usepackage{hyperref}
\begin{document}
\begin{figure}
    \begin{floatrow}
        \killfloatstyle\ttabox
        {\captionsetup{type=table}\caption{Should print "Figure 1" \autoref{fig:1}}
        \label{tab:1}}
        {\begin{tabular}{*{2}{c}}
        Test & test \\
        1 & 2 \\
        \end{tabular}}
        \ffigbox
        {\includegraphics{}}
        {\caption{Should print "Table 1" \autoref{tab:1}}\label{fig:1}}
    \end{floatrow}
\end{figure}
\end{document}
```

For the second, I was trying to move the subcaptions of
the subfigures in a `subfloatrow` closer to the image. I tried
using the `caption` package option `skip`, but it turns out
that `floatrow` overwrites this in certain cases. The solution is
to use the `captionskip` option for `subfigure` setup. If this
change should apply document-wide, put it in the preamble.
Otherwise, put it just after `\begin{figure}` in the figure
you want to change.

```latex
\captionsetup[subfigure]{captionskip=value}
```
