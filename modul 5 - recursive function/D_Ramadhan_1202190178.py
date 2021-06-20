# Muhammad Ramadhan Kurniawan (1202190178)
def perpangkatan(angka, pangkatnya):
    if pangkatnya == 0:
        return 1
    else:
        return angka * perpangkatan(angka,pangkatnya - 1)

print("Silahkan masukkan angka beserta pangkatnya\n===========================================")
a = int(input("Masukkan angkanya : "))
p = int(input("Masukkan pangkatnya : "))

print("-------------------------------------------")
print("Hasil dari {} dipangkatkan {} adalah {}".format(a,p,perpangkatan(a,p)))
print("-------------------------------------------")