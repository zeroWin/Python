'makeTextFile.py -- create text file'

import os

# Get filename
while True:
	try:
		fname = input('Enter file name: ')
		fobj = open(fname,'r')
	except IOError as e:
		# Get file context(text) lines
		all = []
		print("Enter lines('.' by itself to quit).")

		# loop until user terminates input
		while True:
			entry = input('Enter str > ')
			if entry == '.':
				break
			else:
				all.append(entry)

		# Write lines to file with proper line-ending
		fobj = open(fname,'w')
		fobj.write('\n'.join(all))
		fobj.writelines([])
		fobj.close()
		print('Done')
		break
	else: # Open succeed
		fobj.close()
		print("ERROR: '%s' already exists" % fname)
		
