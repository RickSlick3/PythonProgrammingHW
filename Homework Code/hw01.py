_author_ = "Richard Roberts"
_credits_ = ["Module 3 Lab Sheet, greedy algorithm"]
_email_ = "Roberrf@mail.uc.edu" # Your email address
   
import math 

denominators = []
i = 0;

def gcd(a, b):    
  """
  >>> gcd(15, 12)
  3
  >>> gcd(24, 60)
  12
  >>> gcd(33, 99)
  33
  """ 
  a, b = max(a, b), min(a, b)
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

def egypt(n, d):   
  """
  >>> egypt(3,4)
  '1/2 + 1/4 = 3/4'
  >>> egypt(11,12)
  '1/2 + 1/3 + 1/12 = 11/12'
  >>> egypt(123,124)
  '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124'
  >>> egypt(103,104)
  '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424 = 103/104'
  """
  global i #i wont reset after every recursive call, can only run once per outside function after i is reset to 0
  if(i < 1):
      denominators.append(n) #saves the original numerator in the list for printing purposes
      denominators.append(d) #saves the original denominator in the list for printing purposes
      i += 1
      
  if(n == 1):
    denominators.append(d) #add new denominator to list
    #styles and prints all denominators and original fraction from the denominators list
    print('\'', end = '')
    for x in range(len(denominators)):
      if x > 1:    
        print('1/{0}'.format(denominators[x]), end = '')
        if(x != len(denominators)-1):
          print(' + ', end = '')
        else:
          print(' = {0}/{1}\''.format(denominators[0], denominators[1]))
    #clears denominators list and resets value of i before next function call
    denominators.clear() 
    i = 0 
      
  else:
    ceilDen = math.ceil(d/n) #finds the new largest denominator
    denominators.append(ceilDen) #add new denominator to list
    #the calculated arguments pass the most recent fraction - (1/the new denominator) to gcd in the form (numerator, denominator)
    gcdOutput = gcd((n * ceilDen) - d, d * ceilDen) 
    #egypt is called recursively with whole number values because of the // operator
    egypt((((n * ceilDen) - d)) // gcdOutput, ((d * ceilDen) // gcdOutput))


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)