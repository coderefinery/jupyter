---
layout: episode
title: Motivation
teaching: 10
exercises: 0
questions:
  - What are Jupyter Notebooks?
  - Why use Jupyter and JupyterLab?
objectives:
  - Learn about the background of Jupyter
  - See a few inspirational use cases of Jupyter
keypoints:
  - K1 
---

# Jupyter notebooks and JupyterLab

## Some history
- In 2014, Fernando Pérez announced a spin-off project from IPython called Project Jupyter, moving the notebook and other language-agnostic parts of IPython to Jupyter
- JupyterLab is the next generation interface for Project Jupyter, the first stable release was announced in February 2018.
- [The popularity of Jupyter is steadily increasing across many sciences](https://www.nature.com/articles/d41586-018-07196-1).
- The name "Jupyter" derives from Julia+Python+R, but today Jupyter kernels exist for [dozens of programming languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
- Galileo's publication in a pamphlet in 1610 in Sidereus Nuncius, one of the first notebooks!  
<img src="http://media.gettyimages.com/photos/pages-from-sidereus-nuncius-magna-by-galileo-galilei-a-book-of-and-picture-id90732970" width="500">

## Why notebooks? 

- A [literate programming](https://en.wikipedia.org/wiki/Literate_programming) tool.
- Code, text, equations, figures, etc. are interleaved, creating a *computational narrative*.
- 

### Common use cases

- Experimenting with new ideas, testing new libraries/databases 
- As an *interactive* development environment for code, data analysis and visualization
- Interactive work on HPC clusters
- Sharing and explaining code to colleagues
- Learning from other notebooks
- Keeping track of interactive sessions, like a digital lab notebook
- Supplementary information with published articles
- Teaching (programming, experimental/theoretical science)
- Slide presentations using [Reveal.js](https://github.com/damianavila/RISE)

### When not to use notebooks

- Less useful for large codebases 
- More difficult to do automated testing on 
- Tricky when it comes to non-linear execution of cells, discipline is needed!


## A case example 

<img src="{{ site.baseurl }}/img/MergingBlackHoles_V2.jpg" width="50%">

Let us have a look at the analysis published together with the discovery of gravitational waves. [This page](https://losc.ligo.org/tutorials/)
lists the available analyses and presents several options to browse them: 
- Download zip-file with source and data
- Open the notebooks on [Microsoft Azure Notebooks](https://notebooks.azure.com/losc/libraries/tutorials) platform.
- Open the notebooks on [mybinder](http://beta.mybinder.org/repo/losc-tutorial/quickview).

Since Microsoft Azure requires a login to run the notebooks live (which is still free), we can try running the "Quickview Notebook" on mybinder, [here's a direct link](http://beta.mybinder.org/repo/losc-tutorial/quickview).

> For further inspiration, head over to the [Gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)




