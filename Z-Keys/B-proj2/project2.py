'''
Paul De Palma
CPSC 222
9/21/2025
Project 2
Data Science 1: Do shorter texts appear to follow a power law distribution more closely
than longer texts
'''
import re
import sys
from operator import itemgetter
import matplotlib.pyplot as plt
import math

PATH = "/Users/depalma/Desktop/CPSC222/A-Data/"
MM = "middlemarch.txt"
MR = "the_masque_of_the_red_death.txt"
UL = "ulysses.txt"

'''
 Opens a file
 Parameter: name of input file
 Returns: opened file object or prints error if input file does not exist.
'''
def my_open(text):
   try:
      fin = open(text, 'r')
   except:
      print("Invalid file name")
      quit()
   return fin

'''
 Tokenizes an input string
 Parameter: input string
 Returns: list of tokenized words from the input string
'''
def tokenize(string_in):
   #substitute space for eol character
   string = re.sub('\n',' ', string_in)

   #create a list containing all lower case characters
   good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
   good_chars.append(' ') #spaces are good characters
   string = string.lower()

   new_str = ''
   for ch in string:
      if ch in good_chars:
         new_str = new_str + ch
	 #remove spaces, create a list of words
   wordLst= new_str.split()
   return wordLst

'''
 Counts words in a list of words
 Parameter: list of words
 Returns: list of frequencies of each word from most frequent to least frequent
'''
def count(wordLst):
   count_dict = {}
   for word in wordLst:
      if word in count_dict:
         count_dict[word] = count_dict[word] + 1
      else:
         count_dict[word] = 1
  
   #sort the items by the number of times they occur, with highest occurence on top
   sorted_lst = sorted(count_dict.items(), key = itemgetter(1), reverse = True)
   freqLst = [item[1] for item in sorted_lst]
   return freqLst
	
'''
 Constructs x and y axes for plotting
 Parameter: frequency list gotten from count and plot type (conventional or log-log)
 Returns: lists comprising x and y axes
'''
def construct_axes(freqLst,plotType):
  if plotType == 'C':
     x = [i+1 for i in range(len(freqLst))]
     y = [num for num in freqLst]
  if plotType == "LL":
     x = [math.log(i+1) for i in range(len(freqLst))]
     y = [math.log(num) for num in freqLst]		
  return x,y

'''
 Plots frequency of words against rank
 Parameters: lists comprising x and y axes
 Returns: nothing
'''	 
def plot(x,y):
    pl = plt.gca()
    pl.plot(x,y)
    pl.set_xlabel("Rank")
    pl.set_ylabel("Probability")
    plt.show()


def main():
   textIn = sys.argv[1]
   if textIn == "MM":
      text = MM
   if textIn == "MR":
      text = MR
   if textIn == "UL":
      text = UL
   plotType = sys.argv[2]
	
   complete = PATH + text
   fin = my_open(complete)

   inpString = fin.read()
   fin.close()
  
   wordLst= tokenize(inpString)
   freqLst = count(wordLst)
	
   x,y = construct_axes(freqLst,plotType)
   plot(x,y)
 
   
if __name__ == "__main__":
  main()     
