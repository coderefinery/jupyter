# JupyterLab and notebook interface

```{objectives}
- Learn to navigate JupyterLab user interface.
- Discuss integrated development environments.
- Get an overview of useful keyboard shortcuts.
- Learn about command/edit modes and markdown/code cells.
```

```{instructor-note}
- 15 min teaching
- 0 min exercises
```

JupyterLab is the next-generation user interface for Jupyter Notebooks
and is intended to replace the conventional interface.
It is a highly modular and customizable interface.

---

## How to start JupyterLab

Let's have a look at how it works. We go to terminal, and type:
```console
$ mkdir jupyterlab-demo
$ cd jupyterlab-demo
$ jupyter-lab
```

---

## Components: the big picture

```{figure} img/notebook_components.png
:alt: Components of a Jupyter notebook

Components of a Jupyter notebook.
```

---

## Navigation

```{figure} img/JupyterInterface.png
:alt: Jupyter used interface has a file browser and a notebook view
:width: 100%

Jupyter Lab user interface has a left side toolbar – that has a file browser and a git tab. The file browser shows the file that Jupyter Lab was opened in. The right side shows the files that are open. You can have split view by dragging from the top tab view. (CC-BY)
```

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

![Jupyter logo](https://jupyter.org/assets/homepage/main-logo.svg)

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


### Command and edit modes

- To add contents to a cell, you need to enter *edit mode* by pressing `Enter` or
  double-clicking on a cell
- To navigate between cells, create new cells, etc., you need to enter *command* mode by
  pressing `Escape` key or executing the current cell.

---

## Keyboard shortcuts

Some shortcuts only work in Command or Edit mode.
It can also happen that these shortcuts interfere with browser shortcuts.


### Cell shortcuts

| Shortcut | Effect |
| -------- | ------ |
| `Enter` | Enter Edit mode |
|`Escape` or `Ctrl`-`m` | Enter Command mode |
| `Ctrl`-`Enter` | Run the cell |
| `Shift`-`Enter`| Run the cell and select the cell below |
| `Alt`-`Enter`| Run the cell and insert a new cell below |
| `m` and `y` | Toggle between Markdown and Code cells |
| `d-d` | Delete a cell |
| `z` | Undo deleting  |
| `a/b` | Insert cells above/below current cell |
| `x/c/v` | Cut/copy/paste cells |
| `Up/Down` or `k/j` | Select previous/next cells |


### Notebook shortcuts

| Shortcut | Effect |
| -------- | ------ |
| `Ctrl(⌘)`-`s` | Save notebook |
| `Shift`-`Ctrl(⌘)`-`s` | Save notebook as |
| `Ctrl`-q | Close notebook |
| `Ctrl(⌘)`-`b` | Toggle left-hand menu |
| `Shift`-`Ctrl(⌘)`-`c` | Open command palette |
| `Shift`-`Ctrl(⌘)`-d | Toggle single-document mode |

---

(integrated-development-environments)=

### Tools for writing, testing and debugging code

```{admonition} What tools do you use for writing, testing, and debugging code?
Some people prefer **terminal-based text editors** for writing code (e.g. Vi/Vim, Nano, Emacs, etc.).

Others prefer **integrated development environments (IDEs)**,
which can bring "everything" one needs for productive programming to one's fingertips.a

Yet others prefer **code editors**, which are light-weight IDEs.

**Terminal editor**
- Good command line skills are needed for effectively using terminal editors
- Continue using Emacs and Vim, if you are already proficient
- Supports multiple programming languages

**IDE**
- If you are working with large code bases, then you should definitely checkout the IDE suitable for your programming language
- IDEs offer rich support for Debugging and Code refactoring
- Focused on a single language

**Code editor**
- If you use multiple programming languages then code editors offer good support
- Both IDE and code editors share common features such as code completion, hints, highlighting sections of code
- Supports multiple programming languages
```
