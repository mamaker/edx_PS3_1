#! python2.7

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = string.ascii_lowercase
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, '')

    return availableLetters


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#getAvailableLetters(lettersGuessed)
print getAvailableLetters(lettersGuessed)
#abcdfghjlmnoqtuvwxyz