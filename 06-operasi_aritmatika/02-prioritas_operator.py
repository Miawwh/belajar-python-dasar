# ====================================
# Belajar Python - Prioritas Operator
# Materi: Urutan pengerjaan operasi
# ====================================

# 🔹 Python mengikuti aturan *precedence* (urutan prioritas operasi)
# Urutannya (dari yang paling tinggi ke rendah):
# 1. **            (pangkat)
# 2. *, /, //, %   (perkalian, pembagian, pembagian bulat, modulus)
# 3. +, -          (penjumlahan, pengurangan)
#
# Jika ada operasi dengan tingkat yang sama, maka dikerjakan dari kiri ke kanan.
# Kita juga bisa menggunakan tanda kurung () untuk mengatur prioritas.

print(f"Hasil dari 2 + 3 * 4 = {2+3*4}")    
# hasil = 14, karena * dikerjakan lebih dulu (3*4=12, lalu 2+12)

print(f"Hasil dari (2 + 3) * 4 = {(2 + 3) * 4}")  
# hasil = 20, karena () dikerjakan lebih dulu (2+3=5, lalu 5*4)

print(f"Hasil dari 2 ** 3 * 4 = {2 ** 3 * 4}")    
# hasil = 32, karena ** lebih tinggi dari * (2**3=8, lalu 8*4)

print(f"Hasil dari 2 ** (3 * 4) = {2 ** (3 * 4)}") 
# hasil = 4096, karena () dikerjakan dulu (3*4=12, lalu 2**12)


# 🔹 Kurung lebih dari satu
# Jika ada banyak tanda kurung, Python mengerjakannya dari "dalam" dulu baru keluar (inside-out).
print("\nContoh dengan kurung lebih dari satu:")
print(f"(5 + 3) * (12 * 4) % 2 = {(5 + 3) * (12 * 4) % 2 }")
# (5+3)=8, (12*4)=48 → 8*48=384 → 384%2=0

print(f"(6 ** 4) * (10 % 4) = {(6 ** 4) * (10 % 4)}")
# 6**4=1296, 10%4=2 → 1296*2=2592

print(f"(6 + 3 / 20) ** (12 // 30) * (12 % 2 + 3) = {(6 + 3 / 20) ** (12 // 30) * (12 % 2 + 3)}")
# 3/20=0.15 → 6+0.15=6.15
# 12//30=0
# 12%2=0 → 0+3=3
# jadi 6.15**0 * 3 = 1 * 3 = 3.0
