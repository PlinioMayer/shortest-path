import os
import time
from copy import deepcopy
import sys
from pathlib import Path
from typing import List, Optional, Tuple


def main():
    path: Path = Path(sys.argv[1])
    matrix: Optional[List[List[str]]] = None

    if not path.is_file():
        exit('Provided path is not a file!')

    with path.open('r', encoding='utf-8') as file:
        matrix = list(map(lambda string: list(string.strip()), file.readlines()))

    x, y = validate_matrix(matrix)

    shortest_path = find_shortest_path(matrix, x, y)

    if shortest_path:
        print(f"Path: {shortest_path[0]}")
        print('\n'.join(map(lambda arr: ''.join(arr), shortest_path[1])))
    else:
        print('Impossible!')


def find_shortest_path(matrix: List[List[str]], x: int, y: int) -> Optional[Tuple[int, List[List[str]]]]:
    left_result: Optional[Tuple[int, List[str]]] = go(matrix, x - 1, y)
    right_result: Optional[Tuple[int, List[str]]] = go(matrix, x + 1, y)
    up_result: Optional[Tuple[int, List[str]]] = go(matrix, x, y + 1)
    down_result: Optional[Tuple[int, List[str]]] = go(matrix, x, y - 1)

    current_result: Optional[Tuple[int, List[str]]] = None

    if left_result:
        current_result = left_result

        if right_result and right_result[0] < current_result[0]:
            current_result = right_result

        if up_result and up_result[0] < current_result[0]:
            current_result = up_result

        if down_result and down_result[0] < current_result[0]:
            current_result = down_result

        return current_result
    elif right_result:
        current_result = right_result

        if up_result and up_result[0] < current_result[0]:
            current_result = up_result

        if down_result and down_result[0] < current_result[0]:
            current_result = down_result
    elif up_result:
        current_result = up_result

        if down_result and down_result[0] < current_result[0]:
            current_result = down_result
    elif down_result:
        current_result = down_result

    return current_result


def go(matrix: List[List[str]], x: int, y: int) -> Optional[Tuple[int, List[List[str]]]]:
    if matrix[y][x] == 'E':
        return 1, deepcopy(matrix)

    if matrix[y][x] == ' ':
        new_matrix: List[List[str]] = deepcopy(matrix)
        new_matrix[y][x] = '•'

        print('\n'.join(map(lambda arr: ''.join(arr), new_matrix)))

        time.sleep(0.5)

        os.system('cls||clear')

        result = find_shortest_path(new_matrix, x, y)

        if result:
            return 1 + result[0], result[1]

    return None


def validate_matrix(matrix: List[List[str]]) -> Tuple[int, int]:
    matrix_len: int = len(matrix)
    row_len: int = len(matrix[0])
    found_s: int = 0
    found_e: int = 0
    start: Optional[Tuple[int, int]] = None

    validate_all_blocks(matrix[0])

    for y, row in enumerate(matrix[1:matrix_len - 1]):
        if len(row) != row_len:
            exit(f"Invalid map!\nLine {y + 1} isn't the same size as first.")

        for x, char in enumerate(row):
            if char == 'S':
                found_s += 1
                start = (x, y + 1)
            elif char == 'E':
                found_e += 1

    if len(matrix[matrix_len - 1]) != row_len:
        exit('Invalid map!\nLast line isn\'t the same size as first.')

    validate_all_blocks(matrix[matrix_len - 1])

    validate_all_blocks(list(map(lambda string: string[0], matrix)))
    validate_all_blocks(list(map(lambda string: string[row_len - 1], matrix)))

    if found_e != 1 or found_s != 1:
        exit(f"Invalid map!\nFound {found_e} E's and {found_s} S's.\nOne of each is allowed.")

    return start


def validate_all_blocks(row: List[str]):
    for char in row:
        if char != '#':
            exit('Invalid map!\nAll boundaries must be \'#\'')


def exit(message: str):
    print(message)
    sys.exit()


if __name__ == '__main__':
    main()
