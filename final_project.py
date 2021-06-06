# Get a list of name as an input from the user and make the first letters in caps and print each word as a list
i = 5
list_of_names = []
while i>=1:
    list_of_names.append(input("Enter any names "+str(i)+" more times:\n"))
    i = i-1
list_of_names = [x.capitalize() for x in list_of_names]
print(list_of_names)

# Write a Python code to configure the MySQL Connector in your system and Insert data to MySQL Table after which you Fetch and Display data from Table

import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user = "username",
  password = "password",
  database = "madhu"
) 
  
mycursor = mydb.cursor()
sql = "INSERT INTO Student (Name, Age) VALUES (%s, %s)"
val = ("madhu", "22")
  
mycursor.execute(sql, val)
mydb.commit()
  
print(mycursor.rowcount, "details inserted")
mycursor.execute("SELECT * FROM Student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
# disconnecting from server
mydb.close()


# Write a Python code to reverse the given integer and print the integer
number = input("Enter any integer:\n")
lenth = len(number)
number = int(number)
rev = 0
while number > 0:
    remainder = number % 10
    rev = rev * 10 + remainder
    number = number//10
print(rev)

# Write a Python code to read an integer in a file e.g 123 
# Convert it to words e.g One hundred and twenty three
# write the result back to the same file such that your file will have 123 One hundred and twenty three in it.

num = open('support_file.txt').read()
number = int(num)

def integer_to_english(number):
    if number>=1 and number<=1000:
        a = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninty ']
        if number<=20:
            if number%10==0: return a[number]
            else: return a[number]
        elif number<100:
            b=number-20
            r=b%10
            b//=10
            return a[20+b]+a[r]
        elif number<1000:
            if number%100==0:
                b=number//100
                return a[b]+' hundred'
            else:
                r=number%100
                b=number//100
                if r<=20:
                    return a[b]+' hundred'+' and '+a[r]
                else:
                    r=r-20
                    d=r//10
                    r%=10
                    return a[b]+' hundred'+' and '+a[20+d]+a[r]
        elif number==1000:
            return 'one thousand'
        else:
            return -1
my_list = str(integer_to_english(number))

f = open("support_file.txt", "a")
i = 1
while i < 2:
    f.write(str(my_list))
    i = i + 1
f.close()

#open and read the file after the appending:
f = open("support_file.txt", "r")
print(f.read())