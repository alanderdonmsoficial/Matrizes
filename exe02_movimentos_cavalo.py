# Exercicio 2 - Cavalo

TAMANHO = 8

# Os 8 movimentos possíveis do cavalo (variação de linha, variação de coluna)
MOVIMENTOS = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1),
]


def criar_tabuleiro():
    """Cria a matriz 8x8 preenchida com '.'."""
    return [["." for _ in range(TAMANHO)] for _ in range(TAMANHO)]


def ler_posicao(mensagem):
    """Lê um inteiro entre 0 e 7, repetindo até ser válido."""
    while True:
        try:
            valor = int(input(mensagem))
            if 0 <= valor < TAMANHO:
                return valor
            print(f"Valor inválido! Digite um número entre 0 e {TAMANHO - 1}.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def movimentos_validos(linha, coluna):
    """Retorna as posições dentro do tabuleiro para onde o cavalo pode ir."""
    validos = []
    for dl, dc in MOVIMENTOS:
        nova_linha = linha + dl
        nova_coluna = coluna + dc
        if 0 <= nova_linha < TAMANHO and 0 <= nova_coluna < TAMANHO:
            validos.append((nova_linha, nova_coluna))
    return validos


def exibir_tabuleiro(tabuleiro):
    print("\n    " + " ".join(str(c) for c in range(TAMANHO)))
    for i, linha in enumerate(tabuleiro):
        print(f"{i} | " + " ".join(linha))
    print()


def main():
    print("=== MOVIMENTOS DO CAVALO ===")
    linha = ler_posicao("Linha inicial do cavalo (0 a 7): ")
    coluna = ler_posicao("Coluna inicial do cavalo (0 a 7): ")

    tabuleiro = criar_tabuleiro()
    tabuleiro[linha][coluna] = "C"

    possiveis = movimentos_validos(linha, coluna)
    for l, c in possiveis:
        tabuleiro[l][c] = "*"

    exibir_tabuleiro(tabuleiro)
    print(f"O cavalo em ({linha}, {coluna}) tem {len(possiveis)} movimento(s) válido(s):")
    for l, c in possiveis:
        print(f"  -> ({l}, {c})")


if __name__ == "__main__":
    main()