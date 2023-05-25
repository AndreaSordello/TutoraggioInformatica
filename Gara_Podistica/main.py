from math import floor


def leggi_database(percorso_file):
    input_file = open(percorso_file,'r',encoding='UTF-8')
    dizionario_record={}

    for linea in input_file:
        linea=linea.rstrip()
        campi = linea.split(';')
        #print(campi)
        key=campi[0]
        dizionario_record[key]=float(campi[1])
    print(dizionario_record)
    input_file.close()
    return dizionario_record

def leggi_risultati(percorso_file):
    input_file = open(percorso_file,'r',encoding='UTF-8')
    lista_risultati=[]
    for linea in input_file:
        linea=linea.rstrip()
        campi=linea.split(';')
        diz_atleta={
            'nome':campi[0],
            'cognome':campi[1],
            'cat' : campi[3],
            'tempo': int(campi[4]),
            'id': campi[5]
        }
        lista_risultati.append(diz_atleta)
    print(lista_risultati)
    input_file.close()
    return lista_risultati
def calcola(diz_record,lista_risultati):
    #1° CALCOLARE IL PASSO DI OGNI ATLETA E STAMPARLO DIVISO IN CATEGORIA
    listaM=[]
    listaF=[]
    listaRecord=[]
    for atleta in lista_risultati:
        passo_temporaneo= atleta['tempo']/10
        #print(passo_temporaneo)
          #print(passo)
         #   3.3 -> 0.3
        #    3.3 - 3 =0.3
         #  abs(x)
        #round(n)
       #floor(n) floor(3.3) -> 3
        #ceil(n)
        #trunc(n) trunc(3.3) -> 3
        parte_decimale=passo_temporaneo-floor(passo_temporaneo)
        parte_decimale=parte_decimale*0.6
        passo = floor(passo_temporaneo)+parte_decimale
        diz={
                'nome':atleta['nome'],
                'cognome':atleta['cognome'],
                'passo':passo
            }
        if atleta['cat']=='M':
            #aggiungiamo l'atleta a listaM
            listaM.append(diz)
        else:
            listaF.append(diz)

        #ha superato il record personale?
        key=atleta['id']
        recordAtleta=diz_record[key]
        if passo < recordAtleta:
            listaRecord.append(diz) # passo è in più ma lo ignoro


    print("CLASSIFICA PARTECIPANTI\n")
    print("Categoria:M")
    for atleta in listaM:
        print(f"{atleta['nome']} {atleta['cognome']}, {atleta['passo']:.2f} min/km")
    print("\nCategoria:F")
    for atleta in listaF:
        print(f"{atleta['nome']} {atleta['cognome']}, {atleta['passo']:.2f} min/km")

    print("\nATLETI CHE HANNO SUPERATO IL RECORD PERSONALE\n")
    for atleta in listaRecord:
        print(f"{atleta['nome']} {atleta['cognome']}")


def main():
    diz_record=leggi_database('database_atleti.txt')
    lista_risulati=leggi_risultati('risultati_gara.txt')
    calcola(diz_record,lista_risulati)
main()
