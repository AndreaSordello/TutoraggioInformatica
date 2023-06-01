from operator import itemgetter


def media(lista_misurazioni_giornaliere):
    #[{'Temp': 4.6, 'Rugiada': 2.1, 'Pressione': 1028.0, "Umidita'": 84.0},
    # {'Temp': 4.6, 'Rugiada': 2.1, 'Pressione': 1027.7, "Umidita'": 84.0}]
    # ciclare sulle chiavi del dizionario
    titolo ="Media"
    print(f"{titolo:>10}",end="  ")
    for key in lista_misurazioni_giornaliere[0].keys():
        #keys restituisce la lista di chiavi di un dizionario,
        # ma noi abbiamo una lista di dizionari che hanno tutti le stesse chiavi, e quindi prendo il primo elemento come riferimento
        #key ='Temp', key= 'Rugiada',...
        cont=0
        somma=0
        for misurazione in lista_misurazioni_giornaliere:

            somma+=misurazione[key]
            cont+=1

        media=somma/cont
        print(f"{media:<25.2f}",end="")

    print()


def massimo(lista_misurazioni_giornaliere):
    titolo ="Massimo"
    print(f"{titolo:>10}",end="  ")
    for chiave in lista_misurazioni_giornaliere[0].keys():
        massimo= max (lista_misurazioni_giornaliere,key=itemgetter(chiave))
        print(f"{massimo[chiave]:<25.2f}",end="")
    print()

def minimo(lista_misurazioni_giornaliere):
    titolo ="Minimo"
    print(f"{titolo:>10}",end="  ")
    for chiave in lista_misurazioni_giornaliere[0].keys():
        minimo= min (lista_misurazioni_giornaliere,key=itemgetter(chiave))
        print(f"{minimo[chiave]:<25.2f}",end="")
    print()

def moda(lista_misurazioni_giornaliere):
    # elemento che compare più volte
    titolo ="Moda"
    print(f"{titolo:>10}",end="  ")
    for chiave in lista_misurazioni_giornaliere[0].keys():
        diz_occorenze={}
        for misurazione in lista_misurazioni_giornaliere:
            if misurazione[chiave] in diz_occorenze:
                 diz_occorenze[ misurazione[chiave] ] = diz_occorenze[ misurazione[chiave] ] + 1
            else:
                diz_occorenze[ misurazione[chiave] ] = 1

        #cercare il massimo tra i valori del dizionario
        #print(diz_occorenze)

        first=True
        for elementi in diz_occorenze.items():
            #.items() restituisce una tupla composta da (chiave,valore)
            if first:
                chiave_massimo=elementi[0]
                valore_massimo=elementi[1]
                first=False

            if valore_massimo<elementi[1]:
                valore_massimo=elementi[1]
                chiave_massimo=elementi[0]

        print(f"{chiave_massimo:<25.2f}",end="")

    print()


def leggi_file_stazione(nome_file):
    "Torino.csv"
    campi_file=nome_file.split(".")
    nome_citta= campi_file[0]
    print(f"Report meteorologico per la stazione di {nome_citta}")

    input_file = open(nome_file, 'r', encoding='UTF-8')

    intestazione = input_file.readline()
    intestazione = intestazione.rstrip()  # c'è sempre \n
    campiIntestazione = intestazione.split(';')
    #print(campiIntestazione)
    spazio=""
    print(f"{spazio:>10}",end="  ")
    for i in range (1,len(campiIntestazione)):
        print(f"{campiIntestazione[i]:<25}",end="")
    print()
    lista_misurazioni_giornaliere = []
    giorno = ""
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(';')
        # print(campi)
        dataOra = campi[0].split(' ')
        # print(dataOra)
        giornoLetto = dataOra[0]
        # print(giornoLetto)

        if giornoLetto != giorno:  # prima volta  1-06!=""  ,seconda volta 2-06!=1-06
            #print("Nuovo giorno")
           # print(giornoLetto)
            if (giorno != ""):
               # print(lista_misurazioni_giornaliere)    #lista misurazioni del giorno precedente
                # calcoli della giornata precedente
                print(f"{giorno:>10}")
                    #media,massimo,minimo e la moda su lista di dizionari
                media(lista_misurazioni_giornaliere)
                massimo(lista_misurazioni_giornaliere)
                minimo(lista_misurazioni_giornaliere)
                moda(lista_misurazioni_giornaliere)
                # resettare lista_misurazioni

                lista_misurazioni_giornaliere=[]
            giorno = giornoLetto

        misurazione = {}

        # misurazione[key] = campi[n]
        # misurazione[ campiIntestazione[n] ] = campi[n]

        for i in range(1, len(campiIntestazione)):
            misurazione[campiIntestazione[i]] = float(campi[i])
        #print(misurazione)
        lista_misurazioni_giornaliere.append(misurazione)

    print(f"{giorno}")
    media(lista_misurazioni_giornaliere)
    massimo(lista_misurazioni_giornaliere)
    minimo(lista_misurazioni_giornaliere)
    moda(lista_misurazioni_giornaliere)
def main():
    leggi_file_stazione('Vercelli.csv')


main()
