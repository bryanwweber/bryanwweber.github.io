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

Clone the repository. Install the Python requirements:

```shell
python -m pip install -r requirements.txt
```

Install Node via Homebrew (on macOS) or otherwise for other platforms:

```shell
brew install node
```

Install Less via NPM:

```shell
npm install less
export PATH="$PATH:$(pwd)/node_modules/.bin"
```

This will add `lessc` to the `PATH` temporarily for this shell session.

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
