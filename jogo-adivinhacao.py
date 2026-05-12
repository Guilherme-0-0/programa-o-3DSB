import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas_restantes = 5
    ganhou = False

    print("--- Bem-vindo ao Desafio de Adivinhação! ---")
    print("Tente adivinhar o número entre 1 e 10.")

    # O loop while permite que o número de tentativas seja alterado dinamicamente
    while tentativas_restantes > 0:
        print(f"\nVocê tem {tentativas_restantes} tentativas.")
        palpite = int(input("Digite seu palpite: "))

        if palpite == numero_secreto:
            print(f"Parabéns! Você descobriu o número {numero_secreto}!")
            ganhou = True
            break
        
        # Lógica do bônus: Diferença de apenas 1 unidade
        elif abs(palpite - numero_secreto) == 1:
            print("Quase lá! Você estava a apenas 1 unidade de distância.")
            print("BÔNUS: Você ganhou +1 tentativa extra!")
            # Não subtraímos a tentativa atual, o que na prática mantém o saldo
            # ou podemos somar 1 e deixar a subtração padrão ocorrer abaixo.
            tentativas_restantes += 1 
        
        else:
            print("Palpite incorreto.")

        tentativas_restantes -= 1

    if not ganhou:
        print(f"\nGame Over! O número era {numero_secreto}.")

# Iniciar o jogo
jogo_adivinhacao()
