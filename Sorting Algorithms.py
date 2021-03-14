#############################################################################
## Assignment 5: Sorting Lists                                             ##
## CS 301                                                                  ##
## Due Wednesday, April 22, at 5:00pm                                      ##
## By: Vicente Ramos                                                       ##
#############################################################################

import random
test = random.sample(range(1, 1000), 500)


####################
## INSERTION SORT ##
####################

## Running Time: The worst case scenario would be if the items in the list are in reversed order. In this 
##               case the insertion sorting algorithm running time is O(n2). Best case scenarie would be
##               if the list is already sorted, but the algorithm still checks to make sure its sorted
##               correctly so the best case scenario is still O(n).

def insertionSort(alist):
    blist = [len(alist)]
    
    for i in range(1, len(alist)): 
  
        key = alist[i]
        temp = i-1

        blist.append(temp)
        
        while temp >= 0 and key < blist[temp]: 
                blist[temp + 1] = blist[temp]
                temp -= 1
        blist[temp + 1] = key

    return blist
        
  
## Testing the Insertion Sort:
    
print("############## INSERTION SORT ##############")
alist = [55,1,7,35,18,43]
print("Unsorted List: ", alist)
print("Sorted List: ", insertionSort(alist))
#print("Unsorted List: ",test)
#print("Unsorted List: ", isertionSort(test))



#################
## BUBBLE SORT ##
#################

## Running Time: Just like in Insertion sort the worst case scenario would be if the items in the list are in reversed order.
##               In the worst case scenario every comparison will cause an exchange and the total running time is O(n2). 
##               The best case scenario would be if the list is already in order, which means no exchanges will be made.
##               Even without making any exchnages, the best running time of this algorithm is O(n).       

def bubbleSort(alist): 
    n = len(alist) 
   
    for x in range(n):
        
        for i in range(0, n-x-1):
            
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
    return alist
                

## Testing the Bubble Sort:
                
print("############## BUBBLE SORT ##############")
blist = [55,1,7,35,18,43]
print("Unsorted List: ", blist)
print("Sorted List: ", bubbleSort(blist))
#print("Unsorted List: ",test)
#print("Sorted List: ", bubbleSort(test))


  
####################
## SELECTION SORT ##
####################

## Running Time: The total running time of the Selection sort algorithm is O(n2).
##               This O(n2) complexity is due to the nested for loop. This sorting algorithm 
##               is similar to Bubble sort as it makes the same number of comparisons. The major
##               advantge for Selection sort over Bubble sort is that it performs a lower
##               number of exchnages, making it more efficient but its still O(n2).

def selectionSort(alist):
    for x in range(len(alist)-1, 0, -1):
        maxnum_index = 0
        
        for i in range(1, x+1):
            
            if alist[i] > alist[maxnum_index]:
                maxnum_index = i
                
        temp = alist[x]
        alist[x] = alist[maxnum_index]
        alist[maxnum_index] = temp

    return alist


## Testing the Selection Sort:
       
print("############## SELECTION SORT ##############")
clist = [55,1,7,35,18,43]
print("Unsorted List: ",clist)
print("Sorted List: ", selectionSort(clist))
#print("Unsorted List: ", test)
#print("Sorted List: ", selectionSort(test))



#################  
## MERGE SORT  ##
#################

## Running Time: The running time for the Merge sorting algorithm is O(nlogn), this is because
##               it takes O(logn) to divide a list in half where n is the length of the list.
##               The second part of this algorithm merges the lists together, this takes n time.
##               This gives us a total running time of O(nlogn) for the Merge Sorting algorithm


# Function that inputs two sorted list and merges them to create one sorted output list
def merge(alist, blist):
    clist = [] 
    x = 0
    i = 0
  
    while x < len(alist) and i < len(blist): 
        if alist[x] < blist[i]:
            clist.append(alist[x])
            x+=1
  
        else:
            clist.append(blist[i])
            i+=1
            
    while x < len(alist): 
            clist.append(alist[x])
            x+=1
          
    while i < len(blist): 
            clist.append(blist[i])
            i+=1
    
    clist.extend(alist[x:])
    clist.extend(blist[i:])
    return clist

 
# Recursive function to sort a single unsorted list
def mergeSort(alist):
    if len(alist) == 0 or len(alist) == 1:
        return alist[:len(alist)]

    middle = len(alist) // 2 
    Left = alist[0:middle]  
    Right = alist[middle:len(alist)]

    print(middle)
    print("left: ",Left)
    print("right: ",Right)
  
    newLeft = mergeSort(Left) 
    newRight = mergeSort(Right)

    print("new left: ",newLeft)
    print("new right: ",newRight)
  
    newList = merge(newLeft, newRight)

    return newList

            
## Testing the Merge Sort:
            
print("############## MERGE SORT ##############")
dlist = [4,1,57,34,35,27,18] 
print("Unsorted List: ",dlist)
print("Sorted List: ", mergeSort(dlist))
#print("Unsorted List: ", test)
#print("Sorted List: ", mergeSort(dlist))


# Testing the merge Function separately: 

# 'blist' was sorted using Bubble sort and 'clist' was sorted using
# Selection sort, now we use the merge function to create one sorted
# output list containing all the items from both lists.
print("############# COMBINING LISTS ##############")
print("List One: ", blist)
print("List Two: ", clist)
print("Merged List:",merge(blist, clist))


  

