import pytest
from src.validador_expressao import eh_expressao_valida

def deve_aceitar_expressao_simples_valida(self):
    assert ehExpressaoValida("1")
    assert ehExpressaoValida("1025")
    assert ehExpressaoValida("10000000")

