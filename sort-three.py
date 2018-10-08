a = input()
b = input()
c = input()
d = []
d.append(a)
d.append(b)
d.append(c)
tmp = 0 
i = 0 
while i < len(d):
	if d[i] < d[tmp]:
		tmp = i 
	i = i + 1
p = 0 
p = d[tmp]
d[tmp] = d[0]
d[0] = p 




if d[0] > d[1]:
	tmp = d[1]
	d[1] = d[0]
	d[0] = tmp 
if d[1] > d[2]:
	tmp = d[2]
	d[2] = d[1]
	d[1] = tmp 

i = 0
while i < len(d):
	print d[i]
	i = i + 1