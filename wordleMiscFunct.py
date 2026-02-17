################################################################################
# WORDLE SOLVER MISC FUNCTIONS
# This program is to assist users when guessing the wordle of the day
# This has all misc functions
# Created by Aiden Seay Spring'23
################################################################################
# IMPORTS
import os

################################################################################
# CONSTANTS
DICTIONARY = "fiveLetterWords.txt"

################################################################################
# MAIN MISC FUNCTIONS
################################################################################

# access the text file dictionary and returns a list
def accessDictionary():

    # read the txt file
    with open(DICTIONARY, 'r') as words:
        wordList = []

        # iterate through each word and put it in the list
        for word in words:
            wordList.append(word.strip("\n"))
    
    # return the word list
    return wordList


# asks the user if they found the word and if they did, return true
def checkIfFound():
    
    # display prompt for correct word
    wordFound = input("\nEnter 'yes' if you got the correct word: ").upper()

    # check the user input
    if wordFound == "YES":

        # return true for correct word
        return True
    
    # assume false for not the correct word
    return False


# displays the title and purpose of the program
def introduciton():
    
    # clear the screen
    os.system("cls")

    # print title and instrucitons
    print("Wordle Solver\n=============")
    print("This program solves the worldle of the day\n")


################################################################################
# SUPPRTING MISC FUNCTIONS
    # NONE

################################################################################