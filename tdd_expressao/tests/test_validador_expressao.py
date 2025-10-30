from src.validador_expressao import ehExpressaoValida


def test_deve_aceitar_expressao_simples_valida():
    """Happy-path: simple numeric expressions should be valid."""
    assert ehExpressaoValida("1")
    assert ehExpressaoValida("1025")
    assert ehExpressaoValida("10000000")

