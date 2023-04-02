#lambda function
x = lambda x:x+1
print(x(4))

#lambda function in another function
def my_func():
     x=lambda x:x+2
     print(x(7))
my_func()     