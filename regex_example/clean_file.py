'''Remove all non-alphanumberic character(s) in file name
- replace with underscore '_'
'''
import re
import os

def clean_filename(name):
	'''Replace non-alphanumberic character(s) with an underscore "_"
	'''
	return re.sub(r'[\-\.,_ ]+', '_', name)

def check_cleaned_filenames(ls):
	'''Pass in list of file names
	- print out how new names look like
	'''
	for file in ls:
		f, e = os.path.splitext(file)
		fn = clean_filename(f)
		if e != '':
			ext = '.' + clean_filename(e[1:])
		else:
			ext = ''
		print("file:     '{}'".format(file))
		print("new file: '{}{}'".format(fn, ext))
		print('')

if __name__ == '__main__':
	files = ["abc def- ghi_jkl. mno.pqr", 
	         " _d, 562. z_-,p", 
			 "apple"]

	check_cleaned_filenames(files)
	