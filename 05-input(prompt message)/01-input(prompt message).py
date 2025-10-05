# ====================================
# Belajar Python - Input
# Materi: Memasukkan data dari pengguna
# ====================================

# 🔹 Apa itu input()?
# input() adalah fungsi bawaan Python yang digunakan untuk menerima data dari pengguna (user).
# Secara default, input() selalu mengembalikan nilai dalam bentuk string (teks).
# Biasanya kalau tidak menggunakan input(), kita menulis nilai langsung di kode (hard-code).
# Dengan input(prompt) program menjadi interaktif karena meminta nilai dari user saat dijalankan.

# Bentuk umum:
# variabel = input("Teks yang ditampilkan ke user: ")

# Contoh sederhana:
nama = input("Masukkan nama Anda: ")
print("Halo,", nama)
# Variabel 'nama' akan berisi string yang dimasukkan user.

# ====================================
# Menggabungkan input() dengan casting
# ====================================
# Karena input() menghasilkan string, jika ingin menggunakan tipe lain (int/float/bool),
# kita perlu mengubah (casting) string tersebut ke tipe yang diinginkan.

# 🔹 Input integer
# Inputan yang diminta harus berupa bilangan bulat (contoh: 10, 25, -7).
umur = int(input("Masukkan umur Anda: "))   # casting dari string ke int
print("Umur Anda adalah:", umur, "tahun")

# 🔹 Input float
# Input float dapat menerima 2 tipe nilai:
# - bilangan desimal (contoh: 12.5, 3.14)
# - bilangan bulat (contoh: 9, tetapi hasil casting menjadi 9.0)
tinggi = float(input("Masukkan tinggi badan Anda (cm): "))  # casting ke float
print("Tinggi Anda adalah:", tinggi, "cm")

# 🔹 Input boolean
# Jika menggunakan bool(input()):
# - Jika inputan dikosongkan lalu langsung Enter → hasilnya False
# - Jika inputan diisi dengan nilai apa pun → hasilnya True
mahasiswa = bool(input("Apakah Anda mahasiswa? (isi apa saja atau kosongkan): "))
print("Mahasiswa:", mahasiswa)

# ====================================
# Menerima lebih dari satu inputan
# ====================================
# Kadang kita ingin user memasukkan lebih dari satu nilai sekaligus,
# misalnya 2 atau 3 bilangan dalam satu baris.
# Caranya kita bisa menggunakan fungsi split() untuk memisahkan input
# berdasarkan spasi, lalu dipetakan (map) ke tipe data tertentu.

# Bentuk umum (basic syntax):
# variabel1, variabel2, ... = map(tipe_data, input("Pesan: ").split())

# Contoh: menerima 3 bilangan bulat yang dipisahkan spasi
a, b, c = map(int, input("Masukkan 3 bilangan yang dipisah dengan spasi: ").split())
print("Bilangan pertama:", a)
print("Bilangan kedua:", b)
print("Bilangan ketiga:", c)

# Contoh lain: menerima 2 angka desimal (float)
x, y = map(float, input("Masukkan 2 bilangan desimal (dipisah spasi): ").split())
print("Bilangan x:", x)
print("Bilangan y:", y)

