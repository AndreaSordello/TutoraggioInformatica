
def leggi_parcoPC(nome_file):
    input_file=open(nome_file,"r",encoding='UTF-8')
    linee = input_file.readlines()
    lista_pc=[]
    for linea in linee:
        linea=linea.rstrip()
        lista_pc.append(linea)
    #print(lista_pc)
    input_file.close()
    return lista_pc

def leggi_registrazioni(nome_file):
    input_file=open(nome_file,"r",encoding='UTF-8')
    linee = input_file.readlines()
    lista_prestiti=[]
    for linea in linee:
        linea=linea.rstrip()
        campi= linea.split(":")
        print(campi)
        #DAL FILE -> id_pc , id_persona, data
        #STRUTTURA  -> id_persona , lista_pc_in_prestito
        #esiste già la persona che ho appena letto?
        trovato=False
        for persona in lista_prestiti:
            if (campi[1]==persona['id_pers']):
                #ho trovato la persona
                trovato=True
                # devo controllare i suoi prestiti
                #controllare se campi[0] è già presente (quindi restituzione) oppure
                #è un prestito nuovo( non presente)
                trovatoPC=False
                for pc in persona['lista_pc_in_prestito']:
                    if (pc==campi[0]):
                        #è una restituzione
                        trovatoPC=True
                        persona['lista_pc_in_prestito'].remove(campi[0])
                if trovatoPC==False:
                    #è un prestito
                    persona['lista_pc_in_prestito'].append(campi[0])

        if trovato==False:
            #persona è nuova, va aggiunta
            persona_nuova={'id_pers':campi[1],'lista_pc_in_prestito': []}
            persona_nuova['lista_pc_in_prestito'].append(campi[0])
            lista_prestiti.append(persona_nuova)
    print(lista_prestiti)
def main():
    lista_pc = leggi_parcoPC("ParcoPC.txt")
    leggi_registrazioni("registrazioni.txt")

main()
