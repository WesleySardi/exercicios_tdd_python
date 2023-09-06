import random

def gerar_valores_aleatorios(tamanho):
  return [random.randint(-999999, 999999) for _ in range(tamanho)]

valores_aleatorios = gerar_valores_aleatorios(20000)

# print(valores_aleatorios)