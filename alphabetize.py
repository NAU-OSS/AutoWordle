def main():

    # import the text file into a list
    wordList = accessDictionary()

    # alphabetize the list
    sortedWordList = sort( wordList )

    # export the txt file
    export( sortedWordList )



def accessDictionary():

    # read the txt file
    with open("fiveLetterWords.txt", 'r') as words:
        wordList = []

        # iterate through each word and put it in the list
        for word in words:
            wordList.append(word.strip("\n"))
    
    # return the word list
    return wordList



def sort( wordList ):
    return sorted( wordList )


def export( wordList ):

    with open("sortedFiveLetterWords.txt", 'w') as file:
        
        for word in wordList:
            file.write(word)
            file.write('\n')

main()