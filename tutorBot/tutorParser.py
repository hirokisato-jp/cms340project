#!/usr/bin/python3

################################################################################################################################
#  NAME:  Jenny Goldsher, Noah Harvey, Deandra Martin, Hiroki Sato
#  DATE:  09112020
#  IDEA:  holds parsing funcion
################################################################################################################################

####  IMPORTS  #################################################################################################################

####  GLOBALS  #################################################################################################################

####  FUNCTIONS  ###############################################################################################################

# this function takes in an input which is the string that bot receives from user and validates if they used a code block or not
# Output: Boolean value, True if they used the codeblock which is the correct format. False if they did not use the correct Format. 
# By the string slicing and checking the first three character being the triple backquote or not will determine the format which the user used. 

def is_valid(inp):

    valid = True
    
    if len(inp) == 0:
        return False
    
    elif inp[0:3] != "```":
        return False
        
    return valid



def par(inp):                                               # Function takes a line to parse and return as an array
    str1 = inp.split()                                      # Split the line by spaces
    length = len(str1)

   
    arr2 = []
    count1 = 0
    for element in str1:
        if element.isalpha() or len(element) == 1:
            arr2.append(element)
        elif len(element) > 1:
            count1 = 0
            for x in range(len(element)):
                has_underscore = 0
                has_number = 0
                if element[x] == '_':
                    has_underscore +=1
                elif element[x].isdigit():
                    has_number += 1
                elif element[x].isalpha():
                    count1 +=1
            if has_number + has_underscore + count1== len(element):
                arr2.append(element)
            else:
                store = 0
                for f in range(len(element)):
                    store+=1
                    if element[f].isalpha() == False and element[f].isdigit() == False and element[f] != '_':
                        store = f
                        break
                if store != 0:
                    word = ""
                    for v in range(0,store):
                        word = word + element[v]
                    arr2.append(word)
                    for a in range(store,len(element)):
                        arr2.append(element[a])
                       
   
   
    if str1[0] == "#" or str1[0] == "```":                  # Disallow comments being parsed by
        return                                              # returning a 'None' value
   
    count = 0                                               # Count all of the spaces and then subtract non starter
    for i in range(len(inp)):                               # spaces to look at line indentation
        if inp[i] == " ":
            count+=1
    count = count - len(str1)+ 1
   
    li = [count]                                            # Make another array that has the count of spaces
    for j in arr2:                                          # then add the parsed line    
        li.append(j)
    return li
   

def callSplit():
    arr = []                                                # Array to store each line array
    #inputtxt = "def function():\n     x = 15"               # TEST
    #inputtxt = "''' testing comments\nx = 15"               # TEST
    inputtxt = 'def func_one():\n    x = "hello"\n     y = 12 + x\n  for i in range(10):'                                       # TEST
    #inputtxt = (input())
    lines = inputtxt.split("\n")                            # Make an array where each value is one line
   
    for i in lines:                                         # Pass each line to the parser, which will return its value
        if par(i) != None:                                  # Populate 2D array with lines without including 'None' values
            arr.append(par(i))
   
    print(arr)
    return arr

####  MAIN  ####################################################################################################################

def main():
    callSplit()

if(__name__=="__main__"): main()
