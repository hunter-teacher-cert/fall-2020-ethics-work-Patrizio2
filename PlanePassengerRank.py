import math
from queue import PriorityQueue
podsize = 6       # the number of passengers traveling in a group
childcount = 0      
ffmiles = 0       # frequent flyer miles of the group or individual traveling together
ticketnumber = 0  # a way to identify order passengers purchased tickets. 
Customerdata = 1  ### value is to just simulate customer data found in the passengers profile
Childcheck = True ### value is to just simulate customer data found in the passengers profile
Age = 6           ### value is to just simulate customer data found in the passengers profile
Group = 8         ### value is to just simulate customer data found in the passengers profile


class Passenger(object):
    
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


passenger1 = Passenger("Maude", 5)
passenger2 = Passenger("Barleen", 9)
passenger3 = Passenger("David", 1)
passenger4 = Passenger("Halen" , 3)
passenger5 = Passenger("Van" , 2)
passenger0 = Passenger("Eddy" , 1)
passengers = [passenger4, passenger1, passenger5, passenger3, passenger2, passenger0]


### These lists will hold the passengers that have been sorted in them
GroupwithChildren = []
Group =[]
Solo = []
Unaccompanied = []


### It takes in a 'pod' of passengers travelling together (solo or group size).
### and generates a ranking number based on fflyer miles, early ticket purchase,
### and category the passengers fall into. The same number is used for each
### passenger in the group as a means of keeping them together.

### It then does two things:
### 1. Stores the ranking in each passengers profile 
### 2. Creates a list of the passengers in each category

for x in range(0, podsize):
    ffmiles = ffmiles + Customerdata
    if Childcheck:   ### counts number of children in group
        if podsize >1:                    ### Group with children
            childcount = childcount + 1
            Childcheck = True
            Group = 3000000
        else:                             ### Unacompanied Minors
            Group = 1000000
    elif podsize >1:                      ### Group
        Group = 2000000
    else:
        Group = 0                         ### Solo Travelers
###    if podsize == 1 and Age <7 :          
###        Group = 50000

print (podsize)
print (Group)
print (ffmiles)

Ranking = (Group + ffmiles + podsize + ticketnumber)

for x in range(0, podsize):
    passengers[x].priority = Ranking
    print (passengers[x].name , passengers[x].priority)


GWCCount = 0
GroupCount = 0
SoloCount = 0
UnaCount = 0

### GroupwithChildren = []
### Group =[]
### Solo = []
### Unaccompanied = []


print (len(passengers))

for x in range(len(passengers)):
    print(x)
    if passengers[x].priority < 1000000:
        Solo.append(passengers[x]) 
 #       Solo[SoloCount] = passengers[x]
        SoloCount = SoloCount + 1
        
    elif passengers[x].priority < 2000000:
        Unaccompanied[UnaCount] = passengers[x]
        UnaCount = UnaCount + 1
        
    elif passengers[x].priority < 3000000:
        Group[GroupCount] = passengers[x]
        Group = Group + 1
        
    else: 
        GroupwithChildren.append(passengers[x])
        GWCCount = GWCCount + 1
    
for x in range(0,len(GroupwithChildren)):
    print (GroupwithChildren[x].name,GroupwithChildren[x].priority)
    

customers = PriorityQueue() 

#for x in range(0, podsize-1):
customers.put((Ranking, "Harry"))

customers.put((podsize, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))




while customers:
     print(customers.get())
#Will print names in the order: Riya, Harry, Charles, Stacy.
