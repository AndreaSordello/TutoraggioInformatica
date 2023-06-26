import random


def leggi_carte(nome_file):
    input_file = open(nome_file,"r",encoding="UTF-8")
    lista_carte=[]
    for linea in input_file:
        linea = linea.rstrip()
        lista_carte.append(linea[1]+linea[0])
    #print(lista_carte)
    return lista_carte
def stampa_tavolo(tavolo):
    for i in range(0,4):
        for j in range (0,9):
            print(tavolo[i][j],end=" ")
        print()


def partita(tavolo,mazzetto):
    semi = ["D","S","B","C"]
    for carta in mazzetto:
        print(f"pesco carta {carta}")
        while "K" not in carta:

            #carta è una stringa con 2 elementi SEME|NUMERO
            colonna = int(carta[0])-1
            seme = carta[1]
            riga = semi.index(seme)

            temp= tavolo[riga][colonna]
            tavolo[riga][colonna] = carta
            carta=temp
        print(f"è stata trovata la carta {carta}, il risultato è il seguente:")
        stampa_tavolo(tavolo)
        print()


    if controlla_vittoria(tavolo):
        print("Gioco finito, hai vinto! :)")
    else:
        print("Gioco finito, hai perso! :(")

def controlla_vittoria(tavolo):
    semi = ["D","S","B","C"]
    ok=True
    for i in range(0,4):
        for j in range(0,9):
            carta = tavolo[i][j]
            carta_giusta =str(j+1) +semi[i]
            if carta!=carta_giusta:
                ok=False
    return ok
def main():
    lista_carte=leggi_carte("carte.txt")

    random.shuffle(lista_carte)


    tavolo =[lista_carte[0:9],
             lista_carte[9:18],
             lista_carte[18:27],
             lista_carte[27:36]
            ]
    print("carte sul tavolo:")
    stampa_tavolo(tavolo)
    mazzetto=lista_carte[36:40]

    partita(tavolo,mazzetto)

main()
