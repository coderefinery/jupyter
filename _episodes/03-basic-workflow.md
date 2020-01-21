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

Let's create our first real computational narrative in a Jupyter notebook.
> Adapted from https://github.com/AaltoScienceIT/python-r-data-analysis-course

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
> points = []
>
> hits = 0
> for _ in range(num_points):
>     x, y = random.random(), random.random()
>     if x*x + y*y < 1.0:
>         hits += 1
>         points.append((x, y, True))
>     else:
>         points.append((x, y, False))
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
