---
layout: episode
title: A first computational notebook
teaching: 10
exercises: 0
questions:
 - What does a simple notebook with some analysis look like?
 - How can keyboard shortcuts speed up my work?
objectives:
 - Get started with notebooks for analysis.
 - Practice common keyboard shortcuts.
 - Get a feeling for the importance of execution order
keypoints:
 - Notebooks provide an intuitive way to perform interactive computational work.
 - Cells can be executed in any order, beware of out-of-order execution bugs!
 - Keyboard shortcuts can save you time and protect your wrists.
---

# Creating a computational narrative

Let's create our first real computational narrative in a Jupyter notebook.
> Adapted from https://github.com/AaltoScienceIT/python-r-data-analysis-course

<img src="{{ site.baseurl }}/img/pi_with_darts.png" width="30%">

Imagine you are on a desert island and wish to compute $\pi$. 
You have a computer with you with Python installed but no 
math libraries and no Wikipedia.

Here is one way of doing it - "throwing darts" by generating 
random points within a square area and checking whether the points 
fall within the unit circle.

> ## Calculating $\pi$ using Monte Carlo methods
> 
> 1. Create a new notebook, name it, and add a heading.
> 2. Document the relevant formulas in a new cell:
>  ```
>  - square area = $(2 r)^2$
>  - circle area = $\pi r^2$
>  - circle / square = $\pi r^2 / 4 r^2$ = $\pi / 4$
>  - $\pi = (circle/square) * 4$
>  ```
>
> 3. Add an image to explain the concept:
> ```
> !wget https://coderefinery.github.io/jupyter/img/darts.svg
> ```
> ```
> ![Darts](darts.svg)
> ```
>
> 4. Import `random` module:
> ```python
> import random
> ```
> 
> 5. Initialize variables:
> ```python
> N = 1000
> points = []
> ```
> 
> 6. "Throw darts":
> ```python
> hits = 0
> for i in range(N):
>     x, y = random.random(), random.random()
>     if x**2 + y**2 < 1:
>         hits += 1
>         points.append((x,y, True))
>     else:
>         points.append((x,y, False))
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
> 8. Compute final estimate of $\pi$:
> ```python
> fraction = hits / N
> 4 * fraction
> ```
{: .task}

