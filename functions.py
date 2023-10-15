def convert(s):
    # Переводит записи вида 10.5K, 11M, ... в числа
    s = s.replace(',', '.')
    s1 = ''
    k = 1
    for symbol in s:
        if symbol in '0123456789.':
            s1 += symbol
        elif symbol == 'K':
            k = 10 ** 3
        elif symbol == 'M':
            k = 10 ** 6
        elif symbol == 'B':
            k = 10 ** 9
        elif symbol == 'T':
            k = 10 ** 12
    result = float(s1) * k
    return result
