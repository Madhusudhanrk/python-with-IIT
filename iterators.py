num = [1,2,3,4,5]
for i in num:
    print(i)
# o/p 1 2 3 4 5
# for loop use internally iterator
# and the iterator works on iter and next , iter method,function makes an object of iterator and next go for next element.

num = [10,20,30,40,50]

x = iter(num)
print(next(x))
# o/p 10
# x.__next__ also be used because it is a function and also a method
print(next(x))
# o/p 20 because next function will remember previous iterable position
