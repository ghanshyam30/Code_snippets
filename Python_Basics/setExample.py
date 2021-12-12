'''
Problem statement - You have 2 strings.
You need to find- 1] String1 characters that are not in String2 2] vice versa
'''
string1 = "Geeks For Geeks"
string2 =  "Geek"

set_1 = set(string1)
set_2 = set(string2)
print("Set1: ",set_1)
print("Set2: ",set_2)
print("======Set difference====")

# characters present in set1 but not in Set2
print("set1-set2: ","".join(set_1 - set_2))

# characters present in set2 but not in set2
print("set2-set1: ","".join(set_2 - set_1))

# OUTPUT
'''
Set1:  {'o', 's', 'r', 'G', 'e', 'k', ' ', 'F'}
Set2:  {'k', 'G', 'e'}
======Set difference====
set1-set2:  osr F
set2-set1:
'''
