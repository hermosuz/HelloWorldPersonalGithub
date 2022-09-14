#this is a comment

print ("hello uzi")

# a list of sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list [ ] and a comma seperated list of values

list_ints = [120, 1, 10, 20]
# there are unique indixes for each element in the list
# 0-based (the first element is at 0, and the last element is at n-1)
# where n is the number of elements in the list

print(list_ints[0])
print(list_ints[-4])

# types can be mixed in a list

list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)
print(type(list_numbers))

# lists are mutable (they can be changed)
list_numbers[0] = "hello"
print(list_numbers)
