from sys import argv # load python module: sys

script, filename = argv # define arguments

txt = open(filename) # open the file 

print "Here's your file %r:" % filename # print the name of file
print txt.read() # print out the content of the txt file

print "I'll also ask you to type it again:" # ask user to input file name again
file_again = raw_input("> ") # output > and get input
txt_again = open(file_again) # open the new file

print txt_again.read() # print out the content of new file

txt.close()
txt_again.close()