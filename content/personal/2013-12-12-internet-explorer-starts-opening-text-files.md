title:  Internet Explorer Starts Opening Text Files
date:   2013-12-12 12:02
category: personal

On Windows 7, Microsoft Office 2010 and 2013 will take over the file association for text-like files.
The Office installer sets the default handler to use Office XML Handler for anything that was associated with
Notepad++. <!--more--> The fix is to delete the registry key `HKEY_CLASSES_ROOT\Notepad++_file` and start Notepad++
with admin privileges. Go into the settings, remove and re-add one file association, and quit Notepad++.
The file associations should be fixed, no reboot required. Fixing the icons <del>may require a reboot</del>
requires restarting the `explorer.exe` process. Open a Task Manager window (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+
<kbd>Esc</kbd>), end the "explorer.exe" process, and in the File menu, choose "New Task", type explorer.exe and
bingo, fixed.


Source: <http://sourceforge.net/p/notepad-plus/discussion/331754/thread/0a714707>
