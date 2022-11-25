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

def isOperator(variabel):
    valid = False
    operator = ["+", "-", "/", "%", "*", "==", "++", "--", "**", "+=", "-=", "/=", "*=", "%=", ">", "<", "<=", ">=", "!=", "**="]
    for i in range(len(operator)):
        if (variabel == operator[i]):
           valid = True 
    return valid  
   
def isString(variabel):
    if variabel.Contains("\""):
        return True
    else:
        return False
#Final state var -> state2
#Final state num -> state8
#Final state operator -> state 9
#dead state = 100
def opState0(variabel):
    
    if (isVariable(variabel) or isNumber(variabel)):
        state = 1
    elif(variabel == "++" or variabel =="--"):
        state = 9
    else:
        state = 100
    
    return state

def opState1(variabel):
    if (variabel == "=" or variabel == ">" or variabel == "<" or variabel == "==" or variabel == ">=" or variabel == "<=" or variabel == "!="):
        state = 2
    elif (variabel == "+" or variabel == "-" or variabel == "*" or variabel == "/" or variabel == "%"):
        state = 4
    elif (variabel == "++" or variabel == "--"):
        state = 7
    elif (variabel == "+=" or variabel == "-=" or variabel == "*=" or variabel == "%=" or variabel == "/=" or variabel == "**=" or variabel == "**"):
        state = 8
    else:
        state = 100
    return state

def opState2(variabel):
    if (isVariable(variabel)):
        state = 3
    elif (isNumber(variabel)):
        state = 6
    else:
        state = 100
    return state

def opState3(variabel):
    if(isVariable(variabel)):
        state = 3
    elif(variabel == "=" ):
        state = 100
    elif((variabel == ">" or variabel == "<" or variabel == "==" or variabel == ">=" or variabel == "<=" or variabel == "!=")):
        state = 2
    elif((variabel == "+" or variabel == "-" or variabel == "*" or variabel == "/" or variabel == "%" or variabel == "**")):
        state = 4
    elif((variabel == "+=" or variabel == "-=" or variabel == "*=" or variabel == "%=" or variabel == "/=" or variabel == "**=")):
        state = 8
    else:
        state = 100
    return state
    
def opState4(variabel):
    if(isVariable(variabel)):
        state = 3
    elif (isNumber(variabel)):
        state = 5
    else:
        state = 100
    return state

def opState5(variabel):
    if (variabel == "=" or variabel == ">" or variabel == "<" or variabel == "==" or variabel == ">=" or variabel == "<=" or variabel == "!="):
        state = 2
    else:
        state = 100
    return state

def opState6(variabel):
    if(isNumber(variabel)):
        state = 6
    else:
        state = 100
    return state

def opState7(variabel):
    if(not isVariable(variabel)) or (not isNumber(variabel)):
        state = 7
    else:
        state = 100
    return state

def opState8(variabel):
    if isVariable(variabel):
        state = 3
    elif isNumber(variabel):
        state = 6
    else:
        state = 100
    return state

def openState9(variabel):
    if isVariable(variabel):
        state = 3
    else:
        state = 100
    return state

def checkOperator(operator):
    operatorlist = operator.split()
    state = 0
    listState = []
    for i in range(len(operatorlist)):
        if (state == 0):
            state = opState0(operatorlist[i])
            print(state)
            listState.append(state)
        elif (state == 1):
            state = opState1(operatorlist[i])
            print(state)
            listState.append(state)
        elif (state == 2):
            state = opState2(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 3):
            state = opState3(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 4):
            state = opState4(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 5):
            state = opState5(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 6):
            state = opState6(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 7):
            state = opState7(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 8):
            state = opState8(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 9):
            state = openState9(operatorlist[i])
            print(state)
            listState.append(state)
        elif(state == 100):
            listState.append(state)
            return False
        
    print(listState)
    
    if (state == 3 or state == 6 or state == 7):
        return True
    else :
        return False

      

#tes = ' aa = "test" '
#valid = isOperator(tes)

#tes4 = opState3(" ")
#tes = isOperator("))")
#print(valid)
#print(valid)
#print(tes4)

#yang boleh
# a = 0 -- var = num
# a == b+c
# a = a + b
# a + b == c
# a== 0 -- var == num
# 9 + 4 == 13
# i++
# i--
#  a = b = c += d = 3 
# 1 + 2 == 3
# 1 == 3
# 1 <= 3
# a + b = c

#belom ke handle
# func1 = function()
# object



#gaboleh
# a + b = c (a+b) bakal dianngep variabel
# 1++
# += 1