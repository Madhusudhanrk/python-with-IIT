#list comprehension is a method to make ur code short when list involved

fruits = ["mango","kiwi","apple","grapes"]

#normal method
sorted_fruits_list=[]
for x in fruits:
    if "a" in x:
        sorted_fruits_list.append(x)
print(sorted_fruits_list)
        
#list comprehension method
sorted_fruits_list = [x for x in fruits if "s" in x]
print(sorted_fruits_list)
#another 1

sorted_fruits_list = [x if x%2==0 else x%2==0 for x in range(10)]
print(sorted_fruits_list)