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

# menampilkan data peserta
def tampil():
    list1 = []
    number = 1
    for i in availableAtlet:
        list1.append(i)
        for item in i:
            nama = i[0]
            usia = i[1]
        print("Peserta ke -",number)
        print("Nama:",nama)
        print("Usia:",usia,"tahun\n")
        number += 1

# user menambahkan data peserta baru
def tambah():
    listTambah = []
    nama = str(input("Nama : "))
    usia = int(input("Usia : "))
    listTambah.insert(0, nama)
    listTambah.insert(1, usia)
    availableAtlet.append(listTambah)
    print("Data peserta berhasil ditambahkan!")

# mengurutkan data menurut usia dari yang tertua ke yang termuda
def sortAge():  
    a = sorted(availableAtlet, key = lambda x: x[1])
    number = 1
    for x in reversed(a):
        nama = x[0]
        usia = x[1]
        print("Peserta ke -",number)
        print("Nama :",nama)
        print("Usia :",usia,"tahun\n")
        number += 1

# seleksi usia 20 tahun kebawah
def seleksi():
    lolosSeleksi = []
    number = 1
    for i in availableAtlet:
        if 0 < i[1] <= 20:
            lolosSeleksi.append(i)
    for x in lolosSeleksi:
        nama = x[0]
        usia = x[1]
        print("Peserta ke -",number)
        print("Nama :",nama)
        print("Usia :",usia,"tahun\n")
        number += 1

# mengurutkan data menurut alphabet
def sortAlphabet():
    urutHuruf = []
    number = 1
    for i in availableAtlet:
        urutHuruf.append(i)
        sorted1 = sorted(urutHuruf)
    for x in sorted1:
        nama = x[0]
        usia = x[1]
        print("Peserta ke -",number)
        print("Nama :",nama)
        print("Usia :",usia,"tahun\n")
        number += 1

# mencari data peserta dengan usia termuda dan tertua
def searchData():
    a = min(availableAtlet, key = lambda x: x[1])
    b = max(availableAtlet, key = lambda x: x[1])
    nama1 = a[0]
    usia1 = a[1]
    nama2 = b[0]
    usia2 = b[1]
    print("Atlit Termuda")
    print("Nama :",nama1)
    print("Usia :",usia1)
    print()
    print("Atlit Tertua")
    print("Nama: ",nama2)
    print("Usia: ",usia2)



# tampil()
# tambah()
# sortAge()
# searchData()
# seleksi()
# sortAlphabet()