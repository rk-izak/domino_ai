import random


def snake_count(mat):
    count = 0
    rad = mat[0][0]
    for x in range(0, len(mat)):
        if mat[x][0] == rad:
            count += 1
        if mat[x][1] == rad:
            count += 1
    return count


def starting_player(set_1, set_2):
    doubles_1 = [[-1, -1]]
    doubles_2 = [[-1, -1]]
    max_val = []
    n = 0
    for i in range(0, len(set_1)):
        if set_1[i][0] == set_1[i][1]:
            doubles_1.extend([set_1[i]])
    for j in range(0, len(set_2)):
        if set_2[j][0] == set_2[j][1]:
            doubles_2.extend([set_2[j]])

    if max(max(doubles_1)) > max(max(doubles_2)):
        max_val = max(doubles_1)
        n = 1
    elif max(max(doubles_1)) < max(max(doubles_2)):
        max_val = max(doubles_2)
        n = 2
    elif max(max(doubles_1)) == max(max(doubles_2)):
        n = -1
    return max_val, n


def snake_printer(mat, numb):
    if numb == 0:
        print('{}'.format(mat[0]))
    elif numb == 1:
        print('{}{}'.format(mat[0], mat[1]))
    elif numb == 2:
        print('{}{}{}'.format(mat[0], mat[1], mat[2]))
    elif numb == 3:
        print('{}{}{}{}'.format(mat[0], mat[1], mat[2], mat[3]))
    elif numb == 4:
        print('{}{}{}{}{}'.format(mat[0], mat[1], mat[2], mat[3], mat[4]))
    elif numb == 5:
        print('{}{}{}{}{}{}'.format(mat[0], mat[1], mat[2], mat[3], mat[4], mat[5]))
    elif numb >= 6:
        print('{}{}{}{}{}{}{}'.format(mat[0], mat[1], mat[2], '...', mat[-3], mat[-2], mat[-1]))


def ai_picker(ai_pieces, snake_pieces):
    all_numbers = [0, 1, 2, 3, 4, 5, 6]
    ai_vals = [sum(x.count(val) for x in ai_pieces) for val in all_numbers]
    snake_vals = [sum(x.count(val) for x in snake_pieces) for val in all_numbers]
    total_vals = [x + y for x, y in zip(ai_vals, snake_vals)]
    total_dict = dict(zip(all_numbers, total_vals))
    scores = [[[(total_dict[ai_pieces[i][0]] + total_dict[ai_pieces[i][1]])], ai_pieces[i]]
              for i in range(0, len(ai_pieces))]

    n = 0
    while True:
        best = scores[n][1]
        if best[0] == snake_pieces[-1][1] or best[1] == snake_pieces[-1][1]:
            best_move = ai_pieces.index(best) + 1
            break
        elif best[0] == snake_pieces[0][0] or best[1] == snake_pieces[0][0]:
            best_move = (ai_pieces.index(best) + 1) * -1
            break
        if n >= (len(ai_pieces) - 1):
            best_move = 0
            break
        n += 1
    return best_move


while True:
    full_set = [[value_1, value_2] for value_1 in range(7) for value_2 in range(value_1, 7)]
    player_set = random.sample(full_set, k=7)
    full_set = [item for item in full_set if item not in player_set]
    computer_set = random.sample(full_set, k=7)
    full_set = [item for item in full_set if item not in computer_set]
    snake, who = starting_player(player_set, computer_set)
    if who == 1:
        player_set.remove(snake)
        status = 'computer'
    elif who == 2:
        computer_set.remove(snake)
        status = 'player'
    if who > 0:
        break

