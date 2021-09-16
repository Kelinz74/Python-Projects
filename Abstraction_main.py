#imported abc (AbstractBaseClass)
from abc import ABC, abstractmethod
#parent Class
class Hero(ABC):
    #class attributes
    health = 0
    armor = 0
    power = 0
    # class method giving the value 10 to health from the object peter.heal(10) 
    def heal(self, a):
        self.health += a 
    # abstract method
    @abstractmethod
    def wound(self,x):
        pass
# child class defining the implementation of the Parent abstract method
class Attack(Hero):
    def wound(self,x):
        self.health = self.health - x
        print('You were hit!  Your health is now {}.'.format(self.health))    

# Created the object peter for class Attack and Hero
peter = Attack()
# object giving variable health 10 through the heal method
peter.heal(10)
print('Your health is {}.'.format(peter.health))
# object taking away 3 from the variable health in the class Hero via the Class Attack with
# wound method
peter.wound(3)


