import random

def jogo_adivinhacao():
    while True:
        print("\n🎯 Jogo de Adivinha do jose sergio!")
        print("Pensei em um número entre 1 e 100")
        print("Digite 0 para sair do jogo")

        numero_secreto = random.randint(1, 100)
        tentativas = 0

        while True:
            try:
                palpite = int(input("Seu palpite: "))
            except ValueError:
                print("Digite um número válido!")
                continue

            if palpite == 0:
                print("Saindo do jogo 👋")
                return

            tentativas += 1

            if palpite < numero_secreto:
                print("🔼 Muito baixo!")
            elif palpite > numero_secreto:
                print("🔽 Muito alto!")
            else:
                print(f"🎉 Acertou! Número: {numero_secreto}")
                print(f"Tentativas: {tentativas}")
                break

        jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            print("Obrigado por jogar 😄")
            break

jogo_adivinhacao()
