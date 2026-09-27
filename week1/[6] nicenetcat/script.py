desimal = "97 99 97 100 101 109 121 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 102 54 55 51 57 125 10"
hasil = "".join(chr(int(angka)) for angka in desimal.split())
print(hasil)
