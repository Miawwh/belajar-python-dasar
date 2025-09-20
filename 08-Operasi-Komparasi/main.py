 #Operasi Komparasi

# Setiap hasil dari operasi komparasi(perbandingan) adalah boolean

# >,<,>=,<=,==,is,is not

a = 4
b = 2

# lebih besar dari >
print("=============== Lebih besar(>) ======================")
hasil = a > 3
print(f"{a} > 3 = {hasil}")
hasil = b > 3
print(f"{b} > 3 = {hasil}")

# lebih besar dari <
print("=============== Kurang dari(<) ======================")
hasil = a < 3
print(f"{a} < 3 = {hasil}")
hasil = b < 3
print(f"{b} < 3 = {hasil}")

# lebih besar sama dengan dari >=
print("=============== Lebih dari sama dengan (>=) ======================")
hasil = a >= 3
print(f"{a} >= 3 = {hasil}")
hasil = b >= 3
print(f"{b} >= 3 = {hasil}")
hasil = b >= 2
print(f"{b} >= 2 = {hasil}")

# Kurang dari sama dengan <=
print("=============== Kurang dari sama dengan (<=) ======================")
hasil = a <= 3
print(f"{a} <= 3 = {hasil}")
hasil = b <= 3
print(f"{b} <= 3 = {hasil}")
hasil = b <= 2
print(f"{b} <= 2 = {hasil}")

# sama dengan ==
print("=============== Sama dengan (==) ======================")
hasil = a == 3
print(f"{a} == 3 = {hasil}")
hasil = b == 3
print(f"{b} == 3 = {hasil}")
hasil = b == 2
print(f"{b} == 2 = {hasil}")

# Tidak sama dengan !=
print("=============== Tidak sama dengan (!=) ======================")
hasil = a != 3
print(f"{a} != 3 = {hasil}")
hasil = b != 3
print(f"{b} != 3 = {hasil}")
hasil = b != 2
print(f"{b} != 2 = {hasil}")

#  'is' sebagai komparasi object identity
print("=============== Object identity(is) ======================")
x = 5 # ini adalah assigment membuat object
y = 5 # ini adalah assigment membuat object
print(f"Nilai x = {x}, id = {hex(id(x))}")
print(f"Nilai y = {y}, id = {hex(id(y))}")
hasil = x is y
print(f"x is y = {hasil}")

p = 5 # ini adalah assigment membuat object
o = 6 
print(f"Nilai p = {p}, id = {hex(id(p))}")
print(f"Nilai o = {o}, id = {hex(id(o))}")
hasil = p is o
print(f"p is o = {hasil}")

#  'is not' sebagai komparasi object identity
print("=============== Object identity(is not) ======================")
x = 5 # ini adalah assigment membuat object
y = 5 # ini adalah assigment membuat object
print(f"Nilai x = {x}, id = {hex(id(x))}")
print(f"Nilai y = {y}, id = {hex(id(y))}")
hasil = x is not y
print(f"x is not y = {hasil}")

p = 5 # ini adalah assigment membuat object
o = 6 
print(f"Nilai p = {p}, id = {hex(id(p))}")
print(f"Nilai o = {o}, id = {hex(id(o))}")
hasil = p is not o
print(f"p is not o = {hasil}")
