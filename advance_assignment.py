# def primenumber(number):
#    count=2
#    divided = 0
#    while(count<=10):
#       if(number%count==0):
#           divided = divided+1
#       count = count+1
#    if(divided>1):
#     	print(str(number) + "this is not prime Number")
#    else:
#     	print(str(number) + "this is prime Number")
	
# input_number = input("Enter a Number I will tell the number is primenumber or not:")
# if(input_number.isdigit()):
# 	input_number = int(input_number)
# 	primenumber(input_number)

# def evenorodd(number):
#     if(number%2==0):
#         print(str(number) + "this is even Number")
#     else:
#         print(str(number) + "this is odd Number")
# input_number = input("Enter a Number I will tell the number is even or odd:")
# if(input_number.isdigit()):
# 	input_number = int(input_number)
# 	evenorodd(input_number)

def fibonacci(number):
    i=0
    ans = 0
    value = 1
    temp = 0
    fibonacci_list = []
    while(ans<=number):
        ans = temp + value
        temp = value
        value = ans
        if ans<=number:
            fibonacci_list.append(ans)
        i = i+1
    for j in fibonacci_list:
         print(j)
  
input_number = input("Enter a N Number I will print all fibonacci numbers in the range:")
if(input_number.isdigit()):
	input_number = int(input_number)
	fibonacci(input_number)