# All methods in list
# List is a built-in data type in Python.

# List is a collection of items in a particular order.
# List is a mutable data type.
# List is a collection of items in a particular order.
# List is a mutable data type.
# List is a collection of items in a particular order.
# List is a mutable data type.

# append() method
# The append() method adds an item to the end of the list.
# The append() method takes a single argument, which is the item to be added to the list.
# The append() method returns None.
# The append() method does not return a new list.

# clear() method
# The clear() method removes all items from the list.
# The clear() method returns None.
# The clear() method does not return a new list.
# The clear() method removes all items from the list.


# copy
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()

list = [1, 2, 3, 4, 5]
# append
list.append(6)
print(list)

list.insert(2, "yyy")
print(list)

list2 = list.copy()
print(list2)
list2.extend([7, 8, 9])
print(list2)

list.pop(2)
print(list)

list.remove(3)
print(list)

list.reverse()
print(list)

list.sort()
print(list)