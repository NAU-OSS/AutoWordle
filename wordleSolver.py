################################################################################
# WORDLE SOLVER MAIN PROGRAM
# This program is to assist users when guessing the wordle of the day
# Created by Aiden Seay Spring'23
################################################################################
# IMPORTS
from wordleMiscFunct import *
from wordleInputFunct import *
from wordleElimFunct import *
from wordleDispFunct import *
 
################################################################################
# CONSTANTS
    # NONE

################################################################################
# MAIN FUNCITON
################################################################################

def main():
    
    # get the list of known words from the txt file
    wordList = accessDictionary()

    # set while loop condition to false
    foundWord = False

    # initialize already inputted letters
    lettersInPlaceBank = []
    lettersOutPlaceBank = []
    noLettersBank = []

    # run this loop until word is found
    while not foundWord:

        # clear the screen and display title
        introduciton()

        # get an check the input from the user
        getUserInput( lettersInPlaceBank, lettersOutPlaceBank, noLettersBank )

        # eliminate the words based off of the user conditions
        eliminateWords( wordList, lettersInPlaceBank, lettersOutPlaceBank, 
                                                                 noLettersBank )

        # display the words that still meet the conditions
        displayResults( wordList, lettersOutPlaceBank, lettersInPlaceBank, 
                                                                noLettersBank ) 

        # ask the user if they found the word. End loop if they did
        foundWord = checkIfFound()

    # print closing statement
    print("\nEND PROGRAM")

################################################################################
# MAIN SUPPORTING FUNCTIONS
################################################################################

def getUserInput( lettersInPlaceBank, lettersOutPlaceBank, noLettersBank ):

    # find word conditions
    lettersInPlace, lettersOutPlace, noLetters = findConditions()

    # add conditions to the bank of conditions
    addConditionsToBank( lettersInPlace, lettersOutPlace, noLetters, 
                        lettersInPlaceBank, lettersOutPlaceBank, noLettersBank )
    

# eliminate words that do not fit the letter characteristics
def eliminateWords( wordList, lettersInPlaceBank, lettersOutPlaceBank, 
                                                                noLettersBank ):

    # eliminate words without letters in a specific place
    eliminateLettersInPlace( wordList, lettersInPlaceBank )

    # eliminate words without the letters
    eliminateLettersOutPlace( wordList, lettersOutPlaceBank )

    # eliminate words that has letters
    eliminateNoLetters( wordList, noLettersBank ) 

# display the words remaining that meet the conditions
def displayResults( wordList, lettersInPlaceBank, lettersOutPlaceBank, 
                                                                noLettersBank ):
    
    # display the words that are remaining in the list
    displayWords( wordList )

    # display the conditons the user put for the words
    displayConditions( lettersOutPlaceBank, lettersInPlaceBank, noLettersBank )

################################################################################
main()