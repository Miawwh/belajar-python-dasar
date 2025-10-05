# ====================================
# Belajar Python - Operasi Relasional
# Materi: Operator Relational (Perbandingan)
# ====================================

# 🔹 Apa itu operator relasional?
# Operator relasional (perbandingan) digunakan untuk
# membandingkan dua nilai. 
# Hasil dari perbandingan selalu berupa boolean:
# True (benar) atau False (salah).

# Daftar operator relasional di Python:
# ==   -> sama dengan
# !=   -> tidak sama dengan
# >    -> lebih besar dari
# <    -> lebih kecil dari
# >=   -> lebih besar sama dengan
# <=   -> lebih kecil sama dengan


# ====================================
# 1. Perbandingan Integer dengan Integer
# ====================================
a = 10
b = 3
print("Perbandingan Integer:")
print(f"{a} == {b} -> {a == b}")
print(f"{a} != {b} -> {a != b}")
print(f"{a} > {b}  -> {a > b}") 
print(f"{a} < {b}  -> {a < b}")
print(f"{a} >= {b} -> {a >= b}")
print(f"{a} <= {b} -> {a <= b}")
print("\n")

# 🔎 Catatan:
# - Jika 10 > 10 → hasilnya False, karena 10 tidak lebih besar dari 10.
# - Jika ingin hasil True, nilainya harus lebih dari 10 (contoh: 10.1).
# - Untuk kasus 10 >= 10 → hasilnya True, karena 10 sama dengan 10.
#   Hal ini berlaku juga untuk <= dan <.


# ====================================
# 2. Perbandingan Integer dengan Float
# ====================================
x = 10       # int
y = 10.0     # float
z = 7.5      # float

print("Perbandingan Integer dengan Float:")
print(f"{x} == {y} -> {x == y}")   # True, karena 10 sama dengan 10.0
print(f"{x} != {z} -> {x != z}")   # True, karena 10 tidak sama dengan 7.5
print(f"{x} > {z}  -> {x > z}")    # True, karena 10 lebih besar dari 7.5
print(f"{x} < {y}  -> {x < y}")    # False, karena 10 tidak lebih kecil dari 10.0
print("\n")

# 🔎 Catatan:
# - Python bisa membandingkan int dan float langsung.
# - Hasilnya tetap akurat, karena Python otomatis menyesuaikan tipe data.


# ====================================
# 3. Perbandingan String dengan String
# ====================================
s1 = "apel"
s2 = "jeruk"
s3 = "Apel"

print("Perbandingan String:")
print(f"{s1} == {s2} -> {s1 == s2}")   # False, "apel" ≠ "jeruk"
print(f"{s1} != {s2} -> {s1 != s2}")   # True
print(f"{s1} < {s2}  -> {s1 < s2}")    # True, karena 'a' lebih kecil dari 'j'
print(f"{s1} > {s3}  -> {s1 > s3}")    # True, karena huruf kecil 'a' (97) > huruf besar 'A' (65)
print(f"{s2} >= {s1} -> {s2 >= s1}")   # True, "jeruk" lebih besar dari "apel")

# 🔎 Catatan:
# - Saat string dibandingkan, Python melihat urutan abjad berdasarkan Unicode/ASCII.
# - Huruf besar (A-Z) punya nilai lebih kecil daripada huruf kecil (a-z).
#   Jadi "apel" > "Apel".
# - Semakin dekat huruf ke "z", makin tinggi nilainya.
