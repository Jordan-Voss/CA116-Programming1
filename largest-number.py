n = input()
i = 0
largest = -999999999999999999999
if largest < n:
      largest = n
elif n < largest:
      largest = largest
while i < 4:
   n = input() 
   if largest < n:
      largest = n
   elif n < largest:
      largest = largest
   i += 1
print largest