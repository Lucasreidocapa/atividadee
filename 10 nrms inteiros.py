soma = 0
for c in range(1,4):
    numero= int(input(f'digite o valor: '))
    
    if numero % 2 == 0:
        soma = soma + numero     
    
print(f'A soma é: {soma}')