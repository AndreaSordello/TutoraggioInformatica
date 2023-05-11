
def leggi_dati_esame(nome_file):
    infile= open(nome_file,'r',encoding='UTF-8')
    linee= infile.readlines()
   # print(linee)
    lista_esami=[]
    for linea in linee:
        linea= linea.rstrip()
       # print(linea)
        campi=linea.split(",")
       # print(campi)
        esame = {
            'codice' : campi[0],
            'cfu' :campi[1],
            'obb': campi[2],
        }
        #print(esame)
        lista_esami.append(esame)
    #print(lista_esami)
    infile.close()
    return lista_esami



def leggi_log_esami(nome_file):
    input_file= open(nome_file,'r',encoding='UTF-8')
    righe= input_file.readlines()
    lista_carriere=[]
    for riga in righe:
       # print(riga)
        riga=riga.rstrip()
        campi=riga.split(',')
       #print(campi)
        # campi[0] -> matricola
        #la matricola esiste già nella lista?
        trovato=False
        for carriera in lista_carriere:
            if carriera['matricola']==campi[0]:
                trovato=True
                #la matricola è già presente nella lista -> aggiungere l'esame se passato
                if not( campi[3] == 'A' or  campi[3]=='R'):
                    #esame passato

                    carriera['lista_esami'].append({ 'codice': campi[2] , 'voto': campi[3]})


        if not trovato:
            #prima volta che trovo quella matricola
            carriera={
                'matricola': campi[0],
                'lista_esami':[]
            }
            if ( campi[3] != 'A' and  campi[3]!='R'):
                #entro se esame valido
                carriera['lista_esami'].append({ 'codice': campi[2] , 'voto': campi[3]})  # campi[2] -> sigla, campi[3] -> voto
            lista_carriere.append(carriera)

    #print(lista_carriere)
    return lista_carriere

def verifica_requisiti(lista_car,lista_esami):

    #prendi uno studente e calcola le sue informazioni
    for studente in lista_car:
        print(f"STUDENTE {studente['matricola']}")
        cfutotali=0
        cfutotaliobbl=0
        sommavoti=0         # conterrà voto*cfu + voto*cfu ....
        for esame in studente['lista_esami']:
            # esame sostenuto dallo studente
            #-> trovare informazioni di quell'esame
            for esameL in lista_esami:
                if (esameL['codice']==esame['codice']):
                    #ho trovato le informazioni dell'esame sostenuto
                   # print(esameL)
                    cfutotali+=int(esameL['cfu'])
                    if esameL['obb']=='1':   # '0' != 0 -> True
                        cfutotaliobbl+=int(esameL['cfu'])

                    if esame['voto']=='30L':
                        sommavoti += int(esameL['cfu'])* 33
                    else:
                        sommavoti += int(esameL['cfu'])* int(esame['voto'])

        #print(cfutotali)
       # print(cfutotaliobbl)
        #print(sommavoti/cfutotali)
        media=sommavoti/cfutotali
        if cfutotali >= 30 and cfutotaliobbl>=10:
            #laurea
            print(f"Studente con {cfutotali} CFU totali; {cfutotaliobbl} CFU obbligatori;{media:.2f} di media")
        else:
            print(f"Studente con {cfutotali} CFU totali; {cfutotaliobbl} CFU obbligatori;{media:.2f} di media; no laurea")

def main():

    lista_esami=leggi_dati_esame("cfu.dati")

    lista_carriere=leggi_log_esami("esami.log")

    verifica_requisiti(lista_carriere,lista_esami)

main()
