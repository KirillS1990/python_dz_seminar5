
'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
# def delete_word(text1, text2):
#     list1 = text1.split()
#     list2 = list(filter(lambda x: text2 not in x, list1))
#     text3 = ""
#     for i in list2:
#         text3 = text3 + " " + i
#     return(text3[1:])
    
# text1 = input('Введите текст: ')
# text2 = input('Введите часть слова, которое нужно удалить: ')

# print(delete_word(text1,text2))


'''
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''

# import random

# def imput_game_mode():
#     while True:
#         try:
#             game_mode = int(input('Введите 1 если хотите играть с ботом и 2 если хотите играть с человеком: '))
#             if 1 <= game_mode <=2:
#                 break
#             else:
#                 print('Вы ввели другое число. Попробуйте еще раз')
#         except ValueError:
#             print('Вы ввели не число. Попробуйте еще раз')
#     return game_mode


# def input_limit():
#     while True:
#         try:
#             limit = int(input('Введите максимальное количество конфет, которое будете забирать за раз: '))
#             if limit > 0:
#                 break
#             else:
#                 print('Количество должно быть больше ноля. Попробуйте еще раз')
#         except ValueError:
#             print('Вы ввели не число. Попробуйте еще раз')
#     return limit

# def input_total():
#     while True:
#         try:
#             total = int(input('Введите общее количество конфет: '))
#             if total > limit:
#                 break
#             else:
#                 print('Слишком мало конфет для этой игры. Попробуйте еще раз')
#         except ValueError:
#             print('Вы ввели не число. Попробуйте еще раз')
#     return total

# def draw():
#     queue = random.randint(1,2)
#     if queue == 1:
#         print('Первым ходит первый игрок')
#     else:
#         print('Первым ходит второй игрок')
#     return queue

# def step(total, limit, player):
#     if player == 1:
#         while True:
#             try:
#                 m = int(input(f'Первый игрок берет(не более {limit} конфет): '))
#                 if 0 < m < limit+1:
#                     break
#                 else:
#                     print(f'Введенное число {m} не входит в указанный диапазон (1-{limit}).\nПопробуйте еще раз')
#             except ValueError:
#                 print('Вы ввели не число. Попробуйте еще раз')
#     else:
#         while True:
#             try:
#                 m = int(input(f'Второй игрок берет(не более {limit} конфет): '))
#                 if 0 < m < limit+1:
#                     break
#                 else:
#                     print(f'Введенное число {m} не входит в указанный диапазон (1-{limit}).\nПопробуйте еще раз')
#             except ValueError:
#                 print('Вы ввели не число. Попробуйте еще раз')
#     total = total - m
#     print(f'Осталось конфет: {total}')
#     return total

# def step_bot(total, limit):
#     m = (total-1)%(limit+1)
#     total = total - m
#     print(f'Бот взял конфет: {m}')
#     print(f'Осталось конфет: {total}')
#     return total

# game_mode = imput_game_mode()
# limit = input_limit()
# total = input_total()

# if game_mode == 1:
#     player = 1
#     if total > limit:
#         while total > limit:
#             if player == 1:
#                 total = step(total, limit, player)
#                 player = 2
#             else:
#                 total = step_bot(total, limit)
#                 player = 1
#     if total <= limit:
#         while total > 0:
#             limit = total
#             if player == 1:
#                 total = step(total, limit, player)
#                 player = 2
#             else:
#                 total = step_bot(total, limit)
#                 player = 1
#     if player == 1:
#         print('Выиграл бот!')
#     else:
#         print ('Выиграл первый игрок!')
    
# else:
#     player = draw()
#     if total > limit:
#         while total > limit:
#             total = step(total, limit, player)
#             if player == 1:
#                 player = 2
#             else:
#                 player = 1
#     if total <= limit:
#         while total > 0:
#             limit = total
#             total = step(total, limit, player)
#             if player == 1:
#                 player = 2
#             else:
#                 player = 1
#     if player == 1:
#         print('Выиграл второй игрок!')
#     else:
#         print ('Выиграл первый игрок!')



'''
3. Создайте программу для игры в ""Крестики-нолики"".
'''

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")


'''
4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''

with open('decoded.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode_rle(my_text)
print(str_code)

with open('encoded.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print(str_decode)