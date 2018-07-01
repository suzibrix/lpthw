## This is for ex19 study drill
## The idea is to call a function 10 ways

## Will rename script when good enough to be useful
## python code (script) ## VLL was here

from sys import argv
from os.path import exists
#import os

script, file_name, name0 =argv

## script should test of file exists;
## should create file if doesn't exist
print(f"Does this file exist? {exists(file_name)}")
# script should prompt user for a name
def name_it(*names):
    name_zero, name1, name2, name3 = names
    name_zero = name0
    print(f"Your first name is {name1}.")
    print(f"Your second name is {name2}.")
    print(" One more name!")
    print(f"YOur third name is {name3}.")
    print(f"Don't forget that name #4 is {name_zero}.")
# new test to see if argv stays persistent
    print(f"{name0} should be {name_zero}.")     
# script should write name in file
    output = open(file_name, 'a')
    output.write(name3); output.write("\n")
    output.write(name2); output.write("\n")
    output.write(name1); output.write( "\n")
    output.write(name_zero); output.write( "\n")
    output.write(name0); output.write(".\n")
    output.close()
print("This is a test of your names.")
print("This is iteration #1.")
print("Please enter four (4) names to enter into the file.")
nameA = input("1> ")
nameB = input("2> ")
nameC = input("3> ")
nameD = input("4> ")

name_it(nameA, nameB, nameC, nameD)
print("Iteration #2 incoming.")
name_it(Trent, Alois, Hubert, Allison)
print("This is iteration #3.")
print(f"Here are your names:\t" name_it)
print("Im going to argue that iteration #4 comes from the arg integration...")
#print(f"Don't forget name #0 :" name_it(name_zero))
print("This is iteration #5.")
print(f"Have some names:" name_it(Fido, Kendel, Shephard, Michael))


print("This counts as six!")
print(f"See what {names} does now!")

print("Now we read names. Onward to SEVEN!")

opera = open(file_name, 'r+')
nom1 = readline.opera
nom2 = readline.opera
nom3 - readline.opera
name_it(nom1, nom2, nom3) 

