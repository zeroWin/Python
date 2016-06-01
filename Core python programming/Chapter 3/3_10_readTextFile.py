'readTextFile.py -- read and display text file'

import os

# get filename
fname = input('Enter filename: ')
print()

# attempt to open file for reading
if os.path.exists(fname):
	fobj = open(fname,'r')
	for readLine in fobj:
		print(readLine,end = "")
	fobj.close()
else:
	print("ERROR:No such file")
