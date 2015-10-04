import subprocess

infile = "200_Hertz_FSK_500bits.wav"
outfile = "encoded.mp3"
encodecmd = ["lame",infile,outfile]

subprocess.call(encodecmd)