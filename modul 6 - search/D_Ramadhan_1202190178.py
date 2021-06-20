# | MUHAMMAD RAMADHAN KURNIAWAN | 1202190178 | SI4303 | TUGAS PRAKTIKUM  WEEK 8 | STRUKTUR DATA DAN ALGORITMA | TELKOM UNIVERSITY |

import time

# data default dari soal yang diberikan
availableAtlet = [
    ["Fadhil", 20],
    ["Fauzi", 17],
    ["Marcell", 21],
    ["Harris", 21],
    ["Fakhri", 18],
    ["Ikhbal", 18],
    ["Abrar", 21],
    ["Budi", 25],
    ["Sanul", 29],
    ["Aldi", 19],
    ["Akhbar", 22],
    ["Farid", 23],
    ["Ghiffary", 23],
    ["Levi", 22],
    ["Jhony", 21],
    ["Fachry", 18],
    ["Raja", 20],
    ["Farraz", 19],
    ["Ghalib", 20],
    ["Alldo", 21],
    ["Wira", 20],
    ["Lucky", 20],
    ["Fadlan", 19],
    ["Ilham", 22],
    ["Crafael", 22],
    ["Genta", 22]]

# variabel list baru sebagai tempat menyimpan data nama dan usia yang lolos seleksi, list ini juga akan digunakan untuk method mengurutkan data sesuai alphabet A-Z
lolosSeleksi = [] 

# merupakan fungsi atau method untuk menampilkan data peserta calon atlit pekan olahraga
def tampil():
    global availableAtlet
    number = 1
    print("\nData Atlit yang tersedia: \n")
    for i in availableAtlet: # untuk list yang ada di dalam list availableAtlet
        for item in i: # untuk setiap item dalam list tersebut
            nama = i[0] # indeks 0 menjadi variabel namanya
            usia = i[1] # indeks 1 menjadi variabel usianya
        print("\nPeserta ke -",number)
        print("-"*20)
        print("Nama:",nama)
        print("Usia:",usia,"tahun")
        number += 1
        print("-"*20)

# merupakan fungsi atau method untuk menambah data peserta oleh pegawai dispora
def tambah():
    global availableAtlet
    listTambah = [] # list baru sebagai tempat menyimpan data nama dan usia
    print("\nLengkapi data dibawah dengan benar!\n")
    nama = str(input("Nama : "))
    usia = int(input("Usia : "))
    listTambah.insert(0, nama) # menambah inputan nama kedalam indeks 0 variabel list listTambah
    listTambah.insert(1, usia) # menambah inputan usia kedalam indeks 1 variabel list listTambah
    availableAtlet.append(listTambah) # list baru tadi ditambahkan kedalam list utama, dimana data baru berhasil ditambahkan
    print("\nData peserta berhasil ditambahkan!")

# merupakan fungsi atau method untuk mengurutkan data peserta dari usia yang paling tua hingga usia yang paling muda
def sortAge():  
    a = sorted(availableAtlet, key = lambda x: x[1]) # fungsi lambda untuk menandakan indeks 0 yang di urutkan dengan built in sorted
    number = 1 
    for x in reversed(a): # variabel a tadi diterapkan built in reversed untuk membalikan urutan data agar dari yang tertua dan untuk setiap item didalamnya
        nama = x[0] # indeks 0 menjadi variabel namanya
        usia = x[1] # indeks 1 menjadi variabel usianya
        print("\nPeserta ke -",number)
        print("-"*20)
        print("Nama :",nama)
        print("Usia :",usia,"tahun")
        print("-"*20)
        number += 1

