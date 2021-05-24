#dict is unordered,changable,not allow duplicate values overwirte
dict={
    "name":"madhu",
    "age":22,
    "sex":"male"
}
print(dict)

#insert
dict["weight"]=80
print(dict)

#update
dict["weight"]=82
print(dict)
dict.update({"weight":81})

#select
print(dict.get("weight"))

#delete
dict.pop("weight")
print(dict)
