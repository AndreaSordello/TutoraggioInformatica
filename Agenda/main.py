from operator import itemgetter

def leggi_agenda(nome_file):
    input_file= open(nome_file,"r",encoding="UTF_8")
    print(input_file)
    righe= input_file.readlines()
    #print(righe)
    agenda=[]
    
    for riga in righe:
        riga=riga.rstrip()
        campi=riga.split(";")
        #print(campi)
        evento={
            "giorno":campi[0],
            "ora": int(campi[1]),
            "desc": campi[2]
        }
        #print(evento)
        agenda.append(evento)
    return agenda
def visualizza_giorno(giorno,agenda):
    listaVisualizza=[]
    for evento in agenda:
        if evento["giorno"]==giorno:
            #print(evento)
            listaVisualizza.append(evento)
    listaVisualizza.sort(key=itemgetter("ora"))
        #print(listaVisualizza)
    for elemento in listaVisualizza:
         print(f"giorno {elemento['giorno']} ora {elemento['ora']:02d}: {elemento['desc']}")

def leggi_comandi(nome_file_comandi,agenda):
    input_file_comandi=open(nome_file_comandi,"r",encoding="UTF-8")
    righe= input_file_comandi.readlines()
    #print(righe)
    for riga in righe:
        riga=riga.rstrip()
        campi=riga.split(" ",maxsplit=3)

        #print(campi)
        if campi[0]=='v':
            #visualizza
            visualizza_giorno(campi[1],agenda)
        else:
                #inserisci
           # print("inserisci")
            trovato=False
            for evento in agenda:
                if evento["giorno"]== campi[1] and evento["ora"]==int(campi[2]):
                    trovato=True

            if trovato==False:
                #inserisco
                print("Appuntamento inserito correttamente")
                eventoNuovo={
                    "giorno":campi[1],
                    "ora":int(campi[2]),
                    "desc":campi[3]
                }
                agenda.append(eventoNuovo)
                visualizza_giorno(campi[1],agenda)
            else:
                #impossibile inserire
                print("Impossibile inserire appuntamento")


def main():
      agenda=leggi_agenda("agenda.txt")
      leggi_comandi("comandi.txt",agenda)
main()

