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
    print(lista_allarmi)
    return lista_allarmi


def main():

    lista_allarmi=leggi_allarmi('allarmi.csv')

main()
