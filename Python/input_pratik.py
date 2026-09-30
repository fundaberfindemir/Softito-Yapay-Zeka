# input() fonksiyonu parantez içine yazılan metni ekrana basar ve
# kullanıcının bir şeyler yazıp Enter tuşuna basmasını bekler.

isim = input("İsminiz nedir? ")
print("Merhaba "+isim) 

yemek = input("En sevdiğiniz yemek nedir?")
icecek = input("En sevdiğiniz içecek nedir?")

print(yemek + " " + icecek)

# terminal çıktısı = İsminiz nedir? berfin
# Merhaba berfin
# En sevdiğiniz yemek nedir?sarma
# En sevdiğiniz içecek nedir?ayran
# sarma ayran

# Kullanıcıdan isim alma
kullanici_adi = input("Lütfen adınızı giriniz: ")

print("Hoş geldin,", kullanici_adi)

isim = "ali"
yas = 25

print(isim + " " + str(yas) + " " + "yaşında")

# terminal çıktısı = ali 25 yaşında

# neden str() kullandık? 
# Çünkü Python'da + (artı) operatörü metinlerle sayıları birleştiremez
# 1. virgül kullanarak ayır
# 2. str() kullanarak ayır
# 3. f-string kullan
# print(f"{isim} {yas} Yaşında")

# matemtik işlemleri

x = 9
y = 5

print(x * y)
print(x + y)
print(x - y)
print(x / y)

print(x // y)

# çift // sayıları tam böler virgül bırakmaz

print(x % y)

# yüzde bölümden kalanı verir

print(x ** y)

# sayının üssünü almak için iki yıldız koyulur

k = input("İlk sayıyı giriniz?") 
l = input("İkinci sayıyı giriniz?")

print(int(k)+int(l))

# terminal çıktısı = İlk sayıyı giriniz?10
# İkinci sayıyı giriniz?5
# 15