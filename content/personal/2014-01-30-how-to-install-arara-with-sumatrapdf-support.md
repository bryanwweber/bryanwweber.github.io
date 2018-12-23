---
title:  How to Install Arara with SumatraPDF Support
date:   2014-01-30 13:00
category: personal
---

[Arara](https://github.com/cereda/arara) is a cross platform build system
written in Java. It is intended for use with TeX and various derivatives
thereof, but can really be used for any build process. I'm using it to help
write my dissertation in XeLaTeX. Installation is a little bit of a pain on
Windows, so here are some notes to ease the process.
<!--more-->

First, download the Arara package from [CTAN](http://www.ctan.org/pkg/arara).
After unizipping, copy the contents of `arara/scripts` to a directory on your
path, and/or add the directory with the `arara.jar` file to your path. For
instance, I copied the files in that folder to `C:\Program Files (x86)\Arara`
and added that folder to my `PATH` variable. Then, add a batch file named
`arara.bat` to the same folder where `arara.jar` exists with the following
contents:

```batch
@echo off
java -jar "%~dp0\arara.jar" %*
```

Now, typing `arara` at a command window should print the Arara help. Next, we
have to add a custom rule to enable SumatraPDF support. Create a file in your
home directory (`C:\Users\<username>\`) called `araraconfig.yaml` with the
following content:

```yaml
!config
paths:
- <arara> @{userhome}\arara\rules
```

Then, create the directory `C:\Users\<username>\arara\rules` and in it, create
two files, `sumatrapdf.yaml` and `sumatra.bat`. The content of these files comes
from the TeX.SX answer of Mr Komandez
<http://tex.stackexchange.com/a/139055/32374>:

```yaml
#sumatrapdf.yaml
!config
# SumatraPDF rule for arara
# Author: Mr Komandez
identifier: sumatrapdf
name: SumatraPDF
commands:
- <arara> C:\Users\<username>\arara\rules\sumatra.bat "@{getBasename(file)}.pdf" "@{options}"
arguments:
- identifier: options
  flag: <arara> @{parameters.options}
```

```batch
::sumatra.bat
START /b "C:\Progra~2\SumatraPDF\SumatraPDF.exe" %1 -reuse-instance %2
EXIT
```

Then, to have Notepad++ able to compile the XeLaTeX document and automatically
open the PDF, put in the top of your `.tex` file:

```tex
% arara: xelatex: { synctex: on shell: off }
% arara: sumatrapdf
```

Next, download the NPPExec plugin from
<http://sourceforge.net/projects/npp-plugins/files/NppExec/>, and copy the
`.dll` file to the `plugins` folder in your Notepad++ installation. Press ++f6++
to open the Execute dialog, and put in that box

    NPP_SAVE
    cd $(CURRENT_DIRECTORY)
    arara.bat $(NAME_PART)

Save the script with a name, then go to the menubar, Plugins -> NppExec ->
Advanced Options... Under 'Menu item', choose the script we just created above,
and click 'Add/Modify'. Restart Notepad++ if prompted. This allows us to assign
shortcut keys through Settings -> Shortcut Mapper, then find the tab called
"Plugins", find the name of the script, click "Modify" and add a keyboard
shortcut.

Forward search can be enabled by setting up another NppExec script, this one a
one-liner (for formatting purposes, its on two lines here but make sure its all
one in the NppExec dialog).

    NPP_RUN "C:\Program Files (x86)\SumatraPDF\SumatraPDF.exe" -reuse-instance \
    $(NAME_PART).pdf -forward-search $(NAME_PART).tex $(CURRENT_LINE)

Then go through the same procedure to set a keyboard shortcut. I'm using
++ctrl+shift+f5++.
