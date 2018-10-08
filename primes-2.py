i = 0
while i < len(a) - 1 and not isprime(a[i]):
   i += 1
if i < len(a):
   print a[i]
