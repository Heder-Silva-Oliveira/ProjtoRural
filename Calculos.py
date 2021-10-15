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
    for x, z in bezerras.items():
        bezerras[x] = tempo
    for k, i in bezerras.items():
        resultado = int(bezerras[k] / 14)
        acr = len(vacas)
        # Adicionando bezerras
        if len(bezerras) > len(vacas):
            break
        elif resultado == resultado:
            outra = {acr: resultado}
            vacas.update(outra)
        else:
            pass



print(outra)
print(vacas)
print(bezerras)
'''print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')'''
