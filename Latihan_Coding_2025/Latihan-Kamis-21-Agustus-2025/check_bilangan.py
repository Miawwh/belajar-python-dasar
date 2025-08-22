print("\n =====Ini adalah pengecekan, apakah bilangan yang kamu masukan sebuah bilangan genap atau ganjil===== \n")

input_nilai = int(input("Masukan nilai = "))
if input_nilai % 2 == 0:
    print(f"Nilai yang kamu masukan adalah {input_nilai} dan itu termasuk bilangan genap!")
else:
    print(f"Nilai yang kamu masukan adalah {input_nilai} dan itu termasuk bilanbgan ganjil")