b = []
i = 0
while i < len(a):
   i += 1
   if len(a[i - 1]) > 0:
      b.append(a[i - 1])
print len(b)