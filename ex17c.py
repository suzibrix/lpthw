## third itteration. hidden things done except breakage
#VLL was here
# Now we get rid of annoying things vis SD #1

from sys import argv; script, from_file, to_file = argv

in_file = open(from_file); indata = in_file.read()
out_file = open(to_file, 'w'); out_file.write(indata)

out_file,in_file.close()

