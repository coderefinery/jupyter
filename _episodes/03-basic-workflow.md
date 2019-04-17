---
layout: episode
title: A first computational notebook
teaching: 10
exercises: 0
questions:
 - What does a simple notebook with data analysis look like?
 - Are there any keyboard shortcuts to speed up work?
objectives:
 - Get a feeling for how to get started with notebooks for analysis
keypoints:
 - Keyboard shortcuts can save you time and protect your wrists
 - Cells can be executed in any order, beware of out-of-order execution bugs!
---

# Creating a computational narrative

Let's create our first real computational narrative in a Jupyter notebook.

<img src="{{ site.baseurl }}/img/pi_with_darts.png" width="30%">

Imagine you are on a desert island and wish to compute $\pi$. 
You have a computer with you with Python installed but no 
math libraries and no Wikipedia.

Here is one way of doing it - "throwing darts" by generating 
random points in an interval and checking whether the points 
are within a given radius:

<img src="{{ site.baseurl }}/img/darts.svg" width="30%">

> ## Calculating $\pi$ using monte carlo methods
> 
> 1. Create a new notebook, name it, and add a heading
> 2. Document the relevant formulas in a new cell:
>  ```
>  - square area = $(2 r)^2$
>  - circle area = $\pi r^2$
>  - circle / square = $\pi r^2 / 4 r^2$ = $\pi / 4$
>  - $\pi = (circle/square) * 4$
>  ```
> 
> 3. Import module:
> ```python
> import random
> ```
> 
> 4. Initialize variables:
> ```python
> N = 1000
> points = []
> ```
> 
> 5. "Throw darts":
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
> 6. Plot results:
> ```python
> %matplotlib inline
> from matplotlib import pyplot
> x, y, colors = zip(*points)
> pyplot.scatter(x, y, c=colors)
> ```
> 
> 7. Compute final estimate of $\pi$:
> ```python
> fraction = hits / N
> 4 * fraction
> ```
{: .task}

