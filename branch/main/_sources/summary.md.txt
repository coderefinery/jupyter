# Summary


## Recommendations for longer notebooks

### Create a table of contents on top

You can do that using Markdown. This produces a nice overview for longer notebooks.
Example: <https://stackoverflow.com/a/39817243>


### Jupyter Book

- <https://jupyterbook.org>
- You can cite and cross-reference
- You can toggle cell visibility
- ... and a lot more

---

## Discussion points

```{discussion} Use cases and reproducibility
- If you are already using Jupyter, what tasks do you use it for?
- If you are new to Jupyter, do you see any possible use cases?
- Do you think Jupyter Notebooks can help tackle the problem of irreproducible results?
```

```{discussion} Are Jupyter notebooks "workflows"?
- A reproducible workflow documents a "pipeline"
- Also a Jupyter notebook can be a data processing and visualization pipeline
- Are Jupyter notebooks "workflows"?
```

---

## Interesting blog posts and articles

- [A. Guzharina, "We Downloaded 10,000,000 Jupyter Notebooks From Github – This Is What We Learned"](https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/)
- [J. M. Perkel, "Reactive, reproducible, collaborative: computational notebooks evolve", Nature 593, 156-157 (2021)](https://doi.org/10.1038/d41586-021-01174-w)

---

## Similar tools for other languages

- R: [R Shiny](https://shiny.rstudio.com/gallery/), [R Markdown](https://rmarkdown.rstudio.com/)
- JavaScript: [Observable](https://observablehq.com/)
- Julia: [Pluto](https://github.com/fonsp/Pluto.jl)

---

## Avoiding repetitive code

**It all started with a short and simple notebook** but how to organize as projects and
notebooks grow?

Let's imagine we wrote this function `fancy_plot` for a hexagonal 2D histogram plot
(please try it in your notebook):
```{code-block} python
---
emphasize-lines: 7-12
---
import seaborn as sns

# to get some random numbers
from numpy.random import default_rng


# this one is simple but let us imagine something very lengthy
def fancy_plot(x_values, y_values, color):
    """
    Fancy function creating fancy plots.
    """
    sns.jointplot(x=x_values, y=y_values, kind="hex", color=color)


rng = default_rng()

x_values = rng.standard_normal(500)
y_values = rng.standard_normal(500)

# call our function
fancy_plot(x_values, y_values, "#4cb391")


other_x_values = rng.standard_normal(500)
other_y_values = rng.standard_normal(500)

# call our function again, this time with other data
fancy_plot(other_x_values, other_y_values, "#fc9272")
```

Now we would like to use this function in 5 other notebooks without duplicating
it over all of the notebooks (imagine the function is very lengthy).

It can be useful to create a Python file `myplotfunctions.py` in the same
folder as the notebooks (you can change the name)
and place this code into `myplotfunctions.py`:
```{code-block} python
import seaborn as sns


# this one is simple but let us imagine something very lengthy
def fancy_plot(x_values, y_values, color):
    """
    Fancy function creating fancy plots.
    """
    sns.jointplot(x=x_values, y=y_values, kind="hex", color=color)
```

Now we can simplify our notebook:
```{code-block} python
---
emphasize-lines: 4, 13, 20
---
# to get some random numbers
from numpy.random import default_rng

from myplotfunctions import fancy_plot


rng = default_rng()

x_values = rng.standard_normal(500)
y_values = rng.standard_normal(500)

# call our function
fancy_plot(x_values, y_values, "#4cb391")


other_x_values = rng.standard_normal(500)
other_y_values = rng.standard_normal(500)

# call our function again, this time with other data
fancy_plot(other_x_values, other_y_values, "#fc9272")
```
