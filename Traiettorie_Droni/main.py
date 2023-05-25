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

def main():
   lista_stop= leggi_stops('stops.txt')
   leggi_drones('drones.txt')

main()
