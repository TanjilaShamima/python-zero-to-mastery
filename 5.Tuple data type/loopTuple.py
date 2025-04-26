# Loop tuple

# Looping through a tuple
# Example of looping through a tuple
# Original tuple
original_tuple = (1, 2, 3, 4, 5)
print(f"Original Tuple : {original_tuple}")  # Output: (1, 2, 3, 4, 5)

# Looping through the tuple using a for loop
for item in original_tuple:
    print(f"Item : {item}")  # Output: 1, 2, 3, 4, 5

for item in range(len(original_tuple)):
    print(f"Item :{item} : {original_tuple[item]}")