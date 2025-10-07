# ====================================
# Belajar Python - Operasi Membership
# Materi: Operator keanggotaan (in, not in)
# ====================================

# 🔹 Apa itu operator membership?
# Operator membership digunakan untuk mengecek apakah suatu nilai 
# ada di dalam sebuah "iterable" atau tidak.
# Iterable adalah tipe data yang bisa diulang satu per satu elemennya.
# Contoh iterable: string, list, tuple, set, dictionary.

# Daftar operator membership:
# in      -> True jika nilai ada di dalam iterable
# not in  -> True jika nilai TIDAK ada di dalam iterable


# ====================================
# 1. Membership pada List
# ====================================
buah = ["apel", "jeruk", "mangga"]   # (List) -> belum dibahas detail di bab ini

print("Membership pada List:")
print(f"'apel' in buah   -> {'apel' in buah}")     # True
print(f"'durian' in buah -> {'durian' in buah}")   # False
print("\n")


# ====================================
# 2. Membership pada Tuple
# ====================================
angka = (1, 2, 3, 4, 5)   # (Tuple) -> akan dibahas lebih lanjut di bab lain

print("Membership pada Tuple:")
print(f"3 in angka   -> {3 in angka}")   # True
print(f"7 in angka   -> {7 in angka}")   # False
print("\n")


# ====================================
# 3. Membership pada Set
# ====================================
huruf = {"a", "i", "u", "e", "o"}   # (Set) -> nanti akan dijelaskan di bab lain

print("Membership pada Set:")
print(f"'a' in huruf -> {'a' in huruf}")   # True
print(f"'b' in huruf -> {'b' in huruf}")   # False
print("\n")


# ====================================
# 4. Membership pada Dictionary
# ====================================
mahasiswa = {
    "nama": "Andi",
    "umur": 20
}   # (Dictionary) -> detail akan dibahas di bab lain

print("Membership pada Dictionary:")
print(f"'nama' in mahasiswa -> {'nama' in mahasiswa}")   # True (cek KEY, bukan value)
print(f"'Andi' in mahasiswa -> {'Andi' in mahasiswa}")   # False (karena 'Andi' adalah value, bukan key)
print("\n")
# 🔎 Catatan:
# Membership pada dictionary hanya mengecek KEY, bukan value.


# ====================================
# 5. Membership pada String
# ====================================
kalimat = "belajar python itu mudah"

print("Membership pada String:")
print(f"'python' in kalimat    -> {'python' in kalimat}")    # True
print(f"'java' in kalimat      -> {'java' in kalimat}")      # False
print(f"'mudah' not in kalimat -> {'mudah' not in kalimat}") # False
print("\n")
# 🔎 Catatan:
# Pada string, membership akan mengecek apakah substring (potongan kata/karakter) ada di dalam string.
