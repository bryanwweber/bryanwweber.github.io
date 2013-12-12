---
layout: post
title:  "Internet Explorer Starts Opening Text Files"
date:   2013-12-12 12:02
categories: Personal
excerpt:
---

On Windows 7, Microsoft Office 2010 and 2013 will take over the file association for text-like files. 
The Office installer sets the default handler to use Office XML Handler for anything that was associated with
Notepad++. The fix is to delete the registry key HKEY_CLASSES_ROOT\Notepad++_file and start Notepad++
with admin priviliges. Go into the settings, remove and re-add one file association, and quit Notepad++.
The file associations should be fixed, no reboot required. Fixing the icons may require a reboot.

Source: http://sourceforge.net/p/notepad-plus/discussion/331754/thread/0a714707