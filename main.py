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

    scores.sort(reverse=True)
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


def move_maker(p_s, f_s, s_s, pos_v, stat):
    if stat == 'computer':
        input("\nStatus: Computer is about to make a move. Press Enter to continue...\n")
    elif stat == 'player':
        print("\nStatus: It's your turn to make a move. Enter your command.")

    while True:
        if stat == 'computer':
            m_v = ai_picker(p_s, s_s)
        elif stat == 'player':
            m_v = input()
        if str(m_v) not in [str(i) for i in range(-len(p_s), len(p_s) + 1)]:
            print("Invalid input. Please try again.")
        elif int(m_v) > 0 and (p_s[abs(int(m_v)) - 1][0] != s_s[-1][1]
                               and p_s[abs(int(m_v)) - 1][1] != s_s[-1][1]):
            print("Illegal move. Please try again.")
        elif int(m_v) < 0 and (p_s[abs(int(m_v)) - 1][0] != s_s[0][0] and p_s[abs(int(m_v)) - 1][1] != s_s[0][0]):
            print("Illegal move. Please try again.")

        else:
            m_v = int(m_v)
            if m_v > 0:
                if p_s[abs(int(m_v)) - 1][0] == s_s[-1][1]:
                    m_v = p_s[abs(m_v) - 1]
                    s_s.extend([m_v])
                    p_s = [item for item in p_s if item != m_v]
                    pos_v += 1
                elif p_s[abs(int(m_v)) - 1][1] == s_s[-1][1]:
                    m_v = p_s[abs(m_v) - 1]
                    m_v.reverse()
                    s_s.extend([m_v])
                    p_s = [item for item in p_s if item != m_v]
                    pos_v += 1
            elif m_v < 0:
                if p_s[abs(int(m_v)) - 1][1] == s_s[0][0]:
                    m_v = p_s[abs(m_v) - 1]
                    s_s[0:0] = [m_v]
                    p_s = [item for item in p_s if item != m_v]
                    pos_v += 1
                elif p_s[abs(int(m_v)) - 1][0] == s_s[0][0]:
                    m_v = p_s[abs(m_v) - 1]
                    m_v.reverse()
                    s_s[0:0] = [m_v]
                    p_s = [item for item in p_s if item != m_v]
                    pos_v += 1
            elif m_v == 0:
                if len(f_s) > 0:
                    p_s[0:0] = [random.choice(f_s)]
                    f_s = [item for item in f_s if item not in p_s]
                else:
                    pass
            break
    return p_s, f_s, s_s, pos_v


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
        computer_set, full_set, snake, pos = move_maker(computer_set, full_set, snake, pos, status)

    elif status == 'player':
        player_set, full_set, snake, pos = move_maker(player_set, full_set, snake, pos, status)

    if status == 'player':
        status = 'computer'
    elif status == 'computer':
        status = 'player'
