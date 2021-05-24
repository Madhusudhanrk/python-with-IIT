"""Functions as arguments"""
list = ["car","bus","bike","tractor",]
def loop(x):
    print(x*3)
# loop(list)
""" A LOCAL FUNCTION CAN RUN INSIDE ANOTHER LOCAL FUNCTION BY PASSING A FUNC AS ARGUMENT BASES ON REF WAY SO THE FUNCTIONS NO NEED TO BE GLOBAL alo consider mapping """
def map_function(loopref,list):
    for items in list:
        loopref(items)
        
map_function(loop,list)