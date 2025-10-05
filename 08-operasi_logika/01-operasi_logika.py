# ====================================
# Belajar Python - Operasi Logika
# Materi: Operator Logika (Boolean)
# ====================================

# 🔹 Apa itu operator logika?
# Operator logika digunakan untuk menggabungkan ekspresi boolean
# (True/False) menjadi satu kondisi baru.
# Hasil akhirnya juga berupa nilai boolean: True atau False.

# Daftar operator logika di Python:
# and  -> True jika SEMUA kondisi bernilai True
# or   -> True jika MINIMAL SATU kondisi bernilai True
# not  -> Membalik nilai (True jadi False, False jadi True)

# ====================================
# 1. Operator AND
# ====================================
print("Operator AND:")
print(f"True and True   -> {True and True}")     # Kedua kondisi True -> hasilnya True
print(f"True and False  -> {True and False}")    # Salah satu kondisi False -> hasilnya False
print(f"False and True  -> {False and True}")    # Salah satu kondisi False -> hasilnya False
print(f"False and False -> {False and False}")   # Kedua kondisi False -> hasilnya False
print("\n")
# 🔎 Catatan:
# - "and" hanya True kalau semua kondisi bernilai True.


# ====================================
# 2. Operator OR
# ====================================
print("Operator OR:")
print(f"True or True   -> {True or True}")       # Kedua kondisi True -> hasilnya True
print(f"True or False  -> {True or False}")      # Salah satu kondisi True -> hasilnya True
print(f"False or True  -> {False or True}")      # Salah satu kondisi True -> hasilnya True
print(f"False or False -> {False or False}")     # Kedua kondisi False -> hasilnya False
print("\n")
# 🔎 Catatan:
# - "or" akan True kalau minimal ada 1 kondisi yang True.


# ====================================
# 3. Operator NOT
# ====================================
print("Operator NOT:")
print(f"not True  -> {not True}")                # Membalik True jadi False
print(f"not False -> {not False}")               # Membalik False jadi True
print("\n")
# 🔎 Catatan:
# - "not" membalikkan nilai boolean.


# ====================================
# 4. Kombinasi Operasi Logika
# ====================================
# Operator logika biasanya digunakan bersama operator relasional (perbandingan)
x = 5
y = 10

print("Kombinasi Operasi Logika dengan Perbandingan:")
print(f"(x > 3) and (y > 5)  -> {(x > 3) and (y > 5)}")   # True and True -> True
print(f"(x < 3) or (y > 5)   -> {(x < 3) or (y > 5)}")    # False or True -> True
print(f"not (x == 5)         -> {not (x == 5)}")          # not True -> False

# Tambahan contoh biar lebih jelas
print(f"(x == 5) and (y == 10) -> {(x == 5) and (y == 10)}") # True and True -> True
print(f"(x != 5) or (y < 5)    -> {(x != 5) or (y < 5)}")    # False or False -> False
