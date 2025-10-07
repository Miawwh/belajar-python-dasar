# =========================================
# Latihan Program - Operator Membership
# =========================================

# 1. Memeriksa apakah suatu kata/huruf ada di dalam teks/nama
# Program ini akan meminta user memasukkan sebuah kalimat/nama,
# lalu user diminta memasukkan kata atau huruf yang ingin dicari.
# Hasil akhirnya berupa True (jika ada) atau False (jika tidak ada).

# Meminta input kalimat/kata/nama dari user
input_user = input("Masukkan nama terserah (kalimat/kata/nama): ")

# Meminta input kata/huruf yang ingin dicari di dalam kalimat di atas
huruf_dicari = input("Kata/huruf apa yang mau dicari? : ")

# Mengecek apakah kata/huruf tersebut ada di dalam kalimat
# Operator `in` akan menghasilkan True jika huruf_dicari ada di input_user
# dan False jika tidak ada.
print(f"Huruf/kata yang anda cari adalah '{huruf_dicari}' di dalam '{input_user}' jawabannya : {huruf_dicari in input_user}")
print("")

# 2. Memeriksa jika jika ada kata/huruf 

# Meminta input kalimat/kata/nama dari user
input_user = input("Masukkan nama terserah (kalimat/kata/nama): ")

# Meminta input kata/huruf yang ingin dicari di dalam kalimat di atas
huruf_dicari = input("Kata/huruf apa yang mau dicari? : ")

# Mengecek apakah kata/huruf tersebut TIDAK ADA di dalam kalimat
# Operator `not in` akan menghasilkan True jika huruf_dicari tidak ada di input_user
# dan False jika ada.
print(f"Apakah '{huruf_dicari}' TIDAK ada di dalam '{input_user}'? : {huruf_dicari not in input_user}")
