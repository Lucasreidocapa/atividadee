a = list()
b = list()
c = a
for contagem in range(0,5):
    a.append(int(input('gite o valor para lista A')))
print('='*40)
for contagem in range(0,5):
    b.append(int(input('digite um valor para lista b')))
print('='*40)
print (f'a lista a é:{a}')
print (f'a lista b é:{b}')
a = c
a = b
print('='*40)
print(f'a lista a é:{a}')
print(f'a lista b é:{b}')