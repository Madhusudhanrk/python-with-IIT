colors = ["orange","black","red","green","silver"]
for color in colors:
    print(color)
print("\n")
    
for color in colors:
    if color=="red":
        continue
    if color=="green":
        break
    print(color)
print("\n")

for a in range(10):
    print(a)
print("\n")

x=1
while x<5:
    print(x)
    x=x+1
    