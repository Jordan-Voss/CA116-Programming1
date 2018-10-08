import sys
s = sys.argv[1]

if len(s) == 4:
	s = '0' + s
mins = int(s[len(s) - 2:]) + int(s[0:2]) * 60

print mins
