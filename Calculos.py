pronta_meses = 14
entregetacao_meses = 2
gestacao_meses = 10
ciclo = int(12)
vacasini = 10
cont = cont2 = 0
bezerras = {}
vacas = {}
novilha = {}
tempo = outra = 0
prazo = int(input("Quantos anos? ")) * 12
numero = len(bezerras)

for x in range(vacasini):
    vacas[x] = -1
tempv = 0
while tempo < prazo:
    tempo += 1
    #Inicio do projeto com vacas emprenhadas
    for x in range(vacasini):
        vacas[x] += 1
        if vacas[x] >= 11:
            cont += 1
            outra = {cont: cont2}
            novilha.update(outra)
            vacas[x] = 1
            #print('oi')
        else:
            pass
    todas = len(vacas)
    for y in range(1, todas):
        novilha[y] = -1
    ou = len(novilha)
    for q, w in novilha.items():
        novilha[q] += 1
        if novilha[q] == 14:
            cont += 1
            out = {cont: cont2}
            bezerras.update(out)
        if novilha[q] >= 15:
            novilha.pop(q, 14)
        else:
            pass
    #print(vacas)
#proxima leva de gado
'''for x, z in novilha.items():
    novilha[x] += 1
    resultado = int(novilha[x] / 14)
    acr = len(vacas)
    # Adicionando bezerras
    if resultado == cont:
        cont += 1
        outra1 = {acr: cont}
        novilha.update(outra1)
    if x == 14:
        novilha[x] = 0
    else:
        pass'''



#print(outra)
print(len(vacas))
print(len(novilha))
print(len(bezerras))
'''print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')'''
