from operator import itemgetter


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
    #print(lista_prestiti)
    return lista_prestiti

def punto_uno(lista_prestiti):
    print("Elenco dei prestiti in corso:")
    lista_prestiti.sort(key=itemgetter('id_pers'))
    #print(lista_prestiti)
    for persona in lista_prestiti:
        print(f"{persona['id_pers']}:",end=" ")
        persona['lista_pc_in_prestito'].sort()
        #print(persona['lista_pc_in_prestito'])
        for pc in persona['lista_pc_in_prestito']:
            print(f" {pc}, " ,end=" ")
        print()
def punto_due(lista_pc,lista_prestiti):
    print("pc disponibili per il prestito",end=" ")
    lista_pc.sort()
    contPcDisponibili=0

    for pc in lista_pc:
        trovato=False
        for persona in lista_prestiti:
            for pc_in_uso in persona['lista_pc_in_prestito']:
                if pc == pc_in_uso:
                    trovato=True
        if not trovato:
            #pc disponibile
            print(pc,end=" ,")
            contPcDisponibili+=1
    if contPcDisponibili==0:
        print("Nessun PC disponibile")


def main():
    lista_pc = leggi_parcoPC("ParcoPC.txt")
    lista_prestiti=leggi_registrazioni("registrazioni.txt")

    punto_uno(lista_prestiti)
    punto_due(lista_pc,lista_prestiti)
main()
