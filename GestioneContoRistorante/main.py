def leggi_menu(nome_file):
    input_file=open(nome_file,'r',encoding='UTF-8')
    menu=[]
    for linea in input_file:
        linea=linea.rstrip()
       #print(linea)
        campi=linea.split(',')
        piatto =  {
            'ID':campi[0],
            'nome':campi[1],
            'prezzoConIVA': float(campi[2]),
            'percIVA': int(campi[3])
        }
        menu.append(piatto)
    input_file.close()
    return menu
def leggi_ordine(nome_file):
    input_file=open(nome_file,'r',encoding='UTF-8')
    ordine=[]
    for linea in input_file:
        linea=linea.rstrip()
        campi=linea.split(',')
        elemento={
            'ID':campi[0],
            'qt':int(campi[1]),
        }
        ordine.append(elemento)
    input_file.close()
    return ordine

def calcolaRicevuta(menu,ordine):

    ricevuta=[]
    for o in ordine:
        for m in menu:
            if o['ID']==m['ID']:
               #per ogni ordine calcolare i costi tenendo conto dell'iva
                costoOrdineConIva=o['qt']*m['prezzoConIVA']
                IVAordine = (m['prezzoConIVA'] * m['percIVA']/100) * o['qt']
                ordineCalcolato={
                    'nome':m['nome'],
                    'qt':o['qt'],
                    'costoOrdineConIva':costoOrdineConIva,
                    'IVAordine':IVAordine,
                    'percIVA':m['percIVA']
                }
                ricevuta.append(ordineCalcolato)
    print(ricevuta)

def main():
    menu=leggi_menu('menu.txt')
    ordine=leggi_ordine('ordine.txt')
    print(menu)
    print(ordine)
    calcolaRicevuta(menu,ordine)

main()
