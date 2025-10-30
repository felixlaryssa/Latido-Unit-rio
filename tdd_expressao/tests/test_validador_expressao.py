import pytest
from src.validador_expressao import ehExpressaoValida

def deveAceitarExpressaoSimplesValida(self):
    assert ehExpressaoValida("1")
    assert ehExpressaoValida("1025")
    assert ehExpressaoValida("10000000")

