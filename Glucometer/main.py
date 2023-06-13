from operator import itemgetter


def leggi_glucometers(nome_file):
    input_file = open(nome_file,"r",encoding="UTF-8")

    lista_pazienti=[]
    for linea in input_file:
        linea =linea.rstrip()
        campi= linea.split(" ")
       # print(campi)
        if int(campi[2])>=200:
            #verificato superamento
            #il paziente è già in lista?
            trovato=False
            for paziente in lista_pazienti:
                if paziente["ID"]==campi[0]:
                    #trovato paziente
                    trovato=True
                    paziente["ListaOra"].append(campi[1])
                    paziente["ListaGlicemia"].append(int(campi[2]))
                    paziente["cont"]+=1
            if not trovato:
                #non ho ancora letto quel paziente
                paziente={
                    "ID":campi[0],
                    "ListaOra":[],
                    "ListaGlicemia":[],
                    "cont":0
                }
                paziente["ListaOra"].append(campi[1])
                paziente["ListaGlicemia"].append(int(campi[2]))
                paziente["cont"]+=1
                lista_pazienti.append(paziente)
    print(lista_pazienti)
    input_file.close()
    return lista_pazienti

def stampa_pazienti(lista_pazienti):

    lista_pazienti.sort(key=itemgetter("cont"),reverse=True)
  #  print(lista_pazienti)
    for paziente in lista_pazienti:
            for i in range(0,paziente["cont"]):
                print(f"{paziente['ID']} {paziente['ListaOra'][i]} {paziente['ListaGlicemia'][i]} ")
            print("")
def main():
   lista_pazienti=leggi_glucometers("glucometers.txt")

   stampa_pazienti(lista_pazienti)

main()
