from operator import itemgetter


def leggi_lingue(nome_file):

    file = open(nome_file,"r",encoding="UTF-8")
    lingue = {}
    linee = file.readlines()
    for linea in linee:
        linea = linea.rstrip()
        campi = linea.split(",")

        lingue[campi[0]] = campi[1:]

    file.close()
    return lingue

def leggi_viaggi(nome_file):
    file = open(nome_file,"r",encoding="UTF-8")
    linee= file.readlines()
    viaggi=[]
    for linea in linee:
        linea = linea.rstrip()
        campi = linea.split(",")
        viaggio ={
            "pianeta" : campi[0],
            "durata": int(campi[1]),
            "passeggeri":int (campi[2])
        }
        viaggi.append(viaggio)

    return viaggi

def elabora(viaggi,lingue):
    contaPassegeri=0
    contaDurata=0
    for viaggio in viaggi:
        contaPassegeri += viaggio["passeggeri"]
        contaDurata += viaggio["durata"]

    print("Durata media dei viaggi:",contaDurata/len(viaggi))
    print("Numero totale di passeggeri:",contaPassegeri)

    print( "Lingue parlate su ciascun pianeta visitato:")
    diz_lingue={}
    for viaggio in viaggi:
        print(f'{viaggio["pianeta"]} : {lingue[viaggio["pianeta"]]}')
        for lingua in lingue[viaggio["pianeta"]]:
            if lingua in diz_lingue:
                diz_lingue[lingua]+=1
            else:
                diz_lingue[lingua]=1


    lista =[]
    for lingua in diz_lingue.keys():
        diz = {
            "nome":lingua,
            "cont":diz_lingue[lingua]
        }
        lista.append(diz)

    lista.sort(key=itemgetter("cont"),reverse=True)


    print( "Tre lingue più ricorrenti tra i pianeti visitati: [",end='')

    for i in range(0,2):
        print(f"'{lista[i]['nome']}', ",end='')
    print(f"'{lista[2]['nome']}'",end='')
    print("]")


def main():
    lingue=leggi_lingue("lingue_pianeti.txt")
    viaggi=leggi_viaggi("viaggi_enterprise.txt")
    elabora(viaggi,lingue)
main()




