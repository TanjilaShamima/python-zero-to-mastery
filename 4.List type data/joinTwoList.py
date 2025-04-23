# Join two list in python

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [1, 'a', 2.5, True, None]
# List is a built-in data type in Python.
# List is a collection of items in a particular order.
# List is a mutable data type.
# Join two list in python

list4 =list1 + list2
print(list4)

# Join two list in python
list1.extend(list2)
print(list1)

list1.extend(list3)

print(list1)