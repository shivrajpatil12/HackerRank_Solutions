import math

AB = int(input())
BC = int(input())

AC = math.sqrt(AB**2 + BC**2)
h = AC/2.0
adj = BC/2.0
# Cos0 = (adj/h)

output = str(int(round(math.degrees(math.acos(adj/h))))) + '°'
print(output)
