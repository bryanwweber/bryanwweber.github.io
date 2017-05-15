title: How to position images in Beamer absolutely
date: 2014-09-02 13:56
category: personal

In Beamer, it is useful to position images absolutely.
There are many ways to do this, but one simple one-liner can be done with `tikz`.
<!--more-->

```latex
\tikz[remember picture, overlay] \node[anchor=center] at (current page.center) {\includegraphics{foo}};
```
Compile twice to have the picture placed at exactly the center of the slide.
The anchors can be changed to move the picture around, and further adjustments can be made by using the `calc` library.

```latex
% Preamble
\usepackage{tikz}
\usetikzlibrary{calc}
% ...
% Main document
\tikz[remember picture, overlay] \node[anchor=center] at ($(current page.center)-(1,0))$) {\includegraphics{foo}};
```

will place the image 1 cm to the left of the center.
