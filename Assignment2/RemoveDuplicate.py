#Write a Python program to remove all duplicates words from a given sentence

str = "This is not a duplicate string This is not a duplicate string This is not a duplicate string"
list_str = str.split(' ')
print("Input string")
print(str)
out_str = []
for each in list_str:
	if each not in out_str:
		out_str.append(each)
#print(out_str)
output = ""
for each in out_str:
	output = output + each + " "
print("Output string")
print(output)

