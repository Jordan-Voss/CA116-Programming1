import sys
files = {}
s = sys.stdin.readline().strip()

while len(s) != 0:
	files['.'.join(s.split('.')[0:2])] = s.split('.')[2]
	s = sys.stdin.readline().strip()
for file in files:
	if files[file] == 'correct':
		print file