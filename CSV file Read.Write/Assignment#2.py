import random
from random import randrange
import csv
import time

##LISTS METHODS
        #alist.append(item)     #Adds a new item to the end of a list
        #alist.insert(i,item)   #Inserts an item at the ith position in a list
        #alist.pop()            #Removes and returns the last item in a list
        #alist.pop(i)           #Removes and returns the ith item in a list
        #alist.sort()           #Modifies a list to be sorted
        #alist.reverse()        #Modifies a list to be in reverse order
        #del alist[i]           #Deletes the item in the ith position
        #alist.index(item)      #Returns the index of the first occurrence of item
        #alist.count(item)      #Returns the number of occurrences of item
        #alist.remove(item)     #Removes the first occurrence of item

##DICTIONARIES METHODS
        #adict.keys()         Returns the keys of the dictionary in a dict_keys object
        #adict.values()       Returns the values of the dictionary in a dict_values object
        #adict.items()        Returns the key-value pairs in a dict_items object
        #adict.get(k)         Returns the value associated with k, None otherwise
        #adict.get(k,alt)     Returns the value associated with k, alt otherwise

def generateLists(funct,filename,i,item):
    
    with open(filename, 'w', newline= '\n') as file:
        #Range(Start Size, End Size, Growth Rate)
        for listSize in range(1000000,10000001,1000000):         
            #Range of the numbers in the list
            alist = [randrange(1000000) for x in range(listSize)]
            returning = None
            #Calculate time for the method
            if i == '' and item == '':
                start = time.time()
                funct(alist)
                end = time.time()
                returning = str(funct.x)
            elif item == '':
                start = time.time()
                funct(alist, i)
                end = time.time()
                returning = str(funct.x)
            else:
                start = time.time()
                funct(alist, i, item)
                end = time.time()
                #returning = str(funct.x)
                

            if returning is None:
                returning = str('None')
            #Write to CSV file
            writer = csv.writer(file)
            writer.writerow((str(listSize),str(end-start)))
            print("Size: %d Time: %f return: %s" % (listSize, end-start, returning))
            
##LISTS METHODS
def listsort(listname):
    listsort.x = listname.sort()
    
def listreverse(listname):
    listreverse.x = listname.reverse()

def listpop(listname):
    listpop.x = listname.pop()

def listpopindex(listname, i):
    listpopindex.x = listname.pop(i)

def listcount(listname, i):
    listcount.x = listname.count(i)

def listdelete(listname, i):
    del listname[i]

def listindex(listname, i):
    listindex.x = listname.index(i)

def listappend(listname, i):
    listname.append(i)
    
def listinsert(listname, i, item):
    listname.insert(i,item)
    
##Dictionary
##Words has 113809 words or "keys"
##Assign each key a value


def dictionary(funct, filename, k):
    #Adds Words from text file to a list
    file = open("words.txt")
    text = file.read().strip().split()
    keywords = []   
    for i in text:
        keywords.append(i)

    values = []
    values = list(range(0,113809))
    returning = None

    with open(filename, 'w', newline= '\n') as file:

        res = dict(zip(keywords,values))
        #print(str(res))
        
        if k == '':
            start = time.time()
            funct(res)
            end = time.time()
            returning = str(funct.x)
        else:
            start = time.time()
            funct(res, k)
            end = time.time()
            
        #Calculate time for the method
        

        #Write to CSV file
        writer = csv.writer(file)
        writer.writerow(str(end-start))
        print("Time: %f return: %s" % (end-start, returning))

##LISTS METHODS  

def dictkeys(dictname):
    dictkeys.x = dictname.keys()
    
def dictvalues(dictname):
    dictname.values()

def dictitems(dictname):
    dictname.items()

def dictget(dictname, k):
    dictname.get(k)




    

