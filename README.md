#Help 2 .md
help2md
A function that allows people to convert the help in their python code to a
    .md file. This is useful for places such as github.


##help2md
```python
def help2md(filepath, output='README.md', name='code'):
	"""help2md
	Converts python help to a .md file.
	params:
	    - filename - The full path of the input file
	    - output - The full path of the output file ( defaults to README.md )
	    - name - The name of the file. It puts this at the top of the document."""
```

# Dependencies
- imp
- inspect

***Made with help2md***