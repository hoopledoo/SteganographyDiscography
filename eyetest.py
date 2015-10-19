def frames(f): 
	# how many bytes we would like in the buffer at a minimum
	min_dat = 16
	
	try:
	    # dat is our read buffer
	    dat = ''
	    # frame tells if the last iteration found an MP3-frame
	    # or something else (e.g. an ID3-tag)
	    frame = 0
	    # number of MP3-frames we have found
	    no = 0
	    # i is the length of the 'something' (e.g. MP3-frame, ID3-tag)
	    # we found last iteration; j is our position in the file
	    i = j = 0
	 
	    while 1:
	        # fill buffer
	        while len(dat) < i + min_dat:
	            rd = f.read(i + min_dat - len(dat))
	            if rd == '':
	                break
	            dat = dat + rd
	 
	        # pass frame up to caller
	        if len(dat) < i:
	            break
	        if frame:
	            yield hdr, dat[:i]
	 
	        # throw away the frame or ID3-tag we found in the last
	        # iteration.
	        j = j + i
	        dat = dat[i:]
	 
	        if len(dat) < min_dat:
	            break
	 
	        if dat.startswith('TAG'):
	            # skip ID3v1 tags
	            frame = 0
	            i = 128
	 
	        elif dat.startswith('ID3'):
	            # skip ID3v2 tags
	            frame = 0
	            i = (ord(dat[6]) << 21) + (ord(dat[7]) << 14) + \
	                (ord(dat[8]) << 7) + ord(dat[9]) + 10
	 
	        else:
	            hdr = frameheader(dat, 0)
	            i = framelen(hdr)
	            frame = 1
	            no = no + 1
	 
	except(MP3FrameHeaderError, e):
	    raise(MP3Error, 'bad frame-header at offset %d (%x): %s' \
	                    % (j, j, e.args[0]))

f = open("encoded.mp3",'rb')

for (hdr, frm) in frames(f):
	print(hdr, frm)

