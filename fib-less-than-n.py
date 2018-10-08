n = input()
i = 0
curr = 1
prev = 0
print curr
new = 0
while new < n:
   new = prev + curr
   if new < n:
      print new
   tmp = new
   new = curr
   curr = tmp
   tmp = new
   new = prev
   prev = tmp
   i = i + 1