'''
Demonstrates:  
1. reading an entire file into a string 
2. use of a constant for a path
'''
import sys 

#The following statement must be adjusted to reflect where the data is 
#stored on your computers
PATH_IN = "/Users/depalma/Desktop/CPSC222/A-Data/"

#Current directory
PATH_OUT = "." + "/"  

def file_read(fileName):
   fin = PATH_IN + fileName
   with open(fin, 'r', encoding='utf-8') as f:
      text = f.read()
   return text 

def file_write(fileName,text_in):
   fout = PATH_OUT + fileName
   lst = [ch.upper() if ch.islower() else ch for ch in text_in] 

   #transform a list to a string for writing
   text_out = "".join(lst)

   with open(fout,'w', encoding='utf-8') as f:
     f.write(text_out)

def main():
    fin = sys.argv[1]
    fout = sys.argv[2] 
    text = file_read(fin) 
    file_write(fout,text)


if __name__ == "__main__":
  main()     
