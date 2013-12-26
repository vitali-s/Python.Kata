try:
    x = int("x")
except ValueError:
    print "Oops!  That was no valid number.  Try again..."


try:
    raise NameError('HiThere')
except NameError:
    print 'An exception flew by!'


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError('HiThere')
except MyError:
    print 'MyError raised!'
finally:
    print 'Goodbye, world!'


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]