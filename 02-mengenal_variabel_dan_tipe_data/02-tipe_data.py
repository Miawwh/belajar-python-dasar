# ====================================
# Belajar Python - Tipe Data
# Materi: Mengenal Tipe Data di Python
# Dibuat oleh: Jeremiah Lengkong
# ====================================

# Apa itu tipe data?
# Tipe data adalah jenis nilai/data yang bisa disimpan di dalam sebuah variabel.
# Setiap nilai yang kita simpan di Python pasti memiliki tipe data tertentu.
# Python akan otomatis mengenali tipe data berdasarkan nilai yang kita berikan.

# Tipe data dasar yang paling sering digunakan:
# 1. String (str)   → kumpulan karakter atau teks
# 2. Integer (int)  → bilangan bulat
# 3. Float (float)  → bilangan desimal
# 4. Boolean (bool) → logika benar (True) atau salah (False)
# 5. Complex (complex) → bilangan kompleks (lebih sering dipakai di bidang matematika/teknik)

# 🔹 String (str)
# String adalah kumpulan karakter atau teks yang ditulis di antara tanda kutip ('' atau "").
nama = "Jeremiah"
hobi = 'Belajar Python'
print("String - nama:", nama)
print("String - hobi:", hobi)

# 🔹 Integer (int)
# Integer adalah bilangan bulat, bisa positif maupun negatif, dan tidak memiliki koma.
umur = 17
tahun = 2025
print("Integer - umur:", umur)
print("Integer - tahun:", tahun)

# 🔹 Float (float)
# Float adalah bilangan desimal, dituliskan dengan titik (.) sebagai pemisah.
tinggi = 162.3
berat = 55.8
print("Float - tinggi:", tinggi)
print("Float - berat:", berat)

# 🔹 Boolean (bool)
# Boolean hanya memiliki dua nilai, yaitu True atau False.
# Perhatikan! Penulisannya harus dengan huruf kapital di awal: "True" atau "False".
# Jika kita menulis "true" atau "false" dengan huruf kecil, Python akan error,
# karena Python bersifat case-sensitive (peka terhadap huruf besar/kecil).
mahasiswa = True
lulus = False
print("Boolean - mahasiswa:", mahasiswa)
print("Boolean - lulus:", lulus)

# 🔹 Complex (complex)
# Complex adalah bilangan yang terdiri dari bagian real dan bagian imajiner.
# Biasanya digunakan di bidang matematika, fisika, atau teknik.
z = 3 + 5j
print("Complex - z:", z)
print("Bagian real:", z.real)      # Bagian real = 3.0
print("Bagian imajiner:", z.imag)  # Bagian imajiner = 5.0

# 🔹 Mengecek tipe data dengan fungsi type()
# Untuk mengetahui tipe data sebuah variabel, kita bisa gunakan fungsi bawaan Python: type()
print("\nCek tipe data masing-masing variabel:")
print("Tipe data nama:", type(nama))             # Output: <class 'str'>
print("Tipe data umur:", type(umur))             # Output: <class 'int'>
print("Tipe data tinggi:", type(tinggi))         # Output: <class 'float'>
print("Tipe data mahasiswa:", type(mahasiswa))   # Output: <class 'bool'>
print("Tipe data z:", type(z))                   # Output: <class 'complex'>

# Catatan:
# Hasil dari fungsi type() akan menampilkan "<class '...'>".
# Kata "class" di sini menunjukkan bahwa tipe data di Python
# sebenarnya dibuat berdasarkan konsep "class" (objek).
# Jadi int, str, float, bool, dan complex semuanya adalah class bawaan di Python.
