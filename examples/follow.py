from pytail.tail import Tail


def my_callback(value: bytes):
    print(value.decode('utf-8'))
    print('-------------------')


if __name__ == '__main__':

    ## Long Version
    # Create a new Tail instance
    my_tail = Tail()
    # Sets the file to follow
    my_tail.file = '/file/to/follow'
    # Sets the callback to be called when a new line is written to the file
    my_tail.callback = my_callback
    # Sets the time to wait before looking for a new line
    my_tail.refresh = 0.5
    # Start the following of the specified file
    my_tail.follow()

    ## Short Version
    # Create a new Tail instance
    my_tail = Tail(file='/file/to/follow', callback=my_callback, refresh=0.5)
    # Start the following of the specified file
    my_tail.follow()