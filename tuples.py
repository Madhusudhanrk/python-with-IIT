#tuple is ORDERED,UNCHANGEABLE,ALLOW DUPLICATES
cars = ("alto 800","fortuner","polo","hummer")
print(cars)
# cars.append("new car") values can't be added or updated

#way to add value to tuples

x = list(cars)
x.append("new car")
cars = tuple(x)
print(cars)
print(len(cars))
print(type(cars))
