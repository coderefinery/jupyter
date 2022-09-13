# Notebooks and version control

```{objectives}
- Demonstrate two tools which make version control of notebooks easier.
```

```{instructor-note}
- 10 min teaching
- 5 min exercises
```

Jupyter Notebooks are stored in [JSON](https://en.wikipedia.org/wiki/JSON) format.
With this format it can be a bit difficult to compare and merge changes which are introduced
through the notebook interface.


## Packages and JupyterLab extensions to simplify version control

Several packages and JupyterLab extensions have been developed
to make it easier to interact with Git and GitHub:

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
[jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) is installed as part
of our [Conda environment](https://coderefinery.github.io/installation/conda-environment/).
[nbdime](http://nbdime.readthedocs.io/) is also already installed in this environment since
it is a dependency of jupyterlab-git.

To install additional extensions, please consult the
[official documentation](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html)
about installing and managing JupyterLab extensions.


## Comparing changes without jupyterlab-git/nbdime

```{instructor-note}
- Create a new folder
- Initialize a new Git repository (which is anyway good to demonstrate)
- Copy the "darts" notebook into it (from the previous episode)
- Add `.ipynb_checkpoints/` to `.gitignore`
- Stage and commit the file before trying the changes below
```

(plain-git-diff)=

### A plain git diff

```{exercise} Instructor demonstrates a plain git diff
1. To understand the problem, the instructor first shows the [example
   notebook](https://github.com/coderefinery/jupyter/blob/main/example/darts.ipynb)
   and then the [source
   code](https://raw.githubusercontent.com/coderefinery/jupyter/main/example/darts.ipynb)
   in JSON format.
2. Then we introduce a simple change to the example notebook, for instance
   changing colors (change "red" and "blue" to something else)
   and also changing dimensions in `fig.set_size_inches(6.0, 6.0)`.
3. Run all cells.
4. We save the change (save icon) and in the JupyterLab terminal try a "normal" `git diff`
   and see that this is not very useful. Discuss why.
```


## Comparing changes with jupyterlab-git/nbdime

Let us inspect the same changes using jupyterlab-git (which uses nbdime).
This is more convenient since it highlights only the changes that we have made:

```{figure} img/git.jpg
:alt: Comparing changes with jupyterlab-git/nbdime

Comparing changes with jupyterlab-git/nbdime. Click on the Git tab, then on the plus-minus symbol.
```


## Using nbdime on the command line

You can configure your (command line) Git to always use nbdime when comparing and merging notebooks:
```console
$ nbdime config-git --enable --global
```
Now when you do git diff or git merge with notebooks, you should see a nice diff view.
For more information please see the
[corresponding documentation](https://nbdime.readthedocs.io/en/latest/#git-integration-quickstart).
