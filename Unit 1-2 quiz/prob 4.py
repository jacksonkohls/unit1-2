import math
year= float(input())
cent =year//100 + (year%100)/100
print(math.ceil(cent))