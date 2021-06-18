from math import pi, sqrt
import matplotlib.pyplot as plt


def draw(title):
    # x axis values
    x = [1, 2, 3]
    # corresponding y axis values
    y = [2, 4, 1]

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('oś x')
    # naming the y axis
    plt.ylabel('oś y')

    # giving a title to my graph
    plt.title(title)

    # function to show the plot
    plt.show()


def triangle():

    plt.xlabel('oś x')
    plt.ylabel('oś y')
    plt.title("TRÓJKĄT")

    print("Podaj współrzędne TRÓJKĄTA")
    a = (input("a(x,y) : ").split(","))
    b = (input("b(x,y) : ").split(","))
    c = (input("c(x,y) : ").split(","))

    x = [int(a[0]), int(b[0]), int(c[0]), int(a[0])]
    y = [int(a[1]), int(b[1]), int(c[1]), int(a[1])]
    print(x)
    print(y)

    plt.plot(x, y)
    plt.show()

    ab = sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
    print(ab)
    bc = sqrt((x[2] - x[1]) ** 2 + (y[2] - y[1]) ** 2)
    print(bc)
    ca = sqrt((x[3] - x[2]) ** 2 + (y[3] - y[2]) ** 2)
    print(ca)

    perimeter = ab + bc + ca
    print("Obwód trójkąta to : ", perimeter)

    half_perimeter = perimeter / 2
    area = sqrt(half_perimeter * (half_perimeter - ab) * (half_perimeter - bc) * (half_perimeter - ca))
    print("Pole trójkąta to : ", area)


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
