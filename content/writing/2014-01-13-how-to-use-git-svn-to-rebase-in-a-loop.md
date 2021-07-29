---
title:  How to use git-svn to rebase in a loop
date:   2014-01-13 07:50
category: personal
original_url: writing/personal/2014/01/13/how-to-use-git-svn-to-rebase-in-a-loop/index.html
---

I'm working on developing for an open source project right now. The source code
is stored in a Subversion repository, but my preferred version control manager
is Git. I use `git-svn` to access the repository so that I can still use Git as
my version control.
<!--more-->

There are just two problems with this approach. First, Subversion prefers a more
linear commit tree than Git; it doesn't handle branches as easily. Plus, since I
don't have commit access to the main repository, I have to submit all my work as
patches. This means that the local commits I make with my work won't necessarily
line up with the commit on the main repository.

My workflow is as follows:

```bash
git svn fetch
for b in $(git branch | cut -c 3-); \
do git checkout $b && git rebase remotes/trunk; done
```

First, I update my repository, then I update all my local branches to match the
remote branch.

For this to work, you can't have conflicts on any of your branches with the
files you'll be updating. This may or may not be the case, so proceed with
caution.

**Update:** If you only have one branch with no local commits, running

```bash
git svn rebase
```

will fast forward that branch to the most recent `refs/remotes/trunk`
