# короче, нужно проверить функцией эти координаты,
# другой функцией определить их значение и занести их в массив от 1 до 36
# третьей функцией перебрать массив, меняя поочередно местами фишки, добавляя возможные комбинации в другой массив
# (или чекая их из другого массива)
# четвертой функцией перебрать получившийся массив возможных комбинаций выбрав приоритетный
# и наконец пятой функцией запустить одну из функций по движению мышкой соответствующих пикселей
# или как-то так, я хз, спать хочу
# и вообще, бот должен был быть парсером





#ВОЗМОЖНО работу бота ускорит проведение проверки на ноль до проведения проверки на 5/4/3 в ряд

import time
import pyautogui
import keyboard
import pytesseract
from PIL import Image, ImageDraw
from pyautogui import ImageNotFoundException

box_list = []
box_list_print = []
box_list_print_vert = []
box_list_print_alt = []
box_list_print_alt2 = []

coord_list = []
coord_list_print = []
coord_list_print_vert = []
coord_list_print_alt = []
coord_list_print_alt2 = []

box_log = [[[], [], [], [], []],
           [[], [], [], [], []],
           [[], [], [], [], []],
           [[], [], [], [], []],
           [[], [], [], [], []],
           [[], [], [], [], []]]

log0 = box_log[0]
log1 = box_log[1]
log2 = box_log[2]
log3 = box_log[3]
log4 = box_log[4]
log5 = box_log[5]

