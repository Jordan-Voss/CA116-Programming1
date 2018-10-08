n = raw_input()
a = []
while n != 'end':
   a.append(int(n))
   n = raw_input()

m = input()
a.append(m)

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
while i < len(a):
   print a[i]
   i += 1
