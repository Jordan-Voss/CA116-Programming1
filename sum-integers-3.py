import sys
i = 1
total = 0
while i < len(sys.argv):
	s = sys.argv[i]
	with open(s) as f_in:
		s = f_in.read().split()
		while 0 < len(s):
			total = total + int(s)
			s = f_in.read().split()
	i += 1
print total
