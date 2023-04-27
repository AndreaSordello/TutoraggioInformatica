

from operator import itemgetter


def main():
    infile = open("costipagine.txt","r",encoding="UTF-8")
   # print(infile)
    righe= infile.readlines()
    infile.close()
    #print(righe)
    listino=[]
    for riga in righe:   #for i in range(0,len(righe))
        #print(riga)
        riga=riga.rstrip()

        campi = riga.split(";")
        #print(campi)
        fascia={
            "n_min" : int(campi[0]),
            "n_max" : int(campi[1]),
            "prezzo" : float(campi[2].rstrip("€")),
        }
        listino.append(fascia)
       # print(fascia)
    #print(listino)

    listino.sort(key=itemgetter('n_min'))   #listino.sort('n_min')
   # print(listino)
    print("LISTINO PREZZI")
    for elemento in listino:
        print(f"Fino a {elemento['n_max']} pagine :  {elemento['prezzo']} €/pagina")

    print("Inserisci nome file libri: ")
    nome_file=input()
    file_libri=open(nome_file,"r",encoding="UTF-8")
    righe_libri= file_libri.readlines()
    #print(righe_libri)
    elenco_libri=[]
    for riga_libri in righe_libri:
        riga_libri=riga_libri.rstrip()
        campi = riga_libri.split(";")
        libro={
            "titolo":campi[0],
            "n_pag":int(campi[1])
        }
        #print(libro)
        elenco_libri.append(libro)
   #print(elenco_libri)

    elenco_libri.sort(key=itemgetter("titolo"))
    print("COSTI STAMPA")
    totale=0
    for libro in elenco_libri:
        for fascia in listino:
            if libro["n_pag"] >= fascia["n_min"] and libro["n_pag"]<= fascia["n_max"]:

                costolibro= fascia["prezzo"] * libro["n_pag"]
               #print(libro["titolo"]," ", costolibro)
                print(f"{libro['titolo']} - Pagine: {libro['n_pag']} - Costo {costolibro:.2f} €")
                totale += costolibro
    print(f"Totale : {totale:.2f}")
    file_libri.close()


main()
