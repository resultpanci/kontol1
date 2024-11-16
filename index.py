x = int(input("Masukan sebuah bilangan : "))
if x < 200:
    print (x, " : Nilai kurang dari 200")
    if x == 150:
        keterangan = " : Sama dengan 150"
        print (x, keterangan)
    elif x == 100:
        keterangan = " : Sama dengan 100"
        print (x, keterangan)
    elif x == 50:
        keterangan = " : Sama dengan 50"
        print (x, keterangan)
    elif x < 50:
        keterangan = " : Kurang dari 50"
        print (x, keterangan)
else:
    keterangan = "Nilai yang dimasukkan salah"
    print (keterangan)

print ("Selesai")