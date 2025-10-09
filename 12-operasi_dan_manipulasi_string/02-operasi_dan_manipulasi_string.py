# =========================================
# Belajar Python - Operasi & Manipulasi String (Part 2)
# =========================================

# ================================
# Pengantar: cara memanggil method
# ================================
# Ada 3 gaya umum memanggil method string:
# 1) simpan string ke variabel lalu panggil method:
#    s = "halo"
#    hasil = s.upper()
#
# 2) langsung panggil method dari literal string:
#    hasil = "halo".upper()
#
# 3) langsung print hasil pemanggilan method:
#    print("halo".upper())
#
# Semuanya sah — pilih yang menurutmu paling jelas/rapi.

# ----------------------------------------
# 1) Mengubah huruf: uppercase, lowercase, capitalize
# ----------------------------------------
teks_awal = "halo semua"
hasil_upper = teks_awal.upper()
print("Normal      : " + teks_awal)
print("Uppercase   : " + hasil_upper)

# contoh direct-call (cara 2)
print("Direct upper: " + "selamat pagi".upper())

# capitalize -> huruf pertama jadi besar, sisanya lowercase
kalimat = "saya belajar python"
print("Capitalize  : " + kalimat.capitalize())

print("")  # spasi pemisah


# ----------------------------------------
# 2) Pengecekan kondisi (method yang mengembalikan boolean)
# ----------------------------------------

# islower() -> True kalau semua huruf alfabet dalam string adalah lowercase
s_true = "hello"
s_false = "Hello"
print("'" + s_true + "'.islower() -> " + str(s_true.islower()))   # True
print("'" + s_false + "'.islower() -> " + str(s_false.islower())) # False
print("")

# isupper()
u_true = "ABC"
u_false = "AbC"
print("'" + u_true + "'.isupper() -> " + str(u_true.isupper()))   # True
print("'" + u_false + "'.isupper() -> " + str(u_false.isupper())) # False
print("")

# isalpha() -> True jika hanya huruf (tidak ada spasi/angka/simbol)
alpha_true = "Python"
alpha_false = "Py3"
print("'" + alpha_true + "'.isalpha() -> " + str(alpha_true.isalpha()))
print("'" + alpha_false + "'.isalpha() -> " + str(alpha_false.isalpha()))
print("")

# isalnum() -> True jika hanya huruf+angka (tanpa spasi atau simbol)
alnum_true = "User123"
alnum_false = "User 123"
print("'" + alnum_true + "'.isalnum() -> " + str(alnum_true.isalnum()))
print("'" + alnum_false + "'.isalnum() -> " + str(alnum_false.isalnum()))
print("")

# isdecimal() -> True jika hanya digit desimal (0-9)
dec_true = "2025"
dec_false = "20.25"
print("'" + dec_true + "'.isdecimal() -> " + str(dec_true.isdecimal()))
print("'" + dec_false + "'.isdecimal() -> " + str(dec_false.isdecimal()))
print("")

# istitle() -> True jika setiap kata diawali huruf besar (Title Case)
title_true = "The Lion King"
title_false = "the lion king"
print("'" + title_true + "'.istitle() -> " + str(title_true.istitle()))
print("'" + title_false + "'.istitle() -> " + str(title_false.istitle()))
print("")

# isspace() -> True jika string hanya berisi whitespace (spasi/tab/newline)
space_true = "   "
space_false = " a "
print("'" + space_true + "'.isspace() -> " + str(space_true.isspace()))
print("'" + space_false + "'.isspace() -> " + str(space_false.isspace()))
print("")


# ----------------------------------------
# 3) startswith() dan endswith()
#    - Mengembalikan boolean
#    - startswith() bisa menerima tuple untuk cek beberapa prefix sekaligus
# ----------------------------------------
namafile = "laporan_2025.txt"
print("'" + namafile + "'.startswith('laporan_') -> " + str(namafile.startswith("laporan_")))
print("'" + namafile + "'.endswith('.txt') -> " + str(namafile.endswith(".txt")))

# contoh: cek beberapa prefix sekaligus (lebih dari 1 argument -> pakai tuple)
cek_prefix = namafile.startswith(("laporan_", "data_", "rekap_"))
print("'" + namafile + "'.startswith((" + "'laporan_', 'data_', 'rekap_')) -> " + str(cek_prefix))
print("")


# ----------------------------------------
# 4) Menghitung kemunculan & mencari posisi:
#    count(), find(), index()
#    - count(sub, start, end) -> dapat menerima 1 hingga 3 argumen
#      * sub = substring yang dicari (wajib)
#      * start (opsional) = posisi mulai pencarian
#      * end (opsional) = posisi akhir pencarian (seperti slicing)
#    - find(sub) -> mengembalikan index pertama, atau -1 jika tidak ditemukan
#    - index(sub) -> sama seperti find() tapi raise error jika tidak ditemukan
# ----------------------------------------
kalimat = "kucing makan ikan kucing"

