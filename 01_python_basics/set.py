# Creating a Set
s = {1, 2, 3, 'Python', 3}
print(s)

# Adding elements
s.add('last')
print(s)

# Removing elements
s.remove(3)  # KeyError if the element is not present

# Accessing elements (No indexing because it is unordered)
# for element in s:
#     print(element)