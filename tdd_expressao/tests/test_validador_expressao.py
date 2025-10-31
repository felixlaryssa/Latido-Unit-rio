import pytest
from src.validador_expressao import ehExpressaoValida

def test_aceita_expressao_simples_valida():
    assert ehExpressaoValida("1")
    assert ehExpressaoValida("1025")
    assert ehExpressaoValida("10000000")


def test_soma_simples_deve_ser_valida():
    assert ehExpressaoValida("1 + 1") 
    assert ehExpressaoValida("10+25")
    assert ehExpressaoValida("1000000 + 2000000")

def test_nao_deve_comecar_terminar_com_operador():
    """Testa a Regra 3: Não pode começar ou terminar com operador."""
    assert not ehExpressaoValida("+1")
    assert not ehExpressaoValida("1+")
    assert not ehExpressaoValida(" * 5")
    assert not ehExpressaoValida("5 / ") 

