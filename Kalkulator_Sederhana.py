print("\n" + 50*"=")
print(" Welcome to My  Program!! ".center(50,"="))

print(" Kalkulator Sederhana ".center(50,"="))
print(50*"=" + "\n")



number_1 = float(input("Masukkan Angka: "))
operator = input("Masukkan Operator: ")
number_2 = float(input(f"mau di {operator} dengan berapa? "))

if operator == "+":
                print(f"Hasil = {number_1 + number_2}")
elif operator =="-":
                print(f"Hasil = {number_1 - number_2}")
elif operator == "*" or operator == "x":
                print(f"Hasil = {number_1 * number_2}")
elif operator == "/":
                print(f"Hasil = {number_1 / number_2}")
else:
                print("Masukkan Operator dengan Benar!")

