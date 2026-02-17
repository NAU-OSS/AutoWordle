################################################################################
# WORDLE SOLVER INPUT FUNCTIONS
# This program is to assist users when guessing the wordle of the day
# This has all of the functions for gathering and checking user input
# Created by Aiden Seay Spring'23
################################################################################
# IMPORTS
import os

################################################################################
# CONSTANTS
LETTERS = 26
LETTERS_IN_WORD = 5
OUT_PLACE = -101
NO_PLACE = -102

################################################################################
# MAIN INPUT FUNCTIONS
################################################################################

# add correct conditions to the banks
def addConditionsToBank( lettersInPlace, lettersOutPlace, noLetters, 
                       lettersInPlaceBank, lettersOutPlaceBank, noLettersBank ):
    
    # ADD IN PLACE CONDITONS
    # check to see if blank
    if( lettersInPlace != [""] ):

        # add letters in place to bank and avoid duplicates
        for letter in lettersInPlace:

            duplicateNum = findIndexDuplicates( lettersInPlace, 
                                                            lettersInPlaceBank )

            # check if it isn't in the bank
            if( letter not in lettersInPlaceBank and not duplicateNum ):

                # add letter to the bank
                lettersInPlaceBank.append( letter )


    # ADD OUT OF PLACE CONDITIONS
    # add letters out place to bank and avoid duplicates
    for letter in lettersOutPlace:

        # check if it isn't in the bank
        if( letter not in lettersOutPlaceBank ):

            # add letter to the bank
            lettersOutPlaceBank.append( letter )


    # ADD NO LETTERS IN WORD CONDITIONS
    # add no letters to bank and avoid duplicates
    for letter in noLetters:

        # check if it isn't in any bank
        if( letter not in noLettersBank and letter not in lettersInPlaceBank 
                                        and letter not in lettersOutPlaceBank ):

            # add letter to the bank
            noLettersBank.append( letter )


# gets word conditions from the user and checks to see if they are correct
def findConditions():

    # set correct input to false
    allInputCorrect = False
    lettersInPlaceCorrect = False
    lettersOutPlaceCorrect = False
    noLettersCorrect = False
    ListConflict = False

    # loop while all of the input is incorrect
    while( not allInputCorrect ):

        # get letters in place input
        if( not lettersInPlaceCorrect ):
            lettersInPlace = getLettersInPlace()

        # get letters out place input
        if( not lettersOutPlaceCorrect ):
            lettersOutPlace = getLettersOutPlace()

        # get no letters input
        if( not noLettersCorrect ):
            noLetters = getNoLetters()

        # check letters in place input
        lettersInPlaceCorrect = checkLettersInPlace( lettersInPlace )

        # check letters out place input
        lettersOutPlaceCorrect = checkNoOrOutLetters( lettersOutPlace, 
                                                                     OUT_PLACE )

        # check no letters input
        noLettersCorrect = checkNoOrOutLetters( noLetters, NO_PLACE )

        # check to see if there is any conflict between lists
        if( lettersInPlaceCorrect and lettersOutPlaceCorrect and 
                                                             noLettersCorrect ):
            ListConflict = checkForConflict( lettersInPlace, lettersOutPlace, 
                                                                      noLetters)
        
        # if there is conflcit between lists then none are correct
        if( ListConflict ):

            lettersInPlaceCorrect = False
            lettersOutPlaceCorrect = False
            noLettersCorrect = False

        # check to see if all conditions are met to exit loop
        if( lettersInPlaceCorrect and lettersOutPlaceCorrect and 
                                                             noLettersCorrect ):
            # set all input correct to true
            allInputCorrect = True

        # assume there is an error and display error messages
        else:

            # display the error messages
            displayErrorMessage( lettersInPlaceCorrect, lettersOutPlaceCorrect,
                                              noLettersCorrect, ListConflict )

    # return the letter conditions
    return lettersInPlace, lettersOutPlace, noLetters

################################################################################
# SUPPORTING INPUT FUNCTIONS FOR FIND CONDITONS
################################################################################

