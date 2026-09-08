from configparser import ConfigParser

# config = ConfigParser() # defining an instance for it
# config.read('config.ini')
# # to get data
# print(config.get("basic info","browserName"))
# print(config.get("basic info","URL"))
# print(config.get("mobile","executionOS"))

# in order to work on utility perspective you need to create a method
def readConfig(section,key):
    config = ConfigParser()
    config.read('config.ini')
    return config.get(section,key)

print(readConfig("basic info","URL"))
print(readConfig("basic info","browserName"))
print(readConfig("mobile","executionOS"))

