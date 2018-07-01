# 16-reader is a stupid program that just spits out text written in a file.
# It even tells the reader what the file is called. 
# But it is the best stupid program.

from sys import argv
script, filename = argv

print(f"You want me to read {filename}.")

text = open(filename)

print("Here is your text: \n")
print(text.read())
print("EOF : That's all, folks!")


