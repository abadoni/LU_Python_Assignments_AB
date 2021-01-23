##Write a Python program to merge two files into a third file.

filenames = ["file1.txt", "file2.txt"]

with open("file3.txt", 'w') as outfile:
	for file in filenames:
		with open(file) as infile:
			outfile.write(infile.read())

		outfile.write("\n")