# PROJE 1: KELİME SAYACI
# BÜYÜK/KÜÇÜK HARF DUYARLILIĞI:
# Bu program büyük/küçük harfe DUYARSIZ çalışacak şekilde tasarlanmıştır.
# Bunun için kullanıcıdan alınan metni lower() metodu ile tamamen küçük harfe
# çeviriyoruz. Böylece cümle başındaki büyük harfli bir kelime ile cümle içindeki
# aynı kelime farklı kelimeler gibi sayılmaz.
# NOKTALAMA İŞARETLERİ:
# "merhaba," ve "merhaba" gibi ifadelerin aynı kelime sayılması için temel
# noktalama işaretlerini replace() metodu ile temizliyoruz.
# Toplam karakter sayısı ise bu temizlikten ÖNCE hesaplanır.

# Kullanıcıdan analiz edilecek cümle veya paragrafı alıyoruz
metin = input("Lütfen bir cümle veya paragraf giriniz: ")

# Metindeki toplam karakter sayısını boşluklar ve noktalama işaretleri dahil hesaplıyoruz
toplam_karakter = len(metin)

# Büyük/küçük harf duyarsızlığı sağlamak için metindeki tüm harfleri küçük harfe çeviriyoruz
temiz_metin = metin.lower()

# Sekme karakteri varsa boşluğa çeviriyoruz ki kelimeler birbirine yapışmasın
temiz_metin = temiz_metin.replace("\t", " ")

# Kelimelere bitişik olabilecek noktalama işaretlerini bir string içinde tanımlıyoruz
noktalama_isaretleri = ".,!?;:\"'()-"

# Her bir noktalama işaretini for döngüsüyle tek tek geziyoruz
for isaret in noktalama_isaretleri:
    # Metin içinde o noktalama işareti varsa boş string ile değiştirerek siliyoruz
    temiz_metin = temiz_metin.replace(isaret, "")

# Metnin başındaki ve sonundaki gereksiz boşlukları strip metodu ile temizliyoruz
temiz_metin = temiz_metin.strip()

# Temizlenmiş metni boşluk karakterinden bölerek ham kelimeler listesi oluşturuyoruz
ham_kelimeler = temiz_metin.split(" ")

# Toplam kelime sayısını tutacak sayaç değişkenini 0'dan başlatıyoruz
toplam_kelime = 0

# En uzun kelimenin harf sayısını tutacak değişkeni 0'dan başlatıyoruz
en_uzun_kelime_uzunlugu = 0

# Her kelimenin kaç kez tekrar ettiğini tutmak için boş bir sözlük oluşturuyoruz
kelime_sayilari = {}

# Bölünmüş kelimeler listesi üzerinde for döngüsüyle tek tek geziyoruz
for kelime in ham_kelimeler:
    # Arada birden fazla boşluk varsa oluşan boş string elemanlarını atlıyoruz
    if kelime == "":
        # Bu adımı pas geçip döngünün bir sonraki elemanına dönüyoruz
        continue

    # Geçerli her kelime için toplam kelime sayısını 1 artırıyoruz
    toplam_kelime += 1

    # Şu anki kelimenin uzunluğu, bildiğimiz en uzun kelimeden büyükse güncelliyoruz
    if len(kelime) > en_uzun_kelime_uzunlugu:
        # Yeni en büyük kelime uzunluğunu kaydediyoruz
        en_uzun_kelime_uzunlugu = len(kelime)

    # Kelime daha önce sözlüğe eklenmiş mi diye in operatörüyle kontrol ediyoruz
    if kelime in kelime_sayilari:
        # Kelime zaten sözlükte varsa tekrar sayısını 1 artırıyoruz
        kelime_sayilari[kelime] += 1
    else:
        # Kelime sözlükte yoksa yeni anahtar olarak ekleyip değerini 1 yapıyoruz
        kelime_sayilari[kelime] = 1

# Sonuçlar başlığını ekrana yazdırıyoruz
print("\n--- METİN İSTATİSTİKLERİ ---")

# Toplam kelime sayısını f-string ile ekrana yazdırıyoruz
print(f"Toplam kelime sayısı: {toplam_kelime}")

# Toplam karakter sayısını f-string ile ekrana yazdırıyoruz
print(f"Toplam karakter sayısı (boşluklar dahil): {toplam_karakter}")

# En uzun kelimenin uzunluğunu f-string ile ekrana yazdırıyoruz
print(f"En uzun kelimenin uzunluğu: {en_uzun_kelime_uzunlugu}")

# Kelime tekrar sayıları alt başlığını ekrana yazdırıyoruz
print("\n--- KELİME TEKRAR SAYILARI ---")

# Eğer metinde hiç geçerli kelime yoksa kullanıcıya bilgi veriyoruz
if toplam_kelime == 0:
    # Metin boş veya sadece noktalama/boşluk içeriyorsa bu mesaj yazılır
    print("Metinde sayılacak kelime bulunamadı.")
else:
    # Sözlükteki her anahtar ve değeri items metodu ile geziyoruz
    for kelime, tekrar_sayisi in kelime_sayilari.items():
        # Her kelimenin kaç kez geçtiğini ekrana yazdırıyoruz
        print(f"'{kelime}': {tekrar_sayisi} kez")
