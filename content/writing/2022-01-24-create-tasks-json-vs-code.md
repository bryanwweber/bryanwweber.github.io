---
title: Creating A tasks.json File for VS Code
date: 2022-01-24 16:49
category: personal
status: published
---

VS Code has a super useful feature called [_tasks_](https://code.visualstudio.com/docs/editor/tasks). These allow you to define and chain arbitrary shell commands or programs together and run them from the VS Code UI. This idea has effectively unlimited potential, but one use I came up with today is to automatically generate an HTML coverage report after running pytest. This is super useful when writing tests to address code coverage, since you can have the tests open in VS Code and the HTML report open in a browser. When you run the task after saving your tests, you only need to refresh the browser tab to see updated results.

<!--more-->

Tasks in VS Code are defined in a JSON file, `tasks.json`. The easiest way to open the file with a placeholder task, if you haven't created any already, is to use the command palette and search for _Configure Tasks_. A basic task is a JSON object with four main keys:

1. **`label`**: A name for the task
2. **`type`**: The type of the task, either `process` or `shell`
3. **`command`**: The command to be executed
4. **`args`**: Any additional arguments to the command

The first task we create will run pytest with the `--cov` argument so that it generates coverage files. Note that this will require the `pytest-cov` plugin to be installed.

```json
{
    "label": "Run tests with coverage",
    "type": "process",
    "command": "pytest",
    "args": [
        "dask",
        "--cov=dask"
    ]
}
```

This task is named _Run tests with coverage_ and the command is naturally `pytest`. We chose a `type` of `process` here because we only need to launch `pytest` as a standalone program, not from within a shell. The `args` are an array of arguments that are passed to pytest. Multiple arguments that you would normally separate with a space should be individual elements in the array, otherwise they'll be grouped with quotes and pytest won't recognize them.

Now let's say you want to make your task here a little bit more intelligent. The Dask test suite takes a few minutes to run and I don't want to wait that long when I'm iterating on a single file. Rather than passing pytest the entire tree to search for tests, I'd rather pass the specific file I'm working on. We can define an input for the task that pops open a box where we can type a value for the argument. The entire `tasks.json` file looks like this now:

```json
"tasks": [
    {
        "label": "Run tests with coverage",
        "type": "process",
        "command": "pytest",
        "args": [
            "${input:testsToRun}",
            "--cov=dask",
        ]
    },
],
"inputs": [
    {
        "id": "testsToRun",
        "description": "Subset of tests to run",
        "default": "dask",
        "type": "promptString"
    },
]
```

`"inputs"` is an array of objects with 4 main keys:

1. **`id`**: An identifier for the input that will be used to identify this input in the task
2. **`description`**: A description
3. **`default`**: The default value for the input
4. **`type`**: The type of input, `promptString` will prompt you for a string

The task is also modified so that the first item in `args` becomes `${input:testsToRun}`. The `${...}` tells VS Code that it needs to substitute a variable, `input` specifies that the variable is from the `inputs` array, and `testsToRun` is the `id` of the relevant input. Now, when I run this task, VS Code asks for a string that becomes the search argument for pytest!

We can similarly add another `process` task to run the `coverage html` command that generates the HTML coverage report.

The last item to accomplish is to define a single task that executes both tasks in sequence. This is known as a _Compound task_ and it relies on a new key for the task object, `dependsOn`. This key must have a value that is an array of task labels to run. By default, the tasks are run in parallel; since we want them to be run in sequence, we also need the `dependsOrder` key set to a string `sequence`. The compound task to run tests and generate the report looks like this:

```json
{
    "label": "Run tests and get coverage HTML",
    "dependsOn": [
    "Run tests with coverage",
    "Coverage HTML report"
    ],
    "dependsOrder": "sequence",
}
```

The task _Run tests and get coverage HTML_ will now execute the two tasks we've defined, which will automatically run the tests and generate the HTML report! All that remains is to refresh your Coverage page in your browser to see the updated information!
