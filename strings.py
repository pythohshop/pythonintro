s = "Today is awesome"

# Some common string operations

# Counts space characters too
print("Length of a string is: ", len(s))

# Use count function to count number of letters in a string object
print("Number of letter 'e' in 's': ", s.count('e'))

# Slicing a part of string
print("Slicing from 0-3: ", s[0: 3])
print("Slicing 0 - 3: ", s[:3])
print("Slicing with step 1: ", s[:3:1])
print("Slcing with step 2: ", s[1:19:2])

# Concatenation 
p = " What do you think?"
print("Concatenating: ", s + p)

# Splitting a string 
print("Splitting s on every occurance of space character: ", s.split(' '))
new_str = 'toatoatoato'
print("Splitting new_str at every occurance of character a: ", new_str.split('a'))

# startswith and endswith 

print("Does string 's' startwith 'T': ", s.startswith('T'))
print("Does string 's' endswith 'k': ", s.endswith('k'))

#Joinig 
print("SPlitting and joining: ", 'a'.join(new_str.split('a')))

