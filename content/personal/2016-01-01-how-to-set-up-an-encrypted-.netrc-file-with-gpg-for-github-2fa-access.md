---
title:  How to set up an encrypted .netrc file with GPG for GitHub 2FA access
date:   2016-01-01 13:20
category: personal
---

Enabling 2 factor authentication on GitHub is a good way to protect your data, but unfortunately, it means you can't use your password to login at the command line on Linux for pushes and pulls to HTTPS repositories.
You can set up a special `.netrc` file to enable 2FA login from the command line.
<!--more-->

First, go to GitHub and create a Personal Access Token.
Then, create a `~/.netrc` file with the following contents:

    machine github.com
    login yourusername
    password <token>
    protocol https

    machine gist.github.com
    login yourusername
    password <token>
    protocol https

where `<token>` is the token set up on the GitHub website.

Then generate a GPG key if one doesn't exist:

    gpg --gen-key

Make sure to put a passphrase on that key.
You may have to do some other tasks on the computer while it generates enough entropy.
Then encrypt the `~/.netrc` file:

    gpg -e -r email@example.com ~/.netrc

Now the `~/.netrc` file can be deleted as long as the `~/.netrc.gpg` file is kept.
Add the netrc credential helper:

    curl -o ~/.local/bin/git-credential-netrc https://raw.githubusercontent.com/git/git/master/contrib/credential/netrc/git-credential-netrc

Finally, set up Git to use this file:

    git config --global credential.helper "netrc -f ~/.netrc.gpg -v"

Install gpg-agent and pinentry

    sudo apt-get install gnupg-agent pinentry-curses

Add to `~/.profile`:

```bash
# Invoke GnuPG-Agent the first time we login.
# Does `~/.gpg-agent-info' exist and points to gpg-agent process accepting signals?
if test -f $HOME/.gpg-agent-info && \
    kill -0 `cut -d: -f 2 $HOME/.gpg-agent-info` 2>/dev/null; then
    GPG_AGENT_INFO=`cat $HOME/.gpg-agent-info | cut -c 16-`
else
    # No, gpg-agent not available; start gpg-agent
    eval `gpg-agent --daemon --no-grab --write-env-file $HOME/.gpg-agent-info`
fi
export GPG_TTY=`tty`
export GPG_AGENT_INFO
```

Now https pushes and pulls should work with GitHub on Linux.

References:
<http://stackoverflow.com/a/18362082/2449192>  
<https://gist.github.com/wikimatze/9790374>  
<http://unix.stackexchange.com/a/47062/40481>
