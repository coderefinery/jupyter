# Instructor guide


## Motivation

How the instructor introduces and motivates Jupyter notebooks is flexible and 
can depend on the instructor's background. The first episode emphasizes the 
"computational narrative" aspect of notebooks, and highlights a few 
common use cases. The gravitational-wave discovery is used as a motivational 
example, and it's helpful if the instructor clicks the mybinder link to see how 
the notebooks become available for interactive exploration in the cloud.
The instructor should also open the link "Gallery of interesting Jupyter notebooks"
to show the wide variety of notebooks that people have shared online.


## The JupyterLab interface

The second episode deals with the JupyterLab interface and how notebooks work. At 
this stage the instructor should open Jupyter-Lab, demonstrate the 
interface by clicking around and then launch a new notebook. Inside this notebook 
the instructor can add headings and text and a simple code cell to illustrate 
how cells work (copy-pasting from the lesson works well). A few important keyboard 
shortcuts can be demonstrated.

There is a discussion point on integrated development environments. This can 
be used as a discussion exercise, where participants are invited to talk about 
their prefered way to write code. The instructur can mention that JupyterLab is 
sort of like an IDE for notebooks.

There's a paragraph on Git extensions to Jupyter notebooks and JupyterLab (nbdime, jupyterlab-git, jupyterlab/github). It is useful if the instructor has installed and enabled these extensions in order to demostrate how they are used:
- `nbdime`: show how the `git` button works in the notebook (it opens a new window with git diff output)
- `jupyterlab-git`: show how the new Git button on the left menubar works. One can add and commit files, unstage, push and pull, create branches etc.
- `jupyterlab-github`: show how one can browse repositories on GitHub, open online notebooks and run them locally (in local Python environment) or launch them on mybinder.org

Take-home messages:
- The JupyterLab interface is flexible and one can customize the workspace by dragging 
  notebooks, terminals and text editors around.
- There are code cells and markdown cells that work differently, and there are 
  command and edit modes. It's easy to switch between these.
- The Git integration in JupyterLab is powerful and enables tracking notebooks in just 
  the same way as one would with source code files.

## Simple type-along

To show that Jupyter Notebooks are rather simple and intuitive, the third episode
demonstrates the building up of a computational narrative 
to compute pi and adding comments, equations and figures. 
The instructor should create a new notebook, name it and then copy-paste from the lesson 
into notebook cells. Learners should be given time to follow along interactively.

Take-home messages:
- Notebooks provide a simple and interactive tool for various kinds of analysis. 
- Keyboard shortcuts enable efficient usage. The instructor should clearly
  explain the most common ones for executing cells, creating new cells, changing 
  between markdown and code cells, etc.
- The execution order of cells matters, the instructor can demonstrate this by 
  going up and down in the notebook.


## Magics, shell commands, widgets

Take-home messages:
- There is more to notebooks than just code.
- Magics and shell commands can be useful for various kinds of workflows, and enable 
  users to stay within the notebook instead of jumping to another terminal.
- Widgets add even more interactivity to notebooks.





