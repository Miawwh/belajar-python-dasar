# ini beberapa latihan dengan operasi logika dengan tambahan beberapa materi yang sudah dipelajari

# ====================================
# 1. Mengecek jika umur sudah >= 17 dan mempunyai SIM
# ====================================
umur_user = int(input("Masukkan umur anda : "))
punya_sim = input("apakah punya sim? (ya/tidak) : ")

# syarat:
# - umur >= 17
# - punya SIM
kesimpulan = umur_user >= 17 and punya_sim == "ya"
print("Boleh mengemudi? :", kesimpulan)
print("\n")


# ====================================
# 2. Bilangan antara 1 dan 10 -> True, selain itu -> False
# ====================================
bilangan = int(input("Masukkan bilangan antara 1 - 10 : "))

# syarat: bilangan > 0 DAN bilangan <= 10
kesimpulan = bilangan > 0 and bilangan <= 10
print("Bilangan dalam rentang 1-10? :", kesimpulan)
print("\n")


# ====================================
# 3. Daerah +++++3-----10++++
# ====================================
# Maksudnya: bilangan <= 3 atau bilangan >= 10
bilangan = int(input("Masukkan suatu bilangan : ")) 
kesimpulan = bilangan <= 3 or bilangan >= 10 
print("Bilangan di luar (3,10)? :", kesimpulan)
print("\n")


# ====================================
# 4. Daerah ----3++++10----
# ====================================
# Maksudnya: bilangan di antara 3 dan 10 (inklusif)
bilangan = int(input("Masukkan bilangan anda : "))
kesimpulan = bilangan >= 3 and bilangan <= 10
print("Bilangan di antara 3 sampai 10? :", kesimpulan)
print("\n")


# ====================================
# 5. Daerah ----0+++++5----8+++++11----
# ====================================
# Maksudnya:
# (0,5] atau [8,11]
bilangan = int(input("Masukkan angka : "))
kesimpulan = (bilangan > 0 and bilangan <= 5) or (bilangan >= 8 and bilangan <= 11)
print("Bilangan dalam daerah (0,5] atau [8,11]? :", kesimpulan)
print("\n")


# ====================================
# 6. Daerah ++++0-----5+++++8----11+++++
# ====================================
# Maksudnya:
# bilangan <= 0, atau di antara [5,8], atau >= 11
bilangan = int(input("Masukkan bilangan : "))
kesimpulan = (bilangan <= 0) or (bilangan >= 5 and bilangan <= 8) or (bilangan >= 11)
print("Bilangan di luar (0,5) dan (8,11)? :", kesimpulan)
print("\n")
