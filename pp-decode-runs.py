n = raw_input()
output = ''
while n != 'END':
   output = output + (n[0] * int(n[2:]))
   n = raw_input()
print output