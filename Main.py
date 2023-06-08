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
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.__tecrube}\nYeni Maaş: {self.__maas * (1 + self.zam_hakki()/100)}"
    
"""Mavi yaka sınıfı için (MaviYaka.py) yıpranma payı (float: 0.2, 0.5 gibi değer almalıdır) değişkeni private olarak bulunmalıdır.
• Değişkenlere göre Initializer metot olmalıdır.
• Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
• Çalışanın zam hakkını hesaplayan zam_hakki metodu yazılacaktır (2 sene öncesi tecrübesi olanın zam oranı önerisi “yıpranma_payi*10” olacaktır. 2-4 sene arası çalışan ise ve maaş 15000TL altıysa “(maaş%tecrübe)/2 + (yıpranma_payi*10)” sonucu zam oranı önerilecektir. 4 seneden fazla tecrübe varsa ve maaş 25000 altıysa “(maaş%tecrübe)/3+ (yıpranma_payi*10)” zam oranı önerilecektir). Yeni maaş, eski maaş ile aynıysa eski maaş, yeni maaşa atanmalıdır.
• İlgili yerlerde try/except kullanılmalıdır.
• __str__ metotunda ad, soyad, tecrübe ve yeni maaşı (public değişken ile yazdırılmamalı) yazılmalıdır."""

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
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.__tecrube}\nYeni Maaş: {self.__maas + self.zam_hakki()}"


