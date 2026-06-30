narx = float(input("1_kg konfet narxi: "))

for i in range(12,21,2):
    kg = i/10
    print(f"{kg:.1f} kg konfet narxi {kg*narx:.2f} dollar")