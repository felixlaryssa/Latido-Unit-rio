import pytest
from src.validador_expressao import eh_expressao_valida

def test_deve_aceitar_expressao_simples_valida():
    assert eh_expressao_valida("1")
    assert eh_expressao_valida("1025")
    assert eh_expressao_valida("10000000")

