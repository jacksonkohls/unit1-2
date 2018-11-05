a = int(input())
b = int(input())
h = int(input())
# 28 days if a = 3 b = 2 h = 30
# if a = 2 b = 1 and h = 15, days = 14
# if a = 2 b = 0 and h = 2 days = 1
# if a = 2 b = 0 and h = 4 days = 2
# if a = 2 b = 1 and h = 4 days = 3
# days = (h/(a-b)) - b 
# so long as h >= a it works.

z= (h/(a-b)) - b
if z >= 0:
    print (z)
else:
    print("1")
    