number_of_sticks = 10
player_turn = 1

while number_of_sticks > 0:
    print(f'Сколько палочек вы возьмете? Осталось {number_of_sticks}')
    taken = int(input())

    if taken < 1 or taken > 3:
        print(f'Вы взяли {taken} палочек:) Можете взять 1,2,3 палочки!')
        continue
    number_of_sticks -= taken
    print(f'Палочек взято: {taken}\n')

    if number_of_sticks <= 0:
        print(f'Нет больше палочек в игре. \n Игрок {player_turn} проиграл!')

    player_turn = 1 if player_turn == 2 else 2
