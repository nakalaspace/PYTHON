# operasi aritmatika
# memasukkan variabel

p = 12
l = 5
t = 8

# menghitung luas bangunan
# rumus luas balok = 2 * ((p * l) + (p * t) + (l * t))
luas = 2 * ((p * l) + (p * t) + (l * t))
print(2,'*',((p,'*',l),'+',(p,'*',t),'+',(l,'*',t)),'=', luas)

# menghitung volume bangunan
# rumus volume balok = p * l * t
volume = p * l * t
print(p,'*',l,'*',t,'=', volume)

# menghitung keliling bangunan
# rumus keliling balok = 4 * (p + l + t)
keliling = 4 * (p + l + t)
print(4,'*',(p,'+',l,'+',t),'=', keliling)

# menentukan lebih besar dari ( > )
print("Apakah luas bangunan lebih besar dari (>) 50?")
hasil = luas > 50
print(luas,'>',50,'=', hasil)

# menentukan sama dengan ( == )
print("Apakah volume bangunan sama dengan (==) 480?")
hasil = volume == 480
print(volume,'==',480,'=', hasil)

# konversi satuan temperatur

# program konversi suhu celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit 
fahrenheit = (9/5) * celcius + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")