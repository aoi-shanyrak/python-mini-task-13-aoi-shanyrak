import os
import random

from config import (
    VERBOSE,
    TEST_DIR,
    FIELD_NUMBER,
    FIELD_SIZE,
    DENSITY_MODE,
    DENSITY_VALUE,
    DENSITY_MODES
)


def get_field() -> str:
    filename = f"{TEST_DIR}/{FIELD_NUMBER}.txt"
    if FIELD_NUMBER is not None and os.path.exists(filename):
        return filename
    
    return create_field()


def create_field() -> str:
    os.makedirs(TEST_DIR, exist_ok=True)

    if DENSITY_VALUE is not None:
        density = max(0.0, min(1.0, DENSITY_VALUE))
        mode_name = f"custom_{density:.3f}"
    elif DENSITY_MODE == "random":
        density = random.uniform(0.02, 0.25)
        mode_name = f"random_{density:.3f}"
    else:
        density = DENSITY_MODES.get(DENSITY_MODE, DENSITY_MODES["optimal"])
        mode_name = DENSITY_MODE
    
    existing_files = []
    if os.path.exists(TEST_DIR):
        existing_files = [f for f in os.listdir(TEST_DIR)
                          if f.endswith(".txt") and f[:-4].isdigit()]
        
    if len(existing_files) < 10:
        file_numbers = [int(f[:-4]) for f in existing_files] if existing_files else [0]
        next_number = max(file_numbers) + 1
    else:
        oldest_file = min(existing_files, key=lambda f: os.path.getctime(f"{TEST_DIR}/{f}"))
        next_number = int(oldest_file[:-4])
    
    filename = f"{TEST_DIR}/{next_number}.txt"
    with open(filename, "w") as f:
        for _ in range(FIELD_SIZE):
            row = ''.join("1" if random.random() < density else "0"
                          for _ in range(FIELD_SIZE))
            f.write(row + '\n')

    with open(filename, 'r') as f:
        content = f.read()
        ones = content.count('1')
        zeros = content.count('0')
        total_cells = ones + zeros
        actual_density = ones / total_cells if total_cells > 0 else 0
    
    if VERBOSE:
        print(f"created file: {filename}")
        print(f"  mode: {mode_name}")
        print(f"  density: {actual_density*100:.2f}%")
        print(f"  cells: {total_cells:,} ({ones:,} alive, {zeros:,} dead)")
    
    return filename


if __name__ == "__main__":
    create_field()