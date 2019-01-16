"""///////////////// ALL ASSIGNMENTS INCLUDE THIS SECTION /////////////////////
//
// Title:           WordGuesser.py
// Files:           WordGuesser.py, dictionary.csv
//
// Author:          Hunter Abraham
//
// Online Sources:  None
// Description: This program uses a binary search algorithm to try to guess a
//              the word a person gives.
/////////////////////////////// 80 COLUMNS WIDE ////////////////////////////"""

import numpy as np
import pandas as pd

#Binary search to find word
def binary_search(item_list,item):
    start = 0
    end = item_list.shape[0] - 1
    found = False
    mid = int((start + end)/ 2)
    found = False
    while start <= end and not found:
        #Finds middle of start and end points of search area
        mid = int((start + end)/ 2)        
        if item_list[mid] == item:
            return item
        print("My guess is " + item_list[mid] + ".")
        user_input = get_user_input()
        if user_input == "before":
            #If user val is before guessed val, refines search area to the half before guessed val
            end = mid - 1
        elif user_input == "after":
            #If user val is after guessed val, refines search area to the half after guessed val
            start = mid + 1
    #If no match found, return -1 as issue code
    return -1

   
#Gets user input
def get_user_input():
    user_input = input("Is your word before or after this word alphabetically?\n")
    return user_input

#Main body
#Read csv with pandas
f = pd.read_csv("dictionary.csv", delimiter = ",")
#Conver pandas series to numpy nd array
f = f.values
play_again = "yes"
#Start game loop
while play_again == "yes":
    userWord = input("Please enter a word: ")
    foundWord = binary_search(f, userWord)
    if foundWord == -1:
        print("Hmm... It looks like your word isn't in my vocabulary")
    else:
        print("I found it! Your word is " + str(foundWord))
    play_again = input("Would you like to give me another word?\n")

print("Goodbye!")
