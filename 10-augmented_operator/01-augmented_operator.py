# ====================================
# Belajar Python - Augmented Operator
# Materi: Operator gabungan assignment
# ====================================

# 🔹 Apa itu augmented operator?
# Augmented operator adalah cara singkat untuk menuliskan operasi aritmatika
# atau bitwise yang digabungkan dengan assignment (=).
# Misalnya:
#   x = x + 5  ➝ bisa ditulis lebih singkat sebagai x += 5
#   y = y & 3  ➝ bisa ditulis lebih singkat sebagai y &= 3
#
# Jadi operator ini membuat kode lebih ringkas dan mudah dibaca.

# ====================================
# Contoh Augmented Operator Aritmatika
# ====================================

x = 10
print(f"Nilai awal x = {x}")

# Penjumlahan dan assignment
x += 5   # sama dengan x = x(10) + 5
print(f"x += 5 ➝ {x}")

# Pengurangan dan assignment
x -= 3   # sama dengan x = x(15) - 3
print(f"x -= 3 ➝ {x}")

# Perkalian dan assignment
x *= 2   # sama dengan x = x(12) * 2
print(f"x *= 2 ➝ {x}")

# Pembagian dan assignment
x /= 4   # sama dengan x = x(24) / 4
print(f"x /= 4 ➝ {x}")

# Modulus dan assignment
x %= 4   # sama dengan x = x(6.0)% 4
print(f"x %= 4 ➝ {x}")

# Pangkat dan assignment
x **= 3  # sama dengan x = x(2.0) ** 3
print(f"x **= 3 ➝ {x}")

# Floor division dan assignment
x //= 2  # sama dengan x = x(8.0) // 2
print(f"x //= 2 ➝ {x}")
# x = 4.0

# ====================================
# Contoh Augmented Operator Bitwise
# ====================================
# Bitwise bekerja pada bentuk biner.
# Misalnya angka 5 = 0b0101, angka 3 = 0b0011

y = 5

print(f"\nNilai awal y = {y}, binary: {format(y, '08b')}")
                                          
# & (AND) assignment         128 64 32 16 8 4 2 1 
y &= 3   # sama dengan y = y(5) & 3
print(f"y &= 3 ➝ {y}, binary : {format(y, '08b')}")

# | (OR) assignment
y |= 2   # sama dengan y = y(1) | 2
print(f"y |= 2 ➝ {y}, binary : {format(y, '08b')}")

# ^ (XOR) assignment
y ^= 4   # sama dengan y = y(2) ^ 4
print(f"y ^= 4 ➝ {y}, binary : {format(y, '08b')}")

# << (Shift left assignment)
y <<= 1  # sama dengan y = y(7) << 1
print(f"y <<= 1 ➝ {y}, binary : {format(y, '08b')}")

# >> (Shift right assignment)
y >>= 2  # sama dengan y = y(14) >> 2
print(f"y >>= 2 ➝ {y}, binary : {format(y, '08b')}")
# y = 3


# ====================================
# 📌 Ringkasan Augmented Operator
# ====================================
# 🔹 Aritmatika:
#   +=   ➝ tambah lalu simpan
#   -=   ➝ kurang lalu simpan
#   *=   ➝ kali lalu simpan
#   /=   ➝ bagi lalu simpan
#   %=   ➝ sisa bagi lalu simpan
#   **=  ➝ pangkat lalu simpan
#   //=  ➝ floor division lalu simpan
#
# 🔹 Bitwise:
#   &=   ➝ AND lalu simpan
#   |=   ➝ OR lalu simpan
#   ^=   ➝ XOR lalu simpan
#   <<=  ➝ geser kiri lalu simpan
#   >>=  ➝ geser kanan lalu simpan
