# logic.py
def calcular_orcamento(pecas, arte_aplicada):
    """
    pecas: lista de dicionários com 'materia' (float)
    arte_aplicada: float
    """
    soma_materia = sum(p["materia"] for p in pecas)
    total_final = soma_materia + arte_aplicada
    return soma_materia, total_final
