title: Fixing Blank Notepad++ File Icons
date: 2014-04-07 18:53
category: personal

I had a problem recently that the file icons in Windows Explorer for
all the filetypes set to open in Notepad++ were coming up as the blank
icon. To fix the issue, I had to reset the icon handler for Notepad++.
I'm not sure if this was related to an update for Notepad++, or something
I did. <!--more--> Anyhow, the solution was to delete the registry key

```registry
HKEY_CLASSES_ROOT/Notepad++_file
```

then open Notepad++ with administrator rights, remove/add a file association,
and restart Explorer. Problem fixed!
