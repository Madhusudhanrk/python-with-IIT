# n doubles,triples
def multiply(n):
    return lambda val:val*n
doubles = multiply(2)
print(doubles(2))
triples = multiply(3)
print(triples(3))
#lamda takes multiple parameters,only 1 expression this is an single line anonymus function

#filter takes one function should be return true or false and takes a sequence of character and store the characters based on func return true if false it will ommit the passed argument.

#prime numbers using filter

def prime(max):
    for n in range(2,max):
        if max%n == 0:
            return False
        else:
            return True
filtered = filter(prime,range(10))
filtered = list(filtered)
print(filtered)

#map is also like a filter function except it won't depend on the return boolean it takes two parameters one is excutable func and other one is sequence of values.
def prime(max):
    for n in range(1,max):
        if max%n == 0:
            return False
        else:
            return True
mapped = map(prime,range(2,10))
mapped = list(mapped)
print(mapped)

def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters):
         return True 
    else: 
        return False 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
    print(s)
    