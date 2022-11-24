############### NOTES #####################

'''
Variables in javascript
var, let, const
1. Depan harus huruf atau underscore, gaboleh angka
2. Spasi, simbol, punctuation ga boleh
'''

'''
Operators in javascript

'''

############### CODE #####################


def checkFirstElementVariables(variable):
    
    if((ord(variable[0]) >= 65 and ord(variable[0]) <= 90) or (ord(variable[0]) >= 97 and ord(variable[0]) <= 122) or (variable[0] == "$") or (variable[0] == "_")) :
        valid = True
    else :
        valid = False   
    return valid

def checkVariables(variable):
    
    validFirst = checkFirstElementVariables(variable)
    
    if(validFirst):
        for i in variable:
            if((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57) or (i == "$") or (i == "_")):
                valid = True
            else:
                valid = False
                break
    else:
        valid = False
    return valid


#Start state kalo nerima angka atau tanda selain $ / _ ke dead state(2)
def q0(char):
    if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or (char == "$") or (char == "_")):
        state = 1
    else:
        state = 2
    return state

def q1(char):
    if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or (char == "$") or (char == "_")):
        state = 1
    elif ((ord(char) >= 48 and ord(char) <= 57)):
        state = 3
    else:
        state = 2
    return state

def q2(char):
    state = 2
    return state

def q3(char):
    if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or (char == "$") or (char == "_")):
        state = 1
    elif ((ord(char) >= 48 and ord(char) <= 57)):
        state = 3
    else:
        state = 2
        
    return state


def isVariable(variable):
    state = 0
    for i in range(len(variable)):
        if(state == 0):
            state = q0(variable[i])
        if(state == 1):
            state = q1(variable[i])
        if(state == 2):
            state = q2(variable[i])
        if(state == 3):
            state = q3(variable[i])
    
    if(state==1):
        return True
    
    else:
        return False

def isNumber(number):
    state = 3
    for i in range(len(number)):
        if(state == 3):
            state = q3(number[i])
        else:
            state = q2(number[i])
    
    if(state == 3):
        return True
    else:
        return False
    