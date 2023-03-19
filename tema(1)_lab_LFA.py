cuvant_initial=input("Dati cuvantul: ")
with open("fisier_intrare_automat.txt", "r") as f:
    parcurs={}
    stari=f.readline().strip().split()
    stare_initiala=f.readline().strip().split()
    stari_finale=f.readline().strip().split()
    alfabet=f.readline().strip().split()
    cuvant=''
    ok=1
    for i in stare_initiala:
        parcurs['start']=i
    for linie in f:
        L=[str(x) for x in linie.strip().split()]
        if (L[0] and L[2]) not in stari:
            ok=0
            break
        if L[1] in alfabet:
            cuvant=cuvant+L[1]
            parcurs[cuvant]=L[2]
        else:
            ok=0
            break

if cuvant==cuvant_initial and ok==1:
    if parcurs[cuvant] in stari_finale:
        print("Acceptat")
        print("Parcursul: ")
        lista=[]
        for element in parcurs:
            lista.append(parcurs[element])
        Afisare=' -> '.join(lista)
        print('Start:',Afisare)
    else:
        print("Neacceptat")
else:
     print("Neacceptat")