# py-tail - Unix tail follow implementation in Python #

## Installation ##

python3 setup.py install

## Basic Usage Follow ##
```from pytail import tail
    
    --- Create a new tail instance ---
    t = tail.Tail()
    
    --- Set file to follow --- 
    t.file = "path/to/file"
    
    --- Register a callback function ---
    t.callback = callback_function
    
    --- Set refresh interval ---
    t.refresh = 0.5

    --- start following ---
    t.follow()```
