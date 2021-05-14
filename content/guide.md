# Instructor guide

## Why we teach this lesson

When CodeRefinery started teaching this lesson it was meant to introduce participants
to a cool new tool around which there was a lot of buzz (particularly in data science),
and which could be useful to researchers to quickly prototype code and analyze data in an interactive way.
Since then, more and more participants are already using Jupyter for various purposes
when they come to a workshop.

One purpose of teaching this lesson is still to introduce Jupyter to participants who haven't
used it before. The episodes "Motivation", "The JupyterLab and notebook interface" and
"A first computational notebook" are meant to inspire participants to use notebooks for
certain appropriate tasks, highlighting in particular the "computational narrative" aspect
which is brilliantly enabled by notebooks.

But to cater to participants who already use Jupyter, the lesson also covers
topics which might not be well known, or at least not well used, such as
- version control of Jupyter notebooks through JupyterLab plugins
- widgets for even more interactivity when e.g. analyzing data
- useful magic commands to time, profile and debug code cells
- using notebooks more efficiently, e.g. by keyboard shortcuts and quick access to documentation
- making notebooks reproducible by anyone via Binder

Especially the first and last points connect well with the rest of the CodeRefinery lessons,
and as more and more researchers use notebooks in their daily work it will be important
to focus on these aspects when teaching this lesson.

Finally, the "Examples" episode has a long list of exercises focusing on
different aspects and use cases of notebooks. In workshops where there is enough time
to go into this episode, participants can choose whichever exercises they find interesting.

A key take-home message from this lesson should be that Jupyter notebooks
can be a very useful tool for reproducible research, if used wisely.


## Intended learning outcomes

By the end of this lesson, learners should:
- be able to explain what a computational narrative is
- be able to identify areas of their own work where Jupyter notebooks could be an appropriate tool
- be able to use the JupyterLab user interface somewhat efficiently
- be able to use magics, shell commands and widgets in their own notebooks
- understand that version control is equally important for notebooks as for other code
- know how to version control notebooks efficiently using JupyterLab plugins and the nbdime tool
- realize that notebooks can be used to document scientific analysis, and published
  e.g. as supplementary information with journal articles to aid reproducibility
- know how to share notebooks via Binder
- be able to relate to the possible pitfalls of using notebooks
- be able to distinguish good and bad examples of notebook usage


## Exercises

- "A first computational notebook" can be done either as a 20 minute exercise
  or as a type-along demo.
- "Version control of notebooks" should be done as demonstration.
- "Making your notebooks reproducible by anyone via Binder" should be done as a
  20 minute exercise but can be done as a demo.
- Note that there is an optional exercise for R users who can try to deploy R
  Studio/ R Markdown to Binder.
- The "Examples" episode contains many interesting examples which can be used
  for demonstration or as exercise. The dependencies for ipywidget examples are
  typically tricky to install/enable in a group exercise. Instead they can be
  demonstrated on Binder (there is an optional exercise for this).


## How to teach this lesson

### Motivation

How the instructor introduces and motivates Jupyter notebooks is flexible and
can depend on the instructor's background. The first episode emphasizes the
"computational narrative" aspect of notebooks, and highlights a few
common use cases. The gravitational-wave discovery is used as a motivational
example, and it's helpful if the instructor clicks the Binder link to see how
the notebooks become available for interactive exploration in the cloud.
The instructor should also open the link "Gallery of interesting Jupyter notebooks"
to show the wide variety of notebooks that people have shared online.


### The JupyterLab interface

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

There's a paragraph and an exercise on Git extensions to Jupyter notebooks and JupyterLab
(nbdime, jupyterlab-git, jupyterlab/github). It is useful if the instructor has installed and
enabled these extensions in order to demostrate how they are used:
- `nbdime`: show how the `git` button works in the notebook (it opens a new window with git diff output)
- `jupyterlab-git`: show how the new Git button on the left menubar works. One can add and commit files,
  unstage, push and pull, create branches etc.
- `jupyterlab-github`: show how one can browse repositories on GitHub, open online notebooks and run them
  locally (in local Python environment) or launch them on mybinder.org

After discussing the Git integrations, the instructor should encourage participants to
initialize a Git repo in their notebook directory, and commit the first "testing" notebook.
They can do this via the JupyterLab interface if they have the plugins installed, or via
terminal inside JupyterLab, or via regular terminal.

Take-home messages:
- The JupyterLab interface is flexible and one can customize the workspace by dragging
  notebooks, terminals and text editors around.
- There are code cells and markdown cells that work differently, and there are
  command and edit modes. It's easy to switch between these.
- The Git integration in JupyterLab is powerful and enables tracking notebooks in just
  the same way as one would with source code files.


### A first computational notebook

To show that Jupyter Notebooks are rather simple and intuitive, the third episode
demonstrates the building up of a computational narrative
to compute pi and adding comments, equations and figures.
The instructor should create a new notebook, name it and then type out or copy-paste from the lesson
into notebook cells. Learners should be given time to follow along interactively.

After the notebook is completed, participants and instructor should commit it to the
repository.

Take-home messages:
- Notebooks provide a simple and interactive tool for various kinds of analysis.
- Keyboard shortcuts enable efficient usage. The instructor should clearly
  explain the most common ones for executing cells, creating new cells, changing
  between markdown and code cells, etc.
- The execution order of cells matters, the instructor can demonstrate this by
  going up and down in the notebook.


### Shell commands, magics and widgets

Take-home messages:
- There is more to notebooks than just code.
- Magics and shell commands can be useful for various kinds of workflows, and enable
  users to stay within the notebook instead of jumping to another terminal.
- Widgets add even more interactivity to notebooks.


### Sharing notebooks

This episode has a list of services and tools to share and collaborate on Jupyter
notebooks. The instructor doesn't have to go through each item in the list, but
rather emphasize that many services and tools built around Jupyter exist.

The exercise on making notebooks reproducible via Binder is an important one as
it connects with other lessons and emphasizes the reproducibility benefits of notebooks.
If time allows, the instructor can let participants set up a remote repository on GitHub
for their local notebook repos, and push to the remote. After that they can follow the
exercise steps to obtain a Binder badge to add to their repository README files.
If time is short, the instructor can instead just demonstrate all steps and encourage
participants to try it out themselves later.
