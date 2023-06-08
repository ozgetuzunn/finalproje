class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no

    def get_tc_no(self):
        return self.__tc_no

    def set_ad(self, ad):
        self.__ad = ad

    def get_ad(self):
        return self.__ad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_soyad(self):
        return self.__soyad

    def set_yas(self, yas):
        self.__yas = yas

    def get_yas(self):
        return self.__yas

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def get_uyruk(self):
        return self.__uyruk

    def __str__(self):
        return f"TC No: {self.__tc_no}\nAd: {self.__ad}\nSoyad: {self.__soyad}\nYaş: {self.__yas}\nCinsiyet: {self.__cinsiyet}\nUyruk: {self.__uyruk}"
    
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
    
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_sektor(self):
        return self.__sektor

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_tecrube(self):
        return self.__tecrube

    def set_maas(self, maas):
        self.__maas = maas

    def get_maas(self):
        return self.__maas

    def zam_hakki(self):
        try:
            if self.__tecrube < 24:
                return 0
            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                return self.__maas % self.__tecrube
            elif self.__tecrube > 48 and self.__maas < 25000:
                return (self.__maas % self.__tecrube) / 2
            else:
                return 0
        except:
            print("Bir hata oluştu!")

    def __str__(self):
        return f"{super().__str__()}\nSektör: {self.__sektor}\nTecrübe: {self.__tecrube}\nYeni Maaş: {self.__maas * (1 + self.zam_hakki()/100)}"
