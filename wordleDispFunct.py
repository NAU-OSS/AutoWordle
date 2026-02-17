################################################################################
# WORDLE SOLVER DISPLAY FUNCTIONS
# This program is to assist users when guessing the wordle of the day
# This has all of the functions for the program display
# Created by Aiden Seay Spring'23
################################################################################
# IMPORTS
    # NONE

################################################################################
# CONSTANTS
OUT_PLACE = -101
NO_PLACE = -102
IN_PLACE = -103

################################################################################
# MAIN DISPLAY FUNCTIONS
################################################################################

# display the conditons the user put for the words
def displayConditions( lettersInPlaceBank, lettersOutPlaceBank, noLettersBank ):

    # print the display title
    print( "\nWord Conditions:")
    
    # display letters in place bank
    displayBank( lettersInPlaceBank, IN_PLACE )

    # display letters out of place bank
    displayBank( lettersOutPlaceBank, OUT_PLACE )

    # display no letters bank
    displayBank( noLettersBank, NO_PLACE )


# display the words that are remaining in the list
def displayWords( wordList ):

    # print title
    print("\nPossible Words:\n")

    # iterate through the word list
    counter = 0
    for word in wordList:
        counter += 1
        if counter % 8 == 0:
            print(word)

        elif counter == len(wordList):
            print(word)

        else:
            print(word, end = ", ")

    
    # print how many words are left
    print(f"\nNumber of Words: {len(wordList)}")

################################################################################
# SUPPORTING DISPLAY FUNCTIONS
################################################################################

# displays conditions for in place or no place
def displayBank( conditionBank, bankType ):
    
    # DISPLAY TITLE
    # check if title should out place
    if( bankType == OUT_PLACE ):
        
        # print out place title
        print( "Letters out of place |", end="" )

    elif( bankType == IN_PLACE ):

        # print in place title
        print( "Letters in place |", end="" )

    # assume that it is no place
    else:

        # print no place title
        print( "Letters not in word |", end= "" )

    # iterate through the list
    for set in conditionBank:

        print( f" {set} |", end="" )

    # print a new line
    print()
################################################################################