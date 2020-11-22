---
layout: episode
title: Notebooks and version control
teaching: 15
exercises: 0
questions:
 - How can notebooks interact with version control?
 - How can we compare and merge notebooks using Git?
---

# Version control of notebooks

> ## Working with Git from JupyterLab
>
> 1. Make sure that you have installed the [Git extension](https://coderefinery.github.io/installation/jupyter/#git-extension) for JupyterLab.
> 2. Initialize a Git repository from the top Git menu.
> 3. Save the computing-pi notebook and use the left-hand Git menu to stage and commit it.
> 4. Go to GitHub and create a new repository, e.g. jupyterlab-demo.
> 5. Open a terminal inside JupyterLab and set the remote, e.g.
>   `git remote add origin https://github.com/user/jupyterlab-demo.git`
>   You can use the option "Open Git Repository in Terminal" in the top level Git menu.
> 6. The first push needs to be done via terminal (to set the upstream
>   branch for our local master branch):
>   `git push -u origin master`
> 7. Future pushes (and pulls) can be done from the left-hand Git menu.
> 8. Make another change to the notebook and save it, and click the
>   `git` button in the notebook menu bar (or the Diff button in the left-side Git menu).
{: .challenge}

---

Jupyter Notebooks are stored in json format, which doesn't play nicely
with Git, but several packages and JupyterLab extensions have been developed
to make it easier:

- [nbdime](http://nbdime.readthedocs.io/en/latest/) provides
  "content-aware" diffing and merging.
  - Adds a Git button to the notebook interface.
  - `git diff` and `git merge` shell commands will use nbdime's diff
    and merge for notebook files, but leave Git's behavior unchanged
    for non-notebook files.
- [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git)
  is a JupyterLab extension for version control using Git.
  - Adds a Git tab to the left-side manubar for version control inside JupyterLab.
- [jupyterlab/github](https://www.npmjs.com/package/@jupyterlab/github)
  is a JupyterLab extension for accessing GitHub repositories.
  - Adds a GitHub tab to the left-side manubar where you can browse
    and open notebooks from your GitHub repositories.

All three extensions can be used from within the JupyterLab interface.

> ## Installing extensions: Is the git interface not showing up?
>
> JupyterLab is modular, and some parts need to be installed as extensions.
> In general, either copy and paste installation and configuration commands
> into a shell or use the JupyterLab extension manager. See the [installation
> instructions](https://coderefinery.github.io/installation/jupyter/).
>
> There are two modes of extension: backend (for the Python server)
> and frontend (for the browser).
>
{: .discussion}

