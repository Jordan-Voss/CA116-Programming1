n = 10
hist = [0] * n
line = raw_input()
while line != "end":
   hist[int(line)] += 1
   line = raw_input()
i = 0
while i < n:
   print i, "*" * hist[i]
   i = i + 1