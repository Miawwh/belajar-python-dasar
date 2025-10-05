# ====================================
# Belajar Python - Fungsi print()
# Materi: Output dengan print() di Python
# ====================================

# Di bab sebelumnya (tipe data dan casting) kita sudah beberapa kali menggunakan print().
# Nah, sekarang kita akan bahas lebih detail tentang apa itu print() dan bagaimana penggunaannya.

# 🔹 Apa itu print()?
# print() adalah fungsi bawaan Python yang digunakan untuk menampilkan data ke layar (output).
# print() juga sering disebut sebagai "basic output statement".

# Bentuk umum fungsi print():
# print(object(s), sep=" ", end="\n", file=sys.stdout, flush=False)
#
# Penjelasan parameter:
# - object(s) → parameter ini berisi semua hal yang ingin ditampilkan
#               (bisa berupa string, angka, variabel, ekspresi, dsb).
# - sep       → pemisah antar object jika ada lebih dari satu (default: spasi " ").
# - end       → karakter yang ditambahkan di akhir output (default: "\n" artinya baris baru).
# - file      → kemana output dikirim (default: sys.stdout yaitu layar/console).
# - flush     → True/False, untuk memaksa sistem langsung mencetak output (default: False).
#
# Catatan: jika nilai dari parameter-parameter (sep sampai flush) tidak disebutkan,
# maka Python akan menggunakan nilai default dari masing-masing parameter.

# Contoh penggunaan dasar
print("Hello World")            # menampilkan string
print("Nama:", "Jeremiah")      # menampilkan lebih dari satu object (dipisah spasi secara default)

# 🔹 Menampilkan teks panjang / menu / tabel dengan print()
# Kalau ingin menampilkan teks panjang tanpa harus banyak print(),
# kita bisa pakai triple quote ("""...""") untuk string multi-baris.

print("""
Menu Makanan:
1. Nasi
2. Ikan
3. Pizza
""")

# Atau bisa juga untuk membuat tampilan tabel sederhana
print("""
=========================
| No |   Nama Makanan   |
=========================
|  1 | Nasi             |
|  2 | Ikan             |
|  3 | Pizza            |
=========================
""")


# 🔹 Memanggil variabel dalam print() (basic output statement)
nama = "Jeremiah"
umur = 17
tinggi = 162.3

# Cara pemanggilan variabel di basic output statement:
# → langsung menuliskan nama variabel di dalam print(), dipisahkan dengan koma jika lebih dari satu.
print("Nama saya:", nama, ", umur:", umur, "tahun, tinggi:", tinggi, "cm")
# Kekurangan cara ini: jika variabel banyak, output bisa terlihat kurang rapi.

# 🔹 Parameter sep
print("A", "B", "C", sep="-")   # defaultnya spasi, tapi diubah jadi tanda "-"

# 🔹 Parameter end
print("Hello", end=" ")         # mengganti akhir default (\n) jadi spasi
print("World")                  # hasil: Hello World (di baris yang sama)

# 🔹 Parameter file dan flush
# Parameter ini jarang dipakai untuk pemula,
# biasanya digunakan di aplikasi khusus (contoh: menulis output ke file log).

# ====================================
# Formatted Output: f-string
# ====================================

# f-string memungkinkan kita menuliskan variabel/ekspresi langsung di dalam string.
# Bentuk umum:
# f"teks {expression:format specifier}"

print("\nMenggunakan f-string:")
print(f"Nama saya {nama}, umur {umur} tahun, dan tinggi {tinggi} cm")
# Cara pemanggilan variabel di f-string:
# → tuliskan nama variabel di dalam kurung kurawal {}.
# Selain variabel, kita juga bisa langsung menuliskan ekspresi/operasi Python di dalam {}.

# Contoh pemanggilan ekspresi langsung di f-string:
print(f"Dua tahun lagi umur saya {umur + 2}")
print(f"Tinggi dalam meter: {tinggi / 100} m")
print(f"Panjang nama saya adalah {len(nama)} huruf")

# Format specifier memungkinkan kita mengatur bagaimana data ditampilkan.
# Bentuk umum format specifier:
# [fill] [align] [sign] [#] [0] [width] [,] [.precision] [type]
#
# Contoh penggunaan format specifier:
nilai = 90.5678
print("\nFormat Specifier:")
print(f"Nilai ujian: {nilai:.2f}")   # menampilkan 2 angka di belakang koma
print(f"Nilai ujian: {nilai:10.2f}") # lebar 10 karakter, dengan 2 angka desimal

# ====================================
# Escape Sequence
# ====================================

# Escape sequence digunakan untuk menambahkan karakter khusus ke dalam string.
# Contoh yang sering dipakai:
# \n  → baris baru (newline)
# \t  → tab (spasi panjang)
# \"  → tanda kutip ganda
# \'  → tanda kutip tunggal
# \\  → backslash

print("\nEscape Sequence:")
print("Halo\nDunia")    # \n membuat baris baru
print("Nama\tSaya")     # \t menambahkan tab
print("Dia berkata: \"Belajar Python itu mudah\"")
print('It\'s a sunny day')   # kutip tunggal di dalam string
print("C:\\Users\\Jeremiah") # menampilkan backslash

# ====================================
# Tambahan (opsional / advanced)
# ====================================

# Sebenarnya kita juga bisa mengubah gaya teks di output terminal,
# seperti warna (foreground color), bold, underline, italic, dll.
# Namun ini bukan materi wajib, lebih ke tambahan saja.
# Caranya menggunakan ANSI Escape Code.

print("\nTeks dengan format khusus:")
print("\033[1mTeks Bold\033[0m")           # Bold
print("\033[4mTeks Underline\033[0m")      # Underline
print("\033[3mTeks Italic\033[0m")         # Italic
print("\033[31mTeks Merah\033[0m")         # Merah (31 = red)
print("\033[32mTeks Hijau\033[0m")         # Hijau (32 = green)
print("\033[34mTeks Biru\033[0m")          # Biru (34 = blue)
