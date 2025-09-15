import sys, os
import pytest

# adiciona a pasta raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic import calcular_orcamento


def test_calculo_orcamento_basico():
    pecas = [
        {"materia": 10.0},
        {"materia": 5.5},
    ]
    arte = 4.5

    soma, total = calcular_orcamento(pecas, arte)

    assert soma == 15.5
    assert total == 20.0
