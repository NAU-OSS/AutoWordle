################################################################################
# WORDLE SOLVER ELIMINATION FUNCTIONS
# This program is to assist users when guessing the wordle of the day
# This has all of the functions for word elimination
# Created by Aiden Seay Spring'23
################################################################################
# IMPORTS
    # NONE

################################################################################
# CONSTANTS
    # NONE

################################################################################
# MAIN ELIMINATION FUNCTIONS
################################################################################

# eliminate words without letters in a specific place
def eliminateLettersInPlace( wordList, lettersInPlaceBank ):
    
    # check to see if the list is empty
    if lettersInPlaceBank != [""]:

        # iterate through each set
        for letterSet in lettersInPlaceBank:
            
            index = int(letterSet[2])
            char = letterSet[0]
            
            # iterate through each word to see if condition is met
            for word in wordList[:]:
                if word[index] != char:
                    wordList.remove(word)


# eliminate words without the letters
def eliminateLettersOutPlace( wordList, lettersOutPlaceBank ):
    
    # check to see if list is empty
    if lettersOutPlaceBank != [""]:

        # iterate through each letter in the bank
        for letter in lettersOutPlaceBank:

            # iterate through each word to see if the conditon is met
            for word in wordList[:]:

                if letter not in word:
                    
                    wordList.remove(word)


# eliminate words that has letters
def eliminateNoLetters( wordList, noLettersBank ):
    
    # check to see if list is empty
    if noLettersBank != [""]:

        # iterate through each letter in the bank
        for letter in noLettersBank:

            # iterate through each word to see if the conditon is met
            for word in wordList[:]:

                if letter in word:
                    
                    wordList.remove(word)

################################################################################
# SUPPORTING ELIMINATION FUNCTIONS
    # NONE

################################################################################