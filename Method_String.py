## 1. Menggabungkan String concatenate

nama_awal = "Aditya"
nama_akhir = "Chandra"

nama_lengkap = nama_awal + " " + nama_akhir
print(nama_lengkap)

## 2. Menghitung panjang String

panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

#;# 3. Operator String
# ngecek apakah ada (string) dalam string

r = "r"
status = r in nama_lengkap
print("r dalam " + nama_lengkap + " = " + str(status))

R = "R"
status = R in nama_lengkap
print("R ada di " + nama_lengkap + " = " + str(status))

# ngecek apakah tidak ada (string) dalam string

R = "R"
status = R not in nama_lengkap
print("R ada di " + nama_lengkap + " = " + str(status))

# pengulangan 
print("\nADIT"*3)

# Mencari index dalam string

print("\nindex ke-0 dari " + nama_lengkap + " = " + nama_lengkap[0])
print("index ke-1 dari " + nama_lengkap + " = " + nama_lengkap[1])
print("index ke-2 dari " + nama_lengkap + " = " + nama_lengkap[2])
print("index ke-3 dari " + nama_lengkap + " = " + nama_lengkap[3])
print("index ke-[0:3] dari " + nama_lengkap + " = " + nama_lengkap[0:4])

# Split dalam string

print("Split -6 " + nama_lengkap[0:14:6])

# Mencari kata terkecil menurut ASCII Code

print("Kata Terkecil :" + min(nama_lengkap))
print("Kata Terbesar : " + max(nama_lengkap))

# Mengecek ASCII code dari sebuah string
ascii_code = ord(" ")
print("ASCII code untuk spasi :" + str(ascii_code))
ascii_code2 = ord("r")
print("ASCII code untuk r :" + str(ascii_code2))

#Mengecek Character dari sebuah ASCII code

data = 70
print("char dari " + str(data) + " : " + chr(data))

# Menghitung (string) dalam string

data2 = nama_lengkap.count("a")
print("Jumlah a dari " + str(nama_lengkap) + " : " + str(data2))
