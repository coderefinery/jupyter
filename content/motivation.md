# Jupyter notebooks

```{objectives}
- Get an idea of the purpose of Jupyter.
- See some inspirational Jupyter notebooks.
```

## Motivation for Jupyter notebooks

```{figure} img/medicean-stars.png
:alt: Galileo's drawings of Jupiter and its Medicean Stars from Sidereus Nuncius
:width: 50%

**One of the first notebooks: Galileo's drawings of Jupiter and its Medicean
Stars** from Sidereus Nuncius. Image courtesy of the History of Science
Collections, University of Oklahoma Libraries (CC-BY).
```

- **Code, text, equations, figures, plots**, etc. are interleaved, creating a *computational narrative*.
- [*"an environment in which users execute code, see what happens, modify and
  repeat in a kind of iterative conversation between researcher and
  data"*](https://www.nature.com/articles/d41586-018-07196-1)
- The name "Jupyter" derives from Julia+Python+R, but today Jupyter kernels
  exist for [dozens of programming languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

---

## Case examples

### [Gravitational wave discovery](https://www.gw-openscience.org/about/)

```{figure} img/gravity.jpg
:alt: Discovery of gravitational waves
:width: 50%

Discovery of gravitational waves.
```

As a case example, let us have a look at the analysis published together with the
discovery of gravitational waves. [This
page](https://losc.ligo.org/tutorials/) lists the available analyses
and presents several options to browse them.

- A quick look at short segments of data can be found at
  [https://github.com/losc-tutorial/quickview](https://github.com/losc-tutorial/quickview)
- The notebook can be opened and interactively explored
  using Binder by clicking the "launch Binder" button.
- How does the Binder instance know which Python packages to load?


### [Activity inequality](http://activityinequality.stanford.edu/) study

```{figure} img/activity_inequality.png
:alt: Stanford Activity Inequality Study
:width: 80%

Stanford Activity Inequality Study.
```

Researchers in the Stanford Activity Inequality Study measured daily
activity from cell phone tracking data for over 700,000 users in
different countries across the world.
- All data and notebooks are available at
  [https://github.com/timalthoff/activityinequality](https://github.com/timalthoff/activityinequality)
- Even without a "launch binder" button, the notebooks can still be
  [launched on Binder](https://mybinder.org/v2/gh/timalthoff/activityinequality/master)
  (you may see an error "missing R kernel" because a file `runtime.txt` is missing - more about that later)
- Do you see any potential problems in recreating e.g.
  [fig3bc](https://github.com/timalthoff/activityinequality/blob/master/fig3/fig3bc.ipynb)?


### More examples

For further inspiration, head over to the
[Gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks).

---

## Use cases


- Really good for **linear workflows** (e.g. read data, filter data, do some statistics, plot the results)
- Experimenting with new ideas, testing new libraries/databases
- As an *interactive* development environment for code, data analysis, and visualization
- Interactive work on HPC clusters
- Sharing and explaining code to colleagues
- Teaching (programming, experimental/theoretical science)
- Learning from other notebooks
- Keeping track of interactive sessions, like a **digital lab notebook**
- **Supplementary information with published articles**
- Slide presentations using [Reveal.js](https://github.com/damianavila/RISE)


## Pitfalls

- Programs with non-linear code flow
- Large codebase (however it can make sense to use Jupyter as interface to the large codebase and import the codebase as a module)
- You cannot easily write a notebook directly in your text editor (but you can do
  that with [R Markdown](https://rmarkdown.rstudio.com/))
- Notebooks can be **version controlled**
  ([nbdime](https://nbdime.readthedocs.io/) helps with that), but
  there are **still limitations**.
- Notebooks **aren't named by default** and tend to **acquire a bunch of
  unrelated stuff**.  Be careful with organization!
- See also <https://scicomp.aalto.fi/scicomp/jupyter-pitfalls/>.


## Good practices

- Rename notebooks from "Untitled.ipynb".
- Run all cells before sharing/saving to verify that the results you see on your
  computer were not due to cells being run out of order (we will try this later).
