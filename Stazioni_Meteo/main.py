
def leggi_file_stazione(nome_file):

    input_file = open (nome_file,'r',encoding='UTF-8')

    intestazione = input_file.readline()
    intestazione=intestazione.rstrip() # c'è sempre \n
    campiIntestazione=intestazione.split(';')
    print(campiIntestazione)
    lista_misurazioni_giornaliere=[]
    giorno=""
    for linea in input_file:
        linea=linea.rstrip()
        campi=linea.split(';')
       # print(campi)
        dataOra=campi[0].split(' ')
       # print(dataOra)
        giornoLetto=dataOra[0]
       # print(giornoLetto)

        if giornoLetto!=giorno:  #prima volta  1-06!=""  ,seconda volta 2-06!=1-06
            print("Nuovo giorno")
            print(giornoLetto)
            if (giorno!=""):
                #calcoli della giornata precedente
                print("Calcolo giorno ",giorno)
                #resettare lista_misurazioni
                print("reset")
            giorno=giornoLetto

        misurazione={}

        #misurazione[key] = campi[n]
        #misurazione[ campiIntestazione[n] ] = campi[n]

        for i in range(1,len(campiIntestazione)):
            misurazione[ campiIntestazione[i] ] = float(campi[i])
        print(misurazione)
        lista_misurazioni_giornaliere.append(misurazione)
def main():

    leggi_file_stazione('Pinerolo.csv')
main()
