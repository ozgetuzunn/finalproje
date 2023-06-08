from İnsan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__status = self.statu_bul()

    def set_tecrube(self, t):
        self.__tecrube = t
        self.statu_bul()

    def get_tecrube(self):
        return self.__tecrube

    def statu_bul(self):
        try:
            m = self.__tecrube["mavi_yaka"] * 0.2
            b = self.__tecrube["beyaz_yaka"] * 0.35
            y = self.__tecrube["yonetici"] * 0.45
            if m > b and m > y:
                self.__status = "mavi_yaka"
            elif b > m and b > y:
                self.__status = "beyaz_yaka"
            elif y > m and y > b:
                self.__status = "yonetici"
            else:
                self.__status = "mavi_yaka"
            return self.__status
        except:
            print("Bir hata oluştu!")

    def __str__(self):
        return f"{super().__str__()}\nStatü: {self.__status}"
