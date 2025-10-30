import pytest
from src.validador_expressao import ehExpressaoValida

def deveAceitarExpressaoSimplesValida(self):
    assert ehExpressaoValida("1 + 1")
    assert ehExpressaoValida("10 + 25")
    assert ehExpressaoValida("1*2+3/4-5")

