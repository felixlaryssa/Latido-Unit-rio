import re

def obter_expressao() -> str:
    return input()

OPERADORES = {'+', '-', '*', '/'}

def ehExpressaoValida(expressao: str) -> bool:
    expressao = expressao.strip().replace(" ", "")

    if expressao[0] in OPERADORES or expressao[-1] in OPERADORES:
        return False
    
    # 1. É um número simples? 
    if re.fullmatch(r"\d+", expressao):
        return True
        
    # 2. É uma soma simples? 
    if re.fullmatch(r"\d+\+\d+", expressao):
        return True
    
    return False



def main() -> None:
    OPERADORES = '+', '-', '*', '/'
    PARENTESES = '(', ')'
    expressao = obter_expressao()
    resultado = ehExpressaoValida(expressao)
    print("Expressão válida?", resultado)


if __name__ == '__main__':
    main()
