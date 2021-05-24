list = ["knowledge","code","black","22","1.0",False]
for x in list:
    print(x)

print(list)#entire list
print(list[0])#list index
#list is ORDERED,CHANGEABLE,ALLOW DUPLICATES
list[2]="orange"
print(list[2]) #value changed

print(list[2:5])#can use all array functions
list[2:5]=["orange","space","girls"]#multiple values updated or chaged
print(list)
#to insert
list.insert(1,"girls")
print(list)
#append will add value into last index of the list
list.append("style")
print(list)