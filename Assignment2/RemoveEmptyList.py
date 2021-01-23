#Write a Python program to remove empty List from List.

list = ["a","b",1,[],4,2,[],"c",[]]
print(list)
for item in list:
	if item == []:
		#print(list.index(item))
		list.pop(list.index(item))
print(list)
