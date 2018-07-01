# exercise 15 land -- VLL was here
# tail chopped edition
# opens argv from package sys 
from sys import argv

# create arguments/assign variables from argv
script, filename = argv

# access file, assign contents to variable TXT
txt = open(filename)

# print the name of the file accessed.
print(f"Here's your file {filename}:")
# print variable "txt" (contents of file) 
print(txt.read())

