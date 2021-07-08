# This is a sample Python script.
import random
import matplotlib.pyplot as plt
from itertools import groupby


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def showplot(eps, x, a, b):
    plt.plot(eps, x, label="Практические вычисления")
    plt.plot(a, b, label="Теоретические вычисления")

    plt.legend(loc='upper right', frameon=False)
    plt.show()


def geom(per, c):
    return per * ((1 - per) ** (c - 1))


def matb(eps, w):
    S = 0
    for i in range(len(eps)):
        S += eps[i] * w[i]
    return S


def dispb(eps, w):
    S = 0
    for i in range(len(eps)):
        S += (eps[i] ** 2) * w[i]
    return S


def pirs(n, newn):
    S = 0
    for i in range(len(n)):
        S += ((n[i]-newn[i]) ** 2)/newn[i]
    return S


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    xi = []  # Псевдослучайные числа
    epsi = []  # Случайные величины
    wi = []  # Относительные частоты
    pi = []  # теоретические вероятности
    ni = []  # кол-во повторений случайной величины в ходе эксперимента
    segm = [0]  # отрезок [0, 1]
    p = 0.3
    N = 100

    Sum = 0
    for i in range(N):
        xi.append(random.random())
        pi.append(geom(p, i + 1))
        Sum += pi[i]
        segm.append(Sum)
    segm.pop()
    segm.append(1)

    xi.sort()
    for i in range(N):
        k = 0
        for j in range(N):
            if segm[i] > xi[j] >= segm[i - 1]:
                epsi.append(i)
                k = k + 1
        if k != 0:
            ni.append(k)
            wi.append(k / N)
    temp = epsi
    epsi = [el for el, _ in groupby(epsi)]  # Удаление повторяющихся элементов

    xb = matb(epsi, wi)  # Мат ожидание, являющиеся нашим новым значением p

    newpi = []  # Практические значения вероятности
    for i in range(len(ni)):
        newpi.append(geom(1 / xb, i))

    newni = []
    for i in range(len(ni)):
        newni.append(N * newpi[i])

    x2b = pirs(ni, newni)

    alpha = 0.05
    x2kr = 0
    if len(newni) - 1 == 8:
        x2kr = 15.5
    elif len(newni) - 1 == 9:
        x2kr = 16.9
    elif len(newni) - 1 == 10:
        x2kr = 18.3
    elif len(newni) - 1 == 11:
        x2kr = 19.7
    elif len(newni) - 1 == 12:
        x2kr = 21
    elif len(newni) - 1 == 13:
        x2kr = 22.4
    elif len(newni) - 1 == 14:
        x2kr = 23.7

    if x2b < x2kr:
        print("Yes")
    elif x2b >= x2kr:
        print("No")
    print("xb = ", xb)
    print("ni = ", ni)
    print("newni = ", ni)
    print("x2b = ", x2b)
    print("x2kr = ", x2kr)
    print("epsi = ", epsi)
    showplot(epsi, ni, epsi, newni)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
