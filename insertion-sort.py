i = 1
a = []
n = raw_input()
while n != 'end':
   a.append(int(n))
   n = raw_input()
while i < len(a):
      v = a[i]
      p = i
      while 0 < p and v < a[p - 1]:
            a[p] = a[p - 1]
            p = p - 1
      a[p] = v
      i += 1
i = 0
while i < len(a):
   print a[i]
   i += 1
