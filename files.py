# f = open("trial_file.txt","w")#ready the file to get written if exist either create a new file

# f = open("trial_file.txt1","x")#only create file
# f.write("firstline1")
# f.close()#file closing good practice

# f =open("trial_file.txt","a")#appending txt to new file
# f.write("last line")

f = open("trial_file.txt","r")
# print(f.read())#reads all over file
print(f.readline(8))#reads all over line
print(f.readline())#reads all over next line
print(f.readlines())#reads all over lines but place at before

import os
if os.path.exists("trial_file1.txt"):
     os.remove("trial_file1.txt")

# f = open("trial_file.txt")
