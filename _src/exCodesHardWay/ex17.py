# write A file into B file
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata) # caculate length of file

print "Does the output file exists? %r" % exists(to_file) # judge whether it exists ot not
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file,'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()