from math import pi


def triangle():
    print("\nPodaj dane do obliczenia POLA TRÓJKĄTA")
    b = int(input("Długość podstawy : "))
    h = int(input("Wysokość : "))

    area = 0.5 * b * h
    print("Pole trójkąta to : ", area)

    print("Podaj dane do obliczenia OBWODU TRÓJKĄTA")
    a = int(input("Bok 1 : "))
    b = int(input("Bok 2 : "))
    c = int(input("Bok 3 : "))

    perimeter = a + b + c
    print("Obwód trójkąta to : ", perimeter)


def rectangle():
    a = int(input("\nBok a : "))
    b = int(input("Bok b : "))

    area = a * b
    print("Pole prostokąta to : ", area)
    perimeter = 2 * a + 2 * b
    print("Obwód prostokąta to : ", perimeter)


def square():
    a = int(input("\nBok : "))
    area = a ** 2
    print("Pole kwadratu to : ", area)
    perimeter = 4 * a
    print("Obwód kwadratu to : ", perimeter)


def circle():
    r = float(input("\nPodaj promień koła : "))
    area = pi * r ** 2
    print("Pole koła to : %.2f" % area)
    circumference = 2 * pi * r
    print("Obwód koła to : %.2f" % circumference)


def trapezoid():
    print("\nPodaj dane do obliczenia POLA TRAPEZU")
    height = float(input("Wysokość trapezu : "))
    base1 = float(input("Długość podstawy 1 : "))
    base2 = float(input("Długość podstawy 2 : "))
    area = ((base1 + base2) / 2) * height
    print("Pole trapezu to : %.2f" % area)
    print("Podaj dane do obliczenia OBWODU TRAPEZU")
    a = int(input("Bok 1 : "))
    b = int(input("Bok 2 : "))
    c = int(input("Bok 3 : "))
    d = int(input("Bok 4 : "))
    perimeter = a + b + c + d
    print("Obwód trapezu to : ", perimeter)


def creator():
    print('''\nINFORMACJE O AUTORZE:
    Kamil Krajewski
    Album: 24536 
        \n''')


def menu():
    print("\nWybierz akcje podając literę :")
    print("t - Trójkąt\np - prostokąt\nkw - kwadrat\nk - koło\ntr - trapez")
    print("c - aby zobaczyć informacje o twórcy")
    print("x - aby wyjść")

    while True:
        action = input()
        if action.lower() == "t".lower():
            triangle()
            menu()
        elif action.lower() == "p".lower():
            rectangle()
            menu()
        elif action.lower() == "kw".lower():
            square()
            menu()
        elif action.lower() == "k".lower():
            circle()
            menu()
        elif action.lower() == "tr".lower():
            trapezoid()
            menu()
        elif action.lower() == "c".lower():
            creator()
            menu()
        elif action.lower() == "x".lower():
            print("Wybrano wyjście. Do zobaczenia")
            break


if __name__ == "__main__":
    menu()
