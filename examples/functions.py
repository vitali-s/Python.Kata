# filter(function, sequence) returns a sequence consisting of those items
# from the sequence for which function(item) is true.


def f(x):
    return x % 2 != 0 and x % 3 != 0

print filter(f, range(2, 25))

# map(function, sequence) calls function(item) for each of the sequence's
# items and returns a list of the return values.

def cube(x):
    return x*x*x

print map(cube, range(1, 11))

# reduce(function, sequence) returns a single value constructed by calling the binary function function on the first
# two items of the sequence, then on the result and the next item, and so on.

def add(x,y):
    return x + y

print reduce(add, range(1, 11))