def checkForConflict( lettersInPlace, lettersOutPlace, noLetters ):

    listConflict = False

    # check to see if the list is empty
    if( lettersInPlace != [""] ):

        # check to see if no letters conflicts with inPlace
        for set in lettersInPlace:

            # check if letter is in no letter list
            if( set[ 0 ] in noLetters ):

                # set listConflict to true
                listConflict = True

        # check to see if no letters conflcits with outPlace
        for letter in lettersOutPlace:

            # check if letter is in no letter list
            if( letter in noLetters ):

                # set listConflict to true
                notlistConflict = True

    return listConflict


# checks to see if letters in place has correct syntax and no conflict
def checkLettersInPlace( lettersInPlace ):

    correctSyntax = True
    correctEntriesNum = True
    
    # check to see if the entry is not empty
    if( lettersInPlace != [""] ):

        # iterate through each number in list
        for set in lettersInPlace:
        
            # check to see if the syntax is correct for each entry
            if( len( set ) != 3 or not set[ 0 ].isalpha() or set[1] != "," or
                            not set[ 2 ].isnumeric() or not int( set[ 2 ] ) <= 4 
                                                  or not int( set[ 2 ] ) >= 0 ):
                # set correct syntax to false
                correctSyntax = False

        # cannot go over five enteries
        if( len( lettersInPlace ) > LETTERS_IN_WORD ):
            
            # set noconflict to false
            correctEntriesNum = False

    return correctSyntax and correctEntriesNum


# checks to see if no letters has correct syntax and no conflict
def checkNoOrOutLetters( letterEntry, letterType ):

    correctSyntax = True
    correctEntriesNum = True
    
    # check to see if the entry is empty
    if( letterEntry != "" ):

        # check to see if all entries are letters
        if( not letterEntry.isalpha() ):
        
            # set correct syntax to false
            correctSyntax = False

        # see what specific list the function is check
        if( letterType == NO_PLACE ):

            # check to see if over entry limit
            if( len( letterEntry ) > LETTERS - LETTERS_IN_WORD ):

                # set correct number of entries to false
                correctEntriesNum = False

        # assume checking letters out of place
        else:

            # check to see if over entry limit
            if( len( letterEntry ) > LETTERS_IN_WORD ):

                # set correct number of entries to false
                correctEntriesNum = False

    return correctSyntax and correctEntriesNum


def displayErrorMessage( lettersInPlaceCorrect, lettersOutPlaceCorrect,
                                             noLettersCorrect, ListConflict ):
    # print error message title
    print( "\nError Mesages:")

    # check if letters in place error
    if( not lettersInPlaceCorrect ):
        
        # print error message
        print( "ERROR(Letters in place): 0 <= num <= 4 ex. a,0 r,4 ")

    # check if letters out of place error
    if( not lettersOutPlaceCorrect ):
        
        # print error message
        print( "ERROR(Letters out of place): Only letters for input ex. abc" )

    # check if no letters error
    if( not noLettersCorrect ):

        # print error message
        print( "ERROR(Letters not in word): Only letters for input ex. abc" )

    if( ListConflict ):
        
        # print error message
        print( "ERROR(Conflict): Letters not in word conflict with other lists" )

    # print new line
    print()


def findIndexDuplicates( lettersInPlace, lettersInPlaceBank ):

    # initialize index lists
    conditionIndecies = []
    bankIndecies = []
    indexDuplicates = False

    # get the indecies for lettersInPlace
    for set in lettersInPlace:

        # append the index into the list
        conditionIndecies.append( set[ 2 ] )

    # get the indecies for the bank
    for set in lettersInPlaceBank:

        # append the index into the list
        bankIndecies.append( set[ 2 ] )

    # if the index conditions are in bank
    for index in conditionIndecies: 
        if( index in bankIndecies ):

            # set index duplicates to true
            indexDuplicates = True

    # returns true if there are index duplicates
    return indexDuplicates


# get input for letters in place
def getLettersInPlace():

    # gather input from the user
    return input("Letters in place: ").lower().split(" ")


# get input for letters not in word
def getNoLetters():

    # gather input from the user
    return input("Letters not in word: ").lower()


# get input for letters out of place
def getLettersOutPlace():
    
    # gather input from the user
    return input("Letters out of place: ").lower()

################################################################################