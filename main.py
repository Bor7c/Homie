import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    fl = False
    while fl == False:
        try:
            float(coef_str)
        except:
            print("Error")
            fl = False
            coef_str = input()
        else:
            coef = float(coef_str)
            fl = True
    return float(coef_str)


def get_roots(a, b, c):
    result = []
    if a == 0:
        return result
    if (a == 0 and b == 0 and c == 0):
        return result
    if (a > 0 and b > 0 and c > 0):
        return result
    if (a == 0 and b == 0):
        return result
    if (c == 0) and (b == 0 or (b / a > 0)):
        result.append(0)
    if (c == 0) and ((b / a < 0)):
        result.append(0)
        root11 = math.sqrt(abs(b / a))
        root12 = -1 * math.sqrt(abs(b / a))
        result.append(root11)
        result.append(root12)
        return result
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if (root > 0):
            root1 = math.sqrt(root)
            root2 = -1 * math.sqrt(root)
            result.append(root1)
            result.append(root2)
            return result
        elif (root < 0):
            return result
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 < 0 and root2 < 0:
            return result
        if root1 > 0 and root2 > 0:
            root11 = math.sqrt(root1)
            root12 = -1 * math.sqrt(root1)
            result.append(root11)
            result.append(root12)
            root21 = math.sqrt(root2)
            root22 = -1 * math.sqrt(root2)
            result.append(root11)
            result.append(root12)
            return result
        if root1 > 0 and root2 < 0:
            root11 = math.sqrt(root1)
            root12 = -1 * math.sqrt(root1)
            result.append(root11)
            result.append(root12)
            return result
        if root1 < 0 and root2 > 0:
            root21 = math.sqrt(root2)
            root22 = -1 * math.sqrt(root2)
            result.append(root11)
            result.append(root12)
            return result
    elif D < 0.0:
        return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Три корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
