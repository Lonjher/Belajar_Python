## Loop dengan List

print(30*"=")
print(" For Loop List ".center(30,"="))
print(30*"=")

angka_list = [0,1,2,3,4,5]
for i in angka_list:
    print(f"Loop ke -> {i}")
print(" Akhir dari Program ".center(30,"="))

print("\n") 

## Loop dengan Range
# Yang Pertama

print(30*"=")
print(" For Loop Range versi 1 ".center(30,"="))
print(30*"=")

angka_range = range(5)
for i in angka_range:
    print (f"i sekarang -> {i}")
print(" Akhir dari Program ".center(30,"="))

print("\n")

# Yang Kedua
print(30*"=")
print(" For Loop Range versi 2  ".center(30,"="))
print(30*"=")

angka_range = range(3,10)
for i in angka_range:
    print(f"i sekarang -> {i}")
print(" Akhir dari Program ".center(30,"="))

print("\n")

## Loop dengan String

print(30*"=")
print(" For Loop dengan String  ".center(30,"="))
print(30*"=")

kata_str = "Aditya Chandra"

for huruf in kata_str:
    print(huruf)
print(" Akhir dari Program ".center(30,"="))

print("\n")

word = (0)
while word < 5:
    word += 1
    print(" Aku Sayang Kamu ".center(30,"="))
    
for i in range(5):
    print(" *")