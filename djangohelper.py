import sys
import os
import re

# print str(sys.argv)
folderdir=sys.argv[1]
print "Folder to convert is : "+folderdir
for file in os.listdir(folderdir):
	if file.endswith(".html") and file != 'newfile.html':
		print(file)
		with open(file) as f:
			lines=f.readlines()
			print lines
			tempf=open('newfile.html','w')
			for l in lines:
				m=re.search('<script*>',l)
				print m
				print m.group(0)
				tempf.write(l)
			tempf.close()

