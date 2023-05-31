
def leggi_stabilimento(nome_file):
    input_file=open(nome_file,'r',encoding='UTF-8')
    lista_file=[]
    contatore_file=1
    for linea in input_file:
        linea=linea.rstrip()
        campi=linea.split(',')
        #print(campi)
        fila={
            'pos':contatore_file,
            'n_o':int(campi[0]),
            'c_o':int(campi[1]),
            'n_s':int(campi[2]),
            'c_s':int(campi[3])
        }
        contatore_file+=1
        lista_file.append(fila)
   # print(lista_file)
    input_file.close()
    return lista_file

def leggi_ingressi_uscite(nome_file,lista_file):
    input_file=open(nome_file,'r',encoding='UTF-8')
    lista_richieste=[]
    totale=0
    for linea in input_file:
        linea=linea.rstrip()
        campi=linea.split(',')
        #print(campi)
        if len(campi)==4:
            #ingresso
            richiesta_n_o=int(campi[1])
            richiesta_n_s=int(campi[2])
            richiesta_budget=int(campi[3])
            assegnato=False
            for fila in lista_file:
                #if può andar bene questa fila?
                preventito= richiesta_n_o*fila['c_o'] + richiesta_n_s*fila['c_s']
                if fila['n_o']>= richiesta_n_o and fila['n_s']>=richiesta_n_s and preventito<= richiesta_budget and not assegnato:
                   #richiesta soddisfatta
                    print(f"Il cliente {campi[0]} è in fila {fila['pos']}")
                    totale += preventito
                    assegnato=True
                    fila['n_o']-=richiesta_n_o
                    fila['n_s']-=richiesta_n_s
                    richiesta={
                        'n_o':richiesta_n_o,
                        'n_s':richiesta_n_s,
                        'nome':campi[0],
                        'fila':fila['pos'],
                    }
                    lista_richieste.append(richiesta)
                    #break; DA NON USARE

            if not assegnato:
                print(f"Il cliente {campi[0]} non ha trovato posto")

        else:
            #uscita
            print(f"Il cliente {campi[0]} è uscito")
            #Alba
            for richiesta in lista_richieste:
                if richiesta['nome']==campi[0]:
                    # prendere fila X e aggiornare i valori
                    fila_X = richiesta['fila']-1
                    lista_file[fila_X]['n_o'] += richiesta['n_o']
                    lista_file[fila_X]['n_s'] += richiesta['n_s']
    print(f"L'incasso della giornata è {totale}")
    input_file.close()

def main():
   lista_file = leggi_stabilimento('stabilimento.txt')

   leggi_ingressi_uscite('ingressi-uscite.txt',lista_file)

main()
