from exercicio1 import gerar_valores_aleatorios


def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]


valores_aleatorios = gerar_valores_aleatorios(20)
selection_sort(valores_aleatorios)
print(valores_aleatorios)
