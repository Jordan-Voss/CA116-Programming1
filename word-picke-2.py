a = []
n = raw_input()
while n != 'end':
	a.append(n)
	n = raw_input()
b = []
n = raw_input()
while n != 'end':
	if n != '':
		b.append(n)
	n = raw_input()
i = 0
c =[]
while i < len(b):
	c.append(a[int(b[i])])
	print c[i],
	i += 1

