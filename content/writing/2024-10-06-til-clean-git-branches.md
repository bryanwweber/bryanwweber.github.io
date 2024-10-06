---
title: "TIL: How to clean up merged git branches in the local copy"
date: 2024-10-06 14:39
category: personal
status: published
---

Today I learned how to delete local git branches that have been merged to the main remote branch. There are a [bunch][1] [of][2] [sites][3] that give instructions or packages for this, but I always have to search for them. So this is meant to be my reminder to myself of how I like to do this. This approach will work on Linux and macOS (bash or zsh).

```shell
git fetch --prune \
    && for branch in $(git for-each-ref --format '%(refname) %(upstream:track)' refs/heads | awk '$2 == "[gone]" {sub("refs/heads/", "", $1); print $1}'); \
    do git branch -D $branch; \
    done;
```

First, fetch the default remote and prune any remote branches. Then list all the branches, test if they have the string `[gone]` in them, and delete the ones that do. Easy peasy one liner.

[1]: https://mrkaran.dev/tils/gitlab-git-delete-local/
[2]: https://stackoverflow.com/a/17029936/2449192
[3]: https://github.com/hartwork/git-delete-merged-branches
