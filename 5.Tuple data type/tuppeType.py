# Tuple type data in python.....
# matrixMenuTuple = (
#     (1, 2, 3, 4, 5),
#     (4, 5, 6, 7, 8),
#     (7, 8, 9, 10, 11),
#     (10, 11, 12, 13, 14),
#     (13, 14, 15, 16, 17)
# )
#
# print(f"Number of rows in the matrix: {matrixMenuTuple}")


newTuple = (1, 2, 3, 4, "example", 5.6, True, False)
# print the first element of the tuple
print(f"Type : {type(newTuple)}")

# print the first element of the tuple
print(f"First Item : {newTuple[0]}")  # Output: 1


print(f"Range of tuple : {newTuple[2:5]}")  # Output: 8