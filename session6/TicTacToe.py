import pyfiglet

def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

def check_game():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("player 1 wins!")

    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("player 1 wins!")

    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("player 1 wins!")

    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("player 1 wins!")

    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("player 1 wins!")

    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("player 1 wins!")

        

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
show()

while True:
    print("player 1")

    while True:
        row = int(input("row: "))
        col = int(input("col: "))

        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                break
            else:
                print("choose empty space:/n")
        else:
            print("enter num 0-2: |")

    show()
    check_game()

    print("player 2")
    while True:
        row = int(input("row: "))
        col = int(input("col: "))

        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                break
            else:
                print("choose empty space:/n")
        else:
            print("enter num 0-2: |")

    show()
    check_game()


