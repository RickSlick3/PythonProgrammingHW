# hw 3 

# a 235886 item list is very time consuming to traverse multiple times while preforming operations.

# So the first thing I did to make my solution faster is cutting the size of the list I will be 
# traversing over and over again down tremendously by using list comprehension on a copy of words
# to only keep the words of the exact length we expect to get in the output (length of word + 1)
# (line 40). 

# Then I made a singular loop that contains nearly all the necessary operations in order to avoid
# redundant loops (line 44).
 
# I made the loop check if you have already traversed with a certain letter from word in order to 
# reduce the amount of times the list needs to be traversed overall for each step call (line __).

# the previous explaination is made possible by using the .count() method to count the amount of 
# times a letter shows up in the input word (line 51). Then the list comprehension contains a 
# condition to make sure the word in the list also contains that letter a minimum amount of times
# that it shows up in the input word (line 54). This makes it possible to not need other conditions
# or a seperate version of the list comprehension for words with duplicate letters, no matter how
# many times they appear.

# starter code top get the list of words
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

# takes a single word as an input and returns a list of words 
# containing all of its letters PLUS one additional letter
def step(word):
    
    # copys words so we can modify and return without affecting the original list
    # AND so we can use list comprehension
    step_words = words
    
    # eliminates all words that arent the length of word+1
    # this shortens the time of each traversal afterwards by shortening the list
    step_words = [w for w in step_words if len(w) == len(word)+1]
    
    # uses each letter in the input word to travese and compare to the list of words
    all_letters = []
    for letter in word:
        # if this letter has not been used to search through the list, add it to the list
        # if letter has already been searched with, dont traverse the list again to save time
        # because it would yeild the same result as before
        if letter not in all_letters:
            all_letters.append(letter)
            # makes sure duplicate letters are recognized by counting how many times they appear
            freq = word.count(letter)
            # takes each letter in the argument word and only keeps words that contain that letter
            # the same amount of times or more that it occurs in the argument word
            step_words = [w for w in step_words if (w.count(letter) >= freq)]
    
    # removes duplicates from final list using list comprehension
    retVal = []
    [retVal.append(w) for w in step_words if w not in retVal]
    
    return retVal

# runs step(word) until user quits, outputting the resulting list, how many words it contains,
# and the time it took to run the step function.
import time # used to time the execution of each call to step(word) for testing purposes. 
if __name__ == "__main__":
     
    cont = True
    while cont:
        user_word = input("\nChoose a base word to find step words from, or include \"!\" to exit: ")
        if "!" in user_word:
            cont = False
            print("Thank you, bye!")
        else:
            start_time = time.time()
            result = step(user_word.upper())
            print("\nYour search had ", len(result), " results:")
            print(result)
            print("This search took: %s seconds." % round(time.time() - start_time, 5))