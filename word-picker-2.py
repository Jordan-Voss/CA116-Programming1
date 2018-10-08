a = []

n = raw_input()
while n != 'end':
	a.append(n)
	n = raw_input()

t = ''
n = raw_input()
while n != 'end':
	if len(n) == 0:
		print t
		t = ''
	else:
		if len(t) != 0:
			t += ' '
		t += a[int(n)]
	n = raw_input()
if 0 < len(t):
   print t