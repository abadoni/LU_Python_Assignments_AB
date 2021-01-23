
##Write a Python program to find all occurrences of a character in the given string

str = "This is not a duplicate string This is not a duplicate string This is not a duplicate string"

list_str = str.split(' ')
print(str)
dict = {}
for each in list_str:
	#print(each,":",list_str.count(each))
	dict[each] = list_str.count(each)

print(dict)