"""
Print stair of height 10 
and base 10

*
**
***
****
*****
******
*******
********
*********
**********

"""

for i in range(10):
    for j in range(i + 1):
        print("*", end='')
    print()