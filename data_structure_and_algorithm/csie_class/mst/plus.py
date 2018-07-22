
def print_board(board):
	for i in range(3):
		for j in range(3):
			print(board[i][j],end=' ')
		print('\n')

board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']] 

status = True
counter = 0
while True:
	if status:
		O_input = input("O:")
		status = False
		tmp = O_input.split(':')
		tmp = ''.join(tmp)
		print(int(tmp[0]))
		board[int(tmp[0])][int(tmp[2])] = 'O'
	else:
		X_input = input("X:")
		status = True
		tmp = X_input.split(':')
		tmp = ''.join(tmp)
		board[int(tmp[0])][int(tmp[2])] = 'X'

	print_board(board)

	if board[0][0] == board[0][1] == board[0][2] != '*'\
	or board[0][0] == board[1][0] == board[2][0] != '*'\
	or board[0][2] == board[1][2] == board[2][2] != '*'\
	or board[2][0] == board[2][1] == board[2][2] != '*'\
	or board[0][1] == board[1][1] == board[2][1] != '*'\
	or board[1][0] == board[1][1] == board[1][2] != '*'\
	or board[0][0] == board[1][1] == board[2][2] != '*'\
	or board[0][2] == board[1][1] == board[2][0] != '*':
		if status:
			print("X win")
		else:
			print("O win")
		break
	counter += 1
	if counter == 9:
		print("Tie!")
		break