from Çalışan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipr_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipr_payi = yipr_payi

    def set_yipr_payi(self, yipr_payi):
        self.__yipr_payi = yipr_payi

    def get_yipr_payi(self):
        return self.__yipr_payi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                return self.__yipr_payi * 10
            elif self.get_tecrube() >= 24 and self.get_tecrube() <= 48 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube()) / 2 + self.__yipr_payi * 10
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube()) / 3 + self.__yipr_payi * 10
            else:
                return 0
        except:
            print("Bir hata oluştu!")
