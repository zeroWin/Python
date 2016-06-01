'''readTextFile.py -- read and display text file

String format,delete the \r\n on the every line
'''

import os
ls = os.linesep

# get filename
fname = input('Enter filename: ')
print()

# attempt to open file for reading
if os.path.exists(fname):
	fobj = open(fname,'r')
	for readLine in fobj:
		readLine = readLine.strip(ls)
		print(readLine)
	fobj.close()
else:
	print("ERROR:No such file")
