nama = "Tony Stark" # menyimpan data string
umur = 50 # menyimpan data integer
berat = 78.9 # menyimpan data float

# menampilkan data
print("Nama : ", nama)
print("Umur : ", umur)
print("Berat : ", berat)

# mengubah tipe data
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# 1. Konversi angka_string menjadi integer
data_int = int(angka_string)
print("data = ", data_int, ", type =", type(data_int)) # untuk menampilkan data

# 2. Konversi angka_float menjadi integer
data_int2 = int(angka_float)
print("data = ", data_int2, ", type =", type(data_int2)) # untuk menampilkan data

# 3. Konversi angka_integer menjadi float
data_float = float(angka_integer)
print("data = ", data_float, ", type =", type(data_float)) # untuk menampilkan data

# 4. Konversi angka_integer menjadi string
data_string = str(angka_integer)
print("data = ", data_string, ", type =", type(data_string)) # untuk menampilkan data   

# input data user 

# a. meminta input usia dalam bentuk integer
usia = int(input("Masukkan usia : ")) # input data integer
print("data : ",usia,",type =",type(usia)) # untuk menampilkan data

# b. meminta input tinggi badan dalam bentuk float
tinggi_badan = float(input("Masukkan tinggi badan : ")) # input data float
print("data : ",tinggi_badan,",type =",type(tinggi_badan)) # untuk menampilkan data

# c. meminta input nama dalam bentuk string
nama = input("Masukkan nama : ") # input data string 
print("data : ",nama,",type =",type(nama)) # untuk menampilkan data 