### ex 16 land-- VLL was here
# Study Drill #1 complete
# Study Drill #2 complete (it is called 16-reader.py
# Study Drill #3 -- look out. concatinate read processes!   

# Open sys and use argv in this program
from sys import argv
# Use filename attribute to argv
script, filename = argv

# Reminds user that they are erasing and writing over {file}
print(f"Were're going to erase {filename}.")
# Tells user how to get out of program 
print("if you don't want that, hit CTRL-C (^C).")
# tells user how to continue with program
print("if you do want that, hit RETURN.")

# Receives input; assigns prompt variable "?"
input("?")

# Tells user it's opening a file 
print("Opening the file...")
# opens file in write mode 
target = open(filename, 'w')

# Tells user file contents are evaporating
print("Truncating the file. Goodbye!")
# Truncates (ie deletes contents) of file
target.truncate()

# Tells user that program wants three lines
print("Now I'm going to ask you for three lines.")

# Each variable takes one line from user and assigns it to variable
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Tells user it's writing the lines to a file 
print("I'm going to write these to the file.")

# Writes each line to the file individually
target.write(line1 "\n" line2 "\n" line3 "\n")

# tells user that program is closing the file
print("And finally, we close it.")
# Program closes the file
target.close()

