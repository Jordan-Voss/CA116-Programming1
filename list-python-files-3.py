import os
files = os.listdir(".")
i = 0
while i < len(files):
	with open(files[i]) as n:
		n = n.readline()
		if files[i].split('.')[-1] == 'py' and 0 < len(n) or 0 < len(n) and n[0:21] == '#!/usr/bin/env python':
			print files[i]
	i += 1