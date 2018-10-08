n = raw_input()
i = 0
a = []
avg = 0.0
while n != 'end':
   a.append(n)
   avg = avg + int(n)
   n = raw_input()
   i = i + 1
if i == 0:
	i = 1
avg = (float(avg) / float(i))
j = 0
while j < len(a):
	if float(a[j]) > float(avg):
		print a[j]
	j += 1
