from operator import itemgetter


def leggi_file(nome_file):
    file = open(nome_file,"r",encoding="UTF-8")
    linee = file.readlines()
   # print(linee)
    result =[]
    for linea in linee:
        linea = linea.rstrip()
       # print(linea)
        campi = linea.split(":")
        #print(campi)
        result.append(campi)
   # print(result)
    return result

def classifica(lista_partite):

    classifica =[]
    lista_squadre_trovate=[]
    for partita in lista_partite:
        squadra1 = partita[0]
        squadra2 = partita[1]
        punteggio1 = int(partita[2])
        punteggio2 = int(partita[3])
        #verifico se esiste già il dizionario della squadra1
        if squadra1 not in lista_squadre_trovate:
            dati_squadra1={
                    "nome":squadra1,
                    "golFatti":punteggio1,
                    "golSubiti":punteggio2,
            }
            if punteggio1 > punteggio2:
                dati_squadra1["punteggio"] = 3
            if punteggio1 == punteggio2:
                dati_squadra1["punteggio"] = 1
            if punteggio1 < punteggio2:
                dati_squadra1["punteggio"] = 0

            lista_squadre_trovate.append(squadra1)
            classifica.append(dati_squadra1)

        else:
            for squadra in classifica:
                if squadra["nome"]==squadra1:
                    squadra["golFatti"] += punteggio1
                    squadra["golSubiti"] += punteggio2
                    if punteggio1 > punteggio2:
                            squadra["punteggio"] += 3
                    if punteggio1 == punteggio2:
                            squadra["punteggio"] += 1


        #verifico se esiste già il dizionario della squadra2
        if squadra2 not in lista_squadre_trovate:
            dati_squadra2={
                    "nome":squadra2,
                    "golFatti":punteggio2,
                    "golSubiti":punteggio1,
            }
            if punteggio2 > punteggio1:
                dati_squadra2["punteggio"] = 3
            if punteggio1 == punteggio2:
                dati_squadra2["punteggio"] = 1
            if punteggio2 < punteggio1:
                dati_squadra2["punteggio"] = 0
            lista_squadre_trovate.append(squadra2)
            classifica.append(dati_squadra2)
        else:
            for squadra in classifica:
                if squadra["nome"]==squadra2:
                    squadra["golFatti"] += punteggio2
                    squadra["golSubiti"] += punteggio1
                    if punteggio2 > punteggio1:
                            squadra["punteggio"] += 3

                    if punteggio1 == punteggio2:
                            squadra["punteggio"] += 1

    #print(classifica)

    classifica.sort(key = itemgetter("punteggio"),reverse=True)
    #print(classifica)
    print("Classifica\n")
    for i in range(0, len(classifica)):
        y = i+1
        print(f'{y}. {classifica[i]["nome"]} - Punti:{classifica[i]["punteggio"]}, Gol fatti:{classifica[i]["golFatti"]}, Gol subiti: {classifica[i]["golSubiti"]}')

    print()
    return classifica

def miglioreAttacco(classifica):
    migliore= max(classifica,key=itemgetter("golFatti"))
    print(f'Migliore attacco {migliore["nome"]} - Gol fatti: {migliore["golFatti"]}')

def miglioreDifesa(classifica):
    migliore= min(classifica,key=itemgetter("golSubiti"))
    print(f'Migliore difesa {migliore["nome"]} - Gol subiti: {migliore["golSubiti"]}')


def main():

    result= leggi_file("torneo.txt")
    clas = classifica(result)
    miglioreAttacco(clas)
    miglioreDifesa(clas)

main()



