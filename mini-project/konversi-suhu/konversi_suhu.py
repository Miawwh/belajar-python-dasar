# Latihan Konversi Satuan Temperature

# Program Konversi Celcius Ke Satuan Lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

input_celcius = float(input("Masukan Suhu Dalam Celcius : "))
print(f"Suhu Adalah {input_celcius} °C")

# Celcius Ke Reamur
reamur = (4/5) * input_celcius
print(f"Suhu Dalam Reamur Adalah : {reamur} °R")

# Celcius Ke Fahrenheit
fahrenheit = ((9/5) * input_celcius) + 32
print(f"Suhu Dalam Fahrenheit Adalah : {fahrenheit} °F")

# Celcius Ke Kelvin 
kelvin = input_celcius + 273
print(f"Suhu Dalam Kelvin Adalah : {kelvin} K")
