# PathSelector
PathSelector is a simple path selection module for python.

# Setup

`pip install PathSelector`

# Examples

<h3>Code: </h3>

```python
from PathSelector import Selector
print(Selector.selectPath())
```

<h3>Console: </h3>

```cmd
Current folder: C:\Users\mozancetin\Desktop

[ 1 ] - desktop.ini
[ 2 ] - js (folder)
[ 3 ] - MyProjects (folder)
[ 4 ] - program.pdf
[ 5 ] - Web (folder)

[ -1 ] - Cancel
[ -2 ] - .. ( Upper Folder )
[ -3 ] - Select Current Folder

Select a directory or a file: 4


Your choice: program.pdf

Do you really want to select it [Y/n]: y
'C:\\Users\\mozancetin\\Desktop\\program.pdf'
```

<hr>

<h3>Code: </h3>

```python
from PathSelector import Selector
print(Selector.selectPath(startPath = r"C:\Users\mozancetin\Desktop", filters = ["js"], showFolders = False))
```

<h3>Console: </h3>

```cmd
Current folder: C:\Users\mozancetin\Desktop

[ 1 ] - script1.js
[ 2 ] - script2.js
[ 3 ] - script3.js

[ -1 ] - Cancel
[ -2 ] - .. ( Upper Folder )
[ -3 ] - Select Current Folder

Select a directory or a file: 2


Your choice: script2.js

Do you really want to select it [Y/n]: y
'C:\\Users\\mozancetin\\Desktop\\script2.js'
```

<hr>

<h3>Code: </h3>

```python
from PathSelector import Selector
print(Selector.selectPath(startPath = r"C:\Users\mozancetin\Desktop", regex_selector = "^[aA].*", use_regex_on_folder = False, showFolders = False))
```

<h3>Console: </h3>

```cmd
Current folder: C:\Users\mozancetin\Desktop

[ 1 ] - Ask.txt
[ 2 ] - aphrodite.docx

[ -1 ] - Cancel
[ -2 ] - .. ( Upper Folder )
[ -3 ] - Select Current Folder

Select a directory or a file: 2


Your choice: aphrodite.docx

Do you really want to select it [Y/n]: y
'C:\\Users\\mozancetin\\Desktop\\aphrodite.docx'
```
