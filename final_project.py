# Get a list of name as an input from the user and make the first letters in caps and print each word as a list
i = 5
list_of_names = []
while i>=1:
    list_of_names.append(input("Enter any names "+str(i)+" more times:\n"))
    i = i-1
list_of_names = [x.capitalize() for x in list_of_names]
print(list_of_names)
