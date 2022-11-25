import re
import sys


token = [
    (r'[ \t]+', None),
    (r'//[^\n]*', None),
    (r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
    (r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None),


    # Integer and String
    (r'\"[^\"\n]*\"',           "alphabet"),
    (r'\'[^\'\n]*\'',           "alphabet"),
    (r'[\+\-]?[0-9]*\.[0-9]',  "int"),
    (r'[\+\-]?[1-9][0-9]',     "int"),
    (r'[\+\-]?[0-9]',           "int"),

    # Delimiter
    (r'\n',                     "nl"),
    (r'\(',                     "("),  # Kurung Biasa KIri
    (r'\)',                     ")"),
    (r'\[',                     "["),  # Kurung Siku KIri
    (r'\]',                     "]"),
    (r'\{',                     "{"),  # Kurung Kurawal Kiri
    (r'\}',                     "}"),
    (r'\;',                     ";"),
    (r'\:',                     ":"),

    # Operator
    (r'\*\*=',                   "**="),
    (r'\*\*',                    "**"),
    (r'\*',                     "*"),
    (r'\*=',                    "*="),
    (r'/',                      "/"),
    (r'/=',                     "/="),
    (r'\+',                     "+"),
    (r'\+=',                    "+="),
    (r'\-',                     "-"),
    (r'-=',                     "-="),
    (r'%',                      "%"),
    (r'%=',                     "%="),
    (r'<=',                     "<="),
    (r'<',                      "<"),
    (r'>=',                     ">="),
    (r'>',                      ">"),
    (r'!=',                     "!="),
    (r'\==',                    "=="),
    (r'\=(?!\=)',               "="),

    # keyword
    (r'\blet\b', "let"),
    (r'\bvar\b', "var"),
    (r'\bconst\b', "const"),
    (r'\bnone\b', "none"),
    (r'\band\b', "and"),
    (r'\bor\b', "or"),
    (r'\bis\b', "is"),
    (r'\bin\b', "in"),
    (r'\bnot\b', "not"),
    (r'\btrue\b', "true"),
    (r'\bfalse\b', "false"),
    (r'\bfor\b', "for"),
    (r'\bif\b', "if"),
    (r'\belse\b', "else"),
    (r'\bswitch\b', "switch"),
    (r'\bbreak\b', "break"),
    (r'\bcontinue\b', "continue"),
    (r'\bdo\b', "do"),
    (r'\bwhile\b', "while"),
    (r'\breturn\b', "return"),
    (r'\bfunction\b', "function"),
    (r'\bclass\b', "class"),
    (r'\bfrom\b', "from"),
    (r'\bimport\b', "import"),
    (r'\bas\b', "as"),
    (r'\bwith\b', "with"),
    (r'\bcase\b', "case"),
    (r'\bdefault\b', "default"),
    (r'\btry\b', "try"),
    (r'\bcatch\b', "catch"),
    (r'\bfinally\b', "finally"),
    (r'\bthrow\b', "throw"),
    (r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
    (r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
    (r'[A-Za-z_$][A-Za-z0-9_$]*', "alphabet"),
]

# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'


def lexer(teks, tokenDeclared):
    pos = 0  # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1  # posisi karakter relatif terhadap baris tempat dia berada
    line = 1  # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in tokenDeclared:
            key, tag = t
            if line == 1:
                if key == newA:
                    key = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif key == newB:
                    key = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(key)
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


def create_token(wordFile, token):
    file = open(wordFile)
    bacaChar = file.read()
    file.close()
    tokens = lexer(bacaChar, token)
    arr = []
    for token in tokens:
        arr.append(token)
    return arr


# print(create_token('test.txt', token))
