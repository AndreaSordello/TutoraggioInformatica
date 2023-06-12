

def leggi_riviste(nome_file):

    input_file = open(nome_file,"r",encoding="UTF-8")

    input_file.readline()

    lista_riviste=[]
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(",")
       # print(campi)
        rivista = {"nome":campi[0],"ISSN":campi[1],"IF":campi[5]}
        lista_riviste.append(rivista)
    input_file.close()
    #print(lista_riviste)
    return lista_riviste

def leggi_calcola_ricercatore(cognome_ricercatore,lista_riviste):

    nome_file = cognome_ricercatore + ".csv"
   # print(nome_file)
    try:
        input_file = open(nome_file,"r",encoding="UTF-8")
    except:
        print("File non trovato")
        return;
    input_file.readline()
    total_IF = 0
    first_IF = 0
    cont_first =0
    last_IF =0
    cont_last=0
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split('"',maxsplit=3)
        print(campi)
        stringa_autori = campi[1]

        campi2 = linea.split(",")
        print(campi2)
        ISSN = campi2[-1]
        print(stringa_autori,ISSN)
        if ISSN != "":
            for rivista in lista_riviste:
                if rivista["ISSN"] == ISSN:
                    if rivista["IF"] != "N/A":

                        total_IF+=float(rivista["IF"])

                        lista_autori = stringa_autori.split(", ")
                        #print(lista_autori)

                        # autore primo
                        autore_primo = lista_autori[0]
                        cognome_primo = autore_primo.split(" ")[0]

                        if cognome_primo == cognome_ricercatore:
                            first_IF+=float(rivista["IF"])
                            cont_first+=1
                        #autore ultimo
                        autore_ultimo = lista_autori[-1]  # lista_autore[len(lista_autore)-1]
                        cognome_ultimo = autore_ultimo.split(" ")[0]
                        if cognome_ultimo== cognome_ricercatore:
                            last_IF+=float(rivista["IF"])
                            cont_last+=1




    print(f"total IF di ricercatore {cognome_ricercatore}:{total_IF:.2f}")
    print(f"Total IF come primo autore: {first_IF} ({cont_first} pubblicazioni)")
    print(f"Total IF come ultimo autore: {last_IF} ({cont_last} pubblicazioni)")


def main():

    lista_riviste=leggi_riviste("Journal_IF.csv")

    print("Inserisci il nome del ricercatore:")
    cognome_ricercatore=input()
    leggi_calcola_ricercatore(cognome_ricercatore,lista_riviste)

main()
