# python list comprehension
# List comprehension is a concise way to create lists in Python.

testList = ["python", "java", "c++", "c#", "javascript", "typescript"]

testNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # List comprehension is a concise way to create lists in Python.
# # List comprehension is a way to create a new list by applying an expression to each item in an existing list.

for i in testNumber:
    print(i * 2)

double = [i * 2 for i in testNumber]
print(f"Double of testNumber: {double}")