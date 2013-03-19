#!/usr/bin/env python
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="file with correct forms", metavar="FILE")

(options, args) = parser.parse_args()

with open(options.filename) as correct:
	for form in correct:
		form = form.strip()
		print form, sys.stdin.readline()
		
		