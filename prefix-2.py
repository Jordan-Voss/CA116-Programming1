i = 0
while i < len(a) - 1 and a[i][:len(s)] != s:
   i += 1
if i < len(a) - 1:
   print a[i]