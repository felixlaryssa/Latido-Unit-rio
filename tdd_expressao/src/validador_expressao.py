import re

def obter_expressao() -> str:
    return input()

OPERADORES = {'+', '-', '*', '/'}

def ehExpressaoValida(expressao: str) -> bool:
    expressao = expressao.strip().replace(" ", "")

    if not expressao:
        return False

    if expressao[0] in OPERADORES or expressao[-1] in OPERADORES:
        return False
    
    padrao_numero = r"^\d+$"
    padrao_operacao_simples = r"^\d+[+\-*/]\d+$"
        
    if re.fullmatch(padrao_numero, expressao) or \
        re.fullmatch(padrao_operacao_simples, expressao):
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
