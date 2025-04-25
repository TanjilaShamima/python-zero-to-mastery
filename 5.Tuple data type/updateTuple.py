# Update Tuple

# Tuples are immutable, so you cannot change the value of an element in a tuple.
# However, you can convert the tuple to a list, make the changes, and then convert it back to a tuple.

# Example of updating a tuple
# Original tuple
original_tuple = (1, 2, 3, 4, 5)
print(f"Original Tuple : {original_tuple}")  # Output: (1, 2, 3, 4, 5)
# Convert tuple to list
temp_list = list(original_tuple)
# Update the second element
temp_list[1] = 10
# Convert list back to tuple
updated_tuple = tuple(temp_list)
print(f"Updated Tuple : {updated_tuple}")  # Output: (1, 10, 3, 4, 5)

