

def media(lista_misurazioni_giornaliere):
    #[{'Temp': 4.6, 'Rugiada': 2.1, 'Pressione': 1028.0, "Umidita'": 84.0},
    # {'Temp': 4.6, 'Rugiada': 2.1, 'Pressione': 1027.7, "Umidita'": 84.0}]
    # ciclare sulle chiavi del dizionario
    print("MEDIA",end=" ")
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
        print(f"{media:.2f}",end=" ")

    print()

def leggi_file_stazione(nome_file):
    input_file = open(nome_file, 'r', encoding='UTF-8')

    intestazione = input_file.readline()
    intestazione = intestazione.rstrip()  # c'è sempre \n
    campiIntestazione = intestazione.split(';')
    print(campiIntestazione)
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
            print("Nuovo giorno")
            print(giornoLetto)
            if (giorno != ""):
                print(lista_misurazioni_giornaliere)    #lista misurazioni del giorno precedente
                # calcoli della giornata precedente
                print("Calcolo giorno ", giorno)
                    #media,massimo,minimo e la moda su lista di dizionari
                media(lista_misurazioni_giornaliere)


                # resettare lista_misurazioni
                print("reset")
                lista_misurazioni_giornaliere=[]
            giorno = giornoLetto

        misurazione = {}

        # misurazione[key] = campi[n]
        # misurazione[ campiIntestazione[n] ] = campi[n]

        for i in range(1, len(campiIntestazione)):
            misurazione[campiIntestazione[i]] = float(campi[i])
        #print(misurazione)
        lista_misurazioni_giornaliere.append(misurazione)

    print("Calcolo ultimo giorno")
    media(lista_misurazioni_giornaliere)

def main():
    leggi_file_stazione('Torino.csv')


main()
