# İlk Python Kodlarımız
isim = "Berfin"
mesaj = "Python öğrenmeye başladım!"

print("Merhaba,", isim)
print(mesaj)

# Tırnak arasına direkt mesajı yazarsan ekrana yazdıkların basılır
print("Hello World")

# Bu editörün sürümününü kontrol etmek için sys kütüphanesini dahil (import) ederiz
# import, Python'da başkalarının veya Python'ın kendi geliştiricilerinin daha önce hazırladığı 
# hazır kod paketlerini (kütüphaneleri/modülleri) kendi projenize dahil etmeye yarayan komuttur.

import sys
print(sys.version)
    
# Terminalde şuanki yüklü olan sürümün 3.14.7 olduğu yazıyor

# Eğer VScode editöründe değilde terminalde kod yazmamız gerekirse terminale python yazıp >>> bu çıktıyı 
# alırsan artık terminal editör olarak çalışır ardından işin bitince exist() yazıp enter e terminal eski haline döner.

# Ama vscode da exist yazmaya gerek yok.

# Girinti, kod satırının başındaki boşlukları ifade eder.

# Diğer programlama dillerinde koddaki girintiler yalnızca 
# okunabilirliği artırmak için kullanılırken, Python'da girintiler çok önemlidir.

# Python, kod bloklarını belirtmek için girintileme kullanır.

#KOD BLOKLARINA ÖRNEKLER:
# 1. Koşul Yapıları (if, elif, else)
yas = 20  # Önce yas değişkenini tanımlıyoruz
if yas >= 18:
    print("Yetişkinsiniz.")  # İçeride
else:
    print("Çocuksunuz.")     # İçeride

# 2. Döngüler (for, while)
for sayi in range(5):
    print("Tekrar eden kod")  # İçeride

# 3. Fonksiyonlar (def)
def selamla():
    print("Merhaba Berfin!")  # İçeride

# 4. Sınıflar (class)
class Ogrenci:
    adi = "Berfin"  # İçeride

# 5. Hata Yakalama (try, except)
try:
    sayi = int("abc")
except:
    print("Hata oluştu!")  # İçeride

# Satırın sonunda iki nokta varsa altındaki satır girintili başlar
# Aynı blok içindeki tüm satırlar birebir aynı hizada (aynı sayıda boşlukla) olmak zorundadır.

if True:
    print("İlk satır")    # 4 boşluk
    print("İkinci satır") # 4 boşluk (Tam hizada!)

# Değişken atama örnekleri
isim = "Berfin"
yas = 25
kurs = "Softito-PythonDay_1"

# Ekrana yazdırma
print(isim)
print(yas)
print(kurs)

# Statements: Python'da statement (türkçesiyle komut veya ifade),
# bilgisayara "Şu işlemi yap!" diyen en küçük çalıştırılabilir kod talimatıdır.
# Yazdığınız her bir satır kod, Python için birer statement'tır.

# STATEMENT TÜRLERİ:
# Atama Komutu (Assignment Statement):
x = 5

# Yazdırma Komutu (Print Statement):
print("Merhaba")

# Koşul Komutu (If Statement):
if x > 3:
    print("Büyük")

# Döngü Komutu (Loop Statement):
for i in range(3):
    print(i)

# Statement (Komut) ile Expression (İfade) Arasındaki Fark
# Bu ikisi çok karıştırılır, aralarındaki fark şudur:

# Expression (İfade): Bir değer üreten kod parçasıdır.
# (Örnek: 5 + 3 veya "Berfin" birer expression'dır, çünkü geriye 8 veya metin değeri döndürürler.)

# Statement (Komut): Bir eylem gerçekleştiren kod satırının tamamıdır.
# (Örnek: sonuc = 5 + 3 bir statement'tır. Bilgisayara hesap yapıp kutuya koymasını söyler.)

# Birkaç kelimeden oluşan tam bir cümle bir Statement ise, o cümlenin içindeki anlamlı kelimeler birer Expression'dır.

print("Bugün hava güneşli!")
print("Softito eğitimleri çok keyifli ve verimli geçiyor.")
print("Veri yapıları, algoritma derken sıra python'a geldi.")

# Printler ya her satıra ayrı ayrı yazılır ya da tek satıra ';' noktalı virgülle ayrılarak yazılır

print("En sevdiğim kitap Gurur ve Önyargı,") ; print("En sevdiğim şarkıcı Micheal Jackson.")

# end= "" satırda devam eder yeni satıra geçmez
print("Hello World!", end=" ")
print("I will print on the same line.")

print(1999)
print(1903)
print(1999+2001)
print("Berfin", 25, "Adıyaman")