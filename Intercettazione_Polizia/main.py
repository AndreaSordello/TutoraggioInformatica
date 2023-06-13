


def leggi_intercettazione(nome_file):
    input_file = open (nome_file,"r",encoding="UTF-8")
    lista_righe=[]
    for linea in input_file:

        lista_righe.append(linea)
  #  print(lista_righe)
    input_file.close()
    return lista_righe
def censura(lista_righe,nome_file_output):

    lista_indici_vietati =[]

    #for riga in lista_righe:
    for i in range(0,len(lista_righe)):
        if "bob" in lista_righe[i] or "arctor" in lista_righe[i]:
            lista_indici_vietati.append(i)
            lista_indici_vietati.append(i+1)
            lista_indici_vietati.append(i+2)
            lista_indici_vietati.append(i-1)
            lista_indici_vietati.append(i-2)
    #print(lista_indici_vietati)

    lista_righe_censurato=[]
    for i in range(0,len(lista_righe)):
        if i not in lista_indici_vietati:
            lista_righe_censurato.append(lista_righe[i])
    #print(lista_righe_censurato)

    output_file = open(nome_file_output,"w",encoding="UTF-8")

    output_file.writelines(lista_righe_censurato)
    output_file.close()

def calcola_distanza(lista_righe):
    lista_polizia=[]
    lista_bob_arctor=[]

    for i in range(0,len(lista_righe)):
        if "bob" in lista_righe[i] or "arctor" in lista_righe[i]:
            lista_bob_arctor.append(i)
        if "polizia" in lista_righe[i]:
            lista_polizia.append(i)

   # print(lista_polizia,lista_bob_arctor)
    first=True
    for indicePol in lista_polizia:
        for indiceBob in lista_bob_arctor:
            distanza= abs(indicePol-indiceBob)
            #print(distanza)
            if first:
                min =distanza
                first=False

            if distanza< min:
                min=distanza
    if first:
        print("La parola polizia non è mai stata pronunciata insieme al nome")
    else:
        print(f"la parola polizia è stata pronunciata a {min} righe di distanza dal nome")
def main():
    lista_righe=leggi_intercettazione("intercettazione.txt")

    censura(lista_righe,"censurato.txt")
    calcola_distanza(lista_righe)


main()
