---
layout: episode
title: Sharing notebooks
teaching: 10
exercises: 0
questions:
 - How can I share notebooks with colleagues and the community?
objectives:
 - See what platforms and services exist to share Jupyter notebooks.
 - Have a final discussion on notebooks in research.
---

# Sharing notebooks

- You can enter a URL, GitHub repo or username, or GIST ID in [`nbviewer`](https://nbviewer.jupyter.org/) and view a rendered Jupyter notebook
- Read the Docs can render Jupyter Notebooks via the [nbsphinx package](https://nbsphinx.readthedocs.io/)
- [Binder](https://mybinder.org/) creates live notebooks based on a GitHub repository
- [EGI Notebooks](https://notebooks.egi.eu) (see also [https://egi-notebooks.readthedocs.io](https://egi-notebooks.readthedocs.io))
- [JupyterLab](https://github.com/jupyterlab/jupyterlab) supports sharing and collaborative editing of notebooks via Google Drive
- [Notedown](https://github.com/aaren/notedown), [Jupinx](https://github.com/QuantEcon/sphinxcontrib-jupyter) and [DocOnce](https://github.com/hplgit/doconce) can take Markdown or Sphinx files and generate Jupyter Notebooks
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

---

> ## Exercise: Making your notebooks reproducible by anyone via [Binder](https://mybinder.org)
>
> - Create a `requirements.txt` file in your notebook repository, e.g.:
>   ```
>   ipywidgets==7.4.2
>   numpy==1.16.4
>   matplotlib==3.1.0
>   ```
> - Commit and push.
> - Visit [https://mybinder.org](https://mybinder.org), and paste in
>   the URL of your notebook repository.
> - Click on the arrow next to the "Copy the text below ..." to expand it.
> - Copy the markdown line which begins with `[![Binder](https://mybinder.org/badge_logo.svg)]`, and paste it into a README.md file for your
>   notebook repository. Commit and push it.
> - Check that your notebook repository now has a "launch binder"
>   button in your README file on GitHub
> - Try clicking the button and see how your repository in launched
>   on Binder. Your notebooks can now be expored and executed in the cloud.
> - Enjoy being fully reproducible!
> - As a side note you can also run RStudio directly on Binder ([example](https://github.com/bast/rstudio-on-binder)).
{: .challenge}

> ## (Optional) Exercise: what happens without requirements.txt?
>
> Let's look at the same [activity inequality
> repository](https://github.com/timalthoff/activityinequality).  We
> can start this repository [in Binder by using this
> link](https://mybinder.org/v2/gh/timalthoff/activityinequality/master).
>
> - Start the repository in Binder
> - `fig3/fig3bc.ipynb` is a Python notebook, so works in Binder.
>   Most others are in R, which also works in Binder.  [But
>   how?](https://mybinder.readthedocs.io/en/latest/howto/languages.html)
>   Try to run the notebook - can you make it work?
> - Install the missing requirements with `pip`.  Does it work now?
>   Why or why not?
> - How would this be better?
{: .challenge}

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


But Notebooks have some [pitfalls](https://scicomp.aalto.fi/scicomp/jupyter-pitfalls.html):

- They **don't promote modularity**, and once you get started in a
  notebook it can be hard to migrate to modules.
- They are **difficult to test**.  There are things to run notebooks as
  unit tests like [nbval](https://nbval.readthedocs.io/), but it's not
  perfect.
- Notebooks can be **version controlled**
  ([nbdime](https://nbdime.readthedocs.io/) helps with that), but
  there are **still limitations**.
- You can **change code after you run it** and run code out of order.
  This can make debugging hard and results irreproducible if you
  aren't careful.
- Notebooks **aren't named by default** and tend to **acquire a bunch of
  unrelated stuff**.  Be careful with organization!
- Once lots of code is in notebooks, it can be **hard to change to
  proper programs that can be scripted**.
