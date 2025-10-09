# =========================================
# Belajar Python - Operasi dan Manipulasi String (Part 1)
# =========================================

# 🔹 Apa itu string?
# String adalah tipe data yang berisi kumpulan karakter (huruf, angka, simbol, spasi).
# String diapit dengan tanda kutip tunggal ('...') atau ganda ("...").
# Contoh:
#   "Halo Dunia"
#   'Python123'
#   "Ini contoh kalimat dengan spasi"
#
# Ingat:
# - String bisa kosong → "" atau ''
# - String termasuk tipe data yang "immutable" (tidak bisa diubah langsung isinya).
#   Artinya, kalau kita mengubah string, sebenarnya Python membuat string baru.

# =========================================
# Mari kita pelajari operasi dan manipulasi string
# =========================================

# 1. Menyambung string (concatenate)
# -----------------------------------------
nama_depan = "Akira"
nama_tengah = "The"
nama_akhir = "Lafingo"

# Menggabungkan string menggunakan operator +
nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)
print("")

# 2. Menghitung panjang string
# -----------------------------------------
# Fungsi len() menghitung jumlah karakter dalam string (termasuk spasi).
panjang_nama = len(nama_lengkap)

# Karena panjang_nama hasilnya angka (int), maka harus diubah (casting) ke string
# agar bisa digabungkan dengan teks lain dalam print.
print("Panjang dari teks \"" + nama_lengkap + "\" adalah " + str(panjang_nama))
print("")

# 3. Operator membership (in, not in)
# -----------------------------------------
# Mengecek apakah sebuah huruf/kata ada di dalam string.
A = "A"
cek = A in nama_lengkap
print(A + " ada di dalam \"" + nama_lengkap + "\" jawabannya " + str(cek))

X = "X"
cek = X not in nama_lengkap
print(X + " tidak ada di dalam \"" + nama_lengkap + "\" jawabannya " + str(cek))
print("")

# 4. Mengulang string
# -----------------------------------------
# String bisa dikalikan dengan angka (int).
print(10 * "=")
print("=" * 10)
print("")

# 5. Indexing & Slicing
# -----------------------------------------
# String = kumpulan karakter, dan tiap karakter punya index (nomor posisi).
# Index selalu mulai dari 0 (kiri ke kanan).
# Kalau negatif, mulai dari -1 (kanan ke kiri).
print(nama_lengkap)
print("Index ke-0 adalah " + nama_lengkap[0])
print("Index ke-3 adalah " + nama_lengkap[3])
print("Index ke-(-1) adalah " + nama_lengkap[-1])

# Slicing: mengambil beberapa karakter sekaligus
print("Index ke-[0:3] → " + nama_lengkap[0:3])    # ambil index 0 sampai sebelum 3
print("Index ke-[0:6] → " + nama_lengkap[0:6])    # ambil index 0 sampai sebelum 6
print("Index ke-[0:17:2] → " + nama_lengkap[0:17:2])  # ambil dengan langkah 2
print("")


# 6. Karakter terkecil & terbesar
# -----------------------------------------
# Fungsi min() dan max() membandingkan karakter berdasarkan kode ASCII.
print("Paling kecil: " + min(nama_lengkap)) 
print("Paling besar: " + max(nama_lengkap))
print("")


# Melihat kode ASCII dengan ord(), dan sebaliknya dengan chr().
ASCII_CODE = ord(" ")
print("ASCII Code untuk spasi adalah: " + str(ASCII_CODE))
code = 117
print("Char untuk ASCII 117 adalah: " + chr(code))
print("")

# 7. Operator dalam bentuk method
# -----------------------------------------
# Nah, ini bagian penting!
# Selain menggunakan operator (seperti +, *, in, dll),
# string juga punya fungsi bawaan yang menempel langsung pada objek string tersebut.
# Fungsi bawaan ini disebut "method".
# Kenapa disebut method? Karena string di Python adalah sebuah "class",
# dan class itu punya fungsi-fungsi (method) yang bisa dipakai.
# Contoh: .count(), .upper(), .lower(), dll.
# Bedanya dengan operator, method dipanggil langsung dari string itu sendiri.

name = "Alan oehgty gerbet"

# .count("e") → menghitung jumlah huruf "e" di dalam string
jumlah = name.count("e")
print("Huruf 'e' pada \"" + name + "\" ada sebanyak " + str(jumlah))
