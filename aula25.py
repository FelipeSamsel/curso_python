""""
Interpolação básica de string
s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)

% serve para substituir e direcionar variaveis

"""

nome = 'Felipe'
preco = 1000.865495843
variavel1 = 'Felipe, o preço total foi R$ 1000.86'
variavel2 = '%s, o preço total foi R$ %.2f' % (nome, preco)

print(variavel1)
print(variavel2)
print('O hexadecimal de %d é %08X' % (1500, 1500))

