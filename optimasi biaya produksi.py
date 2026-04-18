import math

# Fungsi
def f(x):
    fungsi = x**3 - 6*x**2 + 9*x + 15
    return fungsi

# Turunan pertama
def f1(x):
    turunan_pertama = 3*x**2 - 12*x + 9
    return turunan_pertama

# Turunan kedua
def f2(x):
    turunan_kedua = 6*x - 12
    return turunan_kedua

# INTERVAL
a = 0
b = 5

# TITIK STASIONER
A = 3
B = -12
C = 9

D = B**2 - 4*A*C

x1 = (-B + math.sqrt(D)) / (2*A)
x2 = (-B - math.sqrt(D)) / (2*A)

print("===TITIK KRITIS===")
print("Titik Stasioner")
print(f"x = {x1}")
print(f"x = {x2}")
print("   ")

# TITIK SINGULAR
print("Titik Singular")
print("Tidak ada (fungsi polinom)")
print("   ")

# TITIK UJUNG
titik_ujung = [a, b]
print("Titik Ujung")
print(f"x = {a}")
print(f"x = {b}")
print("   ")

titik_kritis = [x1, x2]
# MINIMUM & MAKSIMUM LOKAL + NILAI
print("=== MINIMUM & MAKSIMUM LOKAL ===")
for x in titik_kritis:
    if f2(x) > 0:
        print(f"Minimum Lokal : x = {x}")
        print(f"Biaya : {f(x)}")
        print("   ")
    elif f2(x) < 0:
        print(f"Maksimum Lokal : x = {x}")
        print(f"Biaya : {f(x)}")
    else:
        print(f"Titik Belok: x = {x} ")
print("   ")
