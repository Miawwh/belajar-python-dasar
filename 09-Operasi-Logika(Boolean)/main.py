# Operasi Logika atau Boolean
# Operasi Logika dipakai untuk menggabungkan atau memanipulasi nilai boolean (True/False). Hasilnya juga dalam bentuk boolean
# Jenis-jenis Asli operasi logika : "Not, And, Or"

# Operasi Logika 'not' berfungsi mengembalikan nilai menjadi (true/false) tergantung nilai awalnya, jika "true" menggunakan 'not' akan menjadi lawan nilainya yairu "False"
print("\n==== NOT ====")
a = True
b = not a 
#Variabel "b" akan berisi nilai false karena menggunakan operasi not (logika not, mengembalikan lawan nilainya)
print(f"data a = {a}")
print(f"-----NOT------")
print(f"data b = {b}")

# Operasi logika 'or' berfungsi jika salah satu "true", maka hasilnya adalah "true"
print("\n==== OR ====")
a = False
b = False
c = a or b
print(f"{a} or {b} = {c}")

a = False
b = True
c = a or b
print(f"{a} or {b}  = {c}")

a = True
b = False
c = a or b
print(f"{a}  or {b} = {c}")

a = True
b = True
c = a or b
print(f"{a}  or {b}  = {c}")

# Operasi logika 'and' berfungsi jika dua buah nilai true maka hasilnya true
print("\n==== AND ====")
a = False
b = False
c = a and b
print(f"{a} and {b} = {c}")

a = False
b = True
c = a and b
print(f"{a} and {b}  = {c}")

a = True
b = False
c = a and b
print(f"{a}  and {b} = {c}")

a = True
b = True
c = a and b
print(f"{a}  and {b}  = {c}")

# XOR sebenarnya bukan asli operasi logikan(boolean), tapi XOR(^) adalah operasi bitwise. Tapi karena di Python, bool adalah turunan dari int (True == 1, False == 0), maka : 
""" 
Kalau operandnya boolean → hasilnya bisa dianggap sebagai logika XOR (eksklusif OR)
Kalau operandnya integer → hasilnya bitwise XOR, bukan logika
"""
# XOR di boolean, berfungsi jika salah satu operandnya bernilai true maka hasilnya true, sisanya false
print("\n==== XOR ====")
a = False
b = False
c = a ^ b
print(f"{a} ^ {b} = {c}")

a = False
b = True
c = a ^ b
print(f"{a} ^ {b}  = {c}")

a = True
b = False
c = a ^ b
print(f"{a}  ^ {b} = {c}")

a = True
b = True
c = a ^ b
print(f"{a}  ^ {b}  = {c}")