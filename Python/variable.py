# type() metodu bize yazılan değişkenin türünü verir

x = 5
y = "John"
print(type(x))
print(type(y))

# Tek tırnak ya da Çift tırnak farketmez

x = "John"
x = 'John'
print(x)

# Değişkenler büyük-küçük harfe duyarlıdır
# x ve X birbirinden farklı iki değişkendir

x = 5
X = 20

print(x)  # Ekrana 5 basar
print(X)  # Ekrana 20 basar

# Duyarlı bir değişken atama sistemi var 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# boşluk, tire, rakamla başlama olmaz
# Pascal case, snake gibi uzun isimle için kullanım yöntemlerş mevcut

# Çıktı değişkeni print()

isim = "Funda Berfin Demir."
yas = 25
sehir = "Adıyaman"
okul = "Beykent University"
meslek = "computer engineering"

print("Ben", isim, yas,"yaşındayım.", sehir,"'lıyım.", okul,"'si mezunuyum.", "Mesleğim", meslek, )

# terminal çıktısı = Ben Funda Berfin Demir. 25 yaşındayım. 
# Adıyaman 'lıyım. Beykent University 'si mezunuyum. Mesleğim computer engineering

sayi1= 25
sayi2= 87
print(sayi1+sayi2)

# terminal çıktısı = 112

sayi1 = 15
sayi2 = 25
toplam = sayi1 + sayi2
print("Toplam:", toplam)

# terminal çıktısı = 40

a= 10
b= 3.17
c= True
d= "berfin"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# terminal çıktısı = <class 'int'>
# <class 'tuple'>
# <class 'bool'>
# <class 'str'>

x = 5
y = 10
x, y = y, x
print("x:", x, "y:", y)

# terminal çıktısı = x: 10 y: 5
