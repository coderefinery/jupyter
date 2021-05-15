# A first computational notebook

```{objectives}
- Get started with notebooks for analysis.
- Get a feeling for the importance of execution order.
```

## Creating a computational narrative

Let's create our first real computational narrative in a Jupyter notebook
(adapted from [Python and R data analysis course](https://github.com/AaltoScienceIT/python-r-data-analysis-course) at Aalto Science IT).

```{figure} img/pi_with_darts.png
:alt: Picture of throwing darts
:width: 30%

Throwing darts to compute pi.
```

Imagine you are on a desert island and wish to compute pi.
You have a computer with you with Python installed but no
math libraries and no Wikipedia.

Here is one way of doing it - "throwing darts" by generating
random points within a square area and checking whether the points
fall within the unit circle.

````{discussion} Hint: Opening a webpage inside JupyterLab
If you would like to copy-paste content from this webpage into your
Jupyter notebook, a cool way of doing it is to open this page inside
an IFrame:
```python
from IPython.display import IFrame
IFrame(src="https://coderefinery.github.io/jupyter/first-notebook/", width='100%', height='500px')
```
````


## Exercise

````{challenge} Exercise/demonstration: Calculating pi using Monte Carlo methods
This can be either done as a 20 minute exercise or as a type-along demo.

1. Create a new notebook, name it, and add a heading.
   ```markdown
   # Calculating pi using Monte Carlo methods
   ```

2. Document the relevant formulas in a new cell:
   ```markdown
   ## Relevant formulas

   - square area: $s = (2 r)^2$
   - circle area: $c = \pi r^2$
   - $c/s = (\pi r^2) / (4 r^2) = \pi / 4$
   - $\pi = 4 * c/s$
   ```

3. Add an image to explain the concept:
   ```markdown
   ## Image to visualize the concept

   ![Darts](https://raw.githubusercontent.com/coderefinery/jupyter/main/example/darts.svg)
   ```

4. Import two modules that we will need:
   ```python
   # importing modules that we will need

   import random
   import matplotlib.pyplot as plt
   ```

5. Initialize the number of points:
   ```python
   # initializing the number of "throws"

   num_points = 1000
   ```

6. "Throw darts":
   ```python
   # here we "throw darts" and count the number of hits

   points = []
   hits = 0
   for _ in range(num_points):
       x, y = random.random(), random.random()
       if x*x + y*y < 1.0:
           hits += 1
           points.append((x, y, "red"))
       else:
           points.append((x, y, "blue"))
   ```

7. Plot results:
   ```python
   # unzip points into 3 lists
   x, y, colors = zip(*points)

   # define figure dimensions
   fig, ax = plt.subplots()
   fig.set_size_inches(6.0, 6.0)

   # plot results
   ax.scatter(x, y, c=colors)
   ```

8. Compute the estimate for pi:
   ```python
   # compute and print the estimate

   fraction = hits / num_points
   4 * fraction
   ```
````

Here is the notebook: <https://github.com/coderefinery/jupyter/blob/main/example/darts.ipynb>
(static version, later we will learn how to share notebooks which are dynamic
and can be modified).

```{instructor-note}
Demonstrate out-of-order execution problems and how to avoid them:
- Add a cell at the end of the notebook which redefines `num_points`
- Then run the cell which computes the pi estimate
- Then demonstrate "run all cells"
```


## Discussion

What do we get from this?

- With code separate from everything else, you might just send one
  number or a plot to your supervisor/collaborator for checking.
- With a notebook as a narratives, you send everything in a **consistent
  story**.
- A reader may still just read the introduction and conclusion, but
  they can easily see more - *and try changes themselves* - if they
  want.

---

```{keypoints}
- Notebooks provide an intuitive way to perform interactive computational work.
- Allows fast feedback in your test-code-refactor loop.
- Cells can be executed in any order, beware of out-of-order execution bugs!
```
