
def leggi_mappa(nome_file):
    input_file=open(nome_file,'r',encoding='UTF-8')
    linee=input_file.readlines()
    mappa=[] #contiene le liste 'riga'
    for linea in linee:         #for linea in input_file:
        #print(linea)
        linea = linea.rstrip()
        elementi = linea.split(' ')
       # print(elementi)
        riga=[]
        for elemento in elementi:
            elemento= int(elemento)
            riga.append(elemento)
        mappa.append(riga)
    print(mappa)
    input_file.close()
    return mappa
def cerca_punte(mappa):

    nRighe=len(mappa)
    nColonne=len(mappa[0])
    sommaPunte=0
    contaPunte=0
    for i in range(0,nRighe):
        for j in range(0,nColonne):
            #mappa[i][j] è un punta?
            isPunta=True
            for y in range(i-1,i+1+1):  #genera elementi tra i-1 <= c < i+1
                for x in range(j-1,j+1+1):
                    #controllo che sia dentro la mappa
                    if x>=0 and y>=0 and x<nColonne and y<nRighe and not(x==j and y==i):
                        #print(f"{i} {j} -> {y} {x}" )
                        if mappa[y][x] >= mappa[i][j]:
                            #NON è una punta
                            isPunta=False
            if isPunta:
                print(mappa[i][j],i,j)
                contaPunte+=1
                sommaPunte+=mappa[i][j]
    print("Altezza media", sommaPunte/contaPunte)

def main():
    mappa=leggi_mappa('mappa.txt')
    cerca_punte(mappa)

main()
