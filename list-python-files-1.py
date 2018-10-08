import os
files = os.listdir(".")

i = 0
while i < len(files):
   if files[i][-3:] == ".py":  
      print files[i]
   i = i + 1