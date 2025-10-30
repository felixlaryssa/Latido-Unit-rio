def obter_expressao() -> str:
    return input()

def eh_expressao_valida(expressao: str):
    """
    Valida se a expressão é um número inteiro positivo simples.
    (Refatorado - Ciclo 1)
    
    Refatoração: O 'if/else' foi removido pois .isdigit()
    já retorna o valor booleano desejado.
    """
    
    return expressao.isdigit()


def ehExpressaoValida(expressao: str) -> bool:
    return eh_expressao_valida(expressao)


def main() -> None:
    while True:
        expressao = obter_expressao()
        
        if expressao.lower() == 'sair':
            break
            
        if eh_expressao_valida(expressao):
            print("Resultado: VÁLIDA\n")
        else:
            print("Resultado: INVÁLIDA\n") 


if __name__ == '__main__':
    main()