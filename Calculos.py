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


cont = 1
while tempo < prazo:
    tempo += 1
    #Inicio do projeto com vacas emprenhadas
    for x in range(vacasini):
        vacas[x] = tempo
        for i in vacas.values():
            resultado = int(vacas[x] / 12)
            if resultado == cont:
                cont += 1
                outra = {cont-2: 0}
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


print(resultado)
print(outra)
print(cont)
print(vacas)
print(bezerras)
'''print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')'''
