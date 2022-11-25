#Program AlgoritmaCYK
#Spesifikasi : Menerapkan algoritma CYK berdasarkan rules dan masukan dengan 
#              menggunakan fitur matriks dalam bahasa pemrograman Python

#IMPLEMENTASI FUNGSI DAN PROSEDUR
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
                if (word[i] == rules[j][1][0]):
                    list_now.append(rules[j][0])
            Tabel_CYK[0].append(list_now)

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
                            if (len(rules[j][1]) != 1):
                                if (list_check[i] == rules[j][1][0]+rules[j][1][1]):
                                    belum_ada = True
                                    for m in range(len(list_now)):
                                        if (list_now[m] == rules[j][0]):
                                            belum_ada = False
                                    if (belum_ada == True):
                                        list_now.append(rules[j][0])
            Tabel_CYK[1].append(list_now)
        
        #Mengisi baris lainnya
        for b in range(2, len(word), 1):
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
                                if (len(rules[j][1]) != 1):
                                    if (list_check[i] == rules[j][1][0]+rules[j][1][1]):
                                        belum_ada = True
                                        for m in range(len(list_now)):
                                            if (list_now[m] == rules[j][0]):
                                                belum_ada = False
                                        if (belum_ada == True):
                                            list_now.append(rules[j][0])
                Tabel_CYK[b].append(list_now)

        #Validasi
        for i in range(len(list_now)):
            if (list_now[i] == "SS"):
                accept = True
                break
        return (accept)

def CYK_Tabel(word, rules):
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
                if (word[i] == rules[j][1][0]):
                    list_now.append(rules[j][0])
            Tabel_CYK[0].append(list_now)

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
                            if (len(rules[j][1]) != 1):
                                if (list_check[i] == rules[j][1][0]+rules[j][1][1]):
                                    belum_ada = True
                                    for m in range(len(list_now)):
                                        if (list_now[m] == rules[j][0]):
                                            belum_ada = False
                                    if (belum_ada == True):
                                        list_now.append(rules[j][0])
            Tabel_CYK[1].append(list_now)
        
        #Mengisi baris lainnya
        for b in range(2, len(word), 1):
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
                                if (len(rules[j][1]) != 1):
                                    if (list_check[i] == rules[j][1][0]+rules[j][1][1]):
                                        belum_ada = True
                                        for m in range(len(list_now)):
                                            if (list_now[m] == rules[j][0]):
                                                belum_ada = False
                                        if (belum_ada == True):
                                            list_now.append(rules[j][0])
                Tabel_CYK[b].append(list_now)

        #Validasi
        for i in range(len(list_now)):
            if (list_now[i] == "SS"):
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
    for i in range(len(Tabel_CYK)):
        counter_baris = len(Tabel_CYK[0]) - i-1
        j = 0
        while (j <= counter_baris):
            if (j == counter_baris):
                print("{", end='')
                for k in range(len(Tabel_CYK[i][j])):
                    if (k == len(Tabel_CYK[i][j])-1):
                        print(Tabel_CYK[i][j][k], end='')
                    else:
                        print(Tabel_CYK[i][j][k], end=',')
                print("}")
            else:
                print("{", end='')
                for k in range(len(Tabel_CYK[i][j])):
                    if (k == len(Tabel_CYK[i][j])-1):
                        print(Tabel_CYK[i][j][k], end='')
                    else:
                        print(Tabel_CYK[i][j][k], end=',')
                print("} ", end='')
            j = j + 1

#Masukan untuk percobaan
# W = ["b","a","d","a"]
# Q = ["c","a","b","a"]
# Z = ["a","b","a","b"]
# P = ["a","b","a","b","a"]
# #Rules untuk percobaan
# R = [("S", ["A","B"]), ("S", ["B","C"]), ("A", ["B","A"]), ("A", ["a"]), ("B", ["C","C"]), ("B", ["b"]), ("C", ["A","B"]), ("C", ["a"])]

# X = CYK_Tabel(P,R)
# printTabel(X)