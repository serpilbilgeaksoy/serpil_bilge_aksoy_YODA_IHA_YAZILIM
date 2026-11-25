# PROJE 2: BASİT BANKA HESAP YÖNETİMİ
# Bu programda bir Hesap sınıfı tanımlayıp kullanıcıdan alınan bilgilerle bir hesap nesnesi oluşturuyoruz ve para yatırma, para çekme, bakiye görüntüleme
# işlemlerini menü üzerinden yönetiyoruz.

# Banka hesabını temsil eden hesap sınıfını oluşturuyoruz
class Hesap:
    # Kurucu metot (__init__): Yeni bir Hesap nesnesi oluşturulduğunda otomatik çalışır
    def __init__(self, hesap_sahibi, hesap_numarasi, bakiye=0.0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    # Hesaba para yatırma işlemini yapan metot
    def para_yatir(self, miktar):
        # Yatırılacak miktarın 0'dan büyük olup olmadığını kontrol ediyoruz
        if miktar > 0:
            self.bakiye += miktar
            # İşlem sonucunu ve güncel bakiyeyi virgülden sonra 2 basamakla yazdırıyoruz
            print(f"{miktar:.2f} TL yatırıldı. Güncel bakiyeniz: {self.bakiye:.2f} TL")
        else:
            # 0 veya negatif bir tutar girilirse kullanıcıyı uyarıyoruz
            print("Hata: Yatırılacak miktar 0'dan büyük olmalıdır.")

    # Hesaptan para çekme işlemini yapan metot
    def para_cek(self, miktar):
        # Çekilecek miktarın 0 veya negatif olup olmadığını kontrol ediyoruz
        if miktar <= 0:
            # Geçersiz tutar uyarısı veriyoruz
            print("Hata: Çekilecek miktar 0'dan büyük olmalıdır.")
        # Çekilecek miktar mevcut bakiyeden fazla mı diye kontrol ediyoruz
        elif miktar > self.bakiye:
            # Bakiye yetersizse uyarı veriyoruz
            print(f"Yetersiz bakiye! Mevcut bakiyeniz: {self.bakiye:.2f} TL")
        else:
            # Çekilen miktarı bakiyeden düşüyoruz
            self.bakiye -= miktar
            # İşlem sonucunu ve kalan bakiyeyi ekrana yazdırıyoruz
            print(f"{miktar:.2f} TL çekildi. Kalan bakiyeniz: {self.bakiye:.2f} TL")

    # Hesap bilgilerini ve güncel bakiyeyi ekrana yazdıran metot
    def bakiye_goruntule(self):
        print("\n--- HESAP BİLGİLERİ ---")
        print(f"Hesap Sahibi  : {self.hesap_sahibi}")
        print(f"Hesap Numarası: {self.hesap_numarasi}")
        print(f"Güncel Bakiye : {self.bakiye:.2f} TL")


# Kullanıcıdan hesap açılış bilgilerini alıyoruz
print("=== BASİT BANKA HESAP YÖNETİMİ ===")
sahip = input("Hesap sahibinin adı soyadı: ")
hesap_no = input("Hesap numarası: ")
baslangic_bakiye = float(input("Başlangıç bakiyesi (TL): "))

# Başlangıç bakiyesi negatif girilirse tekrar istiyoruz
while baslangic_bakiye < 0:
    print("Başlangıç bakiyesi negatif olamaz. Lütfen tekrar giriniz.")
    baslangic_bakiye = float(input("Başlangıç bakiyesi (TL): "))

# Hesap sınıfından yeni bir hesap nesnesi üretiyoruz
kullanici_hesabi = Hesap(sahip, hesap_no, baslangic_bakiye)
print(f"\nHoş geldiniz {kullanici_hesabi.hesap_sahibi}! Hesabınız başarıyla oluşturuldu.")

# Kullanıcı çıkış yapana kadar devam eden menü döngüsü
while True:
    print("\n--- İŞLEM MENÜSÜ ---")
    print("1 - Para Yatır")
    print("2 - Para Çek")
    print("3 - Bakiye Görüntüle")
    print("4 - Çıkış")

    secim = input("Lütfen bir işlem seçiniz (1-4): ")

    if secim == "1":
        yatirilacak_tutar = float(input("Yatırmak istediğiniz miktar (TL): "))
        kullanici_hesabi.para_yatir(yatirilacak_tutar)
    elif secim == "2":
        cekilecek_tutar = float(input("Çekmek istediğiniz miktar (TL): "))
        kullanici_hesabi.para_cek(cekilecek_tutar)
    elif secim == "3":
        kullanici_hesabi.bakiye_goruntule()
    elif secim == "4":
        print("Banka hesap yönetiminden çıkılıyor. İyi günler dileriz!")
        break
    else:
        print("Geçersiz seçim! Lütfen 1 ile 4 arasında bir değer giriniz.")
