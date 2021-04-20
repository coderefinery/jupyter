# Sharing notebooks

```{questions}
 - How can I share notebooks with colleagues and the community?
```

```{objectives}
 - See what platforms and services exist to share Jupyter notebooks.
 - Have a final discussion on notebooks in research.
```


- You can enter a URL, GitHub repo or username, or GIST ID in [`nbviewer`](https://nbviewer.jupyter.org/) and view a rendered Jupyter notebook
- Read the Docs can render Jupyter Notebooks via the [nbsphinx package](https://nbsphinx.readthedocs.io/)
- [Binder](https://mybinder.org/) creates live notebooks based on a GitHub repository
- [EGI Notebooks](https://notebooks.egi.eu) (see also [https://egi-notebooks.readthedocs.io](https://egi-notebooks.readthedocs.io))
- [JupyterLab](https://github.com/jupyterlab/jupyterlab) supports sharing and collaborative editing of notebooks via Google Drive
- [Notedown](https://github.com/aaren/notedown), [Jupinx](https://github.com/QuantEcon/sphinxcontrib-jupyter) and [DocOnce](https://github.com/hplgit/doconce) can take Markdown or Sphinx files and generate Jupyter Notebooks
- [Voilà](https://voila.readthedocs.io/en/stable/) allows you to convert a Jupyter Notebook into an interactive dashboard
- The `jupyter nbconvert` tool can convert a (`.ipynb`) notebook file to:
    - python code (`.py` file)
    - an HTML file
    - a LaTeX file
    - a PDF file
    - a slide-show in the browser


## Commercial offers with free plans

These platforms can be used free of charge but have paid subscriptions for
faster access to cloud resources:

- [CoCalc](https://cocalc.com/) (formerly SageMathCloud) allows collaborative editing of notebooks in the cloud
- Google's [colaboratory](https://colab.research.google.com/) lets you work on notebooks in the cloud, and you can [read and write to notebook files on Drive](https://colab.research.google.com/notebooks/io.ipynb)
- [Microsoft Azure Notebooks](https://notebooks.azure.com/) also offers free notebooks in the cloud
- [Deepnote](https://deepnote.com/) allows real-time collaboration

---

````{challenge} Exercise (20 min): Making your notebooks reproducible by anyone via [Binder](https://mybinder.org)
- Create a GitHub repository.
- Push the notebook which we have created earlier to this repository. If you got stuck earlier,
  you can fork this repository: <https://github.com/coderefinery/jupyter> (our example notebook is under `example`)
- Create a `requirements.txt` file which contains:
  ```
  matplotlib==3.1.0
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
````

````{challenge} (Optional) Exercise: what happens without requirements.txt?
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

````{challenge} (Optional) Exercise: share an interactive (ipywidgets) notebook via [Binder](https://mybinder.org)
- Take one of these two notebooks:
   - the example <https://coderefinery.github.io/jupyter/04-extra-features/#playing-around-with-a-widget>
   - or solution from <https://coderefinery.github.io/jupyter/05-examples/#widgets-for-interactive-data-fitting>
- Push it to a GitHub/GitLab repository (you can also add both files to the same repository).
- Create a `requirements.txt` file in your notebook repository, e.g.:
  ```
  ipywidgets==7.4.2
  numpy==1.16.4
  matplotlib==3.1.0
  ```
- Try to deploy this example via Binder in the same way as the above exercise.
````

````{challenge} (Optional) Exercise: share R Markdown/R Studio project via [Binder](https://mybinder.org)
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
  `https://mybinder.org/v2/gh/myuser/myrepo/mybranch?urlpath=rstudio` (adapt
  "myuser", "myrepo", and "mybranch").
- For more information, see [this guide](https://github.com/alan-turing-institute/the-turing-way/blob/master/workshops/boost-research-reproducibility-binder/workshop-presentations/zero-to-binder-r.md).
````

---

## Recommendations for longer notebooks

### Create a table of contents on top

You can do that using Markdown. This produces a nice overview for longer notebooks.
Example: [https://stackoverflow.com/a/39817243](https://stackoverflow.com/a/39817243)


### How to make it possible to toggle showing code

It is possible to hide all the code and only show the output. This can be nice
for notebook readers who don't need/want to see the code:

```
from IPython.display import HTML

HTML('''<script>
code_show=true;
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
}
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')
```

---

## Final discussion

- If you are already using Jupyter, what tasks do you use it for?
- If you are new to Jupyter, do you see any possible use cases?
- Do you think Jupyter Notebooks can help tackle the problem of irreproducible results?
