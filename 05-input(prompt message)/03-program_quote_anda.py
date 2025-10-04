# ====================================
# Program Quote Harian
# ====================================

# Program ini meminta pengguna untuk:
# - memasukkan sebuah kata/kalimat (quote)
# - memasukkan nama user sebagai penulis
# Hasilnya akan ditampilkan dengan format yang lebih menarik.

kata_kata = input("Masukkan kata-kata hari ini: ")
nama_user = input("Masukkan nama Anda: ")

# Menampilkan hasil dengan format
print("\n")  # membuat baris kosong biar lebih rapi
print(f"\t\"{kata_kata}\",")   # pakai tanda kutip biar seperti quote
print(f"\t   ⎯ {nama_user} ⎯") # nama penulis di bawahnya
