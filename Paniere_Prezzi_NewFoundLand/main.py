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

def main():
   lista_negozi=leggi_shop('shop.txt')
   lista_rilevazioni = leggi_rilevazioni('NLFoodPricing.csv')

   stampa_essenziali(lista_rilevazioni,lista_negozi)

main()
