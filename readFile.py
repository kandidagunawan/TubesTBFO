import re
import fa as fa

def splitOperator(filename):
    f = open(filename, "r")
    inputfile = f.read()
    f.close()

    output = []
    # split the target string on the occurance of one or more whitespace characters
    inputfile = inputfile.split(" ")
    for statement in inputfile:
        if statement != '':
            output.append(statement)
            


    ##operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'none', 'not', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%', '\n']
    #operator2 = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', '+', '*', '**', "'", '"', '(', ')', 'none', 'not', 'true', 'false', '{', '}', '[', ']', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', '%', '\n']
    
    # split the target string with the following pattern
    #for oper in operator:
        #temp = []    
        #for statement in output:
            #elmt = re.split(r'[A..z]*(' + oper + r')[A..z]*', statement)
            
            #for splitted in elmt:
                #temp.append(splitted) 
        #output = temp

    # checking list
    temp = []
    valid = True
    for statement in output:
        if statement == 'as' or statement == 'is' or statement == 'or' or statement == 'in' or statement == 'if' or statement == 'and':
            temp.append(statement)
        elif(fa.isVariable(statement)):
            temp.append(statement)
        elif(fa.isNumber(statement)):
            temp.append(statement)
        elif(fa.isOperator(statement)):
            temp.append(statement)
        elif statement == '':
            continue
        
    for i in range(len(temp)):
        if temp[i] == '\n':
            temp[i] = 'nl'
    return temp,valid

tes = splitOperator("test.txt")
print(tes)