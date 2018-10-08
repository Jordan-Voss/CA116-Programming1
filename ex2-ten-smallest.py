a = []
n = raw_input()
while n != 'end':
   a.append(int(n))
   n = raw_input()
i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   i += 1

i = 0
while i < len(a) and i < 10:
   print a[i]
   i += 1