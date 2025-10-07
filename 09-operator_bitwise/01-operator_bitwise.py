# ====================================
# Belajar Python - Operator Bitwise
# Materi: Operasi pada level bit
# ====================================

# 🔹 Apa itu operator bitwise?
# Operator bitwise bekerja pada representasi biner dari bilangan.
# Misalnya:
#   6 = 0b110
#   3 = 0b011
# Saat dilakukan operasi bitwise, Python akan menghitung tiap bit.
# Kalau angkanya desimal (int), maka Python akan konversi dulu ke biner.

a = 10
b = 16

# Bitwise OR ( | )
# Hasil bit = 1 jika minimal ada salah satu bit bernilai 1.
# Contoh: 1010 | 10000 = 11010 (desimal 26)
c = a | b
print(f"{a}, binary       : {format(a,'08b')}")
print(f"{b}, binary       : {format(b,'08b')}")
print(27 * "-","( | ) Bisa disebut OR")
print(f"Nilai {c}, binary : {format(c,'08b')}")
print("")

# Bitwise AND ( & )
# Hasil bit = 1 hanya jika kedua bit bernilai 1.
# Contoh: 1010 & 10000 = 00000 (desimal 0)
c = a & b
print(f"{a}, binary       : {format(a,'08b')}")
print(f"{b}, binary       : {format(b,'08b')}")
print(27 * "-","( & ) Bisa disebut AND")
print(f"Nilai {c}, binary  : {format(c,'08b')}")
print("")

# Bitwise XOR ( ^ )
# Hasil bit = 1 jika salah satu bit berbeda.
# Contoh: 1010 ^ 10000 = 11010 (desimal 26)
# Jika sama : 1111 ^ 1111 = 0 (desimal 0)
c = a ^ b
print(f"{a}, binary       : {format(a,'08b')}")
print(f"{b}, binary       : {format(b,'08b')}")
print(27 * "-","( ^ ) Bisa disebut XOR")
print(f"Nilai {c}, binary : {format(c,'08b')}")
print("")

# Bitwise NOT ( ~ )
# Membalik semua bit (0 jadi 1, 1 jadi 0), tapi hasilnya bukan hanya dibalik.
# Karena Python pakai representasi komplemen dua (two's complement),
# maka hasilnya = -(a+1). Misal: ~10 = -11.
# Jadi NOT di Python menghasilkan bilangan negatif.
c = ~a
print(f"{a}, binary       : {format(a,'08b')}")
print(27 * "-","( ~ ) Bisa disebut NOT")
print(f"Nilai {c}, binary: {format(c,'08b')}")
print("")
# Jika ingin benar-benar flip bit (misalnya 8-bit), gunakan XOR dengan masker 0b11111111.

# Bitwise Shift Right ( >> )
# Menggeser bit ke kanan, setiap geseran = dibagi 2 (dibulatkan ke bawah).
# Contoh: 00001010 (10) >> 1 = 00000101 (5)
# Ini sama saja dengan a // (2^n).
# a >> 2 = 10 // 4 = 2
c = a >> 1
print(f"{a}, binary       : {format(a,'08b')}")
print(27 * "-","( >> ) Bisa disebut Shift Right")
print(f"Nilai {c}, binary  : {format(c,'08b')}")
print("")

# Bitwise Shift Left ( << )
# Menggeser bit ke kiri, setiap geseran = dikali 2.
# Contoh: 00001010 (10) << 1 = 00010100 (20)
# Ini sama saja dengan a * (2^n).
# a << 2 = 10 * 2^2 = 40
c = a << 1
print(f"{a}, binary       : {format(a,'08b')}")
print(27 * "-","( << ) Bisa disebut Shift left")
print(f"Nilai {c}, binary  : {format(c,'08b')}")

