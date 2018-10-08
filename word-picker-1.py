i = 1
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
	print a[b[i]]
	i += 1
