# ====================================
# Belajar Python - Casting (Konversi Tipe Data)
# Materi: Mengubah (convert) tipe data
# Dibuat oleh: Jeremiah Lengkong
# ====================================

# Apa itu casting?
# Casting adalah proses mengubah tipe data dari suatu nilai/variabel menjadi tipe data lain.
# Contoh: angka menjadi teks, teks menjadi angka, float menjadi integer, dan sebagainya.
# Python menyediakan fungsi bawaan untuk melakukan casting:
# - int()    → mengubah ke bilangan bulat (integer)
# - float()  → mengubah ke bilangan desimal (float)
# - str()    → mengubah ke string (teks)
# - bool()   → mengubah ke boolean (True/False)

# 🔹 Contoh casting ke integer
x = int(3.8)         # dari float ke integer
y = int("10")        # dari string ke integer
print("Casting ke int:", x, y)

# Catatan:
# - Saat bilangan desimal (float) diubah ke bilangan bulat (integer),
#   Python akan mengambil angka bulat terdekat ke bawah (floor).
#   Contoh: 3.9 → 3, bukan 4.
# - Jika tipe data string ingin diubah ke integer, maka string tersebut
#   harus berisi angka. Contoh: "90" → 90 bisa, tetapi "satu" → error.

# 🔹 Contoh casting ke float
a = float(7)         # dari integer ke float
b = float("12.5")    # dari string ke float
print("Casting ke float:", a, b)

# Catatan:
# - Sama seperti int(), string hanya bisa dikonversi ke float jika isinya angka.
#   Contoh: "12.5" → 12.5 bisa, tetapi "tiga koma lima" → error.

# 🔹 Contoh casting ke string
nama = str(123)      # dari integer ke string
nilai = str(45.6)    # dari float ke string
print("Casting ke str:", nama, nilai)

# 🔹 Contoh casting ke boolean
# Aturan bool() di Python:
# - Angka 0 → False, selain itu → True
# - String kosong "" → False, selain itu → True
# - List/Set kosong [] {} → False, selain itu → True
print("Casting ke bool dari 0:", bool(0))
print("Casting ke bool dari 1:", bool(1))
print("Casting ke bool dari '' :", bool(""))
print("Casting ke bool dari 'Halo':", bool("Halo"))
