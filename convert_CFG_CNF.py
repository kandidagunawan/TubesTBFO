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
