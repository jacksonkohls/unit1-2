name = input()
type = input("square, cylinder, or rectangle ")
if type == "square":
    sl = int(input("length "))
    print((sl**3)*7.5)
elif type == "rectangle":
    rl = int(input("length "))
    wl = int(input("width "))
    hl = int(input("height "))
    print((rl * hl * wl)*7.5)
elif type == "cylinder":
    dc = float(input("diamete r"))
    hc = float(input("height "))
    print(((dc/2)**2)*3.14*hc)
else:
    print("invalid")
print(name)