## format string
nama = input("Enter Your Name: ")
format_str = f"\nHello {nama}\n"
print (format_str)

#Boolean
boolean = False
format_str = f"Boolean = {boolean}\n"
print(format_str)

#Bilangan angka
angka = 2257.845
format_str = f"angka = {angka}\n"
print(format_str)

#bilangan bulat
angka = 22
format_str = f"angka = {angka:d}\n"
print(format_str)

#bilangan ordo ribuan
angka = 50000
format_str = f"ribuan = {angka:,}\n"
print(format_str)

#bilangan ordo jutaan
angka = 50000000
format_str = f"jutaan = {angka:,}\n"
print(format_str)

#bilangan desimal
angka = 5079.5618
format_str = f"desimal = {angka:.2f}\n"
print(format_str)

#bilangan leading zero
angka = 6192.39339
format_str = f"leading zero = {angka:0.3f}\n"
print(format_str)

#menampilkan tanda + dan -
angka_minus = -20
angka_plus = 20
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}\n"
print(format_minus)
print(format_plus)

#memformat persen
angka = 0.555
format_persen = f"persentase = {angka:%}\n"
print(format_persen)