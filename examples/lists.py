from collections import deque
import sys

list = range(1, 5)

# add item in the end
list.append(6)

# add item in the end
list[len(list):] = [7];

print list

# extend the list by appending all the items in the given list
list.extend(range(8, 10))

print list

list.insert(2, 100)

print list

try:
    list.remove(111)
except:
    print sys.exc_info()


# using Lists as Stacks
stack = [3, 4, 5, 6]
stack.pop()

# using Lists as Queues
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.popleft()

# remove item from list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]

print a