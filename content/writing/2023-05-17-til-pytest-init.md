---
title: "TIL: Pytest has a flat namespace"
date: 2023-05-17 06:09
category: personal
status: published
---

Pytest imports test modules into a flat namespace _unless_ you have `__init__.py` files in the test folders. This means that your test files and test function names cannot be repeated. This explains several failures I was seeing when loading tests in VS Code in a bigger monorepo project.

The context is that a few weeks ago, [Brian Okken](https://fosstodon.org/@brianokken) had [Anthony Sotille](https://twitter.com/codewithanthony) on [Test and Code](https://testandcode.com/195) and they talked about Pytest features they'd change if they could start Pytest over today. Anthony mentioned he'd change the import system and in passing mentioned my TIL.
