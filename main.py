from math import pi, sqrt
import matplotlib.pyplot as plt


def triangle():
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.title("TRÓJKĄT")

    print("\nPodaj współrzędne TRÓJKĄTA")
    a = (input("a(x,y) : ").split(","))
    b = (input("b(x,y) : ").split(","))
    c = (input("c(x,y) : ").split(","))

    x = [int(a[0]), int(b[0]), int(c[0]), int(a[0])]
    y = [int(a[1]), int(b[1]), int(c[1]), int(a[1])]

    plt.plot(x, y)

    ab = sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
    bc = sqrt((x[2] - x[1]) ** 2 + (y[2] - y[1]) ** 2)
    ca = sqrt((x[3] - x[2]) ** 2 + (y[3] - y[2]) ** 2)

    perimeter = ab + bc + ca
    print("Obwód trójkąta to : ", perimeter)

    half_perimeter = perimeter / 2
    area = sqrt(half_perimeter * (half_perimeter - ab) * (half_perimeter - bc) * (half_perimeter - ca))
    print("Pole trójkąta to : ", area)
    plt.show()


def rectangle():
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.title("PROSTOKĄT")

    print("\nPodaj współrzędne dwóch boków PROSTOKĄTA")
    a = (input("a(x,y) : ").split(","))
    b = (input("b(x,y) : ").split(","))
    c = (input("c(x,y) : ").split(","))

    x = [int(a[0]), int(b[0]), int(c[0]), int(c[0]), int(a[0])]
    y = [int(a[1]), int(b[1]), int(c[1]), int(a[1]), int(a[1])]

    plt.plot(x, y)

    ab = sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
    bc = sqrt((x[2] - x[1]) ** 2 + (y[2] - y[1]) ** 2)

    area = ab * bc
    print("Pole prostokąta to : ", area)
    perimeter = 2 * ab + 2 * bc
    print("Obwód prostokąta to : ", perimeter)
    plt.show()


def square():
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.title("KWADRAT")

    print("\nPodaj współrzędne boku KWADRATU")
    a = (input("a(x,y) : ").split(","))
    b = (input("b(x,y) : ").split(","))
    ab = sqrt((int(b[0]) - int(a[0])) ** 2 + (int(b[1]) - int(a[1])) ** 2)
    c = [int(a[0]) + ab, int(b[1])]

    x = [int(a[0]), int(b[0]), int(b[1]), int(c[0]), int(a[0])]
    y = [int(a[1]), int(b[1]), int(c[1]), int(a[1]), int(a[0])]

    plt.plot(x, y)

    area = ab ** 2
    print("Pole kwadratu to : ", area)
    perimeter = 4 * ab
    print("Obwód kwadratu to : ", perimeter)

    plt.show()


def circle():
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.title("KOŁO")
    figure, axes = plt.subplots()

    r = int(input("\nPodaj promień koła : "))
    center = (input("Podaj środek koła (x,y): ").split(","))

    circ = plt.Circle((int(center[0]), int(center[1])), r)
    axes.autoscale()
    axes.add_patch(circ)

    area = pi * r ** 2
    print("Pole koła to : %.2f" % area)
    circumference = 2 * pi * r
    print("Obwód koła to : %.2f" % circumference)
    plt.show()


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
