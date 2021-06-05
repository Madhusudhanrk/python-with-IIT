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

# WHAT IF NEED CUSTOMIZE ITERATOR
class myNumber():
    def __init__(self):
        self.num = 100
    def __iter__(self):
        """This two functions will automatically initialize when object created and called"""
        return self
    def __next__(self):
       
       val = self.num
       if val <= 100000:
           self.num = self.num * 10
           return val
       else:
           raise StopIteration

x = myNumber()
'''iterable function will return iter object and next function will return 1 by 1 values till infinite without any condition'''
for y in x:#internally it uses __next__function
    print(y)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
