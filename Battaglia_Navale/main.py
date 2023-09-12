#lettere ={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
lettere =["A","B","C","D","E","F","G","H","I","J"]
def read_data(nome_file):
    file = open (nome_file,"r",encoding="UTF-8")
    linee = file.readlines()

    tabella = []
    for linea in linee:
        linea = linea.rstrip()
        celle = linea.split(",")
        tabella.append(celle)

    file.close()
    return tabella

def leggi_mosse(nome_file):
    file = open (nome_file,"r",encoding="UTF-8")
    linee = file.readlines()
    lista=[]
    for linea in linee:
        linea = linea.rstrip()
        campi = linea.split(",")

        d = {
            "r": campi[0],
            "c": campi[1]
        }
        lista.append(d)

    file.close()
    return lista

def tabella_vuota():
    tab = []
    for i in range(0,10):
        riga=[]
        for j in range(0,10):
            riga.append('')
        tab.append(riga)
    return tab

def playround(tab_game,mossa,tab_navi):
   # lettere =["A","B","C"]
   # r= lettere.index("A")

    r = lettere.index(mossa["r"])
    c = int(mossa["c"])-1

    if tab_navi[r][c] != '':
        print("Colpito")
        tab_game[r][c] = "*"
    else:
        print("Acqua")
        tab_game[r][c] = "o"

def stampa_matrice(tabella):
    print("  |",end="")
    for i in range(1,11):
        print(f"{i:2}|",end="")
    print()
    for j in range(0,11):
            print("___",end="")
    print()
    for i in range (0,10):
        print(f"{lettere[i]} |",end="")
        for j in range(0,10):
            print(f"{tabella[i][j]:2}|",end="")
        print()
        for j in range(0,11):
            print("___",end="")
        print()

def check_affondate(tab_game,tab_navi):
    for i in range(0,10):
        for j in range(0,10):
            if tab_navi[i][j] != '' and tab_game[i][j] == "":
                return False
    return True


def main():

    tab1 = read_data("nave1.txt")
    tab2 = read_data("nave2.txt")
    mosse= leggi_mosse("mosse.txt")

    tab1_game =tabella_vuota()
    tab2_game =tabella_vuota()
    #print(tab1_game)
    i = 0
    fine = False
    while i <len(mosse) and not fine:
        giocatore = (i % 2)+1
        print("E' il turno del giocatore",giocatore)
        print(f"Coordinate dell'attacco: {mosse[i]['r']} , {mosse[i]['c']}")
        if giocatore == 1:
            playround(tab2_game,mosse[i],tab2)
            stampa_matrice(tab2_game)
            if check_affondate(tab2_game,tab2):
                print("Giocatore 1 ha vinto")
                fine =True
        else:
            playround(tab1_game,mosse[i],tab1)
            stampa_matrice(tab1_game)
            if check_affondate(tab1_game,tab1):
                print("Giocatore 2 ha vinto")
                fine=True
        i+=1

    if fine == False:
        print("partita sospesa")
main()
