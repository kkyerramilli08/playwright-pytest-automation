# print("this is a normal code without exceptions")
# print(5/0)
# print("we are at the end of the code")

# print("starting of the code")
#  try:
#     print(5/1)
# except:
#     print("we are in catch block")

print("starting of the code")
try:
    print(5/0)
except ZeroDivisionError as e:
    print("we are in catch block ZeroDivisionError")
except IndexError:
    print("we are in catch block IndexError")
except:
    print("we are in generic catch block")

print("at the end of the code")

