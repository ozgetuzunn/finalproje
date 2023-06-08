from İnsan import Insan
from İşsiz import Issiz
from Çalışan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
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