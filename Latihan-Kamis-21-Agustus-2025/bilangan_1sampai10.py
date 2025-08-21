nilai_inputan = int(input("Masukan Nilai = "))

if nilai_inputan < 1 or nilai_inputan > 10:
    print(f'Bilangan yang kamu masukan {nilai_inputan} bukan merupakan bagian dari bilangan 1-10')
else:
    print(f"Bilangan yang kamu masukan adalah {nilai_inputan} dan itu merupakan bilangan 1-10")