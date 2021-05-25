import random

def generaterandom(max):
   result =  random.randint(1,max)
   return result

def main():
   result1 = generaterandom(10)
   result2 = generaterandom(10)
   final_result = result1 * result2
   user_input = input("what ans expected "+str(result1)+"x"+str(result2)+":\n")
   user_input = int(user_input)
   if user_input==final_result:
      print("matched")
   else:
      print("not matched")

main()