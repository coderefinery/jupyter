# Shell commands, magics and widgets

```{questions}
- Are there any other features besides code, text and output?
```

```{objectives}
- Learn how to access help.
- Learn how to use magics and shell commands.
- Learn how to use widgets.
```


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
{: .output}

`%quickref` shows a quick reference card of features and shortcuts:
```python
%quickref
```

---


### Shell commands

- You can run shell commands by prepending with "!"
  - On Windows, GitBash needs to have the following option enabled:
  `Use Git and the optional Unix tools from the Windows Command Prompt`
- Make sure your cell command doesn't require interaction

```python
!echo "hello"
```
```
hello
```
{: .output}

We can also capture the output of a shell command:
```python
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
```python
%lsmagic
```

Question mark shows help:
```python
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
> fine).  See the [installation instructions](https://coderefinery.github.io/installation/jupyter/#jupyterlab-extension-manager).
>
> After installation, you need to reload the page to make it active
> (and if you installed it with pip or conda, restart the whole
> JupyterLab server)
{: .discussion}

---

```{challenge} A few useful magic commands
Using the computing-pi notebook, practice using a few magic commands.
Remember that cell magics need to be on the first line of the cell.
1. In the cell with the for-loop over `num_points` (throwing darts), add the
   ``%%timeit`` cell magic and run the cell.
2. In the same cell, try instead the `%%prun` cell profiling magic.
3. Try introducing a bug in the code (e.g., use an incorrect variable name:
   `points.append((x, y2, True))`)
   - run the cell
   - after the exception occurs, run the `%debug` magic in a new cell
     to enter an interactive debugger
   - type `h` for a help menu, and `help <keyword>` for help on keyword
   - type `p x` to print the value of `x`
   - exit the debugger by typing `q`
4. Have a look at the output of `%lsmagic`, and use a question mark and
   double question mark to see help for a magic command that raises
   your interest.
```

````{challenge} Playing around with a widget

Widgets can be used to interactively explore or analyze data.

1. We return to the pi approximation example and create a new cell where
   we reuse code that we have written earlier but this time we place the
   code into functions. This "hides" details and allows us to reuse the functions
   later or in other notebooks:
   ```python
   import random
   from ipywidgets import interact, widgets

   %matplotlib inline
   from matplotlib import pyplot


   def throw_darts(num_points):
       points = []
       hits = 0
       for _ in range(num_points):
           x, y = random.random(), random.random()
           if x*x + y*y < 1.0:
               hits += 1
               points.append((x, y, True))
           else:
               points.append((x, y, False))
       fraction = hits / num_points
       pi = 4 * fraction
       return pi, points


   def create_plot(points):
       x, y, colors = zip(*points)
       pyplot.scatter(x, y, c=colors)


   def experiment(num_points):
       pi, points = throw_darts(num_points)
       create_plot(points)
       print("approximation:", pi)
   ```
2. Try to call the `experiment` function with e.g. `num_points` set to 2000.
3. Add a cell where we will make it possible to vary the number of points interactively:
   ```python
   interact(experiment, num_points=widgets.IntSlider(min=100, max=10000, step=100, value=1000))
   ```
   If you run into `Error displaying widget: model not found`, you may need to refresh the page.
4. Drag the slider back and forth and observe the results.
5. Can you think of other interesting uses of widgets?
````

```{discussion} RShiny is a nice R alternative/solution à la ipywidgets
[RShiny](https://shiny.rstudio.com) is a nice R alternative/solution a la
ipywidgets which can be interesting for R developers.

See for instance their [gallery of examples](https://shiny.rstudio.com/gallery/).
```

---

```{keypoints}
- Jupyter notebooks have a number of extra features that can come in handy.
```
