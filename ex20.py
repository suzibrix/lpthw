## EX 20 DONE (TG)
##WTHIR
#imports all the cool toys from argv
from sys import argv

# assigns variables for argv
# we assign scriptname and input file as variables
script, input_file = argv

# define a function called "print_all"
# I think the ("f") in peren represents the target file
# then read the file and print it
def print_all(f):
    print(f.read())

# this defines a function called "rewind"
# this seeks to line zero
# from the file (that's what the f. means)
def rewind(f):
    f.seek(0)

# this defines a function called "print_a_line"
# it has two arguments, "f" working file, and line_count variable
def print_a_line(line_count, f):

    # this prints "line_count" contents from file
    print(line_count, f.readline())

# this opens input file; assigns to input_file
current_file = open(input_file)
# This tells the user it's going to print whole file
print("First, let's print the whole file:\n")
# this activates function "print_all" on "current_file" from argv 
print_all(current_file)

# This tells the user it will go back to the beginning of file
print("Now let's rewind, kind of like a tape.\n")

# This activates fuction "rewind" on "current file" from argv
rewind(current_file)

# tells the user printing will start
print("Let's print three lines:\n")

# variable "current_line" is assigned numeral 1
current_line = 1

# this prints a single line from "current_file"
print_a_line(current_line, current_file)

# this adds one to "current_line", creating a counter of sorts
current_line += 1

# this prints the second line from "current_file"
print_a_line(current_line, current_file)

# our counter "current_line" increased by one
current_line += 1

# print_a_line function called again to print a line
# this makes count number three
print_a_line(current_line, current_file)
