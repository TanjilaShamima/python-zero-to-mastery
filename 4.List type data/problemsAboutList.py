# print second element of the list

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Second Item : {fruits[1]}")  # Output: banana

# Change the value from apple to kiwi in the fruits list
fruits[0] = 'kiwi'
print(f"List after change First Item : {fruits}")  # Output: kiwi

# Add a new item to the end of the list

fruits.append('fig')
print(f"List after adding new item : {fruits}")  # Output: ['kiwi', 'banana', 'cherry', 'date', 'elderberry', 'fig']