banyaknya_bilangan = int(input("Halo! Mari kita hitung nilai rata-rata. Berapa banyak bilangan yang ingin kamu masukkan? = "))

total_bilangan = 0

for i in range(banyaknya_bilangan):
    jumlah_per_bilangan = float(input(f"Masukan bilangan ke-{i+1} = "))
    
    total_bilangan += jumlah_per_bilangan

    nilai_rata_rata = total_bilangan / banyaknya_bilangan

print(f"Total dari semua nilai yang kamu berikan per-bilangan adalah = {total_bilangan}")
print(f"Nilai rata-ratanya adalah = {nilai_rata_rata} ")


