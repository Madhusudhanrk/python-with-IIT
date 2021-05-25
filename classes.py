class person:
    def __init__(self,name,age,sex):#this is constructor default method of the class
       self.Name = name
       self.Age = age
       self.Sex = sex
    def person_bio(self):
        information = "This is "+ self.Name +" bio data"
        name = self.Name
        age = self.Age
        sex = self.Sex
        print(information) 
        print(name) 
        print(age) 
        print(sex) 
    def normal_func(self,value):
        print(value+" this is the word u entered")

person1 = person("madhu",22,"male")
person2 = person("keerthi",20,"female")
person1.person_bio()
person2.person_bio()
show = person("lovely",20,"female")#object created but without calling constructor wont work if exist
value = input("type u want:\n")
show.normal_func(value)