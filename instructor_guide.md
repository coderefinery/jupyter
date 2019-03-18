# Instructor guide


## Basics of Jupyter

In the first notebook, `basics_of_jupyter.ipynb`, the first half 
is a presentation of what Jupyter and JupyterLab is and what it can do.

For inspiration, the instructor can open in a new tab the gravitational wave webpage with notebooks, and show how they can be launced in the cloud. It's also good to open the "Gallery of interesting Jupyter Notebooks" link to show a flavor of what's out there.

The IDE section is adopted from the retired IDE lesson. The purpose of including it here is that IDEs deserve at least to be discussed. The instructor can ask the audience what, if any, IDEs they are using, and briefly discuss various pros and cons. 

### Type-along exercise

In the interactive type-along exercise, the instructor should explain
clearly:
- How to toggle between code and markdown cells
- Edit mode and Command mode
- How to execute a cell
- How to insert, copy, paste and remove cells
- Get help with ?
- The importance of execution order - discuss prompt numbers.
- How to use keyboard shortcuts efficiently.
- The difference between executing a cell with `Shift-Enter`, `Ctrl-Enter` or `Alt-Enter`.
- One can edit the cell by clicking on it, or pressing `Enter` when it's selected.
- One can run the cell by pressing the play-button in the toolbar, or press `Shift-Enter`.

### Version control of notebooks

There's a paragraph on Git extensions to Jupyter notebooks and JupyterLab (nbdime, jupyterlab-git, jupyterlab/github). It is useful if the instructor has installed and enabled these extensions in order to demostrate how they are used:
- `nbdime`: show how the `git` button works in the notebook (it opens a new window with git diff output)
- `jupyterlab-git`: show how the new Git button on the left menubar works. One can add and commit files, unstage, push and pull, create branches etc.
- `jupyterlab-github`: show how one can browse repositories on GitHub, open online notebooks and run them locally (in local Python environment) or launch them on mybinder.org
