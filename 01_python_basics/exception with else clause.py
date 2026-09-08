# Try with else clause
# finally block : always executed no matter whether we are in try or except block
print("starting of the code")
try:
    print(5/0)
except:
    print("we are in the catch block")

else:
    print("we are else in the catch block")
finally:
    print("we are the finally block")
print("at the end of the code")
