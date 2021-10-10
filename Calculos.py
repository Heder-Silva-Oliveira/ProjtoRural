pronta_meses = 14
entregetacao_meses = 2
gestacao_meses = 10
ciclo = 12
vacas = 10
bezerras_totais = tempov = bezerras = tempob = tempo = 0
prazo = int(input("Quantos anos? ")) * 12


while tempo <= prazo:
    tempo += 1
    tempob += 1
    tempov += 1
    #Inicio do projeto com vacas emprenhadas
    if tempov == 10:
        bezerras_totais = vacas
        tempov = -2
    elif bezerras_totais > 0:
        if tempob == 14:
            vacas += bezerras_totais
            bezerras = bezerras_totais
            tempob = 0
            bezerras_totais = 0
        else:
            pass
    else:
        pass


print(prazo)
print(tempo)
print(f'Quantiade de vacas {vacas}')
print(f'Quantiade e bezerras {bezerras}')
