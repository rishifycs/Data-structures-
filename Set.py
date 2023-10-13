# Create sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Basic set operations
union_set = set1.union(set2)  # Union of set1 and set2
intersection_set = set1.intersection(set2)  # Intersection of set1 and set2
difference_set = set1.difference(set2)  # Set difference (elements in set1 but not in set2)
symmetric_difference_set = set1.symmetric_difference(set2)  # Symmetric difference

# Adding and removing elements
set1.add(6)  # Add an element
set1.remove(3)  # Remove an element

# Check if an element is in a set
element_present = 2 in set1

# Check if a set is a subset or superset of another set
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)

# Length of a set
set_length = len(set1)

# Display the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
print("Is 2 in Set 1?", element_present)
print("Is Set 1 a subset of Set 2?", is_subset)
print("Is Set 1 a superset of Set 2?", is_superset)
print("Length of Set 1:", set_length)
