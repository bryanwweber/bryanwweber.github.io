title: How to enable journal abbreviations in Mendeley bibliographies
category: personal
date: 2012-07-18

**UPDATE (10/10/2013):** The newest version of Mendeley (1.10.1) now supports journal abbreviations, so go out there and upgrade! I've also removed the file since it isn't necessary any longer.
<!--more-->
Whilst working on my latest journal paper today, I needed to include journal abbreviations in my bibliography. Unfortunately, the software I use to manage my references, Mendeley, does not include a method to automatically abbreviate journal titles in references. Fortunately, there is a workaround.

As detailed in this [forum post](http://support.mendeley.com/customer/portal/questions/179297-how-to-enable-journal-abbreviations-?new=179297), the method is to create a file in the user data folder that Mendeley can read. The following steps worked on Win7, Word 2010, Mendeley 1.5.2:

1. Open the Mendeley Data Folder (`"C:\Users\_Username_\AppData\Local\Mendeley Ltd\Mendeley Desktop"`) or by <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>D</kbd> in Mendeley. The keyboard shortcut opens the Debug dialog, simply click "Open Data Folder"
2. Create a folder called `journalAbbreviations`
3. Create a file in that folder called `default.txt`
4. Put the journal then the abbreviation separated by a tab so:<br>
Proceedings of the Combustion Institute <kbd>TAB</kbd> Proc. Combust. Inst.

Also, other users have invented much more complicated ways of getting the journal abbreviations file: <a href="http://alexchubaty.com/node/15">http://alexchubaty.com/node/15</a>

Finally, your citation style must be set up to use abbreviated journal names - not all of them are, and some that should be aren't. The fix is simple: in the CSL file add the `form="short"` attribute to the `<text>` tag containing your `variable="container-title"`. More about editing CSL for Mendeley can be found by <a href="http://lmgtfy.com/?q=mendeley+edit+citation+styles">googling</a>. I might do a post about more CSL stuff later.
