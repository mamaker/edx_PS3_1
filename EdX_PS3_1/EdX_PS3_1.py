#! python2.7
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
                      False otherwise
    '''
    guess = True
    for c in secretWord:
        if c not in lettersGuessed:
            guess = False
            break
    return guess

secretWord = 'kipps' #'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)
#False
