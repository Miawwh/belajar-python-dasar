# Program Konversi Suhu dari Celcius ke Fahrenheit, Kelvin, dan Reamur

print("\nProgram Konversi Suhu\n")

# Input suhu dari user dalam Celcius
celcius = float(input("Masukkan Suhu ∘C : "))

# Rumus konversi suhu
# Celcius ke Fahrenheit (∘F)
celcius_ke_fahrenheit = (9/5 * celcius) + 32

# Celcius ke Kelvin (∘K)
celcius_ke_kelvin = celcius + 273.15

# Celcius ke Reamur (∘R)
celcius_ke_reamur = 4/5 * celcius

# Menampilkan hasil konversi dalam bentuk tabel
print(f"""
===========================================
| Suhu Celcius : {celcius} ∘C dikonversi ke
===========================================
|  Fahrenheit | {celcius_ke_fahrenheit:.2f} ∘F
|  Kelvin     | {celcius_ke_kelvin:.2f} ∘K
|  Reamur     | {celcius_ke_reamur:.2f} ∘R
===========================================
""")
