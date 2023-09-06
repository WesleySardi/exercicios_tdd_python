import pytest
from exercicio3 import converter_massa_lunar, converter_distancia_marte

def test_converter_massa_lunar():
    assert converter_massa_lunar(6) == 1
    assert converter_massa_lunar(12) == 2

def test_converter_distancia_marte():
    assert converter_distancia_marte(10) == 3.79
    assert converter_distancia_marte(20) == 7.58
