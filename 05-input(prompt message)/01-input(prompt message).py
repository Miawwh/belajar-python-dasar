# ====================================
# Belajar Python - Input
# Materi: Memasukkan data dari pengguna
# Dibuat oleh: Jeremiah Lengkong
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

