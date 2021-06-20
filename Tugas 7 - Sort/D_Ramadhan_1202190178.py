# | Muhammad Ramadhan Kurniawan | 1202190178 | SI4303 |

# Algoritma Bubble Sort
# -----------------------------------------------------------------------------------------------------------------
# 1 Mulai dari index ke 0 (pertama) lalu melakukan perbandingan nilai dengan elemen selanjutnya pada array        |
# 2 Jika elemen pertama lebih besar dari elemen selanjutnya, posisinya akan ditukar                               |
# 3 Jika elemen pertama lebih kecil dari elemen selanjutnya, lanjut pemeriksaan ke elemen selanjutnya pada array  |
# -----------------------------------------------------------------------------------------------------------------
array = [] # array yang masih kosong, akan menjadi tempat user menampung hasil test IQ                            |
# -----------------------------------------------------------------------------------------------------------------
def babelsort(array): # mendefinisikan fungsi bubble sort
    swapped = True # memantau pertukaran yang terjadi apabila kondisi terpenuhi
    for i in range(len(array)): # memulai loop dalam range panjang array
        for j in range(0, len(array) - i - 1): # melakukan loop dalam range 0 sampai panjang array yang dikurang setiap item pada panjang array dan dikurang 1
            if array[j] > array[j + 1]: # kondisi jika item pada indeks ke - j array lebih besar dari item pada indeks setelah j
                (array[j], array[j + 1]) = (array[j + 1], array[j]) # terjadi swap item apabila kondisi diatas terpenuhi
                swapped = False 
    
        if swapped: # jika sudah tidak terjadi swap maka array telah diurutkan dan tidak ada swap lagi
            break

def insertArray(): # fungsi untuk memasukkan inputan user
    count = 1
    print("\n>>> Masukkan data hasil Test IQ\n")
    panjangUser = int(input("Masukkan jumlah hasil test : ")) # user menginput panjang array untuk menyimpan data hasil test IQ
    for i in range(panjangUser): # loop daalm range panjang array yang diinput tadi
        item = int(input("\nHasil test ke - " + str(count) + " --> ")) # user memasukkan hasil test IQ 
        array.append(item) # inputan user dimasukkan kedalam array
        count += 1

def showArray(): # fungsi untuk menampilkan data yang telah diinputkan user
    if array == []: # percabangan jika array masih kosong
        print("\nData masih kosong, silahkan masukkan data hasil test terlebih dahulu pada menu 1\n")
    else: # jika user sudah memasukkan data
        print("\n>>> Data hasil test IQ\n")
        number = 1
        for i in range(len(array)): # loop dalam range panjang array
            print("Hasil test ke -",number," : ",array[i],"\n") # akan ditampilkan urutan data menurut yang dimasukkan pertama kali
            number += 1
    
def sortArray(): # fungsi untuk mengurutkan array
    if array == []: # percabangan jika array masih kosong
        print("\nData masih kosong, silahkan masukkan data hasil test terlebih dahulu pada menu 1\n")
    else: # jika user sudah memasukkan data
        print("\n>>> Urutan hasil Test IQ dari hasil terbesar\n")
        number = 1
        babelsort(array) # memanggil fungsi babelsort yang merupakan fungsi untuk mengurutkan data secara bubble sort
        array.reverse() # menggunakan .reverse untuk mengurutkan data (dibalik)
        for i in array: # loop dalam range panjang array
            print("Urutan ke -",number,"\nHasil test :",i,"\n") # # akan ditampilkan urutan data dari yang terbesar
            number += 1

def showMenu(): # fungsi menu tempat user melakukan input pertama kali
    print("""
    --------------------------------------------
    | >>> Program mengurutkan hasil test IQ <<< |  
    --------------------------------------------
    | [1] Masukkan data hasil test IQ           |
    | [2] Lihat data hasil test IQ              |
    | [3] Urutkan secara descending             |
    | [4] Keluar                                |
    --------------------------------------------
""")
    menu = str(input("Pilih menu : "))
    if menu == "1":
        print("-"*50)
        insertArray()
        kembali = str(input("\nMasukkan data hasil test IQ lagi? [y/n] >> "))
        while True:
            if kembali == "y":
                print("-"*50)
                insertArray()
                kembali = str(input("\nMasukkan data hasil test IQ lagi? [y/n] >> "))
            elif kembali == "n":
                print("-"*50)
                showMenu()
            else:
                print("\nMenu tidak tersedia!")
                print("-"*50)
                kembali = str(input("Masukkan data hasil test IQ lagi? [y/n] >> "))

    elif menu == "2":
        print("-"*50)
        showArray()
        kembali = str(input("Lihat data hasil test IQ lagi? [y/n] >> "))
        while True:
            if kembali == "y":
                print("-"*50)
                showArray()
                kembali = str(input("Lihat data hasil test IQ lagi? [y/n] >> "))
            elif kembali == "n":
                print("-"*50)
                showMenu()
            else:
                print("\nMenu tidak tersedia!")
                print("-"*50)
                kembali = str(input("Lihat data hasil test IQ lagi? [y/n] >> "))
    
    elif menu == "3":
        print("-"*50)
        sortArray()
        kembali = str(input("Kembali ke menu? [y] >> "))
        while True:
            if kembali == "y":
                print("-"*50)
                showMenu()
                kembali = str(input("Kembali ke menu? [y] >> "))
            elif kembali == "n":
                print("\nAnda sudah melakukan pengurutan data secara descending!\n")
                kembali = str(input("Kembali ke menu? [y] >> "))
            else:
                print("\nMenu tidak tersedia!")
                print("-"*50)
                kembali = str(input("Kembali ke menu? [y] >> "))
    
    elif menu == "4":
        print("-"*50)
        cius = str(input("\nAnda yakin ingin keluar? [y/n] > "))
        if cius == "y":
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
        elif cius == "n":
            showMenu()

    else:
        print("\nMenu tidak tersedia!\n")
        showMenu()

showMenu()