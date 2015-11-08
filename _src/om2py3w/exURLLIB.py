
import urllib
fhand = urllib.urlopen('http://www.xxx.com/page1.htm')

for line in fhand:
	print line.strip()
# the above do the exHTTPsocket.py work 

# then what you did next is like what you can do with a file

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
print counts