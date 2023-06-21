
def leggi_prodotti(nome_file):
    input_file = open(nome_file,"r",encoding="UTF-8")
    diz={}
    for linea in input_file:
        linea = linea.rstrip()
        campi=linea.split(" ")
        diz[campi[0]] = campi[1]
   # print(diz)
    input_file.close()
    return diz


def leggi_acquisti(nome_file):
    input_file = open(nome_file,"r",encoding="UTF-8")
    diz ={}

    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(" ")
        #print(campi)
        if campi[0] in diz.keys():
            #caso lettura successiva del prodotto
            diz[campi[0]].append(campi[1])
        else:
            #caso prima lettura del prodotto
            diz[campi[0]]=[]
            diz[campi[0]].append(campi[1])
    #print(diz)
    input_file.close()
    return diz

def controlla(diz_official,diz_acquisti):

    print("Elenco transazioni sospette\n")
    for prodotto in diz_acquisti.keys():
        rivenditore_ufficiale = diz_official[prodotto]
        lista_rivenditori = diz_acquisti[prodotto]
        #print(rivenditore_ufficiale,lista_rivenditori)
        if len(lista_rivenditori)>1 or rivenditore_ufficiale!= lista_rivenditori[0]:
            print(f"Codice prodotto: {prodotto}")
            print(f"Rivenditore ufficiale: {rivenditore_ufficiale}")
            print(f"Lista rivenditori: ",end="")
            for riv in lista_rivenditori:
                print(f"{riv} ",end="")
            print()
            print()




def main():
    diz_official=leggi_prodotti("prodotti.txt")
    diz_acquisti=leggi_acquisti("acquisti.txt")
    controlla(diz_official,diz_acquisti)


main()
