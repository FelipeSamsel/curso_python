"""
Introdução ao Try/Except
Try - tenta executar o códico
except - ocorreu algum erro ao tentar executar

"""

numero_str = input("Vou dobrar o número que você digitar: ")


try:
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2}")
    
except:
    print("Isso não é um número")
