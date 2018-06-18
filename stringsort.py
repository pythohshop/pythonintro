"""
Sorts a string
Assumption: String has no white space
"""

string_to_sort = input('text: ')
temp_list = []

for i in range(len(string_to_sort)):
    temp_list.append(string_to_sort[i])

for i in range(len(string_to_sort)):
    for j in range(i+1, len(string_to_sort)):
        if temp_list[i] > temp_list[j]:
            temp_list[i], temp_list[j] = temp_list[j], temp_list[i]

print(''.join(temp_list))


 