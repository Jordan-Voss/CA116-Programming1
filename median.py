n = raw_input()
a = []
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
while i < len(a):
   i += 1
if len(a) % 2 == 0:
   print a[len(a) / 2]
elif len(a) % 2 != 0:
   print a[len(a) / 2]