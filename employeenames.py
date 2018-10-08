n = raw_input()
a = []
while n != 'end':
   a.append(n[:8] + n[9:])
   n = raw_input()


b = []
n = raw_input()
while n != 'end':
   b.append(int(n))
   n = raw_input()

i = 0
j = 0
while i < len(b):
   if i < len(b) and b[i] != int(a[i][:8]): :
      print a[i][8:]

   i += 1