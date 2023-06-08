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
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()}\nYeni Maaş: {self.get_maas() + self.zam_hakki()}"

import pandas as pd
def main():
    insan1 = Insan("1", "insan1ad", "insan1soyad", 20, "erkek", "tr")
    insan2 = Insan("2", "insan2ad", "insan2soyad", 21, "kadın", "tr")
    print(insan1)
    print(insan2)

    issiz1 = Issiz("3", "issiz1ad", "issiz1soyad", 22, "erkek", "tr", {"mavi_yaka":2, "yonetici":1, "beyaz_yaka":1})
    issiz2 = Issiz("4", "issiz2ad", "issiz2soyad", 23, "kadın", "tr", {"mavi_yaka":10, "yonetici":5, "beyaz_yaka":7})
    issiz3 = Issiz("5", "issiz3ad", "issiz3soyad", 24, "erkek", "tr", {"mavi_yaka":5, "yonetici":2, "beyaz_yaka":3})
    print(issiz1)
    print(issiz2)
    print(issiz3)

    calisan1 = Calisan("6", "calisan1ad", "calisan1soyad", 25, "erkek", "tr", "teknoloji", 10, 10000)
    calisan2 = Calisan("7", "calisan2ad", "calisan2soyad", 26, "kadın", "tr", "muhasebe", 30, 14000)
    calisan3 = Calisan("8", "calisan3ad", "calisan3soyad", 27, "erkek", "tr", "inşaat", 50, 24000)
    print(calisan1)
    print(calisan2)
    print(calisan3)

    mavi_yaka1 = MaviYaka("9", "mavi_yaka1ad", "mavi_yaka1soyad", 28, "erkek", "tr", "teknoloji", 10, 10000, 0.5)
    mavi_yaka2 = MaviYaka("10", "mavi_yaka2ad", "mavi_yaka2soyad", 29, "kadın", "tr", "muhasebe", 30, 14000, 0.1)
    mavi_yaka3 = MaviYaka("11", "mavi_yaka3ad", "mavi_yaka3soyad", 30, "erkek", "tr", "inşaat", 50, 24000, 0.2)
    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)

    beyaz_yaka1 = BeyazYaka("12", "beyaz_yaka1ad", "beyaz_yaka1soyad", 31, "erkek", "tr", "teknoloji", 10, 10000, 1500)
    beyaz_yaka2 = BeyazYaka("13", "beyaz_yaka2ad", "beyaz_yaka2soyad", 32, "kadın", "tr", "muhasebe", 30, 14000, 2000)
    beyaz_yaka3 = BeyazYaka("14", "beyaz_yaka3ad", "beyaz_yaka3soyad", 33, "erkek", "tr", "inşaat", 50, 24000, 2500)
    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)

    df = pd.DataFrame({"çalışan": ["calisan", "calisan", "calisan", 
                                   "mavi_yaka", "mavi_yaka", "mavi_yaka", 
                                   "beyaz_yaka", "beyaz_yaka", "beyaz_yaka"],
                          "tc_no": ["6", "7", "8", 
                                    "9", "10", "11", 
                                    "12", "13", "14"],
                            "ad": ["calisan1ad", "calisan2ad", "calisan3ad",
                                   "mavi_yaka1ad", "mavi_yaka2ad", "mavi_yaka3ad",
                                   "beyaz_yaka1ad", "beyaz_yaka2ad", "beyaz_yaka3ad"],
                            "soyad": ["calisan1soyad", "calisan2soyad", "calisan3soyad",
                                    "mavi_yaka1soyad", "mavi_yaka2soyad", "mavi_yaka3soyad",
                                    "beyaz_yaka1ad", "beyaz_yaka2ad", "beyaz_yaka3ad"],
                            "yas": [25, 26, 27,
                                    28, 29, 30,
                                    31, 32, 33],
                            "cinsiyet": ["erkek", "kadın", "erkek",
                                        "erkek", "kadın", "erkek",
                                        "erkek", "kadın", "erkek"],
                            "uyruk": ["tr", "tr", "tr",
                                    "tr", "tr", "tr",
                                    "tr", "tr", "tr"],
                            "sektör": ["teknoloji", "muhasebe", "inşaat",
                                    "teknoloji", "muhasebe", "inşaat",
                                    "teknoloji", "muhasebe", "inşaat"],
                            "tecrübe": [10/12, 30/12, 50/12,
                                        10/12, 30/12, 50/12,
                                        10/12, 30/12, 50/12],
                            "maaş": [10000, 14000, 24000,
                                    10000, 14000, 24000,
                                    10000, 14000, 24000],
                            "yıpranma_payı": [0, 0, 0,
                                            0.5, 0.1, 0.2,
                                            0, 0, 0],
                            "teşvik_primi": [0, 0, 0,
                                            0, 0, 0,
                                            1500, 2000, 2500],
                            "yeni_maaş": [calisan1.get_maas() * (1 + calisan1.zam_hakki()/100), calisan2.get_maas() * (1 + calisan2.zam_hakki()/100), calisan3.get_maas() * (1 + calisan3.zam_hakki()/100),
                                            mavi_yaka1.get_maas() * (1 + mavi_yaka1.zam_hakki()/100), mavi_yaka2.get_maas() * (1 + mavi_yaka2.zam_hakki()/100), mavi_yaka3.get_maas() * (1 + mavi_yaka3.zam_hakki()/100),
                                            beyaz_yaka1.get_maas() + beyaz_yaka1.zam_hakki(), beyaz_yaka2.get_maas() + beyaz_yaka2.zam_hakki(), beyaz_yaka3.get_maas() + beyaz_yaka3.zam_hakki()]})
    print(df)
    print(df[["çalışan", "tecrübe", "yeni_maaş"]].groupby("çalışan").mean()[["tecrübe", "yeni_maaş"]])
    print("yeni_maaş > 15000 : ", df[df["yeni_maaş"] > 15000].count()["yeni_maaş"])
    print(df.sort_values(by="yeni_maaş"))
    print(df[(df["tecrübe"] > 3) &  (df["çalışan"] == "beyaz_yaka")])
    print(df[df["yeni_maaş"] > 10000].iloc[1:5, [1, 12]])
    print(df[["ad", "soyad", "sektör", "yeni_maaş"]])

if __name__ == "__main__":
    main()