import re
import sys


token = [
    (r'[ \t]+', None),
    (r'//[^\n]*', None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),


    # Integer and String
    (r'\"[^\"\n]*\"',           "STRING"),
    (r'\'[^\'\n]*\'',           "STRING"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
    (r'[\+\-]?[1-9][0-9]+',     "INT"),
    (r'[\+\-]?[0-9]',           "INT"),

    # Delimiter
    (r'\n',                     "NL"),
    (r'\(',                     "RP"),  # Kurung Biasa KIri
    (r'\)',                     "LP"),
    (r'\[',                     "SBR"),  # Kurung Siku KIri
    (r'\]',                     "SBL"),
    (r'\{',                     "CBR"),  # Kurung Kurawal Kiri
    (r'\}',                     "CBL"),
    (r'\;',                     "SEMICOLON"),
    (r'\:',                     "COLON"),

    # Operator
    (r'\*\*=',                   "POWEQ"),
    (r'\*\*',                    "POW"),
    (r'\*',                     "MUL"),
    (r'\*=',                    "MULEQ"),
    (r'/',                      "DIVIDE"),
    (r'/=',                     "DIVIDEQ"),
    (r'\+',                     "PLUS"),
    (r'\+=',                    "PLUSEQ"),
    (r'\-',                     "MIN"),
    (r'-=',                     "MINEQ"),
    (r'%',                      "MOD"),
    (r'%=',                     "MODEQ"),
    (r'<=',                     "LESSEQ"),
    (r'<',                      "LESS"),
    (r'>=',                     "GREATEQ"),
    (r'>',                      "GREAT"),
    (r'!=',                     "NEQ"),
    (r'\==',                    "ISEQ"),
    (r'\=(?!\=)',               "EQUAL"),


    # keyword
    (r'\blet\b', "LETS"),
    (r'\bvar\b', "VARIABLES"),
    (r'\bconst\b', "CONSTANTS"),
    (r'\bnone\b', "NONES"),
    (r'\band\b', "ANDS"),
    (r'\bor\b', "ORS"),
    (r'\bis\b', "ISS"),
    (r'\bin\b', "INS"),
    (r'\bnot\b', "NOTS"),
    (r'\btrue\b', "TRUES"),
    (r'\bfalse\b', "FALSES"),
    (r'\bfor\b', "FORS"),
    (r'\bif\b', "IFS"),
    (r'\belse\b', "ELSES"),
    (r'\bswitch\b', "SWITCHS"),
    (r'\bbreak\b', "BREAKS"),
    (r'\bcontinue\b', "CONTINUES"),
    (r'\bdo\b', "DOS"),
    (r'\bwhile\b', "WHILES"),
    (r'\breturn\b', "RETURNS"),
    (r'\bfunction\b', "FUNCTIONS"),
    (r'\bclass\b', "CLASS"),
    (r'\bfrom\b', "FROMS"),
    (r'\bimport\b', "IMPORTS"),
    (r'\bas\b', "ASS"),
    (r'\bwith\b', "WITHS"),
    (r'\bcase\b', "CASES"),
    (r'\bdefault\b', "DEFAULT"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'[A-Za-z_][A-Za-z0-9_]*', "ID"),
]

# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'


def lexer(teks, token_exp):
    pos = 0  # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1  # posisi karakter relatif terhadap baris tempat dia berada
    line = 1  # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in token_exp:
            pattern, tag = t
            if line == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            print("ILLEGAL CHARACTER")
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens



def create_token(sentence, token):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char, token)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)

    return " ".join(tokenArray)


print(create_token('test.txt', token))