box_log_vert = [[[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []]]

log0_v = box_log_vert[0]
log1_v = box_log_vert[1]
log2_v = box_log_vert[2]
log3_v = box_log_vert[3]
log4_v = box_log_vert[4]
log5_v = box_log_vert[5]

region_list = [(465, 115, 80, 80), (510, 115, 80, 80), (575, 115, 80, 80), (628, 115, 80, 80), (680, 115, 80, 80), (740, 115, 80, 80),
               (465, 180, 80, 80), (510, 180, 80, 80), (575, 180, 80, 80), (628, 180, 80, 80), (680, 180, 80, 80), (740, 180, 80, 80),
               (465, 240, 80, 80), (510, 240, 80, 80), (575, 240, 80, 80), (628, 240, 80, 80), (680, 240, 80, 80), (740, 240, 80, 80),
               (465, 300, 80, 80), (510, 300, 80, 80), (575, 300, 80, 80), (628, 300, 80, 80), (680, 300, 80, 80), (740, 300, 80, 80),
               (465, 340, 80, 80), (510, 340, 80, 80), (575, 340, 80, 80), (628, 340, 80, 80), (680, 340, 80, 80), (740, 340, 80, 80),
               (465, 390, 80, 80), (510, 390, 80, 80), (575, 390, 80, 80), (628, 390, 80, 80), (680, 390, 80, 80), (740, 390, 80, 80)]

# mouth_coord = (827, 163, 22, 25) #28/33

def check_my_turn():
    try:
        screenshot_player = pyautogui.pixel(436, 185)
        screenshot_vrag = pyautogui.pixel(838, 183)
        print(screenshot_player[0], screenshot_vrag[0])
        if screenshot_player[0] >= 200 and screenshot_vrag[0] <= 10:
            print('Ход игрока')
            return True
        elif screenshot_player[0] <= 10 and screenshot_vrag[0] >= 200:
            print('Ход противника')
            time.sleep(5)
            return False
        elif screenshot_player[0] >= 200 and screenshot_vrag[0] >= 200:
            time.sleep(2)
            print('Значение обоих таймбоксов активно')
            pass
        elif screenshot_player[0] <= 10 and screenshot_vrag[0] <= 10:
            time.sleep(2)
            print('Значение обоих таймбоксов не активно')
            pass
        else:
            time.sleep(2)
            print('Таймбоксы не найдены')
            pass


    except ImageNotFoundException:
        print('Картинка не обнаружена')
        return True
def record(reg_l, box_l, coord_l):
    for x in reg_l:
        try:
            skull = pyautogui.locateOnScreen('Skull.png', region=(x), confidence=0.6)
            point_s = pyautogui.center(skull)
            x_s, y_s = point_s
            coord_l.append({1:x_s, 2:y_s})
            box_l.append('S')
        except ImageNotFoundException:
            try:
                boots = pyautogui.locateOnScreen('Boots.png', region=(x), confidence=0.6)
                point_b = pyautogui.center(boots)
                x_b, y_b = point_b
                coord_l.append({1:x_b, 2:y_b})
                box_l.append('B')
            except ImageNotFoundException:
                try:
                    listt = pyautogui.locateOnScreen('List.png', region=(x), confidence=0.6)
                    point_l = pyautogui.center(listt)
                    x_l, y_l = point_l
                    coord_l.append({1:x_l, 2:y_l})
                    box_l.append('L')
                except ImageNotFoundException:
                    try:
                        umbrella = pyautogui.locateOnScreen('Umbrella.png', region=(x), confidence=0.6)
                        point_u = pyautogui.center(umbrella)
                        x_u, y_u = point_u
                        coord_l.append(({1:x_u, 2:y_u}))
                        box_l.append('U')
                    except ImageNotFoundException:
                        box_l.append('N')
                        coord_l.append({0:0})

def horizontal_box(box_l, box_lp):
    for i in range(0, len(box_l), 6):
        chunk = box_l[i:i+6]
        box_lp.append(chunk)

def show_box(box_lp):
    [print(x) for x in box_lp]

def check_hor_combinations(box_lp, box_lg, word_iter, str_iter):
    for x in box_lp:
        try:
            for i in range(len(x)):
                if x[i] == x[i+1] == x[i+2] == x[i+3] == x[i+4]:
                    if x[i] != 'N':
                        print(f'1 Обнаружено "Пять {x[i]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(5)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[0] != x[1] and x[i-5] == x[i-4] == x[i-3] == x[i-2] == x[i-1]:
                    if x[i-5] != 'N':
                        print(f'2 Обнаружено "Пять {x[i-5]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(5)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[i+1] == x[i+2] == x[i+3]:
                    if x[i] != 'N':
                        print(f'1 Обнаружено "Четыре {x[i]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(4)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[0] != x[1] and x[i - 4] == x[i - 3] == x[i - 2] == x[i - 1]:
                    if x[i-4] != 'N':
                        print(f'2 Обнаружено "Четыре {x[i-4]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(4)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[i+1] == x[i+2]:
                    if x[i] != 'N':
                        print(f'1 Обнаружено "Три {x[i]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(3)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[0] != x[1] and x[i - 3] == x[i - 2] == x[i - 1]:
                    if x[i-3] != 'N':
                        print(f'2 Обнаружено "Три {x[i-3]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(3)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                else:
                    continue
        except IndexError:
            pass
    x0 = box_lp[0]
    x1 = box_lp[1]
    x2 = box_lp[2]
    x3 = box_lp[3]
    x4 = box_lp[4]
    x5 = box_lp[5]
    for y in range(0, 6):
        if x0[y] == x1[y] == x2[y] == x3[y] == x4[y]:
            if x0[y] != 'N':
                print(f'H1 Обнаружено "Пять {x0[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(5)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x1[y] == x2[y] == x3[y] == x4[y] == x5[y]:
            if x1[y] != 'N':
                print(f'H2 Обнаружено "Пять {x1[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(5)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x0[y] == x1[y] == x2[y] == x3[y]:
            if x0[y] != 'N':
                print(f'H1 Обнаружено "Четыре {x0[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(4)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x1[y] == x2[y] == x3[y] == x4[y]:
            if x0[y] != 'N':
                print(f'H2 Обнаружено "Четыре {x1[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(4)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x2[y] == x3[y] == x4[y] == x5[y]:
            if x2[y] != 'N':
                print(f'H3 Обнаружено "Четыре {x2[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(4)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x0[y] == x1[y] == x2[y]:
            if x0[y] != 'N':
                print(f'H1 Обнаружено "Три {x0[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x1[y] == x2[y] == x3[y]:
            if x1[y] != 'N':
                print(f'H2 Обнаружено "Три {x1[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x2[y] == x3[y] == x4[y]:
            if x2[y] != 'N':
                print(f'H3 Обнаружено "Три {x2[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x3[y] == x4[y] == x5[y]:
            if x3[y] != 'N':
                print(f'H4 Обнаружено "Три {x3[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        else:
            continue



def vertical_box(box_l, box_la, box_la2, box_lpv):
    for a in range(0, len(box_l), 6):
        chunk = box_l[a:a+6:6]
        box_la.append(chunk)
    for a in range(0, len(box_l), 6):
        chunk = box_l[a+1:a+7:6]
        box_la.append(chunk)
    for a in range(0, len(box_l), 6):
        chunk = box_l[a+2:a+8:6]
        box_la.append(chunk)
    for a in range(0, len(box_l), 6):
        chunk = box_l[a+3:a+9:6]
        box_la.append(chunk)
    for a in range(0, len(box_l), 6):
        chunk = box_l[a+4:a+10:6]
        box_la.append(chunk)
    for a in range(0, len(box_l), 6):
        chunk = box_l[a+5:a+11:6]
        box_la.append(chunk)

    for a in box_la:
        for b in a:
            box_la2.append(b)

    for i in range(0, len(box_la2), 6):
        chunk = box_la2[i:i+6]
        box_lpv.append(chunk)


def check_vert_combinations(box_lp, box_lg, word_iter, str_iter):
    for x in box_lp:
        try:
            for i in range(len(x)):
                if x[i] == x[i+1] == x[i+2] == x[i+3] == x[i+4]:
                    if x[i] != 'N':
                        print(f'1 Обнаружено "Пять {x[i]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(5)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[0] != x[1] and x[i - 5] == x[i - 4] == x[i - 3] == x[i - 2] == x[i - 1]:
                    if x[i-5] != 'N':
                        print(f'2 Обнаружено "Пять {x[i-5]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(5)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[i+1] == x[i+2] == x[i+3]:
                    if x[i] != 'N':
                        print(f'1 Обнаружено "Четыре {x[i]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(4)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[0] != x[1] and x[i-4] == x[i-3] == x[i-2] == x[i-1]:
                    if x[i-4] != 'N':
                        print(f'2 Обнаружено "Четыре {x[i-4]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(4)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[i+1] == x[i+2]:
                    if x[i] != 'N':
                        print(f'1 Обнаружено "Три {x[i]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(3)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                elif x[i] == x[0] != x[1] and x[i-3] == x[i-2] == x[i-1]:
                    if x[i-3] != 'N':
                        print(f'2 Обнаружено "Три {x[i-3]} в ряд"')
                        b_log = box_lg[str_iter]
                        str_it = b_log[word_iter]
                        str_it.append(3)
                        [print(x) for x in box_lp]
                        print(f'\n')
                        break
                else:
                    continue
        except IndexError:
            pass
    x0 = box_lp[0]
    x1 = box_lp[1]
    x2 = box_lp[2]
    x3 = box_lp[3]
    x4 = box_lp[4]
    x5 = box_lp[5]
    for y in range(0, 6):
        if x0[y] == x1[y] == x2[y] == x3[y] == x4[y]:
            if x0[y] != 'N':
                print(f'V1 Обнаружено "Пять {x0[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(5)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x1[y] == x2[y] == x3[y] == x4[y] == x5[y]:
            if x1[y] != 'N':
                print(f'V2 Обнаружено "Пять {x1[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(5)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x0[y] == x1[y] == x2[y] == x3[y]:
            if x0[y] != 'N':
                print(f'V1 Обнаружено "Четыре {x0[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(4)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x1[y] == x2[y] == x3[y] == x4[y]:
            if x1[y] != 'N':
                print(f'V2 Обнаружено "Четыре {x1[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(4)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x2[y] == x3[y] == x4[y] == x5[y]:
            if x2[y] != 'N':
                print(f'V3 Обнаружено "Четыре {x2[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(4)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x0[y] == x1[y] == x2[y]:
            if x0[y] != 'N':
                print(f'V1 Обнаружено "Три {x0[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x1[y] == x2[y] == x3[y]:
            if x1[y] != 'N':
                print(f'V2 Обнаружено "Три {x1[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x2[y] == x3[y] == x4[y]:
            if x2[y] != 'N':
                print(f'V3 Обнаружено "Три {x2[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        elif x3[y] == x4[y] == x5[y]:
            if x3[y] != 'N':
                print(f'V4 Обнаружено "Три {x3[y]} в ряд" вертикально')
                b_log = box_lg[str_iter]
                str_it = b_log[word_iter]
                str_it.append(3)
                [print(x) for x in box_lp]
                print(f'\n')
                break
        else:
            continue

def enum_combinations(box_lp,  box_lg, chc):
    str_iter = 0
    for sixlist in box_lp:
        try:
            # print(f'\nИтерация 1-2 функции {chc.__name__}\n')
            sixlist[0], sixlist[1] = sixlist[1], sixlist[0]
            word_iter = 0
            chc(box_lp, box_lg, word_iter, str_iter)
            # print(f'\nИтерация 2-3 функции {chc.__name__}\n')
            sixlist[0], sixlist[1] = sixlist[1], sixlist[0]
            sixlist[1], sixlist[2] = sixlist[2], sixlist[1]
            word_iter = 1
            chc(box_lp, box_lg, word_iter, str_iter)
            # print(f'\nИтерация 3-4 функции {chc.__name__}\n')
            sixlist[1], sixlist[2] = sixlist[2], sixlist[1]
            sixlist[2], sixlist[3] = sixlist[3], sixlist[2]
            word_iter = 2
            chc(box_lp, box_lg, word_iter, str_iter)
            # print(f'\nИтерация 4-5 функции {chc.__name__}\n')
            sixlist[2], sixlist[3] = sixlist[3], sixlist[2]
            sixlist[3], sixlist[4] = sixlist[4], sixlist[3]
            word_iter = 3
            chc(box_lp, box_lg, word_iter, str_iter)
            # print(f'\nИтерация 5-6 функции {chc.__name__}\n')
            sixlist[3], sixlist[4] = sixlist[4], sixlist[3]
            sixlist[4], sixlist[5] = sixlist[5], sixlist[4]
            word_iter = 4
            chc(box_lp, box_lg, word_iter, str_iter)
            # print(f'\nИтерации функции {chc.__name__} завершены \n')
            sixlist[4], sixlist[5] = sixlist[5], sixlist[4]
            str_iter = str_iter + 1
        except IndexError as ex:
            print(f'Цикл завершился ОШИБКОЙ IndexError {ex} на итерации str_iter {str_iter}')
        finally:
            #print(f'Переменная str_iter окончилась итерацией {str_iter}')
            pass


def if_not_empty(mb_empty_list):
    if mb_empty_list:
        return max(mb_empty_list)
    else:
        return 0

def find_my_index(list_of_lists, value):
    try:
        for iter in list_of_lists:
            for iter2 in iter:
                if value in iter2:
                    return(list_of_lists.index(iter)), (iter.index(iter2))
                else:
                    continue
    finally:
        pass

def play_game(vertical, coord_box, coord_box_vert, log_number, word_number):
    try:
        if vertical is False:
            move = coord_box[log_number]
            move_xy = move[word_number]
            x = move_xy.get(1)
            y = move_xy.get(2)
            x_plus = x + 50
            pyautogui.moveTo(x, y, 0.5)
            pyautogui.dragTo(x_plus, y, duration=0.5, button='left')
            pyautogui.moveTo(640, 510)
        else:
            move = coord_box_vert[log_number]
            move_xy = move[word_number]
            x = move_xy.get(1)
            y = move_xy.get(2)

            y_plus = y + 50
            pyautogui.moveTo(x, y_plus, 0.5)
            pyautogui.dragTo(x, y, duration=0.5, button='left')
            pyautogui.moveTo(640, 510)
    except TypeError as ex:
        if vertical is False:
            move = coord_box[log_number]
            move_xy = move[word_number]
            x = move_xy.get(1)
            y = move_xy.get(2)
            x_plus = x + 50
            pyautogui.moveTo(x_plus, y, 0.5)
            pyautogui.dragTo(x, y, duration=0.5, button='left')
            pyautogui.moveTo(640, 510)
        else:
            move = coord_box_vert[log_number]
            move_xy = move[word_number]
            x = move_xy.get(1)
            y = move_xy.get(2)

            y_plus = y + 50
            pyautogui.moveTo(x, y, 0.5)
            pyautogui.dragTo(x, y_plus, duration=0.5, button='left')
            pyautogui.moveTo(640, 510)
        pass
def max_comb(lg0, lg1, lg2, lg3, lg4, lg5, lgv0, lgv1, lgv2, lgv3, lgv4, lgv5, if_not_empty, find_m_index, play_game):
    max_str00 = if_not_empty(lg0[0])
    max_str01 = if_not_empty(lg0[1])
    max_str02 = if_not_empty(lg0[2])
    max_str03 = if_not_empty(lg0[3])
    max_str04 = if_not_empty(lg0[4])
    max_str10 = if_not_empty(lg1[0])
    max_str11 = if_not_empty(lg1[1])
    max_str12 = if_not_empty(lg1[2])
    max_str13 = if_not_empty(lg1[3])
    max_str14 = if_not_empty(lg1[4])
    max_str20 = if_not_empty(lg2[0])
    max_str21 = if_not_empty(lg2[1])
    max_str22 = if_not_empty(lg2[2])
    max_str23 = if_not_empty(lg2[3])
    max_str24 = if_not_empty(lg2[4])
    max_str30 = if_not_empty(lg3[0])
    max_str31 = if_not_empty(lg3[1])
    max_str32 = if_not_empty(lg3[2])
    max_str33 = if_not_empty(lg3[3])
    max_str34 = if_not_empty(lg3[4])
    max_str40 = if_not_empty(lg4[0])
    max_str41 = if_not_empty(lg4[1])
    max_str42 = if_not_empty(lg4[2])
    max_str43 = if_not_empty(lg4[3])
    max_str44 = if_not_empty(lg4[4])
    max_str50 = if_not_empty(lg5[0])
    max_str51 = if_not_empty(lg5[1])
    max_str52 = if_not_empty(lg5[2])
    max_str53 = if_not_empty(lg5[3])
    max_str54 = if_not_empty(lg5[4])
    max_str_v00 = if_not_empty(lgv0[0])
    max_str_v01 = if_not_empty(lgv0[1])
    max_str_v02 = if_not_empty(lgv0[2])
    max_str_v03 = if_not_empty(lgv0[3])
    max_str_v04 = if_not_empty(lgv0[4])
    max_str_v10 = if_not_empty(lgv1[0])
    max_str_v11 = if_not_empty(lgv1[1])
    max_str_v12 = if_not_empty(lgv1[2])
    max_str_v13 = if_not_empty(lgv1[3])
    max_str_v14 = if_not_empty(lgv1[4])
    max_str_v20 = if_not_empty(lgv2[0])
    max_str_v21 = if_not_empty(lgv2[1])
    max_str_v22 = if_not_empty(lgv2[2])
    max_str_v23 = if_not_empty(lgv2[3])
    max_str_v24 = if_not_empty(lgv2[4])
    max_str_v30 = if_not_empty(lgv3[0])
    max_str_v31 = if_not_empty(lgv3[1])
    max_str_v32 = if_not_empty(lgv3[2])
    max_str_v33 = if_not_empty(lgv3[3])
    max_str_v34 = if_not_empty(lgv3[4])
    max_str_v40 = if_not_empty(lgv4[0])
    max_str_v41 = if_not_empty(lgv4[1])
    max_str_v42 = if_not_empty(lgv4[2])
    max_str_v43 = if_not_empty(lgv4[3])
    max_str_v44 = if_not_empty(lgv4[4])
    max_str_v50 = if_not_empty(lgv5[0])
    max_str_v51 = if_not_empty(lgv5[1])
    max_str_v52 = if_not_empty(lgv5[2])
    max_str_v53 = if_not_empty(lgv5[3])
    max_str_v54 = if_not_empty(lgv5[4])
    log00 = [max_str00, max_str01, max_str02, max_str03, max_str04]
    log01 = [max_str10, max_str11, max_str12, max_str13, max_str14]
    log02 = [max_str20, max_str21, max_str22, max_str23, max_str24]
    log03 = [max_str30, max_str31, max_str32, max_str33, max_str34]
    log04 = [max_str40, max_str41, max_str42, max_str43, max_str44]
    log05 = [max_str50, max_str51, max_str52, max_str53, max_str54]
    log_v00 = [max_str_v00, max_str_v01, max_str_v02, max_str_v03, max_str_v04]
    log_v01 = [max_str_v10, max_str_v11, max_str_v12, max_str_v13, max_str_v14]
    log_v02 = [max_str_v20, max_str_v21, max_str_v22, max_str_v23, max_str_v24]
    log_v03 = [max_str_v30, max_str_v31, max_str_v32, max_str_v33, max_str_v34]
    log_v04 = [max_str_v40, max_str_v41, max_str_v42, max_str_v43, max_str_v44]
    log_v05 = [max_str_v50, max_str_v51, max_str_v52, max_str_v53, max_str_v54]
    log00_max = max(log00)
    log01_max = max(log01)
    log02_max = max(log02)
    log03_max = max(log03)
    log04_max = max(log04)
    log05_max = max(log05)
    log_v00_max = max(log_v00)
    log_v01_max = max(log_v01)
    log_v02_max = max(log_v02)
    log_v03_max = max(log_v03)
    log_v04_max = max(log_v04)
    log_v05_max = max(log_v05)
    logs_box = [log00_max, log01_max, log02_max, log03_max, log04_max, log05_max]
    logs_box_v = [log_v00_max, log_v01_max, log_v02_max, log_v03_max, log_v04_max, log_v05_max]
    logs_box_max = max(logs_box)
    logs_box_v_max = max(logs_box_v)
    find_index_of_log = find_m_index(box_log, logs_box_max)
    find_index_of_log_vert = find_m_index(box_log_vert, logs_box_v_max)
    f = False
    t = True
    try:
        if logs_box_max != logs_box_v_max:
            print(f'Логбоксы НЕРАВНЫ!')
            if logs_box_max > logs_box_v_max:
                print(f'Максимальная комбинация "{logs_box_max} в ряд"!')
                print(f'Значение находится в log_box_max в логе {find_index_of_log[0]}, '
                      f'в ротации {find_index_of_log[1]}')
                return play_game(f, coord_list_print, coord_list_print_vert, find_index_of_log[0], find_index_of_log[1])
            else:
                print(f'Максимальная комбинация "{logs_box_v_max} в ряд"!')
                print(f'Значение находится в log_box_v_max в логе {find_index_of_log_vert[0]}, '
                      f'в ротации {find_index_of_log_vert[1]}')
                play_game(t, coord_list_print, coord_list_print_vert, find_index_of_log_vert[0], find_index_of_log_vert[1])
        else:
            print(f'Логбоксы равны "{logs_box_max} в ряд"')
            print(f'Значение находится в log_box_max в логе {find_index_of_log[0]}, '
                      f'в ротации {find_index_of_log[1]}')
            return play_game(f, coord_list_print, coord_list_print_vert, find_index_of_log[0], find_index_of_log[1])
    finally:
        pass





def massive_clear():
    box_list.clear()
    box_list_print.clear()
    box_list_print_vert.clear()
    box_list_print_alt.clear()
    box_list_print_alt2.clear()
    coord_list.clear()
    coord_list_print.clear()
    coord_list_print_vert.clear()
    coord_list_print_alt.clear()
    coord_list_print_alt2.clear()



while True:
    check_my_turn()
    while check_my_turn() is True:
        try:
            time.sleep(4)
            start_time = time.time()
            record(region_list, box_list, coord_list)
            horizontal_box(coord_list, coord_list_print)
            print(f'\nCoordinate box')
            show_box(coord_list_print)
            vertical_box(coord_list, coord_list_print_alt, coord_list_print_alt2, coord_list_print_vert)
            print(f'\nCoordinate vertical box')
            show_box(coord_list_print_vert)
            print(f'\n')
            horizontal_box(box_list, box_list_print)
            print(f'\nHorizontal box')
            show_box(box_list_print)
            print(f'\n')
            vertical_box(box_list, box_list_print_alt, box_list_print_alt2, box_list_print_vert)
            print(f'\nVertical box')
            show_box(box_list_print_vert)
            print(f'\n')
            enum_combinations(box_list_print, box_log, check_hor_combinations)
            enum_combinations(box_list_print_vert, box_log_vert, check_vert_combinations)
            max_comb(log0, log1, log2, log3, log4, log5,
                     log0_v, log1_v, log2_v, log3_v, log4_v, log5_v,
                     if_not_empty, find_my_index, play_game)
            print(f'box_log {box_log}')
            print(f'box_log_vert {box_log_vert}')
            print('Цикл завершен. Нажмите любую клавишу для повтора.')
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Бот прошел цикл за {round(elapsed_time, 2)}')
            # keyboard.read_key()
            massive_clear()
            box_log = [[[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []]]
            box_log_vert = [[[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []]]
            log0 = box_log[0]
            log1 = box_log[1]
            log2 = box_log[2]
            log3 = box_log[3]
            log4 = box_log[4]
            log5 = box_log[5]
            log0_v = box_log_vert[0]
            log1_v = box_log_vert[1]
            log2_v = box_log_vert[2]
            log3_v = box_log_vert[3]
            log4_v = box_log_vert[4]
            log5_v = box_log_vert[5]
            time.sleep(3)
            print('Цикл запущен.')
        except Exception as ex:
            print('Цикл завершился ОШИБКОЙ!')
            print(f'{ex}')
            pyautogui.click(440, 250, button="left")
            pyautogui.moveTo(1, 1, duration=0.1)
            massive_clear()
            box_log = [[[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []],
                       [[], [], [], [], []]]
            box_log_vert = [[[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []],
                            [[], [], [], [], []]]
            log0 = box_log[0]
            log1 = box_log[1]
            log2 = box_log[2]
            log3 = box_log[3]
            log4 = box_log[4]
            log5 = box_log[5]
            log0_v = box_log_vert[0]
            log1_v = box_log_vert[1]
            log2_v = box_log_vert[2]
            log3_v = box_log_vert[3]
            log4_v = box_log_vert[4]
            log5_v = box_log_vert[5]
            time.sleep(1)
            pass
        finally:
            check_my_turn()
