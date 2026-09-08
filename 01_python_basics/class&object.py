# class syntax - class ClassName:

class DemoClass:
    """
    this is a sample class iam creating for understanding this class and object
    In this class let us create a method and variable and see how can we access then using an object
    """
    a=10

    def sum(self):
        print("this is a sample test program")
# this is an object creation ,syntax is obj=classname():
object=DemoClass()
# objname. desired method we call it
print(object.a)
object.sum()