pos = 0
snake = [snake]
while True:
    print("======================================================================")
    print("Stock size:", len(full_set))
    print("Computer pieces:", len(computer_set))
    print()
    snake_printer(snake, pos)
    print()
    print("Your pieces:")

    for z in range(0, len(player_set)):
        print('{}:{}'.format(z + 1, player_set[z]))

    if len(player_set) == 0:
        print("\nStatus: The game is over. You won!")
        break
    elif len(computer_set) == 0:
        print("\nStatus: The game is over. The computer won!")
        break
    elif snake[0][0] == snake[-1][1] and snake_count(snake) > 7:
        print("\nStatus: The game is over. It's a draw!")
        break

    if status == 'computer':
        input("\nStatus: Computer is about to make a move. Press Enter to continue...\n")
        while True:
            move = ai_picker(computer_set, snake)
            if int(move) > 0 and (
                    computer_set[abs(int(move)) - 1][0] != snake[-1][1] and computer_set[abs(int(move)) - 1][1] !=
                    snake[-1][1]):
                move = move
            elif int(move) < 0 and (
                    computer_set[abs(int(move)) - 1][0] != snake[0][0] and computer_set[abs(int(move)) - 1][1] !=
                    snake[0][0]):
                move = move
            else:
                move = int(move)
                if move > 0:
                    if computer_set[abs(int(move)) - 1][0] == snake[-1][1]:
                        move = computer_set[abs(move) - 1]
                        snake.extend([move])
                        computer_set = [item for item in computer_set if item != move]
                        pos += 1
                    elif computer_set[abs(int(move)) - 1][1] == snake[-1][1]:
                        move = computer_set[abs(move) - 1]
                        move.reverse()
                        snake.extend([move])
                        computer_set = [item for item in computer_set if item != move]
                        pos += 1
                elif move < 0:
                    if computer_set[abs(int(move)) - 1][1] == snake[0][0]:
                        move = computer_set[abs(move) - 1]
                        snake[0:0] = [move]
                        computer_set = [item for item in computer_set if item != move]
                        pos += 1
                    elif computer_set[abs(int(move)) - 1][0] == snake[0][0]:
                        move = computer_set[abs(move) - 1]
                        move.reverse()
                        snake[0:0] = [move]
                        computer_set = [item for item in computer_set if item != move]
                        pos += 1
                elif move == 0:
                    if len(full_set) > 0:
                        computer_set[0:0] = [random.choice(full_set)]
                        full_set = [item for item in full_set if item not in computer_set]
                    else:
                        pass
                break






    elif status == 'player':
        print("\nStatus: It's your turn to make a move. Enter your command.")

        while True:
            move = input()
            if str(move) not in [str(i) for i in range(-len(player_set) - 1, len(player_set) + 1)]:
                print("Invalid input. Please try again.")
            elif int(move) > 0 and (
                    player_set[abs(int(move)) - 1][0] != snake[-1][1] and player_set[abs(int(move)) - 1][1] !=
                    snake[-1][1]):
                print("Illegal move. Please try again.")
            elif int(move) < 0 and (
                    player_set[abs(int(move)) - 1][0] != snake[0][0]
                    and player_set[abs(int(move)) - 1][1] != snake[0][0]):
                print("Illegal move. Please try again.")

            else:
                move = int(move)
                if move > 0:
                    if player_set[abs(int(move)) - 1][0] == snake[-1][1]:
                        move = player_set[abs(move) - 1]
                        snake.extend([move])
                        player_set = [item for item in player_set if item != move]
                        pos += 1
                    elif player_set[abs(int(move)) - 1][1] == snake[-1][1]:
                        move = player_set[abs(move) - 1]
                        move.reverse()
                        snake.extend([move])
                        player_set = [item for item in player_set if item != move]
                        pos += 1
                elif move < 0:
                    if player_set[abs(int(move)) - 1][1] == snake[0][0]:
                        move = player_set[abs(move) - 1]
                        snake[0:0] = [move]
                        player_set = [item for item in player_set if item != move]
                        pos += 1
                    elif player_set[abs(int(move)) - 1][0] == snake[0][0]:
                        move = player_set[abs(move) - 1]
                        move.reverse()
                        snake[0:0] = [move]
                        player_set = [item for item in player_set if item != move]
                        pos += 1
                elif move == 0:
                    if len(full_set) > 0:
                        player_set[0:0] = [random.choice(full_set)]
                        full_set = [item for item in full_set if item not in player_set]
                    else:
                        pass
                break

    if status == 'player':
        status = 'computer'
    elif status == 'computer':
        status = 'player'
