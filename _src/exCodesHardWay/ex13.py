# from sys import argv
# script , first , second , third = argv
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

# not work code about combining argv and raw_input
# Now it worked 
from sys import argv

script,name=argv 
# this line is interesting, it seems that you always need
# to put script as the first argument. Am I right? 

age=raw_input("How old are you? ")
height=raw_input("How tall are you? ")
weight=raw_input("How much do you weigh? ")

print "So, %s, you're %r old, %r tall and %r heavy." % (
	name,age,height,weight)