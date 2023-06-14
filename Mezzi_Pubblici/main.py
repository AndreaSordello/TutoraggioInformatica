from operator import itemgetter


def leggi_database(nome_file):

    input_file = open(nome_file,"r",encoding="UTF-8");

    database={}
    for linea in input_file:
        linea = linea.rstrip()
        campi =linea.split(": ")
        database[campi[0]]=campi[1]
    input_file.close()
   # print(database)
    return database

def leggi_dati(nome_file):
    input_file = open (nome_file,"r",encoding="UTF-8")

    intestazione = input_file.readline()
    intestazione = intestazione.rstrip()
    campi = intestazione.split(",")
   # print(campi)
    lista_fermate = campi[2:]
   # print(lista_fermate)

    lista_tratte=[]
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(",")
        tratta={
            "IDautista":campi[0],
            "fermate":campi[2:]
        }
        lista_tratte.append(tratta)
    input_file.close()
    return lista_fermate,lista_tratte

def conta_saliti_scesi(lista_tratte,lista_fermate,db):

    lista_saliti_scesi=[]
    for i in range(0,len(lista_fermate)):
        count_saliti=0
        count_scesi =0
        for tratta in lista_tratte:
            passeggeri = tratta["fermate"][i]
           # print(passeggeri)
            #CASO -- , n , -n , n/m

            if "/" in passeggeri:
                campi = passeggeri.split("/")
                count_saliti += int(campi[0])
                count_scesi += int(campi[1])
            else:
                if passeggeri != "--":
                    # caso n , -n
                    if passeggeri.isnumeric():
                        count_saliti+= int(passeggeri)
                    else:

                        count_scesi += abs(int(passeggeri))

        lista_saliti_scesi.append({
            "IDfermata":lista_fermate[i],
            "saliti":count_saliti,
            "scesi":count_scesi
        })
   # print(lista_saliti_scesi)

    massimo = max(lista_saliti_scesi,key=itemgetter("saliti"))
    print(f"La fermata in cui salgono più passeggeri ({massimo['saliti']}) è {db[massimo['IDfermata']]}")
    massimo = max(lista_saliti_scesi,key=itemgetter("scesi"))
    print(f"La fermata in cui scendono più passeggeri ({massimo['scesi']}) è {db[massimo['IDfermata']]}")

def conta_saliti_autista(lista_tratte,db):

    diz_autista ={}
    for tratta in lista_tratte:
        count_pass = 0
        for passeggeri in tratta["fermate"]:
                if "/" in passeggeri:
                    campi = passeggeri.split("/")
                    count_pass += int(campi[0])
                else:
                    if passeggeri != "--":
                        # caso n , -n
                        if passeggeri.isnumeric():
                            count_pass+= int(passeggeri)
        if tratta["IDautista"] in diz_autista.keys():
            diz_autista[tratta["IDautista"]] +=count_pass
        else:
            diz_autista[tratta["IDautista"]] =count_pass
    #print(diz_autista)

    lista_autista=[]
    for chiave in diz_autista.keys():
        autista={
            "nome":db[chiave],
            "count": diz_autista[chiave]
        }
        lista_autista.append(autista)
   # print(lista_autista)
    lista_autista.sort(key=itemgetter("count"),reverse=True)
   # print(lista_autista)
    for autista in lista_autista:
        print(f"{autista['nome']} con {autista['count']}")



def main():

    db = leggi_database("database.txt")

    lista_f,lista_t= leggi_dati("dati_aeroporto_torino.csv")

    #print(lista_f)
    #print(lista_t)

    conta_saliti_scesi(lista_t,lista_f,db)
    conta_saliti_autista(lista_t,db)
main()