# merupakan fungsi atau method untuk mencari data peserta yang memiliki usia termuda dan usia tertua
def searchData():
    a = min(availableAtlet, key = lambda x: x[1]) # menggunakan lambda untuk menandakan indeks 1 yang dilakukan proses mencari data terkecil dengan built in MIN
    b = max(availableAtlet, key = lambda x: x[1]) # menggunakan lambda untuk menandakan indeks 1 yang dilakukan proses mencari data terbesar dengan built in MAX
    nama1 = a[0] # indeks 0 menjadi variabel nama untuk peserta termuda
    usia1 = a[1] # indeks 1 menjadi variabel usia untuk peserta termuda
    nama2 = b[0] # indeks 0 menjadi variabel nama untuk peserta tertua
    usia2 = b[1] # indeks 1 menjadi variabel nama untuk peserta tertua
    print("\nAtlit Termuda")
    print("-"*20)
    print("Nama :",nama1)
    print("Usia :",usia1,"tahun")
    print("-"*20,"\n")
    print("="*20)
    print("\nAtlit Tertua")
    print("-"*20)
    print("Nama :",nama2)
    print("Usia :",usia2,"tahun")
    print("-"*20)

# ======================================================================================================================================
# pembatas karena akan terjadi perubahan data dari variabel availableAtlet ke data dari variabel lolosSeleksi
# ======================================================================================================================================

# merupakan fungsi atau method untuk menyeleksi calon peserta sesuai syarat yaitu usia 20 tahun atau kurang
def seleksi():
    count = 0
    global lolosSeleksi
    number = 1
    for i in availableAtlet: # untuk list yang ada di dalam list availableAtlet
        if 0 < i[1] <= 20: # Jika item pada indeks ke 1 yaitu usia <= 20 akan ditambahkan kedalam list baru peserta yang lolos
            lolosSeleksi.append(i)
    for x in lolosSeleksi:
        nama = x[0]
        usia = x[1]
        print("\nPeserta ke -",number)
        print("-"*20)
        print("Nama :",nama)
        print("Usia :",usia,"tahun")
        print("-"*20)
        count += 1
        number += 1
    print("\nNOTES: Jumlah peserta yang lolos seleksi untuk mengikuti pekan olahraga kota cabang basket KU20 adalah sebanyak {} orang.\n".format(count))

# merupakan fungsi atau method untuk mengurutkan sesuai alphabet dari A-Z nama peserta yang sudah lolos seleksi
# method ini menggunakan data baru di dalam variabel lolosSeleksi
def sortAlphabet():
    try: # menggunakan try dan except karena untuk mengakses method ini harus menyeleksi peserta terlebih dahulu
        urutHuruf = [] # list baru sebagai tempat menyimpan data nama dan usia yang diurutkan menurut alphabet A-Z
        number = 1
        for i in lolosSeleksi: # untuk setiap item yang ada dalam list peserta yang lolos seleksi
            urutHuruf.append(i) # data peserta ditambahkan kedalam list baru
            sorted1 = sorted(urutHuruf) # data yang sudah ada akan diurutkan menurut alphabet menggunakan built in sorted
        for x in sorted1: # untuk setiap item pada data yang ada di dalam variabel sorted1
            nama = x[0] # indeks 0 menjadi variabel namanya
            usia = x[1] # indeks 1 menjadi variabel usianya
            print("\nPeserta ke -",number)
            print("-"*20)
            print("Nama :",nama)
            print("Usia :",usia,"tahun")
            print("-"*20)
            number += 1
    except: # Apabila method seleksi peserta belum dilaksanakan, maka akan ditangani error nya
        time.sleep(2)
        print("WARNING! ERROR DITEMUKAN!")
        print(".....")
        time.sleep(1)
        print("Anda tidak dapat mengurutkan data menurut alphabet sebelum menyeleksi peserta!")

