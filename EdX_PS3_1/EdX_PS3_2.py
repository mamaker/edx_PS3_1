#! python2.7
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    BLANK = '_ '
    for c in secretWord:
        if c in lettersGuessed:
            guessedWord += c
        else:
            guessedWord += BLANK
    return guessedWord

secretWord = 'apple' 
lettersGuessed = ['p', 'l', 'a', 'e'] #['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)
#'_ pp_ e'