from Çalışan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                return self.__tesvik_primi
            elif self.get_tecrube() >= 24 and self.get_tecrube() <= 48 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube()) * 5 + self.__tesvik_primi
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube()) * 4 + self.__tesvik_primi
            else:
                return 0
        except:
            print("Bir hata oluştu!")


    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()}\nYeni Maaş: {self.get_maas() + self.zam_hakki()}"

