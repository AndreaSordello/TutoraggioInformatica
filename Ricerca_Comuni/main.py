from operator import itemgetter


def leggi_comuni(nome):

    input_file=open(nome,'r',encoding='UTF-8')

    righe= input_file.readlines() # righe è una lista

     #print(righe)
    lista_comuni=[]
    for riga in righe: #riga è un elemento della lista
        riga=riga.rstrip()
        #print(riga)
        campi= riga.split(';')
        #print(campi)
        comune={
            'nome':campi[0],
            'prov':campi[2],
            'altitudine':campi[4]
        }
        lista_comuni.append(comune)
   # print(lista_comuni)
    input_file.close()
    return lista_comuni

def leggi_province(nome_file):
    input_file=open(nome_file,'r',encoding='UTF-8')
    righe = input_file.readlines()
    #print(righe)
    lista_province=[]
    for riga in righe:
        riga=riga.rstrip()
        lista_province.append(riga)
    #print(lista_province)
    input_file.close()
    return lista_province

def trova_altitudine_massima(lista_comuni,lista_province):

    for provincia in lista_province:
        lista_comuni_nella_provincia=[]
        for comune in lista_comuni:
            if comune['prov']==provincia:
                lista_comuni_nella_provincia.append(comune)
        print(lista_comuni_nella_provincia)

        massimo= max(lista_comuni_nella_provincia,key=itemgetter('altitudine'))
        #massimo { 'nome':.. }
        #print(massimo)
        #Comune più alto nella provincia di AL e' Carrega Ligure che si trova a 958 metri
        print(f"Comune più alto nella provincia di {provincia} è {massimo['nome']} che si trova a {massimo['altitudine']} metri ")
def main():

     print("inserisci il nome del file contenente i comuni:")
     nome_file_1=input()
     try:
        lista_c=leggi_comuni(nome_file_1)
     except FileNotFoundError:
        print("file comuni non trovato")
        print("inserisci il nome del file contenente i comuni:")
        nome_file_1=input()
        lista_c=leggi_comuni(nome_file_1)

     print("inserisci il nome del file contenente le province:")
     nome_file_2=input()
     try:
        lista_p=leggi_province(nome_file_2)
     except FileNotFoundError:
         print("file province non trovato")
         print("inserisci il nome del file contenente le province:")
         nome_file_2=input()
         lista_p=leggi_province(nome_file_2)
     trova_altitudine_massima(lista_c, lista_p)



main()
