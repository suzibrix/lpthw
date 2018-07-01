## VLL was here
# study drill 0: document everything
# take code from sys to gain argument functionality 
from sys import argv
# take code from os.path to test if files exist
from os.path import exists

# tell argv that we want two arguments, called "from_file" and "to_file"
script, from_file, to_file = argv

# tell the user that we are copying file "from_file" to "to_file"
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
## give us time.

# we open the source file and call the object "in_file"
in_file = open(from_file)
# we read the target file and call it "indata"
indata = in_file.read()

# We tell the user how big "in_file" is.
print(f"The input file is {len(indata)} bytes long")

# This both tests whether file exists and tells the user if it does.
# I'm not sure, but I think this creates the file if it doesn't exist.
print(f"Does the output file exist? {exists(to_file)}")
# This prompts the user to press RETURN to continue and how to get out
# if they don't want to do this thing.
print("Ready, hit RETURN to contimue, CTRL-C to abort.")
# This accepts the input from the user 
input()

# This opens the target file in write mode
out_file = open(to_file, 'w')
# This copies the data we gathered from "indata" to "out_file"
out_file.write(indata)

# This tells the user that the job is done
print("Alright, all done.")

# this closes the "out_file"
out_file.close()
# this closes the "in_file"
# not sure why "indata" doesn't actually get closed.
in_file.close()