# count() contoh:
print("count('kucing') -> " + str(kalimat.count("kucing")))        # berapa kali "kucing"
# count dengan batas range (start, end)
print("count('kucing', 0, 15) -> " + str(kalimat.count("kucing", 0, 15))) 

# find() vs index()
print("find('ikan') -> " + str(kalimat.find("ikan")))   # index pertama
print("find('ayam') -> " + str(kalimat.find("ayam")))   # -1 (tidak ada)
# index('makan') -> akan error jika tidak ada, jadi hati-hati
print("index('makan') -> " + str(kalimat.index("makan")))
print("")


# ----------------------------------------
# 5) split() dan join()
#    - split(sep=None, maxsplit=-1)
#      * jika sep=None (tidak disertakan), split memisah berdasarkan whitespace
#      * split() ALWAYS returns a list (tipe list)
#      * maxsplit -> batas berapa kali memecah (opsional)
#    - join(iterable) -> menggabungkan elemen iterable (biasanya list) menjadi string
# ----------------------------------------
kalimat_biasa = "halo dunia ini"
terpisah_default = kalimat_biasa.split()   # tanpa argumen -> split pada whitespace
print("kalimat_biasa.split() -> " + str(terpisah_default) + "  (tipe: " + str(type(terpisah_default)) + ")")

csv = "satu,dua,tiga"
terpisah_csv = csv.split(",")              # split berdasarkan koma
print("csv.split(',') -> " + str(terpisah_csv))

# split dengan maxsplit
text_example = "a b c d e"
print("text_example.split(None, 2) -> " + str(text_example.split(None, 2)))  # maksimal 2 pemisahan

# join: gabungkan list menjadi string
kata_list = ["saya", "suka", "apel"]
print("list -> " + str(kata_list))
print("','.join(list) -> " + ",".join(kata_list))
print("' '.join(list) -> " + " ".join(kata_list))
print("")

# Catatan: split() mengembalikan list (bukan string). Jika kamu mau kembali ke string,
# gunakan join() seperti contoh di atas.


# ----------------------------------------
# 6) replace()  (mengganti substring)
#    - replace(old, new[, count])
#      * old = substring lama (wajib)
#      * new = substring pengganti (wajib)
#      * count = jumlah penggantian maksimal (opsional)
# ----------------------------------------
teks = "apel apel apel"
print("original: " + teks)
print("replace -> " + teks.replace("apel", "pisang"))           # ganti semua
print("replace count=1 -> " + teks.replace("apel", "pisang", 1)) # ganti hanya 1 kemunculan
print("original tetap: " + teks)  # immutable -> original tidak berubah
print("")


# ----------------------------------------
# 7) Penataan / padding & strip
#    - rjust(width[, fillchar]) , ljust(width[, fillchar]), center(width[, fillchar])
#    - strip([chars]) , lstrip([chars]), rstrip([chars])
#    * fillchar default adalah spasi; chars default untuk strip() adalah whitespace
# ----------------------------------------
kata = "kanan"
print("'" + kata.rjust(10) + "'  # rjust: geser ke kanan, pad kiri dengan spasi")
print("'" + "kiri".ljust(10) + "'   # ljust: geser ke kiri, pad kanan dengan spasi")
print("'" + "tengah".center(20, "=") + "'  # center: pad di kiri & kanan dengan '='")

s_padding = "===halo==="
print("before strip -> '" + s_padding + "'")
print("after strip('=') -> '" + s_padding.strip("=") + "'")
print("after lstrip('=') -> '" + s_padding.lstrip("=") + "'")
print("after rstrip('=') -> '" + s_padding.rstrip("=") + "'")
print("")


# ----------------------------------------
# 8) Method penting lain (ringkasan)
# ----------------------------------------
# .upper(), .lower(), .capitalize(), .title()
# .strip(), .lstrip(), .rstrip()
# .split(), .join()
# .replace()
# .count(), .find(), .index()
# .startswith(), .endswith()
# .islower(), .isupper(), .isalpha(), .isalnum(), .isdecimal(), .istitle(), .isspace()
#
# Catatan akhir:
# - String bersifat immutable: method yang "mengubah" mengembalikan string baru.
# - Banyak method punya argumen opsional — baca dokumentasi kalau butuh detail.
# - Jika suatu method menerima lebih dari 1 argumen, biasanya urutannya:
#     contoh: replace(old, new, count)  -> old then new then count.
#     contoh: count(sub, start, end)    -> sub then start then end.
#     contoh: split(sep, maxsplit)     -> sep then maxsplit.

