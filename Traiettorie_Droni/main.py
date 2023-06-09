from math import sqrt
from operator import itemgetter


def leggi_stops(percorso_file):
    input_file=open(percorso_file,'r',encoding='UTF-8')
    lista_stops=[]

    for linea in input_file:
        linea=linea.rstrip()
        # A:0,1
        campi1=linea.split(':')
        #print(campi1)
        nome_stop = campi1[0]
        coordinate= campi1[1]
        campi2=coordinate.split(',')
       # print(campi2)
        x=campi2[0]
        y=campi2[1]
        diz={
            'nome':nome_stop,
            'x':int(x),
            'y':int(y)
        }
        lista_stops.append(diz)
    print(lista_stops)
    input_file.close()
    return lista_stops
def leggi_drones(percorso_file):
    input_file=open(percorso_file,'r',encoding='UTF-8')
    lista_drones=[]
    for linea in input_file:
        linea=linea.rstrip()
        campi1=linea.split(':')
        nome_drone=campi1[0]
        elenco=campi1[1]
        lista_stop=elenco.split(',')
        #print(lista_stop)
        dizionario={
            'nome':nome_drone,
            'lista_stop':lista_stop
        }
        lista_drones.append(dizionario)
    print(lista_drones)
    input_file.close()
    return lista_drones
def calcola_traiettorie(lista_stop,lista_drones):
    #per ogni drone devo calcolare la distanza percorsa
    lista_traiettorie=[]
    for drone in lista_drones:
        distanza=0
        elemento_precedente=drone['lista_stop'][0]

        for i in range(1,len(drone['lista_stop'])) :
            elemento_attuale = drone['lista_stop'][i]
            #distanza += (elemento_precedente,elemento_attuale)
            #print(elemento_precedente,elemento_attuale)

            #CERCO LE COORDINATE DEI PUNTI
            for stop in lista_stop:
                if stop['nome']==elemento_precedente:
                    x_prec=stop['x']
                    y_prec=stop['y']
                if stop['nome']==elemento_attuale:
                    x_attuale=stop['x']
                    y_attuale=stop['y']

            distanza += sqrt( (x_attuale-x_prec)**2 + (y_attuale-y_prec)**2 )

            print  (distanza)
            elemento_precedente=elemento_attuale

        print()
        print(distanza)
        n_stop=len(drone['lista_stop'])-1
        diz={
                'nome':drone['nome'],
                'distanza':distanza,
                'n_stop':n_stop,
                'rapporto':distanza/n_stop,
            }
        lista_traiettorie.append(diz)
    print(lista_traiettorie)

    massimo=max(lista_traiettorie,key=itemgetter('rapporto'))
    print(f"highest battery capacity for {massimo['nome']}")
    print(f"total distance = {massimo['distanza']}")
    print(f"number of stops = {massimo['n_stop']}")

def main():
   lista_stop = leggi_stops('stops.txt')
   lista_drones = leggi_drones('drones.txt')
   calcola_traiettorie(lista_stop,lista_drones)
main()
