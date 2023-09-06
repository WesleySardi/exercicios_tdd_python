from exercicio1 import gerar_valores_aleatorios
import pytest

def test_no_duplicates():
    valores_aleatorios = gerar_valores_aleatorios(20000)
    assert len(valores_aleatorios) == len(set(valores_aleatorios))