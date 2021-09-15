
### Private attribute. ###

# a class Encapsulating private methods indicated by the use of double underscores __ .
class Protected:
    # class method initializing the object __privateVar = 12. Utilizing the a private variable
    # indicated by the use of double underscores __
    def __init__(self):
        self.__privateVar = 12

        
    # class method printing the __privateVar value by calling the value through self. from the
    # __privateVar variable within the class.
    def getPrivate(self):
        print(self.__privateVar)
        
        
    # class method that is setting the __privateVar variable to be equal with an aurgument
    # set outside of the class.  obj.setPrivate(23) will change the peramiter of the function 
    # setPrivate(private) to equal 23.  Then will be called to be displayed in the consol via 
    # obj.getPrivate()
    def setPrivate(self, private):
        self.__privateVar = private

# setting the class to an object = obj
obj = Protected()
# calling the object obj and the method getPrivate() =obj.getPrivate() which will then run the
# code for that method
obj.getPrivate()
# calling the object obj and the method setPrivate() =obj.setPrivate() which will set the
# variable self.privateVar = 12 to self.privateVar = 23 via the function aurgument set by
# the object obj.setPrivate(23)
obj.setPrivate(23)
# calling the object obj.getPrivate() to display the new value of self.privateVar = 23.
obj.getPrivate()



###  Protected attribute ###

# a class Encaplusating protected methods indocated by the use of a single underscore _ .
class Protected:
    # class method initializing the object _protectedVar = 0. Utilizing the protected variable
    # indicated by the use of a single underscore _
    def __init__(self):
        self._protectedVar = 0

# setting the classe to an object = obj
obj = Protected()
# changing the value of the variable self.protectedVar to 34
obj._protectedVar = 34
# object obj.protectedVar print the value of self.protectedVar to the console
print(obj._protectedVar)
