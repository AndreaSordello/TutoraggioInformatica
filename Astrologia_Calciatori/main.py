from operator import itemgetter


def leggi_zodiaco(nome_file):
    input_file = open(nome_file,"r",encoding="UTF-8")
    lista_zodiaco=[]
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(",")
       # print(campi)
        data = campi[1].split("/")
        dataInizio = data[1] + data[0]
        data = campi[2].split("/")
        dataFine = data[1]+data[0]

        zodiaco = {
            "segno":campi[0],
            "inizio":dataInizio,
            "fine":dataFine,
            "count":0,
        }
        lista_zodiaco.append(zodiaco)
    input_file.close()
    #print(lista_zodiaco)
    return lista_zodiaco

def leggi_calciatori(nome_file,lista_zodiaco):
    input_file = open(nome_file,"r",encoding="UTF-8")

    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(",")
        gol = int(campi[1])

       # print(campi[3])
        data = campi[3].split("/")
        dataNascita= data[1] + data[0]
        #print(dataNascita)

       # assegnato=False   #se si cerca il capricorno
        for segno in lista_zodiaco:
            if dataNascita>= segno["inizio"] and dataNascita<=segno["fine"]:
               # print(segno["segno"])
                #HO TROVATO IL SEGNO
                segno["count"] += gol
              #  assegnato=True
            if segno["segno"]=="Capricorno":
                if dataNascita<=segno["fine"] or dataNascita>=segno["inizio"]:
                   # print(segno["segno"])
                    #HO TROVATO IL SEGNO
                    segno["count"] += gol
         #if assegnato==False:
        #    print("Assegnato capricorno")
    #print(lista_zodiaco)


    lista_zodiaco.sort(key=itemgetter("count"),reverse=True)
    #num_max : 50 = num_gol : num_asterischi
    #num_asterischi = 50*num_gol/num_max

    fattoreRiscalamento = 50 /lista_zodiaco[0]["count"]

    for segno in sorted(lista_zodiaco,key=itemgetter("count"),reverse=True):


        print(f"{segno['segno']:<10} ({segno['count']})",end=" ")
        print("*"*round(segno["count"]*fattoreRiscalamento))




def main():
    lista_zodiaco=leggi_zodiaco("zodiaco.csv")
    leggi_calciatori("sportivi.csv",lista_zodiaco)
main()
