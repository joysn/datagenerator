import sys
import logging
import os
import random
import argparse
import string

'''
(base) D:\>python datagen.py --help
usage: datagen.py [-h] [--o O] [--c C] [--r R] [--cs CS [CS ...]] [--d D]

A Simple Data Generator
***********************
row delimiter = Space
column delimiter = New line

optional arguments:
  -h, --help            show this help message and exit
  --o O                 Name of Output Data File
  --c C                 No of columns
  --r R                 No of rows
  --cs CS [CS ...], --list CS [CS ...]
                        Space separated list of colum sizes
  --d D                 Debug Level: INFO, DEBUG, WARNING

Contact:- joysn1980@yahoo.com
'''

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description='''
A Simple Data Generator 
***********************
row delimiter = Space
column delimiter = New line''',epilog='''
Contact:- joysn1980@yahoo.com
''')
parser.add_argument('--o', help='Name of Output Data File')
parser.add_argument('--c', help='No of columns',type=int,default=2)
parser.add_argument('--r', help='No of rows',type=int,default=100)
parser.add_argument('--cs','--list', nargs='+', help='Space separated list of colum sizes',default=[25,5])
parser.add_argument('--d', help='Debug Level: INFO, DEBUG, WARNING')

args = vars(parser.parse_args())

if args["o"] == None:
	args["o"] = "gen_data.txt"
	
	
''' Debuging '''
if args["d"] == 'DEBUG':
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt = '%m/%d/%y %I:%M%S %p')
if args["d"] == 'INFO':
	logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt = '%m/%d/%y %I:%M%S %p')
	
''' Check the arguments '''
logging.debug(args)
logging.debug(args["o"])
logging.debug(args["c"])
logging.debug(args["r"])
logging.debug(args["cs"])
logging.debug(args["d"])

if (len(args["cs"]) != args["c"]):
	print("incorrect argument. --c [default: 2] value should match # of values specified in --cs [default: 25 5]")
	exit(0)
	

no_of_cols = args["c"]
no_of_rows = args["r"]
ofile = args["o"]
col_size = args["cs"]

col_delimiter = " "
row_delemiter = "\n"


if os.path.exists(ofile):
	os.remove(ofile)


with open(ofile, 'a') as ouf:
	for i in range(0,no_of_rows):
		row = ''
		for j in range(0,no_of_cols):
			col = ''
			cs = int(col_size[j])
			col = ''.join(random.choice(string.ascii_uppercase+ string.ascii_lowercase + string.punctuation+ string.digits) for _ in range(cs))
			if row == '':
				row = col
			else:
				row = row+col_delimiter+col
		if i < no_of_rows-1:
			row = row + row_delemiter
		logging.debug(row)
		ouf.write(row)
		
print("\nContents of Generated File:-", ofile, " ")
with open(ofile, 'r') as f:
	print(f.read())