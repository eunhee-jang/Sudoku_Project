def is_valid(board, row, col, num):  # 3가지 규칙 체크 함수
    # 해당 숫자가 같은 행에 있는지 확인
    if num in board[row]:
        return False
    # 해당 숫자가 같은 열에 있는지 확인
    if num in [board[i][col] for i in range(9)]:
        return False
    # 해당 숫자가 같은 3x3 박스에 있는지 확인
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) # // 몫의 값을 나타낸다. -> 내가 포함된 3x3박스의 좌측 상단 시작점!
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def find_empty_location(board):  # 빈 값을 찾는 함수
    # 비어 있는 위치(0)를 찾음
    for i in range(9):  # 행
        for j in range(9):  # 열
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # 빈 위치 찾기
    empty_loc = find_empty_location(board)
    if not empty_loc: # 빈 위치가 없다면,
        return True  # 모든 빈칸을 다 채운 경우, 끝
    
    # 빈 위치가 있다면,
    row, col = empty_loc

    for num in range(1, 10): # 빈값에 1~9를 다 넣어보면서, 유효한 값을 찾는다.
        if is_valid(board, row, col, num): # 3가지 규칙이 맞을 때
            board[row][col] = num # 유효하면, 대입!

            # 위 규칙에 의거, 값을 채워 넣었는데, 결국 스도쿠를 해결하지 못했다면,
            if solve_sudoku(board):
                return True

            board[row][col] = 0  # 실패한 경우, 백트래킹

    return False  # 이 경로로는 해결 불가

if solve_sudoku(board):
    print_board(board)
else:
    print("해결할 수 없는 스도쿠 퍼즐입니다.")