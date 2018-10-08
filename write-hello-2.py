import sys
s = sys.argv[1]
with open( s, 'w') as f_out:
	f_out.write('Hello world.\n')