# ====================================
# Program Menampilkan Data Diri
# ====================================

# Program ini menggunakan:
# - input() untuk meminta data dari user
# - casting int() dan float() agar data angka sesuai tipe
# - f-string untuk menampilkan data dalam format yang rapi

# Meminta input dari user
nama_lengkap = input("Masukkan nama lengkap Anda: ")
umur = int(input("Masukkan umur Anda sekarang: "))         # input umur → integer
tinggi_badan = float(input("Masukkan tinggi badan Anda: ")) # input tinggi → float (contoh: 162.5)
kota = input("Masukkan kota tempat tinggal Anda: ")

# Menampilkan hasil dengan f-string
print(f"Halo, perkenalkan nama saya {nama_lengkap}, " "tinggi saya {tinggi_badan} cm dan saya berumur {umur} tahun. " "Saya tinggal di {kota}.")
