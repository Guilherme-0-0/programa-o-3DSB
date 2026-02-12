def adicionar(x, y):
    """Função para adicionar dois números"""
    return x + y

def subtrair(x, y):
    """Função para subtrair dois números"""
    return x - y

def multiplicar(x, y):
    """Função para multiplicar dois números"""
    return x * y

def dividir(x, y):
    """Função para dividir dois números"""
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def calculadora():
    """Função principal da calculadora"""
    print("========== CALCULADORA SIMPLES ==========")
    print("Selecione uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("========================================\n")
    
    while True:
        escolha = input("Digite sua escolha (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Obrigado por usar a calculadora. Até logo!")
            break
        
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if escolha == '1':
                    print(f"\n{num1} + {num2} = {adicionar(num1, num2)}\n")
                
                elif escolha == '2':
                    print(f"\n{num1} - {num2} = {subtrair(num1, num2)}\n")
                
                elif escolha == '3':
                    print(f"\n{num1} × {num2} = {multiplicar(num1, num2)}\n")
                
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {resultado}\n")
            
            except ValueError:
                print("Entrada inválida! Por favor, digite números válidos.\n")
        
        else:
            print("Escolha inválida! Por favor, selecione uma opção válida (1/2/3/4/5).\n")

if __name__ == "__main__":
    calculadora()
