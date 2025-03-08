import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros do grid
LARGURA = 100
ALTURA = 100
VAZIO = 0
AREIA = 1

# Função para criar o grid
def criar_grid():
    return np.zeros((ALTURA, LARGURA), dtype=int)

# Função para adicionar areia
def adicionar_areia(grid):
    for x in range(LARGURA):
        if np.random.rand() < 0.1:  # Probabilidade de adicionar areia
            grid[0, x] = AREIA

# Função para atualizar o grid
def atualizar(grid):
    novo_grid = grid.copy()
    for y in range(ALTURA - 1, -1, -1):
        for x in range(LARGURA):
            if grid[y, x] == AREIA:
                if y < ALTURA - 1 and grid[y + 1, x] == VAZIO:
                    novo_grid[y, x] = VAZIO
                    novo_grid[y + 1, x] = AREIA
                elif y < ALTURA - 1:
                    direcao = np.random.choice([-1, 1])
                    if 0 <= x + direcao < LARGURA and grid[y + 1, x + direcao] == VAZIO:
                        novo_grid[y, x] = VAZIO
                        novo_grid[y + 1, x + direcao] = AREIA
    return novo_grid

# Função de animação
def animar(frameNum, img, grid):
    adicionar_areia(grid)
    grid[:] = atualizar(grid)
    img.set_data(grid)
    return img,

# Configuração da animação
def main():
    grid = criar_grid()
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='YlOrBr', vmin=0, vmax=1)
    plt.colorbar(img, ticks=[0, 1], label='Estado')
    ani = animation.FuncAnimation(fig, animar, fargs=(img, grid),
                                  frames=200, interval=50, save_count=50)
    plt.title("Formação de Padrões em Areia")
    plt.show()

if __name__ == '__main__':
    main()