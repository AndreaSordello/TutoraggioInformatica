from operator import itemgetter


def leggi_viaggi(nome_file):
    file = open(nome_file,"r",encoding="UTF-8")
    lista=[]
    for linea in file:
        linea=linea.rstrip()
        campi = linea.split(",")
        d = {
            "luogo":campi[0],
            "durata": int(campi[1]),
            "passeggeri": int(campi[2])
        }
        lista.append(d)
    #print(lista)
    file.close()
    return lista
def leggi_pietre(nome_file):
    file = open(nome_file,"r",encoding="UTF-8")
    diz_pietre={}
    for linea in file:
        linea = linea.rstrip()
        campi = linea.split(",")
        #print(campi)
        diz_pietre[campi[0]] = campi[1:]
    #print(diz_pietre)
    file.close()
    return diz_pietre
def main():
    viaggi=leggi_viaggi("viaggi_nemo.txt")
    pietre = leggi_pietre("pietre_preziose_luoghi.txt")

    sumPasseggeri =0
    sumDurata=0
    for viaggio in viaggi:
        sumPasseggeri += viaggio["passeggeri"]
       #sumPasseggeri = sumPasseggeri + viaggio["passeggeri"]
        sumDurata += viaggio["durata"]
    media= sumDurata /len(viaggi)
    print(f"Durata media dei viaggi:{media:.1f}")
    print("Numero totale di passeggeri:",sumPasseggeri)
    print("Tipi di pietre preziose per luogo visitato:")
    diz_occorrenze={}
    for viaggio in viaggi:

        elenco = pietre[viaggio["luogo"]]

        stringa= ", ".join(elenco)
        print(f"- {viaggio['luogo']}: {stringa}")
        for pietra in elenco:
            if pietra not in diz_occorrenze:
                diz_occorrenze[pietra]=1
            else:
                diz_occorrenze[pietra]+=1
    #print(diz_occorrenze)

    lista=[]
    for elem in diz_occorrenze:
        lista.append({
            "pietra":elem,
            "occorrenza":diz_occorrenze[elem]
        })
    #print(lista)

    lista.sort(key=itemgetter("occorrenza"),reverse=True)
    #print(lista)
    comuni=[]
    for pietra in lista[0:3]:
        comuni.append(pietra["pietra"])
    #print(comuni)

    print("I tre tipi di pietre preziose più comuni:",", ".join(comuni))

main()



