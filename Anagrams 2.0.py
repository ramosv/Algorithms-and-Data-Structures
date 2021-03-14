##1/22/2020 @ 5:00 PM
##Cs 301

##First Assignment
##Problem 1

import time

##Timer Function
def timer_one_param(function_name, param):
    start_time = time.time()
    value = function_name(param)
    end_time = time.time()
    return [end_time - start_time, value]

def timer_two_function(function_name, param1, param2):
    start_time = time.time()
    value = function_name(param1, param2)
    end_time = time.time()
    return [end_time - start_time, value]


def problem1(n):
    number=0
        
    for a in range(n+1):
        number+=a
        
    return number
## second version

def problem12(n):
    sum = n* (n+1)/2
    return sum

##Problem 2

def problem2(n):
    #Open the file
    file = open("words.txt")
    text = file.read().strip().split()
    checkwords=[]
     
#Conditions
    userInput = n
    if userInput in text:
        print("This IS a legit word "+ userInput)
    else:
        print("This word is NOT legit")
    return 
    file.close()

##Problem #3
from itertools import permutations
def problem3(n):

    file = open("words.txt")
    text = file.read().strip().split()   
    read= n
    
    perms = [''.join(p) for p in permutations(read)]
    counter = 0
    
    for i in perms:
        if i in text:
            counter += 1
            continue

    print("Number of words you can make: " )
    return counter
    

## Problem #4
from itertools import permutations

def problem4(n):
    
    file = open("words.txt")
    text = file.read().strip().split()   
    read= n
    
    perms = [''.join(p) for p in permutations(n)]
    words=[]
    
    for i in perms:
        if i in text:
            words.append(i)

    print("The words are you can make are " + str(words))
    words.clear()

def problem5():
    with open("words.txt") as word_file:
        actual_words = set(word.strip().lower() for word in word_file)

    Letters = set()
                       
    print("Problem 5")
    centerLetter = input("Center Letter: ")
    Letters.add(centerLetter)
    Letters.add(input("Letter 1: "))
    Letters.add(input("Letter 2: "))
    Letters.add(input("Letter 3: "))
    Letters.add(input("Letter 4: "))
    Letters.add(input("Letter 5: "))
    Letters.add(input("Letter 6: "))
    
    spellBee(actual_words, Letters, centerLetter)


def spellBee(wordset, letterset, centerLetter):
    stuff = set()
    output = set()
    count=0

    for word in wordset:
        tempset = set(word)
        if tempset - letterset == set() and len(word) >= 5:
            stuff.add(word)
            
    for thing in stuff:
        tempset2 = set(thing)
        if centerLetter in tempset2:
            output.add(thing)
            count=count+1
        
    finalWords = ', '.join(output)
    print("WORDS FOUND: ", finalWords)
    print("There are " + str(count) +" words!")

#def problem6():
    

