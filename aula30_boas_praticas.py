"""
CONSTANTE -> "Variáveis" que não vão mudar
Muitas condições no mesmo IF é ruim
.... <- contagem de complexidade é ruim

"""

velocidade = 61
local_carro = 100

# variáveis com letra maiuscula são consideradas constantes - não devem mudar o valor

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE_1 = 1

# Exercicios

multar_carro = (velocidade > RADAR_1)
nao_multar_carro = (velocidade <= RADAR_1)

range_para_multar = local_carro <= ((LOCAL_1 - RADAR_RANGE_1) and (LOCAL_1 + RADAR_RANGE_1))

if multar_carro:
    print("Carro passou acima da velocidade permitida!")

if nao_multar_carro:
    print("Carro passou na velocidade permitida!")

if range_para_multar and multar_carro:
    print("O carro foi multado")
