"""
Exercício
- Peça ao usuário para digitar seu nome
- Peça ao usuário para digitar sua idade
- Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}   - OK
        Seu nome invertido é {nome invertido}    - OK
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {ultima letra}
- Se nada for digitado em nome ou idade:
    Exiba:
        - "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if (nome == '' or idade == ''):
    print("Desculpe, você deixou campos vazios.")
else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if(' ' in nome):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")