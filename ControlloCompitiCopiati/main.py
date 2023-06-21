

def leggi_risposte(nome_file):
    input_file = open (nome_file,"r",encoding="UTF-8")

    diz_risposte ={}

    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(" ")
       # print(campi)
        diz_risposte[campi[0]] = campi[1:]
    print(diz_risposte)
    input_file.close()
    return diz_risposte

def leggi_posizioni(nome_file):
    input_file = open(nome_file,"r",encoding="UTF-8")
    matrice_posizioni=[]
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(" ")
        #print(campi)
        matrice_posizioni.append(campi)
    print(matrice_posizioni)
    input_file.close()
    return matrice_posizioni

def verificaRisposte(studenteA,studenteB,listaRisposteA,listaRisposteB):

    #caso risposte completamente uguali
    if listaRisposteA==listaRisposteB:
        print(f"le risposte di {studenteA} e {studenteB} sono uguali")

    copiatoDa=False
    isDifferente=False
    for i in range(0,len(listaRisposteA)):
            if listaRisposteA[i] != listaRisposteB[i]:
                if listaRisposteA[i] =="-" and listaRisposteB[i]!="-":
                    copiatoDa=True
                else:
                    isDifferente=True

    if copiatoDa and isDifferente==False:
        print(f"{studenteA} può aver copiato da {studenteB}")


def controllaCopiature(matrice_posizioni,diz_risposte):

    for i in range(0,len(matrice_posizioni)):
        for j in range(0,len(matrice_posizioni[i])):

            studenteA=matrice_posizioni[i][j]
            listaRisposteA=diz_risposte[studenteA]
           # print(studenteA,listaRisposteA)
            if j-1 >=0:
                #matrice_posizioni[i][j-1] VICINO DI SX
                studenteB=matrice_posizioni[i][j-1]
                listaRisposteB=diz_risposte[studenteB]
              #  print(studenteB,listaRisposteB)
                verificaRisposte(studenteA,studenteB,listaRisposteA,listaRisposteB)

            if j+1 < len(matrice_posizioni[i]):
                studenteB=matrice_posizioni[i][j+1]
                listaRisposteB=diz_risposte[studenteB]
              #  print(studenteB,listaRisposteB)
                verificaRisposte(studenteA,studenteB,listaRisposteA,listaRisposteB)
           # print()


            #matrice_posizioni[i][j+1]



def main():
    diz_risposte = leggi_risposte("risposte.txt")
    matrice_posizioni=leggi_posizioni("posizioni.txt")

    controllaCopiature(matrice_posizioni,diz_risposte)

main()
