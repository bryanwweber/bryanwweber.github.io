---
title: Controlling plugin task execution order in Nikola
date: 2018-12-20 18:00
category: personal
status: published
---

When writing a plugin for [Nikola](https://getnikola.com), it may be useful to
have a task that has to run another task. For instance, you may want to be able
to link to specific points on other pages, which requires parsing those pages
before the posts are rendered in the `render_posts` task. If you're developing
both tasks, this is fairly simple with the `task_dep` parameter for the doit
task engine. However, if the task that must run later is already built in to
Nikola, you can't set its `task_dep` list.
<!--more-->

Never fear though, there is a way out of this problem. The Nikola
[`BasePlugin`][BasePlugin] has a method to
[`inject_dependency`][inject_dependency] to a task. The signature of the
function is

```python
inject_dependency(self, target, dependency)
```

The `target` is the task where the dependency should be added, and the
`dependency` is the task the `target` should depend on. This method can be
called in the `set_site` method that sets up your plugin. For example, something
like

```python
from nikola.plugin_categories import Task

class MyTask(Task):

    name = 'my_task'

    def set_site(self, site):
        self.site = site

        self.inject_dependency('render_posts', 'my_task')

        super(self, MyTask).set_site(site)

    def gen_tasks(self):
        pass
```

Here, the `MyTask` task was added as a dependency to the `render_posts` task.
Note that the name of the task `my_task` is used in the `inject_dependency`
function. Now, Nikola will run the plugin named `my_task` before it runs the
built-in `render_posts` plugin.

[BasePlugin]: https://github.com/getnikola/nikola/blob/d7dcb55201b22764a81cb468316a4a73a18e7891/nikola/plugin_categories.py#L65
[inject_dependency]: https://github.com/getnikola/nikola/blob/d7dcb55201b22764a81cb468316a4a73a18e7891/nikola/plugin_categories.py#L96
