import math
import  sys

def finder(a, b, c):
    roots = []
    if a != 0:
        d = b * b - 4 * a * c
        if d >= 0:
            x1 = ((-b + math.sqrt(d)) / (2 * a))
            x2 = ((-b - math.sqrt(d)) / (2 * a))
            if x1 >= 0:
                roots.append(math.sqrt(x1))
                roots.append(-math.sqrt(x1))
            if x2 >= 0:
                roots.append(math.sqrt(x2))
                roots.append(-math.sqrt(x2))
    else:
        if b != 0:
            x = -c / b
            if x >= 0:
                roots.append(math.sqrt(x))
                roots.append(-math.sqrt(x))
        elif c == 0:
            roots.append(0)
    return roots
def remove_duplicates(lst):
    return list(set(lst))

print("Введите коэффициенты биквадратного уравнения вида a*x^4+b*x^2+c=0:")

def read_coefficient(prompt):
    while True:
        try:
            coefficient = float(input(prompt))
            return coefficient
        except ValueError:
            print("Некорректное значение. Повторите ввод.")

def main():

    # Считывание коэффициентов A, B, C
    if len(sys.argv) > 1:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    else:
        print("Введите коэффициенты биквадратного уравнения вида a*x^4+b*x^2+c=0:")
        a = float(input("Введите коэффициент A: "))
        b = float(input("Введите коэффициент B: "))
        c = float(input("Введите коэффициент C: "))

    arr = finder(a, b, c)
    if arr is None:
        arr = []

    print("Корни биквадратного уравнения", a, "* x^4 + ", b, "* x^2 + ", c, " = 0:")
    remove_duplicates_flag = input("Хотите ли вы удалить дубликаты корней? (да/нет): ").strip().lower()
    if remove_duplicates_flag == "да":
        arr = remove_duplicates(arr)  # Удаление дубликатов
    arr.sort()
    if len(arr) != 0:
        print(arr)
    else:
        print("Нет корней.")

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()