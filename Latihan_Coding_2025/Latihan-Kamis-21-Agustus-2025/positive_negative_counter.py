Total_Positif = 0
Total_Negatif = 0

for i in range(5):
    bilangan = int(input(f"Masukan bilangan ke-{i+1} = "))
    if bilangan > 0 :
        Total_Positif += bilangan
    elif bilangan < 0:
        Total_Negatif += 1

print(f"Nilai Total Positif adalah = {Total_Positif}")
print(f"Jumlah Negatif Yang Ada di Bilangan {Total_Negatif} ")
