---
layout: episode
title: Notebook features
teaching: 10
exercises: 0
questions:
 - Is there anything extra besides code, text and output?
objectives:
 - Learn how to use magics and shell commands
 - Learn how to use widgets
keypoints:
 - K1
---

## Extra features

---

### Magics

Magics are a simple command language which significantly extend the power of Jupyter.

There are two kinds of magics:

 - **Line magics**: commands prepended by one % character and whose arguments only extend to the end of the current line.
 - **Cell magics**: use two percent characters as a marker (%%), receive as argument the whole cell (must be used as the first line in a cell)

`%lsmagic` lists all available line and cell magics:
```
%lsmagic
```

`%quickref` shows a quick reference card: 
```
%quickref
```

Question mark shows help:
```
%sx?
```

Additional magics can also be installed or created.

---

### Shell commands
  - You can run shell commands by prepending with !
    - On Windows, GitBash needs to have the following option enabled:   
    `Use Git and the optional Unix tools from the Windows Command Prompt` 
  - Make sure your cell command doesn't require interaction

```
!echo "hello"
```
```
hello
```

- Common linux shell commands are also available as *magics*: %ls, %pwd, %mkdir, %cp, %mv, %cd, *etc.*. 

---

### Widgets

Widgets add more interactivity to Notebooks, allowing one to visualize and control changes in data, parameters etc.

```python
from ipywidgets import interact
```

#### Use `interact` as a function
```python
def f(x, y, s):
    return (x, y, s)

interact(f, x=True, y=1.0, s="Hello");
```

#### Use `interact` as a decorator
```python
@interact(x=True, y=1.0, s="Hello")
def g(x, y, s):
    return (x, y, s)
```
