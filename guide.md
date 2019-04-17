# Instructor guide


## Basics of Jupyter

In the first notebook, `basics_of_jupyter.ipynb`, the first half 
is a presentation of what Jupyter and JupyterLab is and what it can do.

For inspiration, the instructor can open in a new tab the gravitational wave webpage with notebooks, and show how they can be launched in the cloud. It's also good to open the "Gallery of interesting Jupyter Notebooks" link to show a flavor of what's out there.

The IDE section is adopted from the retired IDE lesson, and is included here as a general 
discussion about IDEs.. The instructor can ask the audience what, if any, IDEs they are using, and briefly discuss various pros and cons. 

### Simple type-along

To show that Jupyter Notebooks are rather simple and intuitive, it is good to 
create a new code cell (e.g. under the Code Cells section) and type some simple code, 
execute it and show that the output is displayed below.  
The type-along exercise in the jupyter-usecases notebook is more advanced so it's good 
to show some simple usage first.

### Version control of notebooks

There's a paragraph on Git extensions to Jupyter notebooks and JupyterLab (nbdime, jupyterlab-git, jupyterlab/github). It is useful if the instructor has installed and enabled these extensions in order to demostrate how they are used:
- `nbdime`: show how the `git` button works in the notebook (it opens a new window with git diff output)
- `jupyterlab-git`: show how the new Git button on the left menubar works. One can add and commit files, unstage, push and pull, create branches etc.
- `jupyterlab-github`: show how one can browse repositories on GitHub, open online notebooks and run them locally (in local Python environment) or launch them on mybinder.org



## Jupyter usecases

### Type-along exercise 1

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

The first 4 steps of the exercise are about the JupyterLab interface and the instructor should 
practice these steps before the workshop. The remaining steps can be performed as follows:

`5. In terminal, change directory to the `word-count` example project (if you don't already have it, clone `https://github.com/coderefinery/word-count.git`). Run `snakemake -s Snakefile_all` (this could be done from notebook too).`

```shell
$ cd ../word-count
$ snakemake -s Snakefile_all
```

`6. In notebook, use a magic to load the word-count project README file at the top, and add a heading.`

```python
%load ../word-count/README.md
```

`7. In notebook, create a directory `zipf-test`, and copy the `word_count/processed_data` folder to it.`

```python
%mkdir zipf-test
%cp -r ../word-count/processed_data zipf_test/
```

`8. Copy-paste the code below to a code cell (pretending that we just wrote it), and save it to a file `zipf.py``

```python
# copy paste the code, and add at the top:
%%writefile zipf.py
```
- The instructor can remove the cell again, mentioning that it's good practice to write tested and finished code to an external module and then import it to notebook:
  ```python
     import zipf
     zipf.top_n_word?
  ```

`9. Run the `zipf_analysis()` function for a processed datafile. Plot the output, and compare with a 1/N function.`

```python
nmax = 10
z = zipf_analysis("processed_data/isles.dat", nmax)
n = range(1,nmax+1)
z_norm = [i/z[0] for i in z]
plt.plot(n,z_norm)

inv_n = [1.0/i for i in n]
plt.plot(n, inv_n)
```


### Type-along exercise 2

Here the instructor should change the code from step 9 above to the following:

```python
import matplotlib.pyplot as plt
from ipywidgets import interact

%matplotlib inline
```

```python
@interact(nmax=(6,14), p=-1.0)
def zipf_plot(nmax, p):
    plt.clf()
    #plt.figure() 
    z = zipf_analysis("processed_data/last.dat", nmax)
    n = range(1,nmax+1)
    z_norm = [i/z[0] for i in z]
    plt.plot(n,z_norm)
    inv_n = [i**p for i in n]
    plt.plot(n, inv_n)
```