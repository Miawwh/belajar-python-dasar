# ====================================
# Belajar Python - Variabel 
# Materi: Mengenal Variabel 
# Dibuat oleh: Jeremiah Lengkong
# ====================================

# 🔹 Apa itu variabel?
# Variabel adalah tempat untuk menyimpan data di dalam memori komputer.
# Ibaratkan variabel sebagai sebuah "wadah" atau "kotak" yang dapat menampung data.
# Analogi sederhana:
# Bayangkan sebuah kotak dengan label di luarnya. Kita bisa memasukkan berbagai jenis barang ke dalam kotak tersebut.
# Label yang menempel di luar kotak itulah yang menjadi nama variabel, 
# sedangkan barang di dalam kotak adalah data atau nilai yang disimpan.
# Dalam bahasa pemrograman Python, kita tidak perlu menentukan tipe data secara langsung.
# Python akan otomatis mengenali tipe data berdasarkan nilai yang dimasukkan ke dalam variabel.

# Membuat variabel biasa disebut dengan "assignment statement".
# Assignment berarti memberikan nilai, sedangkan statement berarti pernyataan atau instruksi.
# Jadi, assignment statement adalah pernyataan untuk memberikan sebuah nilai ke dalam variabel.

# Contoh membuat variabel sederhana:
nama = "jeremiah"       # Variabel bernama "nama" berisi teks (string) dengan nilai: "jeremiah"
umur = 17               # Variabel bernama "umur" berisi angka (integer) dengan nilai: 17
tinggi = 162.3          # Variabel bernama "tinggi" berisi angka desimal (float) dengan nilai: 162.3
mahasiswa = True        # Variabel bernama "mahasiswa" berisi nilai True (boolean)

# Sintaks dasar (basic syntax) untuk membuat variabel adalah:
# variabel = expression
# "expression" di sini bisa berupa nilai langsung (contoh: 10, "halo", True),
# atau bisa juga berupa hasil operasi/perhitungan (contoh: 5+3, a*2),
# bahkan bisa berupa nilai dari variabel lain.

# 🔹 Multiple Assignment
# Di Python, kita juga bisa memberikan nilai ke beberapa variabel sekaligus dalam satu baris.
# Contoh:
x = y = z = 0           # Semua variabel x, y, dan z berisi angka 0
a, b, c = 1, 2, 3       # Variabel a=1, b=2, dan c=3
nama, umur = "jeremiah", 17  # Variabel nama berisi "jeremiah" dan umur berisi 17

# 🔹 Mengubah Nilai Variabel
# Nilai di dalam variabel bisa diganti atau diperbarui dengan memberikan nilai baru.
umur = 17
print("Umur awal:", umur)   # Hasil: 17
umur = 20
print("Umur setelah diubah:", umur)   # Hasil: 20

# Perlu diingat: Python akan mengeksekusi program dari baris paling atas ke bawah secara berurutan.
# Jadi nilai terbaru yang diberikan ke sebuah variabel akan menimpa (overwrite) nilai sebelumnya.

# Aturan penamaan variabel di Python:
# 1. Nama variabel tidak boleh diawali dengan angka.
#    Contoh:  123nama (salah)  →  nama123 (benar)
# 2. Nama variabel tidak boleh menggunakan tanda minus (-).
#    Contoh:  nama-saya (salah)  →  nama_saya (benar)
# 3. Nama variabel tidak boleh mengandung spasi.
#    Contoh:  nama lengkap (salah)  →  nama_lengkap (benar)
# 4. Nama variabel tidak boleh sama dengan keyword (kata khusus) milik Python,
#    misalnya: if, for, while, class, import, dan lain-lain.
# 5. Di python itu case sensitive, jadi variabel bernama "nama" tidak sama dengan variabel "Nama"
