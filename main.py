import random # random sayılarla işlem yapmak için kullanılır
from sympy import primerange # sympy: matematik işlemleri için, primerange: asal sayılar için kullanılır.

# Şifreli mesaj 
sifreli_mesaj = [72, 105, 115, 115, 32, 109, 97, 121, 98, 101, 111, 100, 101, 111, 110]
# algoritm = (((B**E1 % M1)**E2 % M2)**E3 % M3)

# 50.000 ile 100.000 arasındaki asal sayıları bulur ve liste oluşturur
asal_sayilar = list(primerange(50000, 100000))

# rastgele olan asal sayıları sabitler (15'de sabitler)
random.seed(42)

# asal_sayilar listesinden 15 farklı asal sayı seç
secili_asallar = random.sample(asal_sayilar, 15) 

# Parametrelerin değerlerinin verilmesi aşaması
E1, E2, E3 = 5, 7, 9
M1, M2, M3 = 1014, 2048, 4096 # ascii tablosu 128 haneli olduğu için 128'in katlarını seçmek istedim

# Modüler üs alma fonksiyonu oluşturulması
def moduler_us(x, e, m): # x: üssü alınacak olan sayı (taban sayı), e: üs, m: mod
    return pow(x, e, m) # son olarak (x**e) mod m olmuş oluyor

# şifre çözüm fonksiyonu oluşturulması
def sifre_coz(sifreli_mesaj, secili_asallar, E1, E2, E3, M1, M2, M3): # ilgili değerler 
    sonuc = [] # sonuçlar için boş liste oluşturulur.
    for i in range(len(sifreli_mesaj)): # her bir şifreli mesaj için (15) döngüye girer ve uzunluğunu döndürür
        B = secili_asallar[i] # seçilen asal sayıların listesinden elemanlar tek tek çağırılır.
        deger = moduler_us(B, E1, M1) # (B**E1) mod M1
        deger = moduler_us(deger, E2, M2) #(deger**E2) mod M2
        deger = moduler_us(deger, E3, M3) # (deger**E3) mod M3

        sonuc.append((i+1, B, deger)) # sonuç listesine bulunan değerler ve seçilen asal sayı (B) aktarılır. i: sıra numarası, 0'dan başladığı için i+1 yazıldı.
    return sonuc # sonuç listesini döndürür

# Şifre çözüm adımı
cozumler = sifre_coz(sifreli_mesaj, secili_asallar, E1, E2, E3, M1, M2, M3)
for i, B, deger in cozumler: 
    print(f"{i}. karakter için B asal sayısı: {B} → Şifrenin sayısal değeri: {deger}")