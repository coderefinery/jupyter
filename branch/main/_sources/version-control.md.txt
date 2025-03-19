# Notebooks and version control

```{objectives}
- Demonstrate two tools which make version control of notebooks easier.
```

```{instructor-note}
- 10 min teaching
- 5 min demo
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

All three extensions can be used from within the JupyterLab interface and our
[Conda
environment](https://coderefinery.github.io/installation/conda-environment/)
provides [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) and
[nbdime](http://nbdime.readthedocs.io/).  To install additional extensions,
please consult the [official
documentation](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html)
about installing and managing JupyterLab extensions.

---

## Comparing Jupyter Notebooks on GitHub

For this you really want to enable [Rich Jupyter Notebook
Diffs](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#working-with-jupyter-notebook-files-on-github)
on GitHub:
- On GitHub click on your avatar/image (top right).
- Click on "Feature preview".
- Enable "Rich Jupyter Notebook Diffs".

To demonstrate the difference we have created a small change and you can try to
compare the effect yourself by enabling/disabling the feature:
<https://github.com/coderefinery/jupyter/compare/5ff55b8..fce21e6>

Here is the diff **without "Rich Jupyter Notebook Diffs"**:
```{figure} img/github-without-rich-diff.png
:alt: A small change but without "Rich Jupyter Notebook Diffs"
:width: 100%
:class: with-border

A small change in a notebook viewed on GitHub
without "Rich Jupyter Notebook Diffs" (truncated).
```

Here is the same change, but this time **with "Rich Jupyter Notebook Diffs" enabled**:
```{figure} img/github-with-rich-diff.png
:alt: A small change in a notebook viewed on GitHub with "Rich Jupyter Notebook Diffs" enabled
:width: 100%
:class: with-border

The same change viewed on GitHub, this time
with "Rich Jupyter Notebook Diffs" enabled.
```

---

## Comparing changes locally without jupyterlab-git/nbdime

(plain-git-diff)=

```{instructor-note}
- Create a new folder
- Initialize a new Git repository (which is anyway good to demonstrate)
- Copy the "darts" notebook into it (from the previous episode)
- Add `.ipynb_checkpoints/` to `.gitignore`
- Stage and commit the file before trying the changes below
```

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

---

## Comparing changes with jupyterlab-git/nbdime

Let us inspect the same changes using jupyterlab-git (which uses nbdime).
This is more convenient since it highlights only the changes that we have made:

```{figure} img/git.jpg
:alt: Comparing changes with jupyterlab-git/nbdime

Comparing changes with jupyterlab-git/nbdime. Click on the Git tab, then on the plus-minus symbol.
```

---

## Using nbdime on the command line

You can configure your (command line) Git to always use nbdime when comparing and merging notebooks:
```console
$ nbdime config-git --enable --global
```
Now when you do git diff or git merge with notebooks, you should see a nice diff view.
For more information please see the
[corresponding documentation](https://nbdime.readthedocs.io/en/latest/#git-integration-quickstart).

---

## See also

- [nbdev](https://nbdev.fast.ai/getting_started.html) developed by [fast.ai](https://www.fast.ai/)
  is a notebook-driven development platform which includes support for [git-friendly Jupyter
  notebooks](https://nbdev.fast.ai/tutorials/git_friendly_jupyter.html)
- [Verdant](https://github.com/mkery/Verdant/) is a JupyterLab extension that automatically
  records history of all experiments you run in a Jupyter notebook, and stores them in an
  `.ipyhistory` JSON file.
