a=[1,2,3,4,5,6,7,8,9,10]
# a is a list which has 10 different values in that
'''
"i want to print all the values in the list one after the another"
"the syntax is - for variable in a :"
"whatever the values are there in the list, it will be picking from zero index means first value" \
"and storing it in num" 
'''
for num in a:
    print(num)

for num in range(5):
    print(num)

for num in range(2,7):
    print(num)

print("test1 completed")

b=1
while b<10:
    b = b + 1
    print(b)
# without defining anything it will be an infinity loop means it won't comeout from the execution, it will always execute
# I haven't specified any condition to terminate the loop, so define an increment b value by 1 and it will \
# increment b value by 1  everytime and after 10 times b will become 11 and 11<10 as the condition is false it will come out of the loop
print("test2  completed")

