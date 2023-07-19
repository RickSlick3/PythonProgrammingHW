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
    anagrams = words
    
    # eliminates all words that arent the length of word+1
    # this shortens the time of each traversal afterwards by shortening the list
    anagrams = [w for w in anagrams if len(w) == len(word)+1]
    
    # uses each letter in the input word to travese and compare to the list of words
    all_letters = []
    for letter in word:
        # if this letter has not been used to search through the list, add it to the list
        # if the letter has already been searched with, dont need to traverse the list again (saves time)
        if letter not in all_letters:
            all_letters.append(letter)
            # makes sure duplicate letters are recognized by counting how many times they appear
            freq = word.count(letter)
            # takes each letter in the argument word and only keeps words that contain that letter
            # the same amount of times or more that it occurs in the argument word
            anagrams = [w for w in anagrams if (letter in w) and (w.count(letter) >= freq)]
            
    
    return anagrams

# runs step(word) until user quits
import time # used to time the execution of each call to step(word)
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