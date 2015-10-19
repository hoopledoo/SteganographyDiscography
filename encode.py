import subprocess
import sys

try:
	infile = sys.argv[1]
	outfile = sys.argv[2]
except:
	print("Provide input wav file and name for output file")
	sys.exit(0);

encodecmd = ["lame",infile,outfile]

subprocess.call(encodecmd)