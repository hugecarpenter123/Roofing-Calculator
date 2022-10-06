import math
import os
class RozmieszczenieKrokwi():
    def __init__(self, arguments = None):
        if not arguments:
            print("Wartości w cm:")
            self.d_calkowita = float(input("Długość murłaty: "))
            self.s_krokwi = float(input("Szerokość krokwi: "))
            self.o_przedzial_dolny = float(input("Dolny przedział odstępu: "))
            self.o_przedzial_gorny = float(input("Górny przedział odstępu: "))
        else:
            self.d_calkowita, self.s_krokwi, self.o_przedzial_dolny, self.o_przedzial_gorny = arguments

        self.I_dolna, self.I_gorna = self.przedzial_odstepow()
        self.wymiary = self.__wyniki()
        # self.drukuj()

    def przedzial_odstepow(self):
        I_gorna = (self.d_calkowita - self.s_krokwi) / (self.o_przedzial_dolny + self.s_krokwi)
        I_dolna = (self.d_calkowita - self.s_krokwi) / (self.o_przedzial_gorny + self.s_krokwi)

        return (
            int(I_dolna) if I_dolna == int(I_dolna) else round(I_dolna, 2),
            int(I_gorna) if I_gorna == int(I_gorna) else round(I_gorna, 2)
        )

    def odleglosc(self, ilosc_interwalow):
        """

        :param ilosc_interwalow: przyjmuje ilość odstępów (z grubością krokwi) minus jedna grubość krokwi
        :return: zwraca wartość odstępu dla podanej ilości_interwałów
        """
        O = ((self.d_calkowita - self.s_krokwi) / ilosc_interwalow) - self.s_krokwi
        return O

    def __wyniki(self):
        wymiary = dict()
        wyniki = False
        for i in range(math.ceil(self.I_dolna), int(self.I_gorna) + 1):
            odleglosc = round(self.odleglosc(i), 2)
            wymiary[i+1] = [odleglosc, odleglosc + self.s_krokwi]
            wyniki = True

        return wymiary

    def drukuj(self):
        for key, listValue in self.wymiary.items():
            print(f"{key} krokwi: odstęp->{listValue[0]:.2f}, rysowanie->{listValue[1]:.2f}")
            # print(key * self.s_krokwi + (key - 1) * listValue[0])
        print("\n---rysowanie zawsze z lewej\prawej strony krokwi---")



if __name__ == '__main__':
    dach1 = RozmieszczenieKrokwi()
    os.system('cls' if os.name == 'nt' else 'clear')
    dach1.drukuj()

    run = True
    while run:
        if input("naciśnij enter, żeby wyjść...") == '':
            run = False
