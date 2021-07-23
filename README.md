bryanwweber.com
===============

This repository contains the source code for my personal website, <bryanwweber.com>

License
-------

bryanwweber.com (c) by Bryan Weber

bryanwweber.com is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

You should have received a copy of the license along with this
work.  If not, see <http://creativecommons.org/licenses/by-nc-sa/3.0/>.

Copying
-------

If you want to use the site's theme and customizations, you are generally welcome to (but see the license above and within the various theme files and packages).

Developing
----------

Clone the repository. Install the Python requirements:

```shell
python -m pip install -r requirements.txt
```

Install Node via Homebrew:

```shell
brew install node
```

Install Less via NPM:

```shell
npm install -g less
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
