---
layout: episode
title: A first computational notebook
teaching: 0
exercises: 20
questions:
 - What does a simple notebook with some analysis look like?
 - How can keyboard shortcuts speed up my work?
objectives:
 - Get started with notebooks for analysis.
 - Practice common keyboard shortcuts.
 - Get a feeling for the importance of execution order
keypoints:
 - Notebooks provide an intuitive way to perform interactive computational work.
 - Allows fast feedback in your test-code-refactor loop (see [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)).
 - Cells can be executed in any order, beware of out-of-order execution bugs!
 - Keyboard shortcuts can save you time and protect your wrists.
---

# Creating a computational narrative

Let's create our first real computational narrative in a Jupyter notebook
(adapted from [Python and R data analysis course](https://github.com/AaltoScienceIT/python-r-data-analysis-course) at Aalto Science IT).

<img src="{{ site.baseurl }}/img/pi_with_darts.png" width="30%">

Imagine you are on a desert island and wish to compute pi.
You have a computer with you with Python installed but no
math libraries and no Wikipedia.

Here is one way of doing it - "throwing darts" by generating
random points within a square area and checking whether the points
fall within the unit circle.

> ## Calculating pi using Monte Carlo methods
>
> 1. Create a new notebook, name it, and add a heading.
> 2. Document the relevant formulas in a new cell:
>  ```
>  - square area: $s = (2 r)^2$
>  - circle area: $c = \pi r^2$
>  - $c/s = (\pi r^2) / (4 r^2) = \pi / 4$
>  - $\pi = 4 * c/s$
>  ```
>
> 3. Add an image to explain the concept:
> ```
> ![Darts](https://coderefinery.github.io/jupyter/img/darts.svg)
> ```
>
> 4. Import `random` module:
> ```python
> import random
> ```
>
> 5. Initialize the number of points:
> ```python
> num_points = 1000
> ```
>
> 6. "Throw darts":
> ```python
>    points = []
>    hits = 0
>    for _ in range(num_points):
>        x, y = random.random(), random.random()
>        if x*x + y*y < 1.0:
>            hits += 1
>            points.append((x, y, True))
>        else:
>            points.append((x, y, False))
> ```
>
> 7. Plot results:
> ```python
> %matplotlib inline
> from matplotlib import pyplot
> x, y, colors = zip(*points)
> pyplot.scatter(x, y, c=colors)
> ```
>
> 8. Compute final estimate of pi:
> ```python
> fraction = hits / num_points
> 4 * fraction
> ```
{: .challenge}

What do we get from this?

- With code separate from everything else, you might just send one
  number or a plot to your supervisor/collaborator for checking.
- With a notebook as a narratives, you send everything in a **consistent
  story**.
- A reader may still just read the introduction and conclusion, but
  they can easily see more - *and try changes themselves* - if they
  want.

> ## Working with Git from JupyterLab
>
> 1. Make sure that you have installed the [Git extension](https://coderefinery.github.io/installation/jupyter/#git-extension) and
    [nbdime](https://coderefinery.github.io/installation/jupyter/#diffingmerging-notebooks) for JupyterLab.
> 2. Initialize a Git repository from the top Git menu.
> 3. Save the computing-pi notebook and use the left-hand Git menu to stage and commit it.
> 4. Go to GitHub and create a new repository, e.g. jupyterlab-demo.
> 5. Open a terminal inside JupyterLab and set the remote, e.g.
>   `git remote add origin https://github.com/user/jupyterlab-demo.git`
>   You can use the option "Open Git Repository in Terminal" in the top level Git menu.
> 6. The first push needs to be done via terminal (to set the upstream
>   branch for our local master branch):
>   `git push -u origin master`
> 7. Future pushes (and pulls) can be done from the left-hand Git menu.
> 8. Make another change to the notebook and save it, and click the
>   `git` button in the notebook menu bar (or the Diff button in the left-side Git menu). 
{: .challenge}
