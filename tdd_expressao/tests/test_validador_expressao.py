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

def test_aceita_outras_operacoes_simples():
    """Testa se operadores simples (-, *, /) são válidos."""
    assert ehExpressaoValida("1 - 1")
    assert ehExpressaoValida("10 * 2")
    assert ehExpressaoValida("100 / 5") 

def test_rejeita_string_vazia_ou_so_de_espacos():
    """Testa se uma string vazia ou só com espaços falha (Regra 6)."""
    assert not ehExpressaoValida("")
    assert not ehExpressaoValida("   ")