
s = a[0]
a[0] = a[len(a) - 1]
a.pop()
a.append(s)