n = raw_input()
a = []

while n != 'end':
	a.append(int(n))
	n = raw_input()
n = raw_input()
k = len(a[:int(n)])
a = a[int(n):]

i = 1
j = 0
while i < len(a):
	if a[i] < a[j]:
		j = i
	i = i + 1
print j + k