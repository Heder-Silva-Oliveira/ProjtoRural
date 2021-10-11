pronta_meses = 14
entregetacao_meses = 2
gestacao_meses = 10
ciclo = int(12)
vacasini = 10
bezerras = {}
vacas = {}
tempo = 0
prazo = int(input("Quantos anos? ")) * 12
tempov = tempo
tempob = tempo
ran = 10

while tempo < prazo:
    tempo += 1
    #Inicio do projeto com vacas emprenhadas
    for x in range(ran):
        vacas[x] = tempo
        for i in vacas.values():
            if vacas[x] == 12:
                vacas[x] = 0


    for y in range(10):
        bezerras[y] = tempo





    #proxima leva de gado
    '''elif bezerras_totais > 0:
        if tempob == 14:
            vacas += bezerras_totais
            bezerras = bezerras_totais
            tempob = 0
            bezerras_totais = 0
        else:
            pass'''



print(tempo)
print(vacas)
print(bezerras)
'''print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')'''
