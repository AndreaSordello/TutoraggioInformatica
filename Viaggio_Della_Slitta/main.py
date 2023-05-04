from operator import itemgetter
import math

def leggi_bambini(nome_file):
    input_file=open(nome_file,"r",encoding='UTF-8')
    input_file.readline()  #leggo l'intestazione
    linee = input_file.readlines()
    lista_bambini=[]
    for linea in linee:
       # print(linea)
        linea=linea.rstrip()
        campi=linea.split(',')
        #print(campi)
        bambino={
            'cognome': campi[0],
            'nome': campi[1],
            'regalo': campi[2],
            'prov':campi[3]
        }
        lista_bambini.append(bambino)
    return lista_bambini
def leggi_province(nome_file):
    input_file=open(nome_file,"r",encoding='UTF-8')
    input_file.readline()  #leggo intestazione e butto via il valore
    linee=input_file.readlines()
    lista_province=[]
    for linea in linee:
        linea=linea.rstrip()
        campi=linea.split(',')
        provincia={
            'prov':campi[4],
            'lat': float(campi[5]),
            'long':float(campi[6]),
        }
        lista_province.append(provincia)
    return lista_province
def calcola_distanza(latA,latB,longA,longB):
    FATTORE=180/math.pi
    R= 6731
    latA_rad=latA/FATTORE
    latB_rad=latB/FATTORE
    longA_rad=longA/FATTORE
    longB_rad=longB/FATTORE
    delta_lat= latA_rad - latB_rad
    delta_long= longA_rad-longB_rad
    h= math.sin(delta_lat/2) **2 + math.cos(latA_rad)*math.cos(latB_rad)*(math.sin(delta_long/2)**2)
    distanza = 2 * R *math.asin( math.sqrt(h) )
    return distanza

def calcola_itinerario(lista_b,lista_p):
    #UNIRE LE INFORMAZIONI
    lista_viaggio=[]
    for b in lista_b:
        for prov in lista_p:
            if b['prov']==prov['prov']:
                #abbiamo trovato la provincia del bambino
                bambino_viaggio=dict(b) # copia del dizionario
                bambino_viaggio['lat']=prov['lat']
                bambino_viaggio['long']=prov['long']
                #print(bambino_viaggio)
                lista_viaggio.append(bambino_viaggio)
    #trovo quello con latitudine più grande
    #-> trovo massimo della latitudine

    primo_bambino=max(lista_viaggio,key=itemgetter('lat'))
   # print()
   # print(primo_bambino)
    #trovare il bambino con distanza minima
    #calcolare le distanze per ogni bambino -> trovare minimo

    bambino_attuale=primo_bambino
    while len(lista_viaggio)>0:
        print(f"Consegnato {bambino_attuale['regalo']} a {bambino_attuale['nome']} {bambino_attuale['cognome']} ({bambino_attuale['prov']})")
        for b in lista_viaggio:
                distanza=calcola_distanza(bambino_attuale['lat'],b['lat'],bambino_attuale['long'],b['long'])
                b['distanza']=distanza
        #print(lista_viaggio)
        lista_viaggio.remove(bambino_attuale)
        if len(lista_viaggio)>0:  # per gestire l'ultimo caso
            bambino_attuale= min(lista_viaggio,key=itemgetter('distanza'))
            print(f" Viaggio per {bambino_attuale['distanza']} km")




def main():
    l_b=leggi_bambini("bambini.csv")
    l_prov = leggi_province("province.csv")

    calcola_itinerario(l_b,l_prov)

main()
