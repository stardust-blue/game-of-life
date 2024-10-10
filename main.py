import numpy as np
import sys
import os
import time


def random_state(height: int, width: int) -> np.ndarray:
    return np.random.randint(2, size=(height, width))


def next_state(state: np.ndarray) -> np.ndarray:
    rows, cols = state.shape
    new_state = np.zeros((rows, cols), dtype=int)

    dirx = np.array([0, 1, 0, -1, -1, 1, -1, 1])
    diry = np.array([-1, 0, 1, 0, -1, 1, 1, -1])

    for x in range(rows):
        for y in range(cols):
            neighbors = 0

            for i in range(8):
                nx, ny = x + dirx[i], y + diry[i]

                if 0 <= nx < rows and 0 <= ny < cols:
                    neighbors += state[nx, ny]

            if state[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_state[x, y] = 0
            elif state[x, y] == 0 and neighbors == 3:
                new_state[x, y] = 1
            else:
                new_state[x, y] = state[x, y]

    return new_state


def render(state: np.ndarray) -> np.ndarray:
    for row in state:
        print(" ".join(["." if cell == 0 else "#" for cell in row]))


def main():
    while True:
        try:
            height = int(input("Height: "))
            width = int(input("Width: "))
            state = random_state(height, width)
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter positive integers.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()

    try:
        while True:
            time.sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
            state = next_state(state)
            render(state)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()


if __name__ == "__main__":
    main()
