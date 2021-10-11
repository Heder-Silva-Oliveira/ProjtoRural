pronta_meses = 14
entregetacao_meses = 2
gestacao_meses = 10
ciclo = int(12)
vacasini = 10
bezerras = {}
vacas = {}
tempo = 0
prazo = int(input("Quantos anos? ")) * 12
tempov = (type(ciclo/prazo))
tempob = (ciclo/prazo)
for x in range(10):
    bezerras[x] = 1

while tempo <= prazo:
    tempo += 1
    #Inicio do projeto com vacas emprenhadas
    if tempov == 12:
        x = bezerras[len(bezerras)]
        bezerras[x] = bezerras[len(bezerras)]
        for k in vacas.items():
            bezerras[x] = tempo


    #proxima leva de gado
    '''elif bezerras_totais > 0:
        if tempob == 14:
            vacas += bezerras_totais
            bezerras = bezerras_totais
            tempob = 0
            bezerras_totais = 0
        else:
            pass'''



'''print(prazo)'''
print(vacas)
print(bezerras)
'''print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')'''
