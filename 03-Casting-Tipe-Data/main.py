# Casting Data
# Merubah dari satu tipe ke tipe lain
# tipe data : integer(int), float, string(str) dan boolean(bool)

print("Casting tipe data dari int ke float")
data_int = 9
print(f"Data = {data_int} | type = {type(data_int)}")

# Kita casting(ubah) tipe datanya menjadi float
data_float = float(data_int)
print(f"Data = {data_float} | type = {type(data_float)}")

print("\n")
print("Casting tipe data dari float ke int")
# Float ke integer(int) akan menghilanglan angka dibelakang bilangan koma
float_ = 17.9
print(f"Data = {float_} | type = {type(float_)}")

flot_int = int(float_)
print(f"Data = {flot_int} | type = {type(flot_int)}")

print("\n")
print("Casting tipe data dari boolean ke int/float/str")
# bool ke int/float/str
print(f"Data = {True} ke int = {int(True)} | {type(int(True))}")
print(f"Data = {False} ke int = {int(False)} | {type(int(False))}")
print(f"Data = {True} ke float = {float(True)} | {type(float(True))}")
print(f"Data = {False} ke float = {float(False)} | {type(float(False))}")
print(f"Data = {True} ke string = {str(True)} | {type(str(True))}")
print(f"Data = {False} ke string = {str(False)} | {type(str(False))}")

print("\n")
print("Casting tipe data dari int/float ke boolean")
print(f"Data = {1} ke boolean = {bool(1)} | {type(bool(1))}")
print(f"Data = {1.0} ke boolean = {bool(1.0)} | {type(bool(1.0))}")
print(f"Data = {0} ke boolean = {bool(0)} | {type(bool(0))}")
print(f"Data = {0.0} ke boolean = {bool(0.0)} | {type(bool(0.0))}")
print(f"Data = {-5} ke boolean = {bool(-5)} | {type(bool(-5))}")

# Jika ingin casting tipe nilai string ke int/float harus dalam bentuk angka
