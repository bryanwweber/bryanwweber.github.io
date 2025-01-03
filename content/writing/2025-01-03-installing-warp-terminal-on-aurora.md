---
title: "TIL: Installing Warp terminal on Aurora/Bluefin Linux"
date: 2025-01-03 09:35
category: personal
status: published
---

Today I learned how to layer the [Warp terminal](https://warp.dev) application into the immutable Linux distro [Aurora] [^1]. Since Aurora uses rpm-ostree, I used the rpm repository provided by Warp from their [Getting Started] section. Merging the instructions from Warp with the instructions to [layer 1Password](https://publish.obsidian.md/monospacementor/Notes/Install+1Password+on+Fedora+Silverblue) that I used previously, I ended up with:

```bash
curl https://releases.warp.dev/linux/keys/warp.asc | sudo tee /etc/pki/rpm-gpg/RPM-GPG-KEY-warp-terminal
sudo sh -c 'echo -e "[warpdotdev]\nname=warpdotdev\nbaseurl=https://releases.warp.dev/linux/rpm/stable\nenabled=1\ngpgcheck=1\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-warp-terminal" > /etc/yum.repos.d/warpdotdev.repo'
rpm-ostree install warp-terminal
```

Then a reboot and Warp is available!

[^1]: Aurora is the KDE-based spin of [Bluefin]

[Aurora]: https://getaurora.dev/
[Bluefin]: https://projectbluefin.io/
[Getting Started]: https://docs.warp.dev/getting-started/getting-started-with-warp
