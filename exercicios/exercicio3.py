def converter_massa_lunar(massa_terrestre):
    massa_lunar = massa_terrestre / 6
    return massa_lunar

def converter_distancia_marte(distancia_terrestre):
    gravidade_terra = 9.81
    gravidade_marte = 3.71

    distancia_marte = (gravidade_terra / gravidade_marte) * distancia_terrestre
    return distancia_marte
