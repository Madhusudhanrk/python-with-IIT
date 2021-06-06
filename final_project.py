# Get a list of name as an input from the user and make the first letters in caps and print each word as a list
# i = 5
# list_of_names = []
# while i>=1:
#     list_of_names.append(input("Enter any names "+str(i)+" more times:\n"))
#     i = i-1
# list_of_names = [x.capitalize() for x in list_of_names]
# print(list_of_names)

# Write a Python code to configure the MySQL Connector in your system and Insert data to MySQL Table after which you Fetch and Display data from Table
  
# import mysql.connector
# mydb = mysql.connector.connect(
#   host = "localhost",
#   user = "username",
#   password = "password",
#   database = "madhu"
# ) 
  
# mycursor = mydb.cursor()
# sql = "INSERT INTO Student (Name, Age) VALUES (%s, %s)"
# val = ("madhu", "22")
  
# mycursor.execute(sql, val)
# mydb.commit()
  
# print(mycursor.rowcount, "details inserted")
# mycursor.execute("SELECT * FROM Student")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
  
# # disconnecting from server
# mydb.close()


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
