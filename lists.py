# List demonstration 
my_list = [2, 3]

# Length 
print("Length of my_list: ", len(my_list))

# Adding an item at the end of a list: append operation 
my_list = my_list.append(4)
print("After appending 4, my_list: ", my_list)

# Inserting an item at a given index.
print("my_list before inserting at index 0: ", my_list)
my_list = my_list.insert(0, 1)
print("my_list after inserting 1 at index 0: ", my_list)

# Concating a list 
gitas_list = ['list are heterogenous in python']
concatinated_list = my_list + gitas_list
print("After concatination: ", concatinated_list)


# Looping through a list
for item in my_list:
    print(item)

