from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests

def main():
    width = 16
    height = 16
    radius = 16
    side = 16

    blue_rectangle = Rectangle(width, height, "blue")
    green_circle = Circle(radius, "green")
    red_square = Square(side, "red")

    print(blue_rectangle.width)
    # Выводим информацию о фигурах
    print(blue_rectangle)
    print(green_circle)
    print(red_square)

    url = 'https://www.wikipedia.org'

    # Выполнение GET-запроса
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Ошибка: Статус-код {response.status_code}")


if __name__ == "__main__":
    main()
