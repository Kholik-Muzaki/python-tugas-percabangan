# BIAYA PENGOBATAN
    # OPERASI MATA
katarak = "Rp. 7.500.000"
plus_minus = "Rp. 5.000.000"
silinder = "Rp. 4.000.000"

    # OPERASI JANTUNG
jantung_koroner = "Rp. 500.000.000"
katup_jantung = "Rp. 350.000.000"
otot_jantung = "Rp. 450.000.000"

print("<--- MENU HITUNG BIAYA OPERASI ---> ")
print("1. Hitung Biaya Operasi Mata")
print("2. Hitung biaya Operasi Jantung")

masukan_pilihan_penyakit = int(input("Masukkan pilihan: "))
if masukan_pilihan_penyakit == 1:
    print("JENIS PENYAKIT MATA : ")
    print("1. Katarak")
    print("2. Plus/Minus")
    print("3. Silinder")
    
    masukkan_jenis_penyakit_mata = int(input("Masukkan Jenis Penyakit Mata : "))
    if masukkan_jenis_penyakit_mata == 1:
        print(f"Biaya Operasi mata Katarak = {katarak}")
    elif masukkan_jenis_penyakit_mata == 2:
        print(f"Biaya operasi mata Plus/Minus = {plus_minus}")
    elif masukkan_jenis_penyakit_mata == 3:
        print(f"Biaya operasi mata Silinder = {silinder}")
    else:
        print("Pilihan tidak tersedia")

elif masukan_pilihan_penyakit == 2:
    print("JENIS PENYAKIT JANTUNG :")
    print("1. Jantung Koroner")
    print("2. Katup Jantung")
    print("3. Otot Jantung")

    masukkkan_jenis_penyakit_jantung =int(input("Masukkan Jenis Penyakit Jantung : "))
    if masukkkan_jenis_penyakit_jantung == 1:
        print(f"Biaya operasi jantung koroner = {jantung_koroner}")
    elif masukkkan_jenis_penyakit_jantung == 2:
        print(f"Biaya operasi katup jantung = {katup_jantung}")
    elif masukkkan_jenis_penyakit_jantung == 3:
        print(f"Biaya operasi otot jantung = {otot_jantung}")
    else:
        print("pilihan tidak tersedia")
else:
    print("Mohon Maaf, pilihan tidak tersedia")