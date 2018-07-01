# exercise 15 land -- VLL was here
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

# prints text requesting file name
print("Type the filename again:")
# Assign variable "file again" to data stream input
# input assigns prompt as ">"
file_again = input("> ")

# text_again is assigned to the contents of file 
txt_again = open(file_again)

# print contents of "txt_again"
print(txt_again.read())
