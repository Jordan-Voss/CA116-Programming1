n = raw_input()
a = []
b = []
c = []

while n != 'end':
	i = 0
	while n[i] != ',':
		i += 1
	a.append(n[:i])
	i += 1
	j = i
	while n[j] != ',':
		j += 1
	b.append(n[i:j])
	j += 1
	c.append(n[j:])
	n = raw_input()

s = input()
i = 0
if s == 0:
	while i < len(a):
		print a[i]
		i += 1
i = 0
if s == 1:
	while i < len(b):
		print b[i]
		i += 1
i = 0
if s == 2:
	while i < len(c):
		print c[i]
		i += 1
