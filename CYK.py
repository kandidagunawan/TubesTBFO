#Program AlgoritmaCYK
#Spesifikasi :

#KAMUS

#ALGORITMA

# def CreateMatrix(n):
#     result = [[None for i in range (n)] for j in range (n)]
#     return (result)

def CYK(word, rules):
    accept = False
    for i in range (len(word)):
        if (word[i] == None):
            accept = True
        else:
            accept = False
            break
    
    if (accept == True):
        return (accept)
    else:
        Tabel_CYK = [[]]

        #Mengisi baris pertama
        for i in range(len(word)):
            list_now = []
            for j in range(len(rules)):
                for k in range(len(rules[j][1])):
                    if (word[i] == rules[j][1][k]):
                        list_now.append(rules[j][0])
            Tabel_CYK[0].append(list_now)
        print(Tabel_CYK)
        print("\n\n")

        #Mengisi baris kedua
        Tabel_CYK.append([])
        for k in range(0, len(word)-1, 1):
            list_now = []
            for c in range(0, 1, 1):
                list1 = Tabel_CYK[c][k]
                list2 = Tabel_CYK[1-c-1][k+c+1]
                list_check = multiplyList(list1,list2)
                if (c == 1-1 or 1-c-1 == 1-1):
                    for i in range(len(list_check)):
                        for j in range(len(rules)):
                            for l in range(len(rules[j][1])):
                                if (list_check[i] == rules[j][1][l]):
                                    belum_ada = True
                                    for m in range(len(list_now)):
                                        if (list_now[m] == rules[j][0]):
                                            belum_ada = False
                                    if (belum_ada == True):
                                        list_now.append(rules[j][0])
            Tabel_CYK[1].append(list_now)
        print(Tabel_CYK)
        print("\n\n")

        #Mengisi baris ketiga
        Tabel_CYK.append([])
        for k in range(0, len(word)-2, 1):
            list_now = []
            for c in range(2):
                list1 = Tabel_CYK[c][k]
                list2 = Tabel_CYK[2-c-1][k+c+1]
                list_check = multiplyList(list1,list2)
                if (c == 2-1 or 2-c-1 == 2-1):
                    for i in range(len(list_check)):
                        for j in range(len(rules)):
                            for l in range(len(rules[j][1])):
                                if (list_check[i] == rules[j][1][l]):
                                    belum_ada = True
                                    for m in range(len(list_now)):
                                        if (list_now[m] == rules[j][0]):
                                            belum_ada = False
                                    if (belum_ada == True):
                                        list_now.append(rules[j][0])
            Tabel_CYK[2].append(list_now)
        print(Tabel_CYK)
        print("\n\n")

        #Mengisi baris keempat
        Tabel_CYK.append([])
        for k in range(0, len(word)-3, 1):
            list_now = []
            for c in range(3):
                list1 = Tabel_CYK[c][k]
                list2 = Tabel_CYK[3-c-1][k+c+1]
                list_check = multiplyList(list1,list2)
                if (c == 3-1 or 3-c-1 == 3-1):
                    for i in range(len(list_check)):
                        for j in range(len(rules)):
                            for l in range(len(rules[j][1])):
                                if (list_check[i] == rules[j][1][l]):
                                    belum_ada = True
                                    for m in range(len(list_now)):
                                        if (list_now[m] == rules[j][0]):
                                            belum_ada = False
                                    if (belum_ada == True):
                                        list_now.append(rules[j][0])
            Tabel_CYK[3].append(list_now)
        
        #Mengisi baris lainnya
        for b in range(4, len(word), 1):
            Tabel_CYK.append([])
            for k in range(0, len(word)-b, 1):
                list_now = []
                for c in range(b):
                    list1 = Tabel_CYK[c][k]
                    list2 = Tabel_CYK[b-c-1][k+c+1]
                    list_check = multiplyList(list1,list2)
                    if (c == b-1 or b-c-1 == b-1):
                        for i in range(len(list_check)):
                            for j in range(len(rules)):
                                for l in range(len(rules[j][1])):
                                    if (list_check[i] == rules[j][1][l]):
                                        belum_ada = True
                                        for m in range(len(list_now)):
                                            if (list_now[m] == rules[j][0]):
                                                belum_ada = False
                                        if (belum_ada == True):
                                            list_now.append(rules[j][0])
                Tabel_CYK[b].append(list_now)

        #Validasi
        for i in range(len(list_now)):
            if (list_now[i] == "S"):
                accept = True
                break
        return (Tabel_CYK)

def multiplyList(L1, L2):
    result = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            result.append(L1[i]+L2[j])
    return (result)

def printTabel (Tabel_CYK):
    for i in range(len(Tabel_CYK[0])-2):
        counter_baris = len(Tabel_CYK[0]) - i 
        j = 0
        while (j < counter_baris):
            if (j == counter_baris-1):
                print("{", end='')
                for k in range(len(Tabel_CYK[i][j])):
                    if (k == len(Tabel_CYK[i][j])-1):
                        print(Tabel_CYK[i][j][k], end='} \n')
                    else:
                        print(Tabel_CYK[i][j][k], end=',')
            else:
                print("{", end='')
                for k in range(len(Tabel_CYK[i][j])):
                    if (k == len(Tabel_CYK[i][j])-1):
                        print(Tabel_CYK[i][j][k], end='} ')
                    else:
                        print(Tabel_CYK[i][j][k], end=',')
            j = j + 1

W = ["b","a","b","d","a"]
Q = ["c","d"]
R = [("S", ["a","b","c","SA"]), ("A", ["a","b","AA"])]
X = CYK (W, R)
print(X)