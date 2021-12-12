pronta_meses = 14
entregetacao_meses = 2
gestacao_meses = 10
ciclo = int(12)
vacasini = 10
cont = cont2 = cont3 = 0
bezerras = {}
vacas = {}
novilha = {}
tempo = outra = 0
prazo = int(input("Quantos anos? ")) * 12
numero = len(bezerras)

for x in range(vacasini):
    vacas[x] = 0
tempv = 0
raz = 12
taok = 0
while tempo < prazo:
    tempo += 1
    #Inicio do projeto com vacas emprenhadas
    for x in range(vacasini):
        vacas[x] += 1
        taok += 1
        if vacas[x] == raz:
            for r in vacas:
                cont += 1
                outra = {cont - 1: 0}
                novilha.update(outra)
            raz += 12
            print(raz)
        else:
            pass
    if tempo >= 13:
        for q, w in novilha.items():
            novilha[q] += 1
            if novilha[q] == 14:
                cont3 += 1
                out = {cont3 - 1: cont2}
                bezerras.update(out)


print(vacas)
print(novilha)
print(bezerras)
