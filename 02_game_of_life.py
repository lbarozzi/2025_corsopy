import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def iteration(grid):
    rows, cols = grid.shape
    out_grid = np.copy(grid)  

    for row in range(rows):
        for col in range(cols):
            
            alives = near_alives(grid, row, col)

            if grid[row, col] == 1:  # alive
                if alives < 2 or alives > 3:
                    out_grid[row, col] = 0  # dead
            else:  # is Dead
                if alives == 3:
                    out_grid[row, col] =1 # != out_grid[row,col] # 1  # resurrect

    return out_grid

def near_alives(grid, row, col):

    rows, cols = grid.shape
    alives = 0

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and grid[i, j] == 1:
                alives += 1

    return alives



def main():
    inter=10
    start_grid = np.random.choice([0, 1], size=(10, 10))  # Griglia casuale 10x10
    img, ax =plt.subplots(inter)
    ax[0].imshow(start_grid, cmap='binary')
    # plt.show()
    print("Griglia iniziale:\n", start_grid)
    new1=start_grid.copy()
    
    for i in range(inter):
        print(f"\nIterazione {i + 1}")
        new1 = iteration(new1)
        ax[i].imshow(new1, cmap='binary')
        # plt.show()
        print("\nGriglia aggiornata:\n", new1)

    plt.show()


if __name__=="__main__":
    main()  