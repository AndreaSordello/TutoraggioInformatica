from operator import itemgetter

def leggi_allarmi(nome_file):
    input_file=open(nome_file,'r',encoding='UTF-8')

    input_file.readline() #legge l'intestazione
    lista_allarmi=[]
    for linea in input_file:
        linea=linea.rstrip()
        campi=linea.split(';')
       #print(campi)
        allarme={
            'id':campi[0],
            'sev':int(campi[1])
        }
        lista_allarmi.append(allarme)
   # print(lista_allarmi)
    input_file.close()
    return lista_allarmi

def conta_allarmi(lista_allarmi):

    lista_contatore=[]

    for allarme in lista_allarmi:
        trovato=False
        for cont in lista_contatore:
            if allarme['id']==cont['id']:
                trovato=True
                cont['n']+=1
        if not trovato:
            cont ={
                'id':allarme['id'],
                'n':1
            }
            lista_contatore.append(cont)
   # print(lista_contatore)

    lista_contatore.sort(key=itemgetter('n'),reverse=True)
   # print(lista_contatore)
    for robot in lista_contatore:
        print(f"Per il robot {robot['id']} si sono verificati {robot['n']} allarmi ")

def severita_massima(lista_allarmi):

    #1 cercare qual'è questa severita
    massimo = max(lista_allarmi,key=itemgetter('sev'))
    #print(massimo)
    severita_max = massimo['sev']
    print(f"Il livello massimo di severità {severita_max} è stato raggiunto dai seguenti robot:")
    #2 cercare tutti i robot con quella severita
    lista_robot_severita_massima=[]
    for allarmi in lista_allarmi:
        if (allarmi['sev']==severita_max):
            if (allarmi['id'] not in lista_robot_severita_massima):
                lista_robot_severita_massima.append(allarmi['id'])

    for robot in lista_robot_severita_massima:
             print(robot)

def main():

    lista_allarmi=leggi_allarmi('allarmi.csv')
    conta_allarmi(lista_allarmi)

    severita_massima(lista_allarmi)

main()
