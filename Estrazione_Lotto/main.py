from operator import itemgetter


def leggi_estrazioni(nome_file):
    input_file = open(nome_file,"r",encoding="UTF-8")
    lista_estrazioni = []
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split("\t")
       # print(campi)
        estrazione = {
            "data" : campi[0],
            "ruota" :campi[1],
            "numeri": campi[2:] # prendiamo gli elementi da 2 in avanti
        }
       # print(estrazione)
        lista_estrazioni.append(estrazione)
    return lista_estrazioni

def ruote_disponibili(lista_estrazioni):

    lista_ruote = set()

    for estrazioni in lista_estrazioni:
        lista_ruote.add(estrazioni["ruota"])
    #print(lista_ruote)
    return lista_ruote

def trova_occorrenze(lista_estrazione,ruota1,ruota2):

    diz_occorrenze={}
    for estrazione1  in lista_estrazione:
        if estrazione1["ruota"] == ruota1:
            for estrazione2 in lista_estrazione:
                if estrazione2["ruota"] == ruota2 and estrazione2["data"] == estrazione1["data"]:
                    #print(estrazione1,estrazione2)
                    #confrontare i numeri
                    for numero1 in estrazione1["numeri"]:
                        if numero1 in estrazione2["numeri"]:
                            print(f"Numero comune {numero1:>2} in data {estrazione1['data']}")
                            if numero1 in diz_occorrenze.keys():
                                diz_occorrenze[numero1]+=1
                            else:
                                diz_occorrenze[numero1]=1
    #print(diz_occorrenze)

    lista_occorrenze=[]
    for chiave in diz_occorrenze.keys():

        occorrenza={
            "numero": chiave,
            "occorrenza":diz_occorrenze[chiave]
        }
        lista_occorrenze.append(occorrenza)
    lista_occorrenze.sort(key=itemgetter("occorrenza"),reverse=True)
   # print(lista_occorrenze)

    print("Numero Frequenza")
    print("------ ---------")
    for elemento in lista_occorrenze:
        print(f"{elemento['numero']:>6} {elemento['occorrenza']:>9}")

def main():
        lista_estrazioni=leggi_estrazioni("long.txt")
       #print(lista_estrazioni)
        lista_ruote=ruote_disponibili(lista_estrazioni)
        print("Ruote disponibili: ",end="")
        for ruota in lista_ruote:
            print(ruota,end=", ")
        print()

        print("Inserisci prima ruota:")
        ruota1= input()
        print("Inserisci seconda ruota:")
        ruota2= input()

        trova_occorrenze(lista_estrazioni,ruota1,ruota2)
main()
