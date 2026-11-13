
def game_result(board):
    lines = []

    for i in range(3):
        lines.append(board[i])  # строка
        lines.append(board[0][i] + board[1][i] + board[2][i])  # столбец

    lines.append(board[0][0] + board[1][1] + board[2][2])
    lines.append(board[0][2] + board[1][1] + board[2][0]) # Диагонали

    for line in lines:
        if line == "XXX":
            return "X"
        if line == "OOO":
            return "O"

    # Если победителя нет, проверяем, остались ли пустые клетки
    for row in board:
        if "." in row:
            return None

    # Если все условия проверены и ничего не дали - ничья
    return "draw"