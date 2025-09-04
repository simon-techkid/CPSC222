'''
Demonstrates: 
1. a simple tokenizer
2. split
'''
import re

def tokenize(string_in):
    #substitute space for eol charactger
    string = re.sub('\n',' ', string_in)

    #create a list containing all lower case characters
    good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
    good_chars.append(' ')
    string = string.lower()
    new_str = ''
    for ch in string:
        if ch in good_chars:
            new_str = new_str + ch

    lst = new_str.split()
    return lst 

def my_open():
    while(True):
        file_in = input('Enter an input file name\n')
        try:
            fin = open(file_in, 'r')
            break
        except:
            print("Invalid file name, Try again")
    return fin

def main():
    fin = my_open()
    contents_raw = fin.read()
    contents_cooked = tokenize(contents_raw)
    print(contents_cooked)
    
    fin.close()
   
if __name__ == "__main__":
  main()     
