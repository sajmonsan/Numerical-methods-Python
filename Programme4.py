import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import norm

a = 1  # todo bok podstawy
h = 10  # todo wysokosc ostrosupa to polowa h
liczba_punktow = 10000000  # todo liczba punktow

xksy_poczatkowe = np.random.rand(liczba_punktow)*a  # todo x
ygreki_poczatkowe = np.random.rand(liczba_punktow)*a  # todo y
zety_poczatkowe = np.random.rand(liczba_punktow)*h  # todo z

punkty_poczatkowe = np.array(
    [xksy_poczatkowe, ygreki_poczatkowe, zety_poczatkowe])

# todo tworzenie strosupa z punktow
punkciki = punkty_poczatkowe[:,
                             punkty_poczatkowe[2, :] < h*punkty_poczatkowe[0, :]]
punkciki = punkciki[:, -punkciki[2, :] > h*(punkciki[0, :]-a)]
punkciki = punkciki[:, -punkciki[2, :] > h*(punkciki[1, :]-a)]
punkciki = punkciki[:, punkciki[2, :] < h*(punkciki[1, :])]

n = np.size(punkciki)/3  # todo ile punktow sie lapie do figury

ro = 1  # todo gestosć ladunku przyjmujemy ze jest rowna 1


# todo funkcja odpowiada za ryspowanie bryły
def rysowanie():
    plt.close('all')
    fig = plt.figure()
    ax = fig.add_subplot(221, projection='3d')
    ax.plot(punkciki[0, :], punkciki[1, :],
            punkciki[2, :], ',k')  # todo 3d ostroslup
    ax2 = fig.add_subplot(222)
    ax2.plot(punkciki[0, :], punkciki[1, :], ',k')  # todo xy
    ax3 = fig.add_subplot(223)
    ax3.plot(punkciki[0, :], punkciki[2, :], ',k')  # todo yz
    ax4 = fig.add_subplot(224)
    ax4.plot(punkciki[1, :], punkciki[2, :], ',k')  # todo xz
    ax.set_title('3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax2.set_title('xy')
    ax3.set_title('yz')
    ax4.set_title('xz')
    plt.show()


# todo Definicja momentu kwadrupolowego
def defninicja_moemntu_kadrupolowego(a, b, delta_kronekera, r):
    return (3*a*b-r*r*delta_kronekera)*ro


# todo funkcja liczy momenty kwadrupolowe
def liczyenie():
    TABELA_9zer = np.zeros((3, 3))  # todo macierz 9 zer
    Obietosc = (1/3)*a**2*h  # todo obietosc ostrosulpa
    # todo zwraca wektor z normami wszystkich współrzędnych
    r = norm(punkciki, axis=0)

    for kolumna in range(3):
        for wiersz in range(3):
            delta_kronekera = 0  # todo delta kronekera rowna 0
            if (kolumna == wiersz):
                delta_kronekera = 1  # todo delta kronekera rowna 1
            tablica = defninicja_moemntu_kadrupolowego(punkciki[kolumna, :], punkciki[wiersz, :],
                                                       delta_kronekera, r)  # todo wartosci funkcji
            max_wartosc = np.amax(
                tablica)+np.abs(np.amax(tablica)) * 0.02  # todo max wartośc plus 2 %
            min_wartosc = np.amin(
                tablica)-np.abs(np.amin(tablica)) * 0.02  # todo min wartośc minus 2 %

            # todo losowanie wartosci funkcji
            f_losowe = (np.random.rand(int(n)) *
                        (max_wartosc-min_wartosc) + min_wartosc)

            zmienna_tym = tablica[f_losowe > tablica]  # todo chwilowa wartość
            zmienna_tym_0 = f_losowe[f_losowe > tablica]
            zmienna_tym2 = zmienna_tym[zmienna_tym_0 < 0]
            liczba_pkt_ujemnych = np.size(zmienna_tym2)

            zmienna_tym = tablica[f_losowe < tablica]  # todo chwilowa wartość
            zmienna_tym_0 = f_losowe[f_losowe < tablica]
            zmienna_tym2 = zmienna_tym[zmienna_tym_0 > 0]
            liczba_pkt_dodatnich = np.size(zmienna_tym2)

            print('punkty :   ', kolumna, wiersz, '   ', 'liczba punktow dodatnich =    ', liczba_pkt_dodatnich, '     ', 'liczba punktow ujemnych =    ', liczba_pkt_ujemnych, '   ',  'maksymalan wartosc funkcji =    ', max_wartosc, '   ',
                  'minimalna wartosc funkcji =    ', min_wartosc, '   ', 'maksimum funkcji_0=    ', np.amax(f_losowe), '   ', 'minimum funkcji_0=    ', np.amin(f_losowe), '   ')  # todo np.amax daje najwyzszą wartość a np.amin daje najniższą wartość

            # ! print('punkt: {:4f}, {:4f} liczba_pkt_dodatnich= {:4f} liczba_pkt_ujemnych= {:4f} max_wartosc f= {:4f}min_wartosc= {:4f} max f0= {:4f} min f0={:4f}'.format(
            # ! kolumna, wiersz, liczba_pkt_dodatnich, liczba_pkt_ujemnych, max_wartosc, min_wartosc, np.amax(f_losowe), np.amin(f_losowe))) no coz nie wychodzi wyjustowanie tekstu

            TABELA_9zer[kolumna][wiersz] = (liczba_pkt_dodatnich-liczba_pkt_ujemnych) * Obietosc*(
                max_wartosc-min_wartosc) / n  # todo moment kwadrupolowey

    # todo ślad macierzy momnetu kwadrupolowego
    slad_macierzy = TABELA_9zer[0][0]+TABELA_9zer[1][1]+TABELA_9zer[2][2]

    print('Moment kwadrupolowy jest rowny: ')
    print(TABELA_9zer)
    print('slad tej macierzy= ', slad_macierzy)


# todo funkcjulki
liczyenie()
rysowanie()
