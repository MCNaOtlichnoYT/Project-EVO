# Математический разнос режима Prison EVO (DiamondWorld)
# Программа создана для канала "Майнкрафт на отлично" исключительно в образовательных целях
# Данные взяты с вики https://dw.senshi.fun
# Данные актуальны на момент 12.30 10.09.2023, но смысл режима не изменится
# Для работы программы требуется Python 3 и библиотека matplotlib


import matplotlib.pyplot as plt
from functions import *
from fileparser import *


boost = 6 # Буст денег
bps = 10 # Blocks per second = Скорость добычи блоков


mines = get_mines()
levels = get_levels()
data = []
# data_i = [Уровень, Цена прокачки, Блоков требуется, Цена блока, Блоков на прокачку, Блоков на прокачку с бустом,
#           Блоков выкопано, Блоков выкопано с бустом, Времени потрачено, Времени потрачено с бустом]
data.append([1, 80, 20, 1])
data[0].append(data[0][1] / data[0][3])
data[0].append(data[0][4] / boost)
data[0].append(data[0][4])
data[0].append(data[0][5])
data[0].append(data[0][6] / bps)
data[0].append(data[0][7] / bps)


for i in range(1, len(mines)):
    new_line = [levels[i][0], levels[i][1], levels[i][2], mines[i][1]]
    new_line.append(levels[i][1] / mines[i][1])
    new_line.append(new_line[-1] / boost)
    new_line.append(new_line[-2] + data[i - 1][6])
    new_line.append(new_line[-1] / boost)
    new_line.append(new_line[-2] / bps)
    new_line.append(new_line[-2] / bps)
    data.append(new_line)


sign = {1: 'Цена повышения уровня',
        2: 'Требуется блоков для повышения',
        3: 'Цена блока',
        4: 'Нужно накопать на этом уровне',
        5: 'Нужно накопать на этом уровне (буст ' + str(boost) + 'x)',
        6: 'Выкопано блоков всего',
        7: 'Выкопано блоков всего (буст ' + str(boost) + 'x)',
        8: 'Время в игре, с',
        9: 'Время в игре, с (буст '+ str(boost) + 'x)'}
k = 9 # Выбор графика

x = [data[i][0] for i in range(len(data))]
y = [data[i][k] for i in range(len(data))]
plt.plot(x, y)
plt.title(sign[k])
plt.xlabel('Уровень')
plt.show()
