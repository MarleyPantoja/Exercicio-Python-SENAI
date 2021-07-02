#Exercício_2
valores = []

for c in range(1, 5):
        valores.append(int(input(f'Digite um valor de 0 a 10= {c}:')))

soma_valores = sum(valores)

media_valores = soma_valores / 4
print('-'*50)
print(f'A média é: {media_valores}')

if media_valores >=7:
    print('Essa média é  acima de 7 = Aprovado')
else:
    print('Essa média é  abaixo de 7 = Reprovado')