a = []
n = raw_input()
while n != 'end':
	a.append(n)
	n = raw_input()

b = []
n = raw_input()
while n != 'end':
	b.append(int(n))
	n = raw_input()

i = 0
while i < len(b):
	j = 0
	while j < len(a) and int(a[j][:8]) != b[i]:
		j += 1
	
	if j < len(a):
		print a[j][9:]
	i += 1