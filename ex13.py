## This is VLL ex13. We get perameters.
#We document with docudrama
# this summons modules which give us features
# presumably, from sys tells us where to go
# and import tells us what
# is the argv module which gives us arguments
from sys import argv
# read the WYSS section for how to run this
# This tells the script how many and what kind of arguments to expect
# I presume it needs the exact number unless we tell it what to do 
# > if it doesn't get as many as expected
script, first, second, third = argv

# This print tells us what the script is called because
# > the script name is the first argument
print("The script is called:", script)
# this print tells us what the first variable is called
# which presumably also returns the script in the same way
# we've seen before. There must be something different
# about this from the old print statements 
# under the hood
print("Your first variable is:", first)
# This tells us what the second variable is
print("Your second variable is:", second)
# This tells us what the third variable is, just like
# > the previous two
print("Your third variable is:", third)
