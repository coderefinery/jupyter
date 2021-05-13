# Notebooks and version control

```{questions}
- How can notebooks interact with version control?
- How can we compare and merge notebooks using Git?
```

Jupyter Notebooks are stored in [JSON](https://en.wikipedia.org/wiki/JSON) format, which doesn't play nicely
with Git, but several packages and JupyterLab extensions have been developed
to make it easier:

- [nbdime](http://nbdime.readthedocs.io/) (notebook "diff" and "merge") provides
  "content-aware" diffing and merging.
  - Adds a Git button to the notebook interface.
  - `git diff` and `git merge` shell commands can use nbdime's diff
    and merge for notebook files, but leave Git's behavior unchanged
    for non-notebook files.
- [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git)
  is a JupyterLab extension for version control using Git.
  - Adds a Git tab to the left-side menu bar for version control inside JupyterLab.
- [JupyterLab GitHub](https://www.npmjs.com/package/@jupyterlab/github)
  is a JupyterLab extension for accessing GitHub repositories.
  - Adds a GitHub tab to the left-side menu bar where you can browse
    and open notebooks from your GitHub repositories.

All three extensions can be used from within the JupyterLab interface.

```{discussion} Installing extensions: Is the git interface not showing up?
JupyterLab is modular, and some parts need to be installed as extensions.
In general, either copy and paste installation and configuration commands
into a shell or use the JupyterLab extension manager. See the [installation
instructions](https://coderefinery.github.io/installation/jupyter/).

There are two modes of extension: backend (for the Python server)
and frontend (for the browser).
```

```{challenge} Instructor demonstrates nbdime
1. To understand the problem, the instructor first shows the [example
   notebook](https://github.com/coderefinery/jupyter/blob/main/example/darts.ipynb)
   and then the [source
   code](https://raw.githubusercontent.com/coderefinery/jupyter/main/example/darts.ipynb)
   in JSON format.
2. Then we introduce a simple change to the example notebook, for instance
   changing colors and also changing dimensions in `fig.set_size_inches(6.0,
   6.0)`.
3. We save the change and in the JupyterLab terminal try "normal" `git diff`
   and see that this is not very useful.
4. Then the instructor installs `jupyterlab-git` which also installs
   `nbdime`.
5. We then inspect the same change we did in the Git tab of the JupyterLab
   sidebar.
6. If there is time, we can also show
   [nbdime](https://nbdime.readthedocs.io/) on the command line.
7. We can point out that Git can be configured to always use nbdime for
   notebooks.
```
