from pytail.tail import Tail

if __name__ == '__main__':

    ## Long Version
    # Create a new Tail instance
    my_tail = Tail()
    # Sets the file to follow
    my_tail.file = '/file/to/follow'
    # Get last 20 lines of the file
    result = my_tail.lines(count=20)

    ## Short Version
    # Create a new Tail instance
    my_tail = Tail(file='/file/to/follow')
    # Get last 20 lines of the file
    result = my_tail.lines(count=20)