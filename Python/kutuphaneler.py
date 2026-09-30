# Python Kütüphaneleri, başkalarının (veya Python geliştiricilerinin) önceden
# yazıp bize hazır sunduğu araç kutuları gibi düşünebilirsin. 
# Tek yapman gereken import diyerek o araç kutusunu projene dahil etmektir.

# Matematik kütüphanesi
import math

# Karekök alma
sayi = 16
print("16'nın karekökü:", math.sqrt(sayi)) 
# Çıktı: 4.0

# Yukarı ve aşağı yuvarlama
print("3.2'yi yukarı yuvarla:", math.ceil(3.2))  # Çıktı: 4
print("3.8'i aşağı yuvarla:", math.floor(3.8)) # Çıktı: 3

# Pi sayısı
print("Pi sayısı:", math.pi)

sayi2 = 49
print("49'un karekökü:", int(math.sqrt(sayi2))) 
#Çıktı= 7

print(round(9.8))

print(min(9,56,789))
print(max(9,56,789))  


print(math.sqrt(9))

# terminal çıktsı = 3.0

# Random Kütüphanesi

import random

# 1 ile 100 arasında rastgele bir tam sayı seçme
rastgele_sayi = random.randint(1, 100)
print("Şanslı sayınız:", rastgele_sayi)

# Bir listeden rastgele eleman seçme
renkler = ["Kırmızı", "Mavi", "Yeşil", "Sarı"]
secilen_renk = random.choice(renkler)
print("Seçilen renk:", secilen_renk)

#Datetime Kütüphanesi
import datetime

# Şu anki tarih ve saati alma
su_an = datetime.datetime.now()
print("Şu anki zaman:", su_an)
print("Sadece Yıl:", su_an.year)
print("Sadece Gün:", su_an.day)

# terminal çıktısı = Şu anki zaman: 2026-09-20 11:05:01.524316
# Sadece Yıl: 2026
# Sadece Gün: 30