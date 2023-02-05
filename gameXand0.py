# Создаем игровое поле
gamepole = list(range(1,10))

def board(gamepole):
    print ("-" * 13)
    for i in range(3):
        print ("|", gamepole[0+i*3], "|", gamepole[1+i*3], "|", gamepole[2+i*3], "|")
        print ("-" * 13)
# Пишем функцию ввода данных игрока и проверки корректности ввода
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда ставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Введи число!!!")
            continue
            #ограничиваем ввод символов в игре в диапазоне от 1 до 9
        if player_answer >= 1 and player_answer <= 9:
            if (str(gamepole[player_answer-1]) not in "XO"):
                gamepole[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клетка уже занята")
        else:
            print ("Некорректный ввод. Введи число от 1 до 9!!!")

def check_win(gamepole):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if gamepole[each[0]] == gamepole[each[1]] == gamepole[each[2]]:
            return gamepole[each[0]]
    return False

def main(gamepole):
    counter = 0
    win = False
    while not win:
        board(gamepole)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(gamepole)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    board(gamepole)

main(gamepole)