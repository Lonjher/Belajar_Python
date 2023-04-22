nama = "Aditya Chandra"
age = "17 th"
tinggi = "80 cm"
berat_badan= "45 kg"

#standard
biodata = f"nama = {nama}, umur = {age}, tinggi = {tinggi}, berat badan = {berat_badan}\n"
print(5*"=" + "Biodata" +"="*5)
print(biodata)

# menggunakan enter, newline (\n)
biodata = f"nama = {nama}, \numur = {age}, \ntinggi = {tinggi}, \nberat badan = {berat_badan}\n"
print(5*"=" + "Biodata" +"="*5)
print(biodata)

# Menggunakan tanda kutip 3
biodata = f"""
nama        = {nama:>14}
umur        = {age:>9}
tinggi      = {tinggi:>9}
berat badan = {berat_badan:>9}"""
print(5*"=" + "Biodata" +"="*5)
print(biodata)
