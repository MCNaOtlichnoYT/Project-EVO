from functions import *


def process_l(raw_elem):
    elem = [int(raw_elem[0]), convert(raw_elem[1]), convert(raw_elem[2])]
    return elem


def read_levels():
    # Составляет список уровней и стоимости их прокачки
    f = open('levels_wiki.txt', 'r')
    result = []
    for line in f.readlines():
        line_s = line.strip().split()
        result.append(process_l(line_s[0:3]))
        if line_s[4:7][0] != '238':
            result.append(process_l(line_s[4:7]))
    result.sort(key=lambda x: x[0])
    return result


def move_levels(data):
    # Сдвигает список уровней на 1, чтобы уровню соответствовала цена перехода на следующий
    levels = []
    for i in range(len(data) - 1):
        elem = [data[i][0], data[i + 1][1], data[i + 1][2]]
        levels.append(elem)
    return levels


def get_levels():
    # Дает список уровней, цен и блоков для повышения
    return move_levels(read_levels())


def process_m(raw_elem):
    elem = [int(raw_elem[0]), convert(raw_elem[1])]
    return elem


def get_mines():
    # Дает список уровней и цен за блок (средних)
    f = open('mines_wiki.txt', 'r')
    result = []
    for raw_line in f.readlines():
        raw_line = raw_line.strip().split()
        line = process_m(raw_line)
        if line[0] == 1:
            result.append(line)
        elif line[0] - 1 == result[-1][0]:
            result.append(line)
        else:
            new_line = result[-1].copy()
            new_line[0] += 1
            result.append(new_line)
            result.append(line)
    for i in range(446, 475):
        result.append([i, 17300000.0])
    return result
