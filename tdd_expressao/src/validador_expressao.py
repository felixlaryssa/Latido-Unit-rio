import re

def obter_expressao() -> str:
    return input()


def ehExpressaoValida(expressao: str) -> bool:
    expressao = expressao.strip().replace(" ", "")
    
    padroes_validos = [
        r"\d+",           # número simples
        r"\d+\+\d+",      # soma simples
    ]
    
    return any(re.fullmatch(p, expressao) for p in padroes_validos)



def main() -> None:
    OPERADORES = '+', '-', '*', '/'
    PARENTESES = '(', ')'
    expressao = obter_expressao()
    resultado = ehExpressaoValida(expressao)
    print("Expressão válida?", resultado)


if __name__ == '__main__':
    main()
