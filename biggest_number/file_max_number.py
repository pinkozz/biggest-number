#program that returns the biggest number from a text file
import regex

#open a text file
with open('test.txt') as pi:
    #read the file
    contents = pi.read()
    
    #make separate integers from one string that is given
    result = [e for e in regex.split("[^0-9]", contents) if e != '']
    
    # list 'result' elements are strings, so we use map(int, list) to get integers
    print (max(map(int, result)))