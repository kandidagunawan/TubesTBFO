from convert_CFG_CNF import *
from CYK import *
from lexer import *
from argparse import ArgumentParser

if __name__ == "__main__":
    argParser = ArgumentParser()
    argParser.add_argument("filename", type=str,
                           help="Nama file yang ingin dicek")
    args = argParser.parse_args()

terminal, var, newP = loadModel('grammar.txt')
hasil = CFG_to_CNF(newP, var, terminal, newVars)
# print(hasil)
print('ini token:')
print(create_token(args.filename, token))
if (CYK(create_token(args.filename, token), hasil)):
    print("Accepted!")
else:
    print("Syntax Error!")
