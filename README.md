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

Run `./develop_server.sh start` to start a server that watches for changes to the content. Note that `make devserver` is broken for some reason.

Publishing
----------

Run `make rsync_upload` to push the changes to the website. Must have SSH keys for the server configured.
