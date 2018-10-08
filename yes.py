n = raw_input()
a =[]
b =[]
c = []
i = 0
while n[i] != ',':
		i += 1
a.append(n[:i])
j = i + 1
i += 1
while n[j] != ',':
	j += 1
b.append(n[i:j])
c.append(n[j:])
print a
print b
print c