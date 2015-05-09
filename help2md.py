#!/urs/bin/env python3
"""help2md
A function that allows people to convert the help in their python code to a
    .md file. This is useful for places such as github."""

import imp
import inspect

def help2md(filepath, output='README.md', name='code'):
    """help2md
    Converts python help to a .md file.
    params:
        - filename - The full path of the input file
        - output - The full path of the output file ( defaults to README.md )
        - name - The name of the file. It puts this at the top of the document.
    """
    document = '#' + name + '\n'
    c = imp.load_source(name, filepath)
    doc = inspect.getdoc(c)
    if doc:
        document += doc + '\n'
    else:
        document += '\n'
    
    main_file = getattr(c, '__file__')
    modules = []
    items = dir(c)
    for i in items:
        item = getattr(c, i)

        if inspect.isfunction(item):
            doc = inspect.getdoc(item)
            if doc == None:
                doc = 'No documentation'
            params = inspect.formatargspec(*inspect.getfullargspec(item))
            document += ('\n\n##' + i + '\n```python\ndef ' + i + params + 
                ':\n\t"""' + '\n\t'.join(doc.split('\n'))
                + '"""\n```')
        
        if inspect.isclass(item):
            doc = inspect.getdoc(item)
            if doc == None:
                doc = 'No documentation'
            document += ('\n\n##' + i + '\n```python\nclass ' + i + 
                '():\n\t"""' + '\n\t'.join(doc.split('\n')) 
                + '"""\n```')
            methods = dir(item)
            
            for m in methods:
                mitem = getattr(item, m)
                if inspect.isfunction(mitem):
                    params = inspect.formatargspec(
                        *inspect.getfullargspec(mitem))
                    doc = inspect.getdoc(mitem)
                    if doc == None:
                        doc = 'No documentation'
                    document += ('\n\n###' + m + '\n```python\n\tdef ' + m 
                    + params + ':\n\t\t"""' + '\n\t\t'.join(
                        doc.split('\n')) + '"""\n```')
        
        if inspect.ismodule(item):
            modules.append(i)
    
    document += '\n\n# Dependencies\n- ' + '\n- '.join(modules)
    document += '\n\n***Made with help2md***'
    with open(output, 'w') as ofile:
        ofile.write(document)
    return None

if __name__ == '__main__':
    help2md('sjbot.py', 'sjBot.md', name='sjBot')
