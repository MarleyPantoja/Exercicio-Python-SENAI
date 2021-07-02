#Exercício_3
listanum = []
maiornum = 0
menornum = 0
for c in range(0, 20):
        listanum.append(int(input(f'Digite um valor para a Posição {c}:')))
        if c == 0:
            maiornum = menornum = listanum[c]
        else:
            if listanum[c] > maiornum:
                maiornum = listanum[c]
            if listanum[c] < menornum:
                menornum = listanum[c]

media = sum(listanum)/len(listanum)
print('=-' * 55)
print(f'O valor digitado: {listanum}')
print(f'O maior valor: {maiornum}')
print(f'O menor valor: {menornum}')
print('=-' * 55)
print(f'A média dos valores: {media}')