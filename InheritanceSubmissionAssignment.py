
##parent class establishing Avengers
class Avenger():
    name = 'Captain America'
    email = 'capamerica@avengers.com'
    password = 'IronMaNisAjerk$5834'
    acount_number = 1


##child class showing who is in the Avengers team
class Hero(Avenger):
    leader = 'Captain America'
    tech = 'Iron Man'
    bio = 'Incredible Hulk'
    demi_god = 'Thor'


##child class showing another part of the Avengers entity
class Shield(Avenger):
    leader = 'Nick Fury'
    headquarters = 'New York City'
    
print(Hero)
