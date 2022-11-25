import itertools


def loadModel(grammarCFG):
    file = open(grammarCFG).read()
    terminal = (file.split("Terminals:\n")[1].split("Variables:\n")[0].replace(
        "Terminals:\n", "").replace("\n", "")).split(' ')
    var = (file.split("Variables:\n")[1].split("Production:\n")[
        0].replace("Variables:\n", "").replace("\n", "")).split(' ')
    prod = (file.split("Production:\n")[1])
    newP = []
    rawRules = prod.split('\n')
    for rule in rawRules:
        left = rule.split(' -> ')[0]
        right = rule.split(' -> ')[1].split(' | ')
        for term in right:
            newP.append((left, term.split(' ')))
    return terminal, var, newP


# Menghasilkan rule dengan production 1 var -> 1 terminal (yang sudah ada di grammar CFG)
def isRule1TerminalOnly(productions, terminals, var):
    isRule1 = False
    for production in range(len(productions)):
        if ((productions[production][0] == var) and (productions[production][1][0] in terminals) and (len(productions[production][1]) == 1)):
            isRule1 = True
            tempKiri = productions[production][0]
            tempKanan = productions[production][1]
            for i in range(len(productions)):
                if (productions[i][0] == tempKiri and productions[i][1] != tempKanan):
                    isRule1 = False
                    break
            break

    return isRule1


def isThereUnitProd(terminals, productions):
    isUnit = False
    for prod in productions:
        if ((prod[1][0] not in terminals) and len(prod[1]) == 1):
            isUnit = True
            break
    return isUnit


def deleteUnitProd(newP, terminals):
    # while (isThereUnitProd(terminals, newP)):
    for prod in range(len(newP)):
        if (len(newP[prod][1]) == 1 and (newP[prod][1][0] not in terminals)):
            count = 0
            temp = newP[prod][1][0]
            for var in range(len(newP)):
                if (newP[var][0] == temp):
                    count += 1
                    # print(count)
                    if (count > 1):
                        newP.append((newP[prod][0], newP[var][1]))
                    else:
                        newP[prod] = (newP[prod][0], newP[var][1])
            # newP.pop(prod)
    return newP


def cekUnusedProd(productions, term, var, terminals):
    used = False
    for production in productions:
        if (production[0] != var and production[1][0] == term and len(production[1]) == 1 and isRule1TerminalOnly(productions, terminals, production[0])):
            used = True
            temp = production[0]
            break
    if (used):
        return True, temp
    else:
        return False, None


def cekUnsusedVarProd(productions, termVar, var):
    used = False
    for production in productions:
        if (production[0] != var and production[1] == termVar and len(production[1]) == 2):
            used = True
            temp = production[0]
            break
    if (used):
        return True, temp
    else:
        return False, None


def cekNumVar(productions):
    under2 = True
    for production in productions:
        if (len(production[1]) > 2):
            under2 = False
            break
    return under2


def CFG_to_CNF(productions, vars, terminals, newVars):
    # if start symbol occurs on RHS, create new start symbol SS0 & new prod SS0 -> S
    productions.append(('SS0', ['SS']))

    # remove unit prod
    productions = deleteUnitProd(productions, terminals)

    # if the right side of any prod is in the form A -> aB, prod is replaced by A -> XB & X -> a
    for production in productions:
        if production[0] in vars and len(production[1]) > 1:
            for rhsId in range(len(production[1])):
                if production[1][rhsId] in terminals:
                    used, prod = cekUnusedProd(
                        productions, production[1][rhsId], production[0], terminals)
                    if (used == False):
                        temp = production[1][rhsId]
                        production[1][rhsId] = newVars.pop(0)
                        productions.append((production[1][rhsId], temp))
                    else:
                        production[1][rhsId] = prod

    # # # replace each prod A -> B1..Bn where n > 2, with A -> B1C , C -> B2..Bn
    while (not cekNumVar(productions)):
        for i in range(len(productions)):
            if len(productions[i][1]) > 2:
                varPengganti = newVars.pop(0)
                first = productions[i][1][0]
                tempRHS = productions[i][1][1:]
                used, prod = cekUnsusedVarProd(
                    productions, tempRHS, productions[i][0])
                if (used == False):
                    productions[i] = (productions[i][0], [
                        first, varPengganti])
                    productions.append((varPengganti, tempRHS))
                else:
                    productions[i] = (
                        productions[i][0], [first, prod])
    return productions


newVars = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15',
           'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
           'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15',
           'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15',
           'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15',
           'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15',
           'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15',
           'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15',
           'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15',
           'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15',
           'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15',
           'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15',
           'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15',
           'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9', 'N10',
           'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10',
           'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10',
           'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10',
           'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10',
           'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
           'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10',
           'U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9', 'U10',
           'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
           'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10',
           'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10',
           'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10',
           'Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8', 'Z9', 'Z10']

# TEST CASE
# var1 = ['S', 'A', 'B']
# term1 = ['a', 'b', 'c']
# prod1 = [('S', ['A', 'S', 'B']), ('S', ['A', 'B']), ('A', ['a', 'A', 'S']), ('A', ['a', 'A']), ('A', ['a']),
#          ('B', ['S', 'b', 'S']), ('B', ['b', 'S']), ('B', ['S', 'b']), ('B', ['b']), ('B', ['A']), ('B', ['b', 'b'])]
# print(CFG_to_CNF(prod1, var1, term1, newVars))


terminal, var, newP = loadModel('grammar.txt')
# # print(terminal)
# print('new grammar: ')
hasil = CFG_to_CNF(newP, var, terminal, newVars)
print('HASIL')
print(hasil)


# print('ini: ')
# # rhs = newVars.pop()
# # print(rhs)
# # print(newVars)
# # CFG_to_CNF(newP, var, terminal, newVars)
