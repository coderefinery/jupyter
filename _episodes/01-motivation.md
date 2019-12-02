---
layout: episode
title: Motivation
teaching: 10
exercises: 0
questions:
  - What are Jupyter Notebooks?
  - What can Jupyter Notebooks be used for?
objectives:
  - Get an idea of the purpose of Jupyter.
  - See some inspirational Jupyter notebooks.
keypoints:
  - Jupyter is an open-source, interactive web tool allowing researchers
    to combine code, output, explanatory text and multimedia resources
    in a single document.
---

# Jupyter Notebooks

## Some history
- In 2014, Fernando Pérez announced a spin-off project from IPython called Project Jupyter, moving the notebook and other language-agnostic parts of IPython to Jupyter.
- The name "Jupyter" derives from Julia+Python+R, but today Jupyter kernels exist for [dozens of programming languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).
- Galileo's publication in a pamphlet in 1610 in Sidereus Nuncius, one of the first notebooks!
<img src="http://media.gettyimages.com/photos/pages-from-sidereus-nuncius-magna-by-galileo-galilei-a-book-of-and-picture-id90732970" width="500">

---

## What are Jupyter notebooks?

- A [literate programming](https://en.wikipedia.org/wiki/Literate_programming) tool.
- Code, text, equations, figures, etc. are interleaved, creating a *computational narrative*.
- [*"an environment in which users execute code, see what happens, modify and repeat in a kind of iterative conversation between researcher and data"*](https://www.nature.com/articles/d41586-018-07196-1)

### Common use cases

- Experimenting with new ideas, testing new libraries/databases
- As an *interactive* development environment for code, data analysis and visualization
- Interactive work on HPC clusters
- Sharing and explaining code to colleagues
- Teaching (programming, experimental/theoretical science)
- Learning from other notebooks
- Keeping track of interactive sessions, like a digital lab notebook
- Supplementary information with published articles
- Slide presentations using [Reveal.js](https://github.com/damianavila/RISE)

### When not to use notebooks

- Less useful for large codebases
- More difficult to do automated testing on
- Tricky when it comes to non-linear execution of cells, discipline is needed
- We will discuss pitfalls later

---

## A case example

<img src="{{ site.baseurl }}/img/MergingBlackHoles_V2.jpg" width="50%">

Let us have a look at the analysis published together with the discovery of gravitational waves. [This page](https://losc.ligo.org/tutorials/)
lists the available analyses and presents several options to browse them:
- Download zip-file with source and data
- Open the notebooks on [Microsoft Azure Notebooks](https://notebooks.azure.com/losc/libraries/tutorials) platform.
- Open the notebooks on [Binder](http://beta.mybinder.org/repo/losc-tutorial/quickview).

Since Microsoft Azure requires a login to run the notebooks live (which is still free), we can try running the "Quickview Notebook" on Binder, [here's a direct link](http://beta.mybinder.org/repo/losc-tutorial/quickview).

> For further inspiration, head over to the [Gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks).
