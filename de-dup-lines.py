line = raw_input()
a = []
i = 0
while line != 'end':
   i = 0
   while i < len(a) and a[i] != line:
      i += 1
   if i == len(a):
      a.append(line)
   line = raw_input()
j = 0
while j < len(a):
	print a[j]
	j = j + 1 