pronta_meses = 14
entregetacao_meses = 2
gestacao_meses = 10
ciclo = int(12)
vacasini = 10
cont = cont2 = 1
bezerras = {}
vacas = {}
tempo = outra = 0
prazo = int(input("Quantos anos? ")) * 12
numero = len(bezerras)

for x in range(vacasini):
    vacas[x] = 1
tempv = 0
while tempo < prazo:
    tempo += 1
    #Inicio do projeto com vacas emprenhadas
    for x in range(vacasini):
        vacas[x] += 1
        if vacas[x] >= 12:
            vacas[x] = 1
    print(vacas)

    for k, i in vacas.items():
        resultado = int(vacas[k] / 12)
        tempv += 1
    #Adicionando bezerras
        if resultado in range(1, 50):
            outra = {cont: cont2}
            bezerras.update(outra)

    else:
        pass
#proxima leva de gado
    for x, z in bezerras.items():
        bezerras[x] += 1
        if x == 14:
            bezerras[x] = 0
    for k, i in bezerras.items():
        resultado = int(bezerras[k] / 14)
        acr = len(vacas)
        # Adicionando bezerras
        if resultado == cont2:
            cont2 += 1
            outra = {acr: resultado}
            vacas.update(outra)
        else:
            pass



#print(outra)
print(vacas)
print(bezerras)
'''print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')'''
