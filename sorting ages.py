elif int(a[j][6:8]) == int(a[p][6:8]) and int(a[j][3:5]) < int(a[p][3:5]):
            p = j
         elif int(a[j][3:5]) == int(a[p][3:5]) and int(a[j][0:2]) < int(a[p][0:2]):
            p = j
      j += 1