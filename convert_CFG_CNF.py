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


def isUnitProd(terminals, prod):
    isUnit = False
    if (prod[1] in terminals and len(prod[1]) == 1):
        isUnit = True
    return isUnit


def deleteUnitProd(newP, terminals):
    for prod in range(len(newP)):
        if (len(newP[prod][1]) == 1 and newP[prod][1][0] not in terminals):
            for var in range(len(newP)):
                if (newP[var][0] == newP[prod][1][0]):
                    newP.append((newP[prod][0], newP[var][1]))
            newP.pop(prod)

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
    # for production in range(len(productions)):
    #     if len(productions[production][1]) > 2:
    #         # used, prod = cekUnusedProd(productions, productions[production[1]])
    #         varPengganti = newVars.pop(0)
    #         first = productions[production][1].pop(0)
    #         tempRHS = productions[production][1]
    #         used, prod = cekUnsusedVarProd(
    #             productions, tempRHS, productions[production][0])
    #         print(prod)
    #         if (used == False):
    #             productions[production] = (productions[production][0], [
    #                 first, varPengganti])
    #             productions.append((varPengganti, tempRHS))
    #         else:
    #             productions[production] = (
    #                 productions[production][0], [first, prod])
    return productions


newVars = ['A1', 'A2', 'A3', 'A4', 'A5',
           'B1', 'B2', 'B3', 'B4', 'B5',
           'C1', 'C2', 'C3', 'C4', 'C5',
           'D1', 'D2', 'D3', 'D4', 'D5',
           'E1', 'E2', 'E3', 'E4', 'E5',
           'F1', 'F2', 'F3', 'F4', 'F5',
           'G1', 'G2', 'G3', 'G4', 'G5',
           'H1', 'H2', 'H3', 'H4', 'H5',
           'I1', 'I2', 'I3', 'I4', 'I5',
           'J1', 'J2', 'J3', 'J4', 'J5']
# # print('prod: ')
# # print(newP)
var1 = ['S', 'A', 'B']
term1 = ['a', 'b', 'c']
prod1 = [('S', ['A', 'S', 'B']), ('S', ['A', 'B']), ('A', ['a', 'A', 'S']), ('A', ['a', 'A']), ('A', ['a']),
         ('B', ['S', 'b', 'S']), ('B', ['b', 'S']), ('B', ['S', 'b']), ('B', ['b']), ('B', ['A']), ('B', ['b', 'b'])]

# print(cekUnusedProd(prod1, 'a', 'A5'))


terminal, var, newP = loadModel('grammar.txt')
print('ini: ')
print(CFG_to_CNF(prod1, var1, term1, newVars))


# # rhs = newVars.pop()
# # print(rhs)
# # print(newVars)
# # CFG_to_CNF(newP, var, terminal, newVars)
