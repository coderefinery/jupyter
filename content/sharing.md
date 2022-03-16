# Sharing notebooks

```{objectives}
- Learn how to share notebooks with colleagues and the community?
```

```{instructor-note}
- 10 min teaching
- 20 min exercises
```

---

(reproducible-via-binder)=

## Sharing dynamic notebooks on [Binder](https://mybinder.org)

````{exercise} Exercise (20 min): Making your notebooks reproducible by anyone via Binder
- Create a new GitHub repository.
- Commit and push the notebook which we have created earlier to this repository. If you got stuck earlier,
  you can download [this notebook](https://raw.githubusercontent.com/coderefinery/jupyter/main/example/darts.ipynb)
  (right-click, "Save as ..."). You can also try [Binder](https://mybinder.org) with a different notebook.
- Create a `requirements.txt` file which contains (adapt this if your notebook has other dependencies):
  ```
  matplotlib==3.4.1
  ```
- Commit and push also this file to your notebook repository.
- Visit [https://mybinder.org](https://mybinder.org):
  ```{figure} img/binder.jpg
  :alt: Screenshot of Binder web interface

  Screenshot of Binder web interface.
  ```
- Check that your notebook repository now has a "launch binder"
  badge in your `README.md` file on GitHub.
- Try clicking the button and see how your repository is launched
  on Binder (can take a minute or two). Your notebooks can now be expored and executed in the cloud.
- Enjoy being fully reproducible!
- Even better would be to get a DOI to your notebook and point Binder to the DOI.
````

```{keypoints} More examples with Binder:
- [Binder documentation](https://mybinder.readthedocs.io/en/latest/introduction.html)
- [Collection of example repositories](https://github.com/binder-examples)
```


## Optional exercises

(without-requirements)=

### Importance of requirements file

````{exercise} (Optional) Exercise: what happens without requirements.txt?
Let's look at the same [activity inequality
repository](https://github.com/timalthoff/activityinequality).  We
can start this repository [in Binder by using this
link](https://mybinder.org/v2/gh/timalthoff/activityinequality/master).

- Start the repository in Binder
- `fig3/fig3bc.ipynb` is a Python notebook, so works in Binder.
  Most others are in R, which also works in Binder.  [But
  how?](https://mybinder.readthedocs.io/en/latest/howto/languages.html)
  Try to run the notebook - can you make it work?
- Install the missing requirements with `pip`.  Does it work now?
  Why or why not?
- How would this be better?
````

(share-widget)=

### Sharing an interactive notebook on Binder

````{exercise} (Optional) Exercise: share an interactive (ipywidgets) notebook via Binder
- Take the solution from the exercise "Widgets for interactive data fitting" in the "Examples" 
  episode and paste it into a notebook.
- Push the notebook to a GitHub/GitLab repository.
- Create a `requirements.txt` file in your notebook repository, e.g.:
  ```
  ipywidgets==7.4.2
  numpy==1.16.4
  matplotlib==3.1.0
  ```
- Try to deploy this example via Binder in the same way as the above exercise.
````

(r-project-binder)=

### Sharing R Markdown/Studio projects

````{exercise} (Optional) Exercise: share R Markdown/R Studio project via Binder
This exercise is for those who use Rmd files instead of Jupyter notebooks.
- Put your Rmd file into a GitHub repository.
- To this repository add a file `runtime.txt` which specifies the R version you want to use:
  ```
  r-3.6-2020-10-13
  ```
- To this repository add a file `install.R` which lists the dependencies, for instance:
  ```
  install.packages(c("readr", "ggplot2"))
  ```
- After you have done that, visit
  https://mybinder.org/v2/gh/myuser/myrepo/mybranch?urlpath=rstudio (adapt
  "myuser", "myrepo", and "mybranch").
- For more information, see [this guide](https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder-r.md).
````

---

## Different ways to share a notebook

- You can enter a URL, GitHub repo or username, or GIST ID in [nbviewer](https://nbviewer.jupyter.org/) and view a rendered Jupyter notebook
- Read the Docs can render Jupyter Notebooks via the [nbsphinx package](https://nbsphinx.readthedocs.io/)
- [Binder](https://mybinder.org/) creates live notebooks based on a GitHub repository
- [EGI Notebooks](https://notebooks.egi.eu) (see also https://egi-notebooks.readthedocs.io)
- [JupyterLab](https://github.com/jupyterlab/jupyterlab) supports sharing and collaborative editing of notebooks via Google Drive. Recently
  it also added support for [Shared editing with collaborative notebook model](https://github.com/jupyterlab/jupyterlab/pull/10118).
- [Notedown](https://github.com/aaren/notedown), [Jupinx](https://github.com/QuantEcon/sphinxcontrib-jupyter) and [DocOnce](https://github.com/hplgit/doconce) can take Markdown or Sphinx files and generate Jupyter Notebooks
- [Voilà](https://voila.readthedocs.io/en/stable/) allows you to convert a Jupyter Notebook into an interactive dashboard
- The `jupyter nbconvert` tool can convert a (`.ipynb`) notebook file to:
    - python code (`.py` file)
    - an HTML file
    - a LaTeX file
    - a PDF file
    - a slide-show in the browser


### Commercial offers with free plans

These platforms can be used free of charge but have paid subscriptions for
faster access to cloud resources:

- [CoCalc](https://cocalc.com/) (formerly SageMathCloud) allows collaborative editing of notebooks in the cloud
- Google's [colaboratory](https://colab.research.google.com/) lets you work on notebooks in the cloud, and you can [read and write to notebook files on Drive](https://colab.research.google.com/notebooks/io.ipynb)
- [Microsoft Azure Notebooks](https://notebooks.azure.com/) also offers free notebooks in the cloud
- [Deepnote](https://deepnote.com/) allows real-time collaboration
