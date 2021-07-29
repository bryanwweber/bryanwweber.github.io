---
title:  Fixing small Notepad++ icons
date:   2014-01-11 15:29
category: personal
original_url: writing/personal/2014/01/11/fixing-small-notepad++-icons/index.html
---

I was recently annoyed by having the wrong icon for certain files that should
open with Notepad++. <!--more--> You can see the proper icon in the top of this
image, and the incorrect icon in the bottom.

![Wrong file icons in Windows 7 Explorer]({static}/files/2014/01/wrong_icons.png)  
Wrong file icons in Windows 7 Explorer

The problem was that instead of setting the file association in Notepad++, I set
it with the "Open With" dialog in Explorer, and Windows chose the wrong icon for
me.

The solution is to delete the file association and reinstate it properly. I
found the solution on [SuperUser]. Open `regedit` and delete the sub-key with
the same name as the extension with the wrong icon, under the following keys:

```registry
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts
HKEY_CLASSES_ROOT
```

Then, open Notepad++ with admin privileges and add the extension to the "File
Exts." panel. You may need to use the "Customize" field. Finally, open Task
Manager (++Ctrl+Shift+Esc++), "End Process" the `explorer.exe` process, open a
New Task from the File, type `explorer.exe`, and you are good to go.

[SuperUser]: http://superuser.com/questions/49615/how-do-you-remove-a-default-program-association-for-file-types-in-windows-7
