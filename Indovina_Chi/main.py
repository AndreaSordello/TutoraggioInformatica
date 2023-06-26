

def leggi_personaggi(nome_file):
    input_file = open(nome_file,"r",encoding='UTF-8')

    intestazione = input_file.readline()
    intestazione = intestazione.rstrip()
    campiIntestazione = intestazione.split(";")
   # print(campiIntestazione)

    lista_personaggi=[]
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split(";")
       # print(campi)
        personaggio={}
        for i in range(0,len(campi)):
            personaggio[campiIntestazione[i]]=campi[i]
        #print(personaggio)
        lista_personaggi.append(personaggio)
   # print(lista_personaggi)
    input_file.close()
    return lista_personaggi

def leggi_applica_domande(nome_file,lista_personaggi):
    input_file = open(nome_file,"r",encoding="UTF-8")
    contatore = 1
    for linea in input_file:
        linea = linea.rstrip()
        campi = linea.split("=")
        domanda = campi[0]
        risposta = campi[1]
      #  domanda,risposta = linea.split("=")
        print(f"\nMossa {contatore} - domanda:{domanda} = {risposta}")
        contatore+=1
        #gestione della domanda letta
        lista_personaggi_filtrata=[]
        for personaggio in lista_personaggi:
            if personaggio[domanda] == risposta:
                #lista_personaggi.remove(personaggio)
                lista_personaggi_filtrata.append(personaggio)

        #print(lista_personaggi_filtrata)
        lista_personaggi=lista_personaggi_filtrata
        for personaggio in lista_personaggi:
            stampa_personaggio(personaggio)
    if len(lista_personaggi) == 1:
        print("\nGioco terminato, hai vinto ! il personaggio selezionato è")
        stampa_personaggio(lista_personaggi[0])
    else:
        print("\nPeccato, hai perso :-(")

def stampa_personaggio(personaggio):
    print(f"{personaggio['Nome']} - ",end="" )
    for chiave in personaggio.keys():
        if chiave != "Nome":
            print(f"{chiave}:{personaggio[chiave]}, ",end ="")
    print()

def main():
      lista_personaggi=leggi_personaggi("personaggi.txt")
      print("Personaggi del gioco:")
      for personaggio in lista_personaggi:
          stampa_personaggio(personaggio)

      leggi_applica_domande("domande1.txt",lista_personaggi)

main()
