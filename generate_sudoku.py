import random

def generate_sudoku():
    puzzle = []

    # 0의 확률을 50%으로 고정 - 전체 18개 중 9개가 0이므로!
    numbers = [0] * 9 + list(range(1, 10))

    for _ in range(9):  # 행 9개
        row = []
        for _ in range(9):  # 열 9개
            
            rand_int = random.choice(numbers) # choice로 '0'이 들어가는 확률을 조절
            row.append(rand_int)
        puzzle.append(row)
        
    return puzzle