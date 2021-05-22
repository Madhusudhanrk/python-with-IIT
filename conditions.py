a=300
b=200
c=100
if a>b:
    print("a is bigger")
elif a==b:
    print("a and b is equal")
else:
    print("b is bigger")
print("\n")
print("a is bigger") if a>b else print("b is bigger")#for single line purpose only

if a>b and c>a :
    print("and condition wins")
elif a>b or c>a :
    print("or condition wins")
else:
    print("else condition wins")

