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
def rule1terminal(productions, vars, terminals):
    result = {}
    for production in productions:
        if production[0] in vars and production[1][0] in terminals and len(production[1]) == 1:
            result[production[0]] = production[1][0]
    return result


def deleteUnitProd(newP):
    for prod in newP:
        if (len(prod[1]) == 1):
            for var in newP:
                if (var[0] == prod[1][0]):
                    prod[1][0] = var[1][0]
                    n = len(var[1])
                    for i in range(1, n):
                        prod[1].append(var[1][i])

    return newP




terminal, var, newP = loadModel('grammar.txt')
print('Old prod: ')
print(newP)
print('New Prod: ')
print(deleteUnitProd(newP))
# print(len(newP[0][1]))
