from operator import itemgetter


def leggi_shop(nome_file):
    input_file = open(nome_file,'r',encoding='UTF-8')
    lista_negozi=[]
    for linea in input_file:
        linea= linea.rstrip()
        lista_negozi.append(linea)
    print(lista_negozi)
    input_file.close()
    return lista_negozi

def leggi_rilevazioni(nome_file):
    input_file = open(nome_file,'r',encoding='UTF-8')

    input_file.readline()
    lista_rilevazioni=[]
    for linea in input_file:
        linea=linea.rstrip()
        campi = linea.split(',')
        #print(campi)
        if campi[4]=='E':
            #prodotto essenziale
            prodotto={
                'negozio':campi[2],
                'nome':campi[3],
                'prezzo':float(campi[5])
            }
            lista_rilevazioni.append(prodotto)
    print(lista_rilevazioni)
    input_file.close()
    return lista_rilevazioni
def stampa_essenziali(l_r,l_n):
    lista_elementi_stampa=[]        # Apple,Tomato,

    for prodotto in l_r:
        if  prodotto['nome'] not in lista_elementi_stampa:
            if prodotto['negozio'] in l_n:      #controllo se è un prodotto venduto dai negozi che sto controllando
                lista_elementi_stampa.append(prodotto['nome'])

    lista_elementi_stampa.sort() # ordine alfabetico/ordine crescente
    print("Prodotti:")
    for p in lista_elementi_stampa:
        print(f"- {p}")         # print ("-",p)
    #print(lista_elementi_stampa)

def stampa_prezzi_minimi(l_r,l_n):
    l_n.sort()

    for negozio in l_n:
        lista_prodotti_negozio=[]    #lista di dizionari con negozio,nome,prezzo
        for prodotto in l_r:
            if prodotto['negozio']==negozio:
                #prodotto venduto da quel negozio
               # print(prodotto)
                #devo fare controlli, esiste già?il prezzo memorizzato è il minimo?
                trovato=False
                for prodotto_negozio in lista_prodotti_negozio:
                    if prodotto_negozio['nome']==prodotto['nome']:
                        #esiste già
                        trovato=True
                        #il prezzo memorizzato è il minimo?
                        if prodotto_negozio['prezzo']>prodotto['prezzo']:
                            #devo memorizzare il nuovo prodotto perchè costa di meno
                            # e buttare via il prodotto vecchio
                            lista_prodotti_negozio.append(prodotto)
                            lista_prodotti_negozio.remove(prodotto_negozio)
                if not trovato:
                    lista_prodotti_negozio.append(prodotto)
        #print(lista_prodotti_negozio)
        print(negozio)
        lista_prodotti_negozio.sort(key=itemgetter('nome'))
        for prodotto_negozio in lista_prodotti_negozio:
            print(f"- {prodotto_negozio['nome']} : {prodotto_negozio['prezzo']} $/chilo")

def trova_minimo(l_r,l_n,prodotto):

    #min(l_r,key=itemgetter('prezzo'))
    lista_prezzi=[]
    for rilevazione in l_r:
        if rilevazione['nome']==prodotto and rilevazione['negozio'] in l_n:
            lista_prezzi.append(rilevazione)
    #print(lista_prezzi)
    if len(lista_prezzi)==0:
        print("Prodotto non disponibile")
    else:
        minimo=min(lista_prezzi,key=itemgetter('prezzo'))
        print(f"Prezzo minimo {minimo['prezzo']} $/chilo da {minimo['negozio']}")


def main():
   lista_negozi=leggi_shop('shop.txt')
   lista_rilevazioni = leggi_rilevazioni('NLFoodPricing.csv')

   stampa_essenziali(lista_rilevazioni,lista_negozi)
   stampa_prezzi_minimi(lista_rilevazioni,lista_negozi)

   print("Che cibo vuoi cercare:")
   prodotto=input()
   while ( prodotto!='q'):
        trova_minimo(lista_rilevazioni,lista_negozi,prodotto)
        print("Che cibo vuoi cercare:")
        prodotto=input()


   print("Arrivederci")

main()
