---
layout: episode
title: Shell commands, magics and widgets
teaching: 10
exercises: 15
questions:
 - Are there any other features besides code, text and output?
objectives:
 - Learn how to access help.
 - Learn how to use magics and shell commands.
 - Learn how to use widgets.
keypoints:
 - Jupyter notebooks have a number of extra features that can come in handy.
---

## Extra features

### Access to help

We can get help on an object using a question mark:
```python
import numpy as np
np.sum?
```

Or two question marks to also see the source code:
```python
np.sum??
```

List all names in a module matching pattern:
```python
?np.*sum*
```
```
np.cumsum
np.einsum
np.einsum_path
np.nancumsum
np.nansum
np.sum
```

`%quickref` shows a quick reference card of features and shortcuts:
```
%quickref
```

---


### Shell commands

- You can run shell commands by prepending with "!"
  - On Windows, GitBash needs to have the following option enabled:
  `Use Git and the optional Unix tools from the Windows Command Prompt`
- Make sure your cell command doesn't require interaction

```
!echo "hello"
```
```
hello
```

We can also capture the output of a shell command:
```
notebooks = !ls *.ipynb
```

- Common linux shell commands are also available as *magics*: %ls, %pwd, %mkdir, %cp, %mv, %cd, *etc.*.
- Using shell commands can be useful when testing a new idea but **for reproducible notebooks be careful
  with shell commands** (will they also work on a different computer?).

---

### Magics

Magics are a simple command language which significantly extend the power of Jupyter.

There are two kinds of magics:

 - **Line magics**: commands prepended by one % character and whose arguments only extend to the end of the current line.
 - **Cell magics**: use two percent characters as a marker (%%), receive as argument the whole cell (must be used as the first line in a cell)

`%lsmagic` lists all available line and cell magics:
```
%lsmagic
```

Question mark shows help:
```
%sx?
```

Additional magics can also be installed or created.

---


### Widgets

Widgets add more interactivity to Notebooks, allowing one to visualize and control changes in data, parameters etc.

```python
from ipywidgets import interact
```

#### Use `interact` as a function
```python
def f(x, y, s):
    return (x, y, s)

interact(f, x=True, y=1.0, s="Hello");
```

#### Use `interact` as a decorator
```python
@interact(x=True, y=1.0, s="Hello")
def g(x, y, s):
    return (x, y, s)
```

> ## Does it not work?  Extensions need to be installed.
>
> The widgets interface have to be installed.  JupyterLab is modular,
> and some parts need to be installed as an extension.  In general,
> copy and paste the command into a shell (the JupyterLab shell works
> fine).
>
> ```shell
> $ jupyter labextension install @jupyter-widgets/jupyterlab-manager
> ```
> But you may need some other support packages installed, too:
> ```shell
> $ conda install nodejs                                  # Do this first!
> $ jupyter nbextension enable --py widgetsnbextension    # If not installed through anaconda
> ```
>
> In this case, we just need to reload the page to make it active.
> Sometimes you have to restart the notebook server.  For more
> information, see [the installation
> instructions](https://coderefinery.github.io/installation/jupyter/)
{: .discussion}


---

> ## A few useful magic commands
>
> Using the computing-pi notebook, practice using a few magic commands.
> Remember that cell magics need to be on the first line of the cell.
> 1. In the cell with the for-loop over `N` (throwing darts), add the
>    ``%%timeit`` cell magic and run the cell.
> 2. In the same cell, try instead the `%%prun` cell profiling magic.
> 3. Try introducing a bug in the code (e.g., use an incorrect variable name:
>    `points.append((x, y2, True))`)
>    - run the cell
>    - after the exception occurs, run the `%debug` magic in a new cell
>      to enter an interactive debugger
>    - type `h` for a help menu, and `help <keyword>` for help on keyword
>    - type `p x` to print the value of `x`
>    - exit the debugger by typing `q`
> 4. Have a look at the output of `%lsmagic`, and use a question mark and
>    double question mark to see help for a magic command that raises
>    your interest.
{: .challenge}

> ## Playing around with a widget
>
> Widgets can be used to interactively explore or analyze data.
> Using the computing-pi notebook, introduce a widget which plots
> subsets of all the random points:
> 1. If you haven't finished the previous episode, copy-paste this
>    code into a cell:
>    ```python
>    import random
>    %matplotlib inline
>    from matplotlib import pyplot
>    from ipywidgets import interact
>
>    N = 1000
>    points = []
>
>    hits = 0
>    for i in range(N):
>        x, y = random.random(), random.random()
>        if x**2 + y**2 < 1.0:
>            hits += 1
>            points.append((x, y, True))
>        else:
>            points.append((x, y, False))
>
>    x, y, colors = zip(*points)
>    ```
> 2. Change the last two lines of the plotting cell into a function
>    taking a tuple as argument, and slice the `points` list:
>    ```python
>    def plot_points(n=(1,10)):
>        # we plot every n-th point
>        x, y, colors = zip(*points[::n])
>        pyplot.scatter(x, y, c=colors)
>    ```
> 3. Add the `@interact` decorator above the function, and execute the cell.
> 4. Drag the slider back and forth and observe the results.
> 5. Can you think of other interesting uses of widgets in the
>    computing-pi notebook?
{: .challenge}
