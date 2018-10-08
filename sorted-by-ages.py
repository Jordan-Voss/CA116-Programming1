a = []
n = raw_input()

while n != 'end':
   a.append(n)
   n = raw_input()

   i = 0
   while i < len(a):
      p = i
      j = i + 1
      while j < (len(a)):
         if int(a[j][6:8]) < int(a[p][6:8]):
            p = j
         elif int(a[j][6:8]) == int(a[p][6:8]) and int(a[j][3:5]) < int(a[p][3:5]):
            p = j
         elif int(a[j][3:5]) == int(a[p][3:5]) and int(a[j][0:2]) < int(a[p][0:2]):
            p = j
         j += 1
         tmp = a[p]
         a[p] = a[i]
         a[i] = tmp
      i += 1
i = 0
while i < len(a):
   print a[i][9:]
   i += 1