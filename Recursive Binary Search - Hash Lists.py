#############################################################################
## Assignment 4: Searching Lists                                           ##
## CS 301                                                                  ##
## Due Monday, April 6, at 5:00pm                                          ##
## By: Vicente Ramos                                                       ##
#############################################################################
import random

test = random.sample(range(1, 1000), 500)
test.sort()

##Question 1
def rec_binarysearch(ilist, item, low_index='', high_index=''):
    if low_index == '' and high_index == '':
        high_index = len(ilist)-1
        low_index = 0
        
    middle_index = (low_index + high_index)//2
    if high_index < low_index:
        print("Not in list")
        return False
    
    temp = ilist[middle_index]
        
    print('low =', low_index)
    print('middle =', middle_index)
    print('high =' , high_index)
    print(temp)
    
    if temp == item:
        return middle_index
    if temp > item:
        return rec_binarysearch(ilist, item, low_index, middle_index-1)
    else:
        return rec_binarysearch(ilist, item, middle_index+1, high_index)
        
##Question 2
class HashList:
    def __init__(self, length):
        self.hlist = [None]* length
        self.len = length
        self.count = -1

    def print(self):
        print(self.hlist)

    def hashfunction(self, item):
        return item % self.len

    def rehashfunction(self, oldpos):
        return (oldpos + 7) % self.len
    
    def put(self,key):
        keys = self.hlist

        if(self.count == len(keys)-1):
            print("ERROR: List is Full")
            return
        self.count +=1
             
        hvalue = self.hashfunction(key)
        if self.hlist[hvalue] == None:
            self.hlist[hvalue] = key
            
        else:
            nextslot = self.rehashfunction(hvalue)
            while self.hlist[nextslot] != None and self.hlist[nextslot] != key:
                nextslot = self.rehashfunction(nextslot)
            if self.hlist[nextslot] == None:
                self.hlist[nextslot]=key  

    def contains(self,key):
        aslot = self.hashfunction(key)

        stop = False
        found = False
        position = aslot
        while self.hlist[position] != None and not found and not stop:
            if self.hlist[position] == key:
                found = True
            else:
                position=self.rehashfunction(position)
                if position == aslot:
                    stop = True
        return found

    def items(self):
        keys = self.hlist
        temp = []
        for x in keys:
            if x != None:
                temp.append(x)
        return temp



##Question 3
#   Best-case scenario: In the case in which there are no coolisions the running time of the HashList
#                       function is O(1) since a constant amount of time is required to compute the hash
#                       value and then index the hash table at that location.
#                       
#   Worst-case scenario: The number of collisions depends heavily on the load factor, a small load factor
#                        has a lower probability of a collision while a large load factor which we experience
#                        when the table is filling up means that there will be more collisions
#                        In the worst case in which there are many collisions the running time of the
#                        HashList function is O(n).

##Question 4
#   A dictionary is a collection of key/value pairs, where the keys work as indexes for the values.
#   A dictionary grows according to the need. In order to convert our HashList into a dictionary
#   I would to change the _init_ functions that takes the size of the list and sets it to the length,
#   since a Dictionary grows independently as needed this would have to be changed. In a HashList the
#   key and value are loosely typed. To modify this into a Dictionary I would have to explicitly defined 
#   in the code the key and value types. The way in which we add items to the Hashlist would also need to change,
#   in a dictionary the order in which the entries are added is maintained. In a hashlist the order is not maintained.
