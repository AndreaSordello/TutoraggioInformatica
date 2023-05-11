
def leggi_matrice(nome_file):
    input_file=open(nome_file,'r',encoding='UTF-8')

    righe=input_file.readlines()
    matrice=[]
    for riga in righe:

        riga=riga.strip()
        #print(riga)
        elementiRiga=riga.split(' ')
        #print(elementiRiga)
        #matrice.append(elementiRiga)
        rigaMatrice=[]
        for elemento in elementiRiga:
            rigaMatrice.append(int(elemento))
        matrice.append(rigaMatrice)
   # print(matrice)
    return matrice
def trova_massimo(matrice):
    matrice_risultato=[]
    #dobbiamo verificare la condizione valore per valore
    nRighe=len(matrice)
    nCol=len(matrice[0])
    for i in range(0,nRighe):
        matrice_risultato_riga=[]
        for j in range(0,nCol):
            #print( matrice [i][j],end =" ")
           #per ottenere i vicini di [i][j]
            massimo=matrice[i][j]
            isMassimoCambiato=False #per gestire due massimi uguali
            for y in range(i-2,i+2+1): # genera valori da i-2<=y<i+2
                for x in range (j-2,j+2+1):

                    #  indici trovati sono validi? >=0 ,<nRighe ,< nCol
                    if y>=0 and x>=0 and y<nRighe and x <nCol and not (y==i and j==x):
                        #print( i,j,y,x,matrice [y][x]) #adesso y e x mi permettono di ottenere valori sempre validi
                        if matrice[y][x] >= matrice[i][j]:
                            isMassimoCambiato=True
            #dopo aver guardato tutti i vicini
            if not isMassimoCambiato:
                #punto di massimo
                #print(massimo)
                matrice_risultato_riga.append(massimo)
            else:
                #non è un punto di massimo
                matrice_risultato_riga.append('-')
        matrice_risultato.append(matrice_risultato_riga)
        print("")


   # print(matrice_risultato)


    for i in range(0,nRighe):
        for j in range(0,nCol):
            print(matrice_risultato[i][j],end ="  ")
        print(" ")

def main():
   matrice=leggi_matrice('mappa.txt')
   trova_massimo(matrice)
main()
