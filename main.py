from convert_CFG_CNF import *
from lexer import *
from argparse import ArgumentParser

if __name__ == "__main__":
    argParser = ArgumentParser()
    argParser.add_argument("filename", type=str,
                           help="Nama file yang ingin dicek")
    arg = argParser.parse_args()

if (True):
    print("Accepted!")
else:
    print("Syntax Error!")
