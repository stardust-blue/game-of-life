import numpy as np
import sys
import os
import time


def random_state(height: int, width: int) -> np.ndarray:
    return np.random.randint(2, size=(height, width))


def next_state(state: np.ndarray) -> np.ndarray:
    rows, cols = state.shape
    new_state = np.zeros((rows, cols), dtype=int)

    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for x in range(rows):
        for y in range(cols):
            neighbors = sum(
                state[x + dx, y + dy]
                for dx, dy in dir
                if 0 <= x + dx < rows and 0 <= y + dy < cols
            )

            if state[x, y] == 1:
                new_state[x, y] = 1 if neighbors in (2, 3) else 0
            else:
                new_state[x, y] = 1 if neighbors == 3 else 0

    return new_state


def render(state: np.ndarray):
    for row in state:
        print(" ".join("#" if cell == 1 else "." for cell in row))


def main():
    while True:
        try:
            height = int(input("Height: "))
            width = int(input("Width: "))
            if height <= 0 or width <= 0:
                raise ValueError("Height and Width must be positive integers.")
            state = random_state(height, width)
            break
        except ValueError as error:
            print(f"Invalid input: {error}. Please enter positive integers.")
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
