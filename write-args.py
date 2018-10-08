import sys
s = sys.argv[1]
i = 2
with open(s,'w') as f_out:
	while i < len(sys.argv):
		f_out.write(sys.argv[i] + '\n')
		i += 1