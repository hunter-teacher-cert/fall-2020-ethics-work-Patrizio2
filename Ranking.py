import math
from queue import PriorityQueue
podsize = 5       # the number of passengers traveling in a group
childcount = 0      
ffmiles = 0       # frequent flyer miles of the group or individual traveling together
ticketnumber = 0  # a way to identify order passengers purchased tickets. 
Customerdata = 1  ### value is to just simulate customer data found in the passengers profile
Childcheck = True ### value is to just simulate customer data found in the passengers profile
Age = 6           ### value is to just simulate customer data found in the passengers profile
Group = 8         ### value is to just simulate customer data found in the passengers profile

customers = PriorityQueue() # This will be changed to accept objects just testing for now.
customers.put((-2, "Harry"))
customers.put((-3, "Charles"))
customers.put((-1, "Riya"))
customers.put((-4, "Stacy"))


# Each "pod" of passengers is recieved in and a ranking number is generated
# A pod are all the people who purchased their tickets together.
# For example a solo traveler has a pod size of 1 and a group of 4 has a pod size of 4.

for x in range(0, podsize-1):
    ffmiles = ffmiles + Customerdata
    if Childcheck:   ### counts number of children in group
        if podsize >1:                    ### Group with children
            childcount = childcount + 1
            Childcheck = True
            Group = 100000
        else:                             ### Unacompanied Minors
            Group = 1000
    elif podsize >1:                      ### Group
        Group = 10000
    else:
        Group = 0
    if podsize == 1 and Age <7 :          ### Solo Travelers
        Group = 50000
    
    ###Calculates the ranking
    ### assumes 300 seat max. The sooner a person buys a ticket, the higher their ranking should be
    ### thus the (300 - 1)
    ### The Group value can be changed to make one group come out of the queue ahead of another
    Ranking = (Group + (ffmiles/10) + podsize + (300 -ticketnumber))     


### The higher the number, the higher the ranking.
### Because the priority queue pulls the "lowest" number first the order would
### come out opposite to what we need. To get around this I needed to multiply the Ranking by -1 to reverse
### the order.  
    
for x in range(0, podsize-1):
    customers.put((Ranking*(-1), "TesterHarry"))
    
        


### I'll use this while statement to call out the prioritized customers and store them
### into the four group categories.

while customers:
     print(customers.get())


### Working on creating an object for the priority queue
class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print ('New Level:', description)
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Q.PriorityQueue()

q.put(Skill(5, 'Proficient'))
q.put(Skill(10, 'Expert'))
q.put(Skill(1, 'Novice'))

while not q.empty():
    next_level = q.get()
    print ('Processing level:', next_level.description)



'''import Queue

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print ('New job:', description)
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()

q.put( Job(3, 'Mid-level job') )
q.put( Job(10, 'Low-level job') )
q.put( Job(1, 'Important job') )

while not q.empty():
    next_job = q.get()
    print ('Processing job:', next_job.description)'''
