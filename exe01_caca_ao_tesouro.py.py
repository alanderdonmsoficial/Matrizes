# Exercício 1 - Caça Tesouro

import random

TAMANHO = 5


def criar_mapa():
    """Cria a matriz 5x5 (lista de listas) que representa o mapa."""
    return [["." for _ in range(TAMANHO)] for _ in range(TAMANHO)]


def exibir_mapa(mapa):
    print("\n    " + " ".join(str(c) for c in range(TAMANHO)))
    for i, linha in enumerate(mapa):
        print(f"{i} | " + " ".join(linha))
    print()


def ler_numero(mensagem):
    """Lê um número inteiro entre 0 e 4, repetindo até ser válido."""
    while True:
        try:
            valor = int(input(mensagem))
            if 0 <= valor < TAMANHO:
                return valor
            print(f"Valor fora do mapa! Digite um número de 0 a {TAMANHO - 1}.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def dar_dica(distancia):
    if distancia == 1:
        return "Muito perto!"
    elif distancia <= 3:
        return "Perto."
    else:
        return "Longe."


def main():
    mapa = criar_mapa()
    linha_tesouro = random.randint(0, TAMANHO - 1)
    coluna_tesouro = random.randint(0, TAMANHO - 1)
    tentativas = 0

    print("=== CAÇA AO TESOURO ===")
    print(f"Um tesouro está escondido em um mapa {TAMANHO}x{TAMANHO}.")
    print("Informe linha e coluna (0 a 4) para encontrá-lo!")

    encontrou = False
    while not encontrou:
        exibir_mapa(mapa)
        linha = ler_numero("Linha: ")
        coluna = ler_numero("Coluna: ")

        if mapa[linha][coluna] == "X":
            print("Você já tentou essa posição! Escolha outra.")
            continue

        tentativas += 1

        if linha == linha_tesouro and coluna == coluna_tesouro:
            mapa[linha][coluna] = "T"
            encontrou = True
        else:
            mapa[linha][coluna] = "X"
            # Distância de Manhattan: |Δlinha| + |Δcoluna|
            distancia = abs(linha - linha_tesouro) + abs(coluna - coluna_tesouro)
            print(dar_dica(distancia))

    exibir_mapa(mapa)
    print(f"Parabéns! Você encontrou o tesouro em {tentativas} tentativa(s)!")


if __name__ == "__main__":
    main()