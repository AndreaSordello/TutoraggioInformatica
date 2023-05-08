
def leggi_dati_esame(nome_file):
    infile= open(nome_file,'r',encoding='UTF-8')
    linee= infile.readlines()
    print(linee)
    lista_esami=[]
    for linea in linee:

        linea= linea.rstrip()
        print(linea)
        campi=linea.split(",")
        print(campi)
        esame = {
            'codice' : campi[0],
            'cfu' :campi[1],
            'obb': campi[2],
        }
        print(esame)
        lista_esami.append(esame)
    print(lista_esami)
    infile.close()
    return lista_esami
def main():
    lista_esami=leggi_dati_esame("cfu.dati")


main()
