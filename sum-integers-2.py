import sys
s = sys.argv[1]
total = 0
with open(s) as f_in:
	s = f_in.readline()
	while 0 < len(s):
		total = total + int(s)
		s = f_in.readline()
print total