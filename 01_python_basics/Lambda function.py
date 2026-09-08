# def sum(a,b):
#     return a+b
# print(sum(2,3))

# i don't want to use this function  multiple times  , i just need to user once
# in that function there is singe line of code
# so use lambda function for this purpose. is a small anonymous function defined by using lambda keyword
# this lambda keyword is single expression itself
# syntax : lamdba parmeters : expression
# lambda a,b,c,d: a+b+c+d

sum = lambda a,b: a+b
print(sum(10,20))
