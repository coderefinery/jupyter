# JupyterLab and notebook interface

```{objectives}
- Learn to navigate JupyterLab user interface.
- Discuss integrated development environments.
- Get an overview of useful keyboard shortcuts.
- Learn about command/edit modes, markdown/code cells and Git integration.
```

JupyterLab is the next-generation user interface for Jupyter notebooks
and is intended to replace the conventional interface.
It is a highly modular and customizable interface.

Let's have a look at how it works. We go to terminal, and type:
```shell
$ mkdir jupyterlab-demo
$ cd jupyterlab-demo
$ jupyter-lab
```
- On Windows, the JupyterLab App can also be launched by clicking on the JupyterLab icon in the Anaconda menu.

---

## Navigation

- Left-hand menu (toggle it with `Ctrl(⌘)-b`):
     - File browser
         - New launcher
         - New folder
         - Upload files
     - Running terminals and kernels
     - Command palette
     - Cell inspector
     - Open tabs
     - Git integration (if `jupyterlab-git` extension installed)
     - GitHub browser (if `jupyterlab-github` extension installed)
- Fully-fledged terminal
- Text editor for source code in different languages
- Code console to run code interactively in a kernel with rich output and linear order
- Modular interface
     - Notebooks, terminals, consoles, data files etc can be moved around
- Classical notebook style is available under the Help menu

---

## Cells

- **Markdown cells** contain formatted text written in Markdown
- **Code cells** contain code to be interpreted by the *kernel* (Python, R, Julia, Octave/Matlab...)

```{figure} img/notebook_components.png
:alt: Components of a Jupyter notebook

Components of a Jupyter notebook.
```


### Markdown cells

```markdown
## Second level heading

This cell contains simple
[markdown](https://daringfireball.net/projects/markdown/syntax), a simple language for writing text that can be automatically converted to other formats, e.g. HTML, LaTeX or any of a number of others.

**Bold**, *italics*, **_combined_**, ~~strikethrough~~, `inline code`.

* bullet points

or

1. numbered
3. lists

**Equations:**
inline $e^{i\pi} + 1 = 0$
or on new line
$$e^{i\pi} + 1 = 0$$

Images:

![Jupyter logo](https://jupyter.org/assets/main-logo.svg)

Links:
[One of many markdown cheat-sheets](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#emphasis)
```

### Code cells

```python
# a code cell can run statements of code.
# when you run this cell, the output is sent
# from the web page to a back-end process, run
# and the results are displayed to you
print("hello world")
```

Output:
```
hello world
```

### Command and edit modes

- To add contents to a cell, you need to enter *edit mode* by pressing `Enter` or
  double-clicking on a cell
- To navigate between cells, create new cells, etc., you need to enter *command* mode by
  pressing `Escape` key or executing the current cell.

---

## Keyboard shortcuts

Some shortcuts only work in Command or Edit mode.
> Warning: it can happen that these shortcuts interfer with browser shortcuts.

| Cell shortcuts | &nbsp; | Notebook/UI shortcuts | &nbsp; |
| -------- | ------ | -------- | ------ |
| **Shortcut** | **Effect** | **Shortcut** | **Effect** |
| `Enter` | Enter Edit mode | `Ctrl(⌘)`-`s` | Save notebook |
|`Escape` or `Ctrl`-`m` | Enter Command mode | `Shift`-`Ctrl(⌘)`-`s` | Save notebook as |
| `Ctrl`-`Enter` | Run the cell | `Ctrl`-q | Close notebook |
| `Shift`-`Enter`| Run the cell and select the cell below | `Ctrl(⌘)`-`b` | Toggle left-hand menu |
| `Alt`-`Enter`| Run the cell and insert a new cell below | `Shift`-`Ctrl(⌘)`-`c` | Open command palette |
| `m` and `y` | Toggle between Markdown and Code cells | `Shift`-`Ctrl(⌘)`-d | Toggle single-document mode |
| `d-d` | Delete a cell | &nbsp; | &nbsp;|
| `z` | Undo deleting  | &nbsp;| &nbsp;|
| `a/b` | Insert cells above/below current cell  | &nbsp;| &nbsp;|
| `x/c/v` | Cut/copy/paste cells |&nbsp; | &nbsp;|
| `Up/Down` or `k/j` | Select previous/next cells  | &nbsp;| &nbsp;|

---

> ## Discussion point: Integrated development environments
>
> - What tools do you use for developing code?
> - How do you compile or execute code?
> - How do you debug code?
>
> Some people prefer terminal-based text editors for writing code (e.g. vi/vim, nano, emacs, etc).
> Others prefer integrated development environments (IDEs), which can bring "everything" one needs for productive programming to one's fingertips.
> Yet others prefer code editors, which are light-weight IDEs.
>
> | Terminal editor | Code editor | IDE |
> | --------------- | ----------- | --- |
> | Good command line skills are needed for effectively using terminal editors | If you use multiple programming languages then code editors offer good support | If you are working with large code bases, then you should definitely checkout the IDE suitable for your programming language |
> | Continue using Emacs and Vim, if you are already proficient | Both IDE and code editors share common features such as code completion, hints, highlighting sections of code | IDEs offer rich support for Debugging and Code refactoring |
> | Supports multiple programming languages | Supports multiple programming languages | Focused on a single language |
{: .challenge}
