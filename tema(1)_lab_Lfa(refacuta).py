with open("fisier_intrare_automat.txt", "r") as f:
    nr_stari=int(f.readline())
    # print(nr_stari)
    alfabet=f.readline().strip().split()
    # print(alfabet)
    stare_initiala=int(f.readline())
    # print(stare_initiala)
    stare_finala=f.readline().strip().split()
    stari_finale=[]
    for nr in stare_finala:
        stari_finale.append(int(nr))
    # print(stare_finala)
    # print(stari_finale)
    matrice=[['-' for x in range(stare_initiala,stare_initiala+nr_stari)] for y in range(stare_initiala,stare_initiala+nr_stari)]
    for linie in f:
        L=[str(x) for x in linie.strip().split()]
        if matrice[int(L[0])][int(L[2])]!='-':
           matrice[int(L[0])][int(L[2])]=matrice[int(L[0])][int(L[2])]+L[1]
        else:
            matrice[int(L[0])][int(L[2])]=L[1]
# print(matrice)

cuvant=input("Dati input: ")
cuvant_final=''
linie=stare_initiala
nr_litera=0
parcurs=[str(stare_initiala)]
if cuvant!="cuvant vid":
    while nr_litera<len(cuvant):
        ok=0
        if cuvant[nr_litera] not in alfabet:
            break
        for nod in range(nr_stari):
            if cuvant[nr_litera] in matrice[linie][nod]:
                cuvant_final=cuvant_final+cuvant[nr_litera]
                ok=1
                parcurs.append(str(nod))
                linie=nod
                nr_litera+=1
                break
        if ok==0:
            break

    if cuvant_final==cuvant and ok==1:
        if nod in stari_finale:
            print("Acceptat")
            parcurs_final = " -> ".join(parcurs)
            print(parcurs_final)
        else:
            print("Neacceptat")
    else:
        print("Neacceptat")
else:
    if cuvant=="cuvant vid" and (stare_initiala in stari_finale):
        print("Acceptat")