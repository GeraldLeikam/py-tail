# py-tail - Unix tail follow implementation in Python #

## Installation ##

```shell
python3 setup.py install
```
<br>

## Basic Usage Follow ##
```python
# Import tail class
from pytail import tail
    
# Create a new tail instance 
t = tail.Tail()
    
# Set file to follow 
t.file = "path/to/file"
    
# Register a callback function 
t.callback = callback_function

#Set refresh interval
t.refresh = 0.5

# Start following
t.follow()
```
<br>

## Basic Usage Bytes ##
```python
# Import tail class
from pytail import tail
    
# Create a new tail instance 
t = tail.Tail()
    
# Set file to follow 
t.file = "path/to/file"

# Get last 50 bytes from file
r = t.bytes(count=50)
```
<br>

## Basic Usage Lines ##
```python
# Import tail class
from pytail import tail
    
# Create a new tail instance 
t = tail.Tail()
    
# Set file to follow 
t.file = "path/to/file"

# Get last 20 lines from file
r = t.lines(count=20)
```
