# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
#from curses.ascii import isalpha
import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    con = True
    for i in secret_word:
        if i in letters_guessed:
            continue
        else:
            con=False
    return con        

#l=['e', 'i', 'k', 'p', 'r', 's']
#word='apple'
#print(is_word_guessed(word,l))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    res=''
    for i in secret_word:
        if i in letters_guessed:
            res+=i
        else:
            res+='_ '
    return res  

#print(get_guessed_word(word,l))
#print(len(get_guessed_word(word,l)))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    res=string.ascii_lowercase
    for i in letters_guessed:
        if i in res:
            res=res.replace(i,'')
        else:
            continue
    return res
    
#print(get_available_letters(l))
    

"""def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    i=6
    warning=3
    myStr=[]
    while i>0:
        problem=False
        print(f'You have {i} guesses left.')
        print('Available letters: ',get_available_letters(myStr))
        myinput=input('Please guess a letter: ')
        myinput=myinput.lower()
        
        if len(myinput)>1 or not str.isalpha(myinput):
            print('In input must be only one latine symbol')
            warning-=1
            problem=True
        if myinput in myStr:
            print(f"Oops! You've already guessed that letter. You now have 2 warnings: {get_guessed_word(secret_word,myStr)}")
            warning-=1
            problem=True
        if warning==0:
            print('You have entered too many wrong inputs, the quantity of quesses have decreased :(')
            warning=3
            i-=1
        if problem:    
            print(f'You have only {warning} warnings. If you lose them, the number of guesses will decrease')
        else:
            myStr.append(myinput)
            if is_word_guessed(secret_word,myStr):
                print('Congratulations, you won!')
                break
            elif myinput in secret_word:
                   print(f'Good guess: {get_guessed_word(secret_word,myStr)}')
            else :
               print(f'Oops! That letter is not in my word:  {get_guessed_word(secret_word,myStr)}')
               i-=1
        print('-------------')
    if i==0:
        print(f"You lost. The word was: \'{secret_word}\'.")
    print(f"Your total score for this game is: {i*len(secret_word)}")
    return 0
               
hangman(word)"""
        
        




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    for i in my_word:
        if i==' ':
            my_word=my_word.replace(i,'')
    j=0
    con=False
    if len(my_word)==len(other_word):
        for i in my_word:
            if my_word[j]=='_' or my_word[j]==other_word[j]:
                con=True
            else:
                con=False
                break
            j+=1
    return con

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    res=''
    for i in wordlist:
        if match_with_gaps(my_word,i):
            res+=i
            res+='  '
    if res=='':
        res="No matches found"
    return res


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    i=6
    warning=3
    myStr=[]
    no_asterrics=True
    while i>0:
        problem=False
        if no_asterrics:
            print(f'You have {i} guesses left.')
        print('Available letters: ',get_available_letters(myStr))
        myinput=input('Please guess a letter: ')
        myinput=myinput.lower()
        if myinput=='*':
            print(f'Possible matches are: {show_possible_matches(get_guessed_word(secret_word,myStr))}')
            print('Guess the word: ', get_guessed_word(secret_word,myStr))
            no_asterrics=False
        
        if len(myinput)>1 or not str.isalpha(myinput) and not myinput== '*':
            print('In input must be only one latine symbol')
            if no_asterrics:
                warning-=1
                problem=True
        if myinput in myStr and not myinput=='*':
            print(f"Oops! You've already guessed that letter. You now have {warning} warnings: {get_guessed_word(secret_word,myStr)}")
            if no_asterrics:
                warning-=1
                problem=True
        if warning==0:
            print('You have entered too many wrong inputs, the quantity of quesses have decreased :(')
            warning=3
            i-=1
        if problem:    
            print(f'You have only {warning} warnings. If you lose them, the number of guesses will decrease')
        else:
            myStr.append(myinput)
            if is_word_guessed(secret_word,myStr):
                print('Congratulations, you won!')
                print('You guessed the word: ',secret_word)
                break
            elif myinput in secret_word:
               print(f'Good guess: {get_guessed_word(secret_word,myStr)}')
            elif myinput not in secret_word and not myinput=='*':
                print(f'Oops! That letter is not in my word:  {get_guessed_word(secret_word,myStr)}')
                if no_asterrics:
                    i-=1
        print('-------------')
        
    if i==0:
        print(f"You lost. The word was: \'{secret_word}\'.")
    if no_asterrics:
        print(f"Your total score for this game is: {i*len(secret_word)}")
    else:
        print('You have used help. Play without hints to get a score')
    return 0



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    