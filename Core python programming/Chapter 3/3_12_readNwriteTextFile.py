'readNwriteTextFile.py -- Read or write file by user choose'

import os
ls = os.linesep

print("(1).Write file input num 1")
print("(2).Read file input num 2")
print("(X).Exit input X")
featureChoose = input("Please input: ")

while featureChoose != 'X':
	if featureChoose == '1':
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
	elif featureChoose == '2':
		fname = input('Enter filename: ')
		print()

		# attempt to open file for reading
		try:
			fobj = open(fname,'r')
		except IOError as e:
			print('*** file open error:',e)
		else:
			# display contents to the screen
			for eachLine in fobj:
				eachLine = eachLine.strip(ls)
				print(eachLine)
			fobj.close()	
	elif featureChoose == 'X':
		break
	print("(1).Write file input num 1")
	print("(2).Read file input num 2")
	print("(X).Exit input X")
	featureChoose = input("Please input: ")
	
