# Unpack Tuple
# Unpacking a tuple means assigning the elements of the tuple to variables.


# Example of unpacking a tuple
# Original tuple
original_tuple = (1, 2, 3, 4, 5)
print(f"Original Tuple : {original_tuple}")  # Output: (1, 2, 3, 4, 5)

# Unpacking the tuple into variables
a, b, c, d, e = original_tuple
print(f"Unpacked Values : {a}, {b}, {c}, {d}, {e}")  # Output: 1, 2, 3, 4, 5

(a, *b, c) = original_tuple
print(f"Unpacked Values : {a}, {b}, {c}")  # Output: 1, [2, 3, 4], 5