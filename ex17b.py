## third itteration. hidden things done except breakage
#VLL was here
# Now we get rid of annoying things vis SD #1

from sys import argv; from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# Like this
in_file = open(from_file); indata = in_file.read()

# print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
##  vll Commented out annoying prompt and feedback requirement
#print("Ready, hit RETURN to contimue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