def showMenu():
    print("""
-------------------------------------------------------------------------------------
|         Program Seleksi Peserta Pekan Olahraga Kota Cabang Basket KU20            |
~                             DISPORA BANDUNG 2020                                  ~
|-----------------------------------------------------------------------------------|      
+   [1] Lihat data peserta tersedia                                                 +
|   [2] Tambah peserta baru                                                         |
+   [3] Urut data peserta dari usia tertua                                          +
|   [4] Lihat data peserta dengan usia termuda dan tertua                           |
+   [5] Lakukan seleksi peserta (<= 20 tahun)                                       +
|   [6] Urut data menurut alphabet (A-Z)*                                           |
|   [7] Keluar                                                                      |
=====================================================================================
[* Menu 6 hanya dapat dilakukan setelah melakukan penyeleksian peserta (Menu 5)     ]
=====================================================================================
""")
    pilih = input("Pilih menu : ")
    if pilih == "1":
        print("-"*60)
        tampil()
        balik = str(input("\nLihat data lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                tampil()
                balik = str(input("\nLihat data lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
            else:
                print("\nMenu tidak tersedia!")
                print("-"*60)
                balik = str(input("\nLihat data lagi? [y/n] > "))

    elif pilih == "2":
        print("-"*60)
        tambah()
        print("-"*60)
        balik = str(input("\nTambah data lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                tambah()
                print("-"*60)
                balik = str(input("\nTambah data lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
            else:
                print("\nMenu tidak tersedia!")
                balik = str(input("\nTambah data lagi? [y/n] > "))

    elif pilih == "3":
        print("-"*60)
        sortAge()
        balik = str(input("\nLihat urutan data dari tertua lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                sortAge()
                balik = str(input("\nLihat urutan data dari tertua lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
            else:
                print("\nMenu tidak tersedia!")
                print("-"*60)
                balik = str(input("\nLihat urutan data dari tertua lagi? [y/n] > "))

    elif pilih == "4":
        print("-"*60)
        searchData()
        balik = str(input("\nLihat data peserta dengan usia termuda dan tertua lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                searchData()
                balik = str(input("\nLihat data peserta dengan usia termuda dan tertua lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
            else:
                print("\nMenu tidak tersedia!")
                balik = str(input("\nLihat data peserta dengan usia termuda dan tertua lagi? [y/n] > "))

    elif pilih == "5":
        print("-"*60)
        print("Berikut ini merupakan peserta yang LOLOS SELEKSI:")
        seleksi()
        print("-"*120)
        balik = str(input("\nKembali ke menu? [y] > "))
        while True:
            if balik == "y":
                showMenu()
                balik = str(input("\nKembali ke menu? [y] > "))
            elif balik == "n":
                print("Anda sudah melakukan seleksi!")
                balik = str(input("\nKembali ke menu? [y] > "))
            else:
                print("\nMenu tidak tersedia!")
                print("-"*60)
                balik = str(input("\nKembali ke menu? [y] > "))
    
    elif pilih == "6":
        print("-"*60)
        sortAlphabet()
        balik = str(input("\nLihat urutan data menurut alphabet lagi? [y/n] > "))
        while True:
            if balik == "y":
                print("-"*60)
                sortAlphabet()
                balik = str(input("\nLihat urutan data menurut alphabet lagi? [y/n] > "))
            elif balik == "n":
                print("-"*60)
                showMenu()
            else:
                print("\nMenu tidak tersedia!")
                print("-"*60)
                balik = str(input("\nLihat urutan data menurut alphabet lagi? [y/n] > "))
        
    elif pilih == "7":
        yakin = input("Anda yakin ingin keluar? [y/n] > ")
        if yakin == "y":
            print(""" 
                    TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI
             --------------------------------------------------------
            | Coder     : Muhammad Ramadhan Kurniawan                |
            | Adress    : Kabupaten Bekasi                           |
            | Phone     : 0812821650022                              |
            | Email     : ramadhanman24@gmail.com                    |
            |--------------------------------------------------------|
            |                  all rights reserved                   |
             --------------------------------------------------------
            """)
            exit()
        elif yakin == "n":
            showMenu()

    else:
        print("""
 -----------------------
| Menu tidak tersedia ! |
 -----------------------
        """)
        showMenu()

showMenu()




# Terima Kasih