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

def main():

    lista_allarmi=leggi_allarmi('allarmi.csv')

    conta_allarmi(lista_allarmi)

main()
