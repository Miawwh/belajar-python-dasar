a = float(input("Masukan nilai untuk sisi 1 = "))
b = float(input("Masukan nilai untuk sisi 2 = "))
c = float(input("Masukan nilai untuk sisi 3 = "))

if a == b == c:
    jenis_sgitiga = "Segitiga sama sisi"
elif a == b or b == c or a == c:
    jenis_sgitiga = "segitiga sama kaki"
else:
    jenis_sgitiga = "Segitiga sembarangan"

print(f"jenis segitiga {jenis_sgitiga}")
 
