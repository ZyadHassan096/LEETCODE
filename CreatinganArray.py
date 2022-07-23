# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:23:10 2022

@author: ROG
"""

class DVD:
    def __init__(self,name,relaseyear,director):
        self.name=name
        self.relaseyear=relaseyear
        self.director=director
        
    def print_DVD(self):
        return self.name + ', directed by ' + self.director + ', released in ' + str(self.relaseyear)
    
avengersDVD = DVD('The Avengers', 2012, 'Joss Whedon')

incrediblesDVD = DVD("The Incredibles", 2004, "Brad Bird")

lionKingDVD = DVD("The Lion King", 2019, "Jon Favreau")



dvdCollection = []

dvdCollection.insert(1, avengersDVD)
dvdCollection.insert(0, incrediblesDVD)
dvdCollection.insert(2, lionKingDVD)

for i in  range(len(dvdCollection)):
    print(i)
    
    
numbers = []

for i in range(1,10):
    numbers.append(i)
    
print (len(numbers))

print (len(dvdCollection))