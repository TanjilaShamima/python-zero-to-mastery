# Join tuple

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# Joining tuples

joined_tuple = tuple1 + tuple2
print(f"Joined Tuple : {joined_tuple}")  # Output: (1, 2, 3, 4, 5, 6)

# Joining tuples with a separator
separator = '-'
joined_tuple_with_separator = separator.join(map(str, joined_tuple))
print(f"Joined Tuple with Separator : {joined_tuple_with_separator}")  # Output: 1-2-3-4-5-6