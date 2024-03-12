bryanwweber.com
===============

This repository contains the source code for my personal website, <https://bryanwweber.com>.

License
-------

bryanwweber.com (c) by Bryan Weber

bryanwweber.com is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

You should have received a copy of the license along with this work. If not, see <https://creativecommons.org/licenses/by-nc-sa/3.0/>.

Developing
----------

Clone the repository. It's set up to use `mise` to install Python and pdmx. Run `mise install`. Then create the Python venv (`python -m venv .venv`) and then install the Python requirements:

```shell
pdm install
```

Run `livereload`:

```shell
invoke livereload
```

Publishing
----------

Published via GitHub Pages.

```shell
invoke gh-pages
```
