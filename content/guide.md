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

After the first three episodes the focus shifts to topics related to version control ("Notebooks and version control"), open science and reproducibility ("Sharing notebooks") which connects to topics covered in other CodeRefinery lessons.

There are also two optional episodes, "Shell commands, magics and widgets" and "Additional exercises" 
which go through various features and use-cases of Jupyter.

A key take-home message from this lesson should be that Jupyter notebooks
can be a very useful tool for reproducible research, if used wisely.


## Intended learning outcomes

By the end of this lesson, learners should:
- be able to explain what a computational narrative is
- be able to identify areas of their own work where Jupyter notebooks could be an appropriate tool
- be able to use the JupyterLab interface efficiently
- understand that version control is equally important for notebooks as for other code
- know how to version control notebooks efficiently using JupyterLab plugins 
- know that notebooks can be used to document scientific analysis, and published
  e.g. as supplementary information with journal articles to aid reproducibility
- know how to share notebooks via Binder
- understand possible pitfalls of using notebooks


## Timing and lesson placement

### Detailed schedule

- 12:00 - 12:10 [Jupyter notebooks](https://coderefinery.github.io/jupyter/motivation/)
- 12:10 - 12:15 [JupyterLab and notebook interface](https://coderefinery.github.io/jupyter/interface/)
- 12:15 - 12:35 [A first computational notebook](https://coderefinery.github.io/jupyter/first-notebook/)
  - [Exercise (20 min)](https://coderefinery.github.io/jupyter/first-notebook/#an-example-computational-notebook)
- 12:35 - 12:50 [Notebooks and version control demo](https://coderefinery.github.io/jupyter/version-control/)
- 12:50 - 12:55 [Sharing notebooks](https://coderefinery.github.io/jupyter/sharing/)
- 12:55 - 13:05 Break
- 13:05 - 13:25 [Binder exercise (20 min)](https://coderefinery.github.io/jupyter/sharing/#sharing-dynamic-notebooks-on-binder)
- 13:25 - 13:30 Wrap-up


## Exercises

- "A first computational notebook" can be done either as a 20 minute exercise
  or as a type-along demo.
- "Instructor demonstrates a plain git diff" should be done as demonstration.
- "Making your notebooks reproducible by anyone via Binder" should be done as a
  20 minute exercise but can also be done as a demo.
- There are three optional exercises in "Sharing notebooks", one on trying to reproduce 
  results from a published notebook, another on sharing an interactive notebook on Binder, 
  and one for R users who can try to deploy R   Studio/ R Markdown to Binder.
- The "Examples" episode contains many interesting examples which can be used
  for demonstration or as exercises. The dependencies for ipywidget examples are
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

Take-home messages:
- The JupyterLab interface is flexible and one can customize the workspace by dragging
  notebooks, terminals and text editors around.
- There are code cells and markdown cells that work differently, and there are
  command and edit modes. It's easy to switch between these.



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


### Notebooks and version control 

After discussing the Git integrations, the instructor should encourage participants to
initialize a Git repo in their notebook directory, and commit the first "testing" notebook.
They can do this via the JupyterLab interface if they have the plugins installed, or via
terminal inside JupyterLab, or via regular terminal.

Take home message: The Git integration in JupyterLab is powerful and enables tracking 
notebooks in just the same way as one would with source code files.

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



### (Optional) Shell commands, magics and widgets

Take-home messages:
- There is more to notebooks than just code.
- Magics and shell commands can be useful for various kinds of workflows, and enable
  users to stay within the notebook instead of jumping to another terminal.
- Widgets add even more interactivity to notebooks.


### (Optional) Additional exercises

Interesting and fun exercises to learn about various Jupyter features and use cases.
