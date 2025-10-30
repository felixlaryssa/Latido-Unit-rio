def obter_expressao() -> str:
    return input()

def eh_expressao_valida(expressao: str):
    
    if expressao.isdigit():
        return True
    return False


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