# Program konversi jam ke menit dan detik

# Menerima input jumlah jam dari user
jam_user = int(input("Masukkan jam = "))

# Konversi jam ke menit
# 1 jam = 60 menit
jam_ke_menit = jam_user * 60

# Konversi jam ke detik
# 1 jam = 3600 detik
jam_ke_detik = jam_user * 3600

# Menampilkan hasil konversi
print(f"Hasil konversi dari {jam_user} jam ke menit dan detik :")
print(f"{jam_ke_menit} menit")
print(f"{jam_ke_detik} detik")
