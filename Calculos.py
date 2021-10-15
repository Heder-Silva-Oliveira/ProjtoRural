pronta_meses = 14
entregetacao_meses = 2
gestacao_meses = 10
ciclo = int(12)
vacasini = 5
bezerras = {}
vacas = {}
tempo = outra = 0
prazo = int(input("Quantos anos? ")) * 12
numero = len(bezerras)


while tempo < prazo:
    tempo += 1
    #Inicio do projeto com vacas emprenhadas
    for x in range(vacasini):
        vacas[x] = tempo
    for k, i in vacas.items():
        resultado = int(vacas[k] / 12)
    #Adicionando bezerras
        if resultado == resultado:
            outra = {k: resultado}
            bezerras.update(outra)

        else:
            pass

    #proxima leva de gado
    '''elif bezerras_totais > 0:
        if tempob == 14:
            vacas += bezerras_totais
            bezerras = bezerras_totais
            tempob = 0
            bezerras_totais = 0
        else:
            pass'''



print(outra)
print(vacas)
print(bezerras)
'''print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')'''
