def obter_expressao() -> str:
    return input()

def eh_expressao_valida(expressao: str): #tem que retornar bool
    pass

def main() -> None:
    OPERADORES = ('+', '-', '*', '/')
    PARENTESES = ('(', ')')
    expressao = obter_expressao()
    eh_expressao_valida(expressao) 


if __name__ == '__main__':
    main()
