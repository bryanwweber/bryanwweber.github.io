---
title: Writing Task Plugins for Nikola
date: 2018-12-22 16:37
category: personal
status: published
---

[Nikola] is an awesome static website generator built in Python. I recently used
it to develop the new [website](https://cantera.org) for the [Cantera
project](https://github.com/cantera/cantera-website). The architecture of Nikola
is quite interesting. It is essentially a series of plugins that find posts and
pages and render the contents to HTML. Nikola supports source files written in
reST, Markdown, and Jupyter Notebooks out-of-the-box, and it is relatively easy
to add plugins that can process other formats, as well as plugins to accomplish
any other task that would be useful for your site.
<!--more-->

Nikola plugins can do more than render pages to HTML. There are plugins that
enable the commands (`nikola build`, `nikola auto`, etc.), plugins that provide
shortcodes you can use in a document, for instance, to link to another page on
your site by its slug instead of the URL, and a general category of `Task`s. I
want to write some more about `Task` plugins here.

`Task` plugins, as the name implies, accomplish tasks on the source files for
the website and are run during the `nikola build` command (or when the `build`
is invoked automatically, such as during `nikola auto`). `Task`s includes
generating tags (and tag pages) for posts, creating image galleries, copying
assets (CSS, favicons, etc.) from the source tree to the output, and more.

Creating your own Nikola plugin is quite simple. They are Python scripts that
are stored in a `plugins` directory at the top level of the source for your
website, right alongside the `pages` and `posts` directories that store your
content. To let Nikola know that a particular Python script is a plugin, you
have to write a `.plugin` file, which is an INI-formatted file to tell Nikola
where to find the module that it should run. Taking the example from the [Nikola
documentation](https://getnikola.com/extending.html#task-plugins):

```ini
[Core]
Name = copy_assets
Module = task_copy_assets
...
```

In the `[Core]` section, the `Name` setting must match the `name` of the `Task`
(see below), and the `Module` setting is the name of the Python script that
should be run (without the `.py`).

Now, to write the Python for the actual plugin. First, your `Task` must inherit
from the `Task` class from the `nikola.plugin_categories` module, or another
class that inherits from that class.

```python
from nikola.plugin_categories import Task

class MyTask(Task):

    name = "my_task"
```

Note that the `name` class attribute must match the `Name` in the plugin INI
file. In the `Task` class, there are two instance methods that are important:
the `set_site` method (which is actually important for all Nikola plugins) and
the `get_tasks` method (which is specific to task plugins).

The `set_site` method has the signature

```python
def set_site(self, site)
```

where `site` is the instance of the website that you're building. The
documentation for the `site` instance is available on the [Nikola ReadTheDocs].
The `set_site` method is run when the plugin is loaded and the site is being
initialized. This is a good place to do any setup that you need to run your
task. For instance, if there are configuration variables that your tasks need
access to, it is common to group those into a dictionary in the `set_site`
method. Another common thing to do is [inject your
task]({static}/personal/2018-12-20-controlling-plugin-task-execution-order.md)
as a dependency to another task. Including the `set_site` method is optional,
but if you do, you should make sure to call the `super` of the class:

```python
from nikola.plugin_categories import Task

class MyTask(Task):

    name = "my_task"

    def set_site(self, site):
        # Conduct setup
        super(MyTask, self).set_site(site)
```

The other method that is important is the `gen_tasks` method. According to the
documentation, the `gen_tasks` method should `yield` [doit tasks].
[`pydoit`](http://pydoit.org/) is an automation library that determines the
appropriate order to run dependent tasks. So, for instance, doit will determine
that rendering the HTML for your pages is dependent on first parsing the source,
and run the appropriate Nikola tasks in the correct order.

A doit task can be most simply represented as a Python dictionary with special
keywords as the keys. In particular, the `actions` keyword specifies what, well,
action(s) the task should take. This is most commonly a function that actually
does the work required for the task. The reason for this indirection is that
doit pre-processes all of the tasks and decides which ones need to be run based
on their output changing or not being current. Therefore, we don't want doit to
be forced to run the "task" we want to be accomplished until it is ready to do
so. Thus, within the `Task` context, a sample might look like

```python
from nikola.plugin_categories import Task

class MyTask(Task):

    name = "my_task"

    def gen_tasks(self):
        def action_function(arg1, arg2):
            pass

        yield {
            "actions": [
                (action_function, ["arg1value", "arg2value"])
            ],
        }
```

This way, Nikola is free to execute the `gen_tasks` function on every `build`
invocation, but the `action_function` will only be executed when Nikola passes
control to doit and doit determines the result of running the task is
out-of-date.

The signature of the `action_function` is totally arbitrary and can be modified
to suit the users needs. Arguments passed to the `action_function` are specified
as the second and third elements of the tuple that specifies the `actions`,
namely, if the second argument is a list, the elements of the list are passed as
arguments to the function, and if the third argument is a dictionary, the values
are passed as keyword arguments (based on the keys) to the function.

There are a few other important keywords in the doit task dictionary. These
include:

* `basename`: The base name for the task, will be appended with the `name`
  keyword to generate a unique name for the task
* `name`: A unique name for the task, see also `basename`
* `uptodate`: A list of `True`, `False`, `None`, or function calls (that must
  return one of `True`, `False`, or `None`) to determine whether the task should
  be executed. Any elements of the list that are `False` will result in the task
  being executed. Note that even if all the elements are `True`, the task may
  still be executed because doit also considers other kinds of dependencies,
  such as output files, to determine whether the task is out-of-date. See also
  the [doit documentation](http://pydoit.org/dependencies.html#attr-uptodate).

  * [`config_changed`][config_changed]: This is a class from the Nikola `utils`
    module (and is an overload of the class of the same name from doit) that
    computes a hash to determine if a "configuration" value has changed. The
    configuration value is passed to the function and can be a string or a
    dictionary. If the value is a dictionary, then each key is hashed to
    determine any changes; if anything comes out different, a `False` element is
    put into the `uptodate` list. Usage is

    ```python
    config_dict = {"keyword": "something that can be hashed"}
    yield {
        # actions, etc.
        "uptodate": [utils.config_changed(config_dict)],
    }
    ```

A very useful place to find out what plugins can do is to look at the [`plugins`
directory](https://github.com/getnikola/nikola/tree/master/nikola/plugins) in
the Nikola source tree. Hopefully, this description will help you understand
what the code is doing!

[Nikola]: https://getnikola.com
[Nikola ReadTheDocs]: https://nikola.readthedocs.io/en/latest/nikola/#module-nikola.nikola
[doit tasks]: http://pydoit.org/tasks.html
[config_changed]: https://github.com/getnikola/nikola/blob/3671c65476c87dbfa55cfd926a1084613289859b/nikola/utils.py#L552
