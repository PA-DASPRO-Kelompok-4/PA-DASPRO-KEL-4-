from prettytable import PrettyTable
import json
import pwinput
import os
import sys
os.system("cls")

#File JSON (list user dan barang)
akun = "C:/Users/david/OneDrive/Documents/Kodepiton/akunuser.json"
makanan = "C:/Users/david/OneDrive/Documents/Kodepiton/barangg.json"

#dictionary
admin = {"Nama": ["adminkeren"],
        "Password":["1234"] 
        }

uang_cust = {"Cash": 0, "e-Money": 0, "total_topup": 0}


#                                                     DATABASE
#json login dan regis
json_path = "C:/Users/david/OneDrive/Documents/Kodepiton/akunuser.json"
with open(akun, "r") as akunwoi:
    data = json.load(akunwoi)

akun = data
nama_user = akun.get("namapengguna")

password_user = akun.get("passwordpengguna")
passw = password_user[1]

#data barang json
json_path = "C:/Users/david/OneDrive/Documents/Kodepiton/barangg.json"


def simpan():
    with open(json_path, "w") as menu:
        json.dump(data1, menu)

def simpanakun(data):
    with open (akun, "w") as akun1:
        json.dump(data, akun1, indent=4)
# prettytable
tabelmakanan = PrettyTable ()
jsonbarang = "C:/Users/david/OneDrive/Documents/Kodepiton/barangg.json"
with open(jsonbarang, "r") as jsonproduk:
    data1 = json.load(jsonproduk)
    tabelmakanan.field_names = ["nomor", "nama makanan", "harga"]
    tabelmakanan.title = "Warungku"

    
tabelmakanan.clear_rows()
for i in range(len(data1["nomor"])):
    nomor = data1["nomor"][i]
    namamakanan = data1["namamakanan"][i]
    harga = data1["harga"][i]
    tabelmakanan.add_row([nomor, namamakanan, harga])

makanan = data1
listnomor = data1.get("nomor")
listmakanan = data1.get("namamakanan")
listharga = data1.get("harga")
listsaldo = data1.get("saldo")

listuser = data.get("namapengguna")
listpassword = data.get("passwordpengguna")
listsaldo = data.get("saldo")

def read():
    tabelmakanan.clear_rows()
    no = 1
    for i in range(len(data1["namamakanan"])):
        tabelmakanan.add_row(
            [
                no,
                data1["namamakanan"][i],
                data1["harga"][i]
            ]
        )
        no+=1
        simpan()
    print(tabelmakanan)

#LOGIN BUAT ADMIN
def loginadmin():
    login_admin()
    while True:
        try :
            namaadmin = input("Nama admin : ")
        except KeyboardInterrupt :
            print (print ("KEYBOARD INTERRUPT, JANGAN CTRL + C"))
            break
        passwordadmin = pwinput.pwinput ("Password : ")
        if namaadmin == "adminkeren" and passwordadmin == "hahaha":
            print ("Login berhasil , Selamat datang :)")
            operasiadmin() 
        else :
            print ("LOGIN GAGAL, SILAHKAN LOGIN ULANG")
            loginadmin()

# REGISTER AKUN BARU
def buat_akun():
    print("+=====================================+")
    print("|----- REGISTRASI AKUN BARU USER -----|")
    print("+=====================================+")
    akun_user = {}
    
    while True:
        try:
            buatakunbaru = input("Masukkan Nama User : ")
            if buatakunbaru in akun_user:
                print("Maaf, Username Anda Sudah Digunakan. Silahkan masukkan username lain.")
            elif buatakunbaru == "":
                print("Username tidak boleh kosong.")
            else:
                password_user = pwinput.pwinput(prompt="Silahkan masukkan password akun : ")
                if not password_user:
                    print("Password tidak boleh kosong !!")
                else:
                    akun_user[buatakunbaru] = password_user
                    listuser.append(buatakunbaru)
                    listpassword.append(password_user)
                    # listsaldo.append(0)
                    data["namapengguna"] = listuser
                    data["passwordpengguna"] = listpassword
                    # data["saldo"] = listsaldo
                    print(f"Akun dengan username {buatakunbaru} berhasil dibuat!")
                    simpanakun(data)
                    lanjutan = input("Apakah anda ingin membuat akun lagi? (Ya/Tidak)")
                    if lanjutan.lower() == "ya":
                        buat_akun()
                        break
                    elif lanjutan.lower() == "tidak":
                        menu_utama()
                        break
                    else:
                        print("INPUT ANDA TIDAK SESUAI")
        except Exception as e:
            print("-> INPUTAN DATA TIDAK VALID:", str(e))

#LOGIN AKUN USER
def loginakun():
    login_akun()
    while True:
        try:
            punyaakun = int(input("Apakah kamu sudah memiliki akun: "))
        except KeyboardInterrupt:
            print("KEYBOARDINTERRUPT, JANGAN CTRL + C")
            break  
        try :
            if punyaakun == 1:
                masuknama = input("Silahkan masukkan nama: ")
                masukpw = pwinput.pwinput(prompt="Silahkan masukkan password user: ")
                if masuknama in listuser and masukpw in listpassword:
                    cariakun = listuser.index(masuknama)
                    caripw = listpassword.index(masukpw)
                    if cariakun == caripw:
                        print("Selamat datang :)")
                        menu_customer()
                    else :
                        print ("maaf username/password salah")
            elif punyaakun == 2:
                buat_akun()
        except ValueError:
            ("ANDA SALAH MEMASUKKAN USERNAME ATAU PASSWORD1")


#OPERASI BUAT ADMIN
def operasiadmin(): 
    operasi_admin()
    while True:
        try : 
            operasi = input ("Silahkan pilih 1/2/3/4/5\n")
        except KeyboardInterrupt:
            print ("KEYBOARD INTERRUPT JANGAN CTRL + C")
            operasiadmin()
        try :
            if operasi == "1":
                create()
            elif operasi == "2":
                baca()
            elif operasi == "3":
                update()
            elif operasi == "4":
                delete()
            elif operasi == "5":
                os.system('cls')
                raise SystemExit
            else:
                print("INPUT SALAH MOHON HANYA MASUKKAN 1/2/3/4/5")
                print("SILAHKAN COBA LAGI \n")
        except ValueError:
            print ("INPUT SALAH\n")

def create():
    print("\n------ MEMBUAT MENU RESTORAN ------ \n")
    while True :
        try :
            makananbaru = str(input("Silahkan masukkan nama makanan baru = "))
            if makananbaru in listmakanan:
                print("Makanan sudah ada")
            elif makananbaru == (""):
                print("Input tidak boleh kosong")
            else : 
                hargabaru = int(input("Silahkan masukkan harga baru = "))
                if hargabaru <= 0 :
                    print ("Harga tidak boleh 0 / negatif")
                else:
                    listmakanan.append(makananbaru)
                    listharga.append(hargabaru)
                    print ("Makanan berhasil ditambahkan")
                    read()
                    lanjutan = input ("Apakah anda ingin kembali ke menu awal? (ya/tidak) : ")
                    if lanjutan .lower() == "ya":
                        operasi_admin ()
                        break
                    elif lanjutan == "tidak":
                        create()
                        break
                    else:
                        print("INPUT ANDA TIDAK SESUAI")
        except KeyboardInterrupt:
            print ("\nKEYBOARD INTERRUPT JANGAN CTRL + C")
def baca():
    print("\n ------ MEMBACA MENU RESTORAN ------\n")
    print(tabelmakanan)
    while True:
        lanjutan = input ("-> Apakah anda ingin kembali ke Menu operasi admin ? (y/t) : ")
        if lanjutan.lower () == "y":
            operasi_admin ()
        elif lanjutan .lower () == "t":
            baca()
        else:
            print("INPUT TIDAK SESUAI")

def update():
    print(tabelmakanan)
    print ("\n -------- MENGUBAH MENU -------\n")
    while True:
        try:
            try : 
                gantikode = input("Silahkan pilih nomor berapa yang mau diganti :")
                if gantikode in listnomor :
                    gantikode = listnomor.index(gantikode)
                else:
                    print ("\n -> NOMOR PRODUK TIDAK DITEMUKAN")
                    print ("\n -> SILAHKAN COBA LAGI !")
            except KeyboardInterrupt:
                print ("KEYBOARD INTERRUPT JANGAN CTRL + C")
                update()
        except:
            print ("\n -> TERJADI KESALAHAN ")
            print ("\n -> SILAHKAN COBA LAGI !")
        
        while True:
            try :
                namaupdate = input("Apakah anda ingin mengubah nama makanan/minuman baru? (y/t) : ")
            except KeyboardInterrupt:
                print ("KEYBOARD INTERRUPT JANGAN CTRL + C")
                if namaupdate == "y":
                    nub = input("-> Masukan nama menu baru : ")
                    if nub in listmakanan:
                        print("~ NAMA MENU SUDAH ADA")
                        print("~ SILAHKAN MASUKAN NAMA MENU YANG BERBEDA !\n")
                    elif all(x.isalpha() for x in nub) and len(nub) <= 20:
                        listmakanan[gantikode] = nub
                        print("--- Nama Menu berhasil diubah ---\n")
                        break
                    else:
                        print("~ NAMA PRODUK HANYA BOLEH ALPHABET!")
                        print("~ NAMA TIDAK BOLEH LEBIH DARI 20 HURUF!")
                elif namaupdate == "t":
                    break
                else:
                    print(" -> PILIHAN MENU TIDAK TERSEDIA")
        
        while True:
            try :
                hargaupdate = input("Apakah anda ingin memasukkan harga menu terbaru? (y/t) :")
            except KeyboardInterrupt:
                print ("KEYBOARD INTERRUPT JANGAN CTRL + C")
                if hargaupdate == "y":
                    while True:
                        try:
                            try:
                                hm_b = int(input("~ Masukkan harga produk baru : Rp. "))
                                if hm_b < 0:
                                    print("HARGA TIDAK BOLEH KURANG DARI 0")
                                elif hm_b == 0:
                                    print("HARGA HARUS LEBIH DARI 0")
                                elif hm_b > 0 and hm_b < 30000:
                                    listharga[gantikode] = hm_b
                                    print("--- Harga Produk berhasil diubah ---\n")
                            except KeyboardInterrupt:
                                print ("KEYBOARD INTERRUPT JANGAN CTRL + C")
                                while True:
                                    try :
                                        mau = str(input("Apakah mau mengganti menu lagi? y/t\n"))
                                        if mau == "y":
                                            update()
                                            break
                                        elif mau == "t":
                                            operasi_admin()
                                            break
                                        else :
                                            print ("input salah")
                                    except :
                                        print ("KEYBOARD INTERRUPT JANGAN CTRL + C")
                            else:
                                print("-> HARGA PRODUK TIDAK BISA LEBIH DARI 30000")
                        except:
                            print("[] PERHATIKAN INPUTAN")
                        break
                elif hargaupdate == "t":
                    update()
                    break
                else:
                    print("[] PILIHAN TIDAK TERSEDIA")

        operasi_admin()
            
def delete():
    print(tabelmakanan)
    print("\n ------ MENGHAPUS MENU MAKANAN ------ \n")
    print("Silahkan pilih nama makanan yang mau dihapus")
    while True:
        try:
            hapus_m = input("~ Masukan nama makanan yang akan dihapus : ")
            if hapus_m == "":
                print("input tidak boleh kosong")
            elif hapus_m in listmakanan:
                cari_n = listmakanan.index(hapus_m)
                listmakanan.pop(cari_n)
                listnomor.pop(cari_n)
                listharga.pop(cari_n)
            elif hapus_m not in listmakanan:
                print("----- PRODUK TIDAK DITEMUKAN -----")
                delete()
            elif all(x.isspace() for x in hapus_m):
                print("Input tidak boleh kosong")
                while True:
                    lanjutan = input ("-> Apakah anda ingin kembali ke Menu operasi admin ? (y/t) : ")
                    if lanjutan.lower () == "y":
                        operasi_admin ()
                    elif lanjutan .lower () == "t":
                        delete()
                    else:
                        print("INPUT TIDAK SESUAI")
            read()
            break
        except:
            print("\n~ PRODUK TIDAK DITEMUKAN")
            print(" ~ SILAHKAN COBA LAGI")




def menu_utama ():
    print("""
+========================================+
|      SELAMAT DATANG DI WARUNGKU !!!    |
+========================================+
|           Silahkan Pilih Menu          |
| 1. ADMIN                               |
| 2. PEMBELI                             |
| 3. KELUAR (SELESAI)                    |
+========================================+
""")

def login_admin():
    print("""
|==========================================|
|               LOGIN ADMIN                |
|==========================================|
| SILAHKAN MASUKKAN NAMA DAN PASSWORD ANDA |
|==========================================|
""")
    
def operasi_admin():
    print("""
+===============================================+
|  SILAHKAN APA YANG INGIN DILAKUKAN OLEH ANDA  |
+===============================================+
| 1. Membuat menu makanan                       |
| 2. Membaca menu makanan yang ada              |
| 3. Memperbarui menu makanan                   |
| 4. Menghapus makanan/minuman yang ada di menu |
| 5. Keluar                                     |
+===============================================+
""")
    
def login_akun():
    print("""
+======================================+
|    SELAMAT DATANG DI WARUNGKU !!!    |
+======================================+
|         Pilihlah angka 1/2           |
+--------------------------------------+
|      1. YA                           |
|      2. TIDAK                        |
|======================================|       
""")
    
def menucust():
    print("""
+-------------------------------------+
|            MENU PEMBELI             |
+-------------------------------------+
|1.| REGISTRASI AKUN BARU             |
|2.| LOGIN AKUN                       |
|3.| KELUAR                           |
+-------------------------------------+
""")
def operasi_cust ():
    print("""
+--------------------------------------+
|               WARUNGKU               |
+--------------------------------------+
|  SELAMAT DATANG, SILAHKAN DIPILIH :) |
+--------------------------------------+
|1.| Beli Makanan                      |
|2.| Sortir Menu                       |
|3.| Mencari Menu                      |
|4.| Top Up E-Money                    |
|5.| Lihat Saldo E-Money               |
|6.| Exit                              |
+--------------------------------------+
""")

def menu_topup():
    print("""
+-------- TOP UP E-MONEY --------+
|--------------------------------|
|1.|  Rp 100.000                 |
|2.|  Rp 200.000                 |
|3.|  Rp 300.000                 |
|4.|  Rp 400.000                 |
|5.|  Rp 500.000                 |
+--------------------------------+
""")

def cara_bayar():
    print("""
---------------------------------
|       METODE PEMBAYARAN       |
---------------------------------
|1.| Cash                       |
|2.| E-Money                    |
---------------------------------
""")

#SORTIR MENU
def sortirmenu():
    tabelmakanan.clear_rows()
    tabelmakanan.sortby = "nama makanan"
    no = 1
    for i in range(len(data1["namamakanan"])):
        tabelmakanan.add_row(
            [
                no,
                data1["namamakanan"][i],
                data1["harga"][i]
            ]
        )
        no+=1
        simpan()
    print(tabelmakanan)
#menu customer
def menu_cust():
    while True: 
        print("       WELCOME TO       ")
        print("        WARUNGKU        ")
        menucust()
        try:
            opsi = int(input(" -> MASUKKAN MENU OPSI ANDA : "))
            if opsi == 1:
                os.system("cls")
                buat_akun()
                break
            elif opsi == 2:
                loginakun()
            elif opsi == 3:
                print("----- PROGRAM TELAH SELESAI -----")
                print("-------   TERIMA KASIH   ------- ")
                print("---- SILAHKAN DATANG KEMBALI ----")
                exit()
            
            else:
                print(" X PILIHAN TIDAK ADA  ")
                print(" SILAHKAN COBA LAGI :)")
                menu_cust()
                break
        except ValueError:
            print(" MASUKKAN ANGKA SAJA \n")

def beli_makanminum():
    while True:
        read()
        belimakanminum = input("~ Masukkan menu yang ingin Anda beli: ")
        if belimakanminum in listmakanan:
            search = listmakanan.index(belimakanminum)
            harga=int(listharga[search])
            jumlah1=int(input("Masukan Jumlah Barang yang Akan Dibeli : "))
            if jumlah1 <= 0 :
                print("Jumlah tidak boleh kurang dari 0.")
                print(" Silahkan coba lagi\n")
            else :
                totalharga = int(harga * jumlah1)
                cara_pembayaran(belimakanminum,jumlah1,totalharga)
        else:
            print("Makanan/Minuman tidak ditemukan dalam daftar menu.")

        while True:
            try:
                Lanjut = input(">> Apakah anda ingin belanja lagi? (y/t) : ")
                if Lanjut == "y":
                    pass
                    beli_makanminum()
                elif Lanjut == "t":
                    os.system('cls')
                    menu_cust()
                    break
                else:
                    print("[] INPUT SALAH\n")
            except:
                print("[] MOHON PERHATIKAN INPUTAN\n")

def topup_emoney():
    while True :
        menu_topup()
        try :
            topup = int(input("Silahkan pilih 1/2/3/4/5\n"))
            if topup == 1:
                uang_cust["total_topup"] = uang_cust["e-Money"] + 100000
                uang_cust["e-Money"] = uang_cust["total_topup"]

                with open("emoney.txt", "a") as uang:
                    print(
                        "===========================================================",
                        file=uang,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 100000, file=uang)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["total_topup"],
                        end="\n",
                        file=uang,
                    )
                    print(
                        "===========================================================",
                        file=uang,
                    )

                print("\n--- PENGISIAN SALDO E-MONEY ANDA BERHASIL ---\n")
                print("Saldo e-Money : Rp", uang_cust["total_topup"])
                break
            elif topup == 2:
                uang_cust["total_topup"] = uang_cust["e-Money"] + 200000
                uang_cust["e-Money"] = uang_cust["total_topup"]

                with open("emoney.txt", "a") as uang:
                    print(
                        "===========================================================",
                        file=uang,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 200000, file=uang)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["total_topup"],
                        end="\n",
                        file=uang,
                    )
                    print(
                        "===========================================================",
                        file=uang,
                    )

                print("\n--- PENGISIAN SALDO E-MONEY ANDA BERHASIL ---\n")
                print("Saldo e-Money : Rp", uang_cust["total_topup"])
                break
            elif topup == 3:
                uang_cust["total_topup"] = uang_cust["e-Money"] + 300000
                uang_cust["e-Money"] = uang_cust["total_topup"]

                with open("emoney.txt", "a") as uang:
                    print(
                        "===========================================================",
                        file=uang,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 300000, file=uang)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["total_topup"],
                        end="\n",
                        file=uang,
                    )
                    print(
                        "===========================================================",
                        file=uang,
                    )

                print("\n--- PENGISIAN SALDO E-MONEY ANDA BERHASIL ---\n")
                print("Saldo e-Money : Rp", uang_cust["total_topup"])
                break
            elif topup == 4:
                uang_cust["total_topup"] = uang_cust["e-Money"] + 400000
                uang_cust["e-Money"] = uang_cust["total_topup"]
                with open("emoney.txt", "a") as uang:
                    print(
                        "===========================================================",
                        file=uang,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 400000, file=uang)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["total_topup"],
                        end="\n",
                        file=uang,
                    )
                    print(
                        "===========================================================",
                        file=uang,
                    )

                print("\n--- PENGISIAN SALDO E-MONEY ANDA BERHASIL ---\n")
                print("Saldo e-Money : Rp", uang_cust["total_topup"])
                break
            elif topup == 5:
                uang_cust["total_topup"] = uang_cust["e-Money"] + 500000
                uang_cust["e-Money"] = uang_cust["total_topup"]

                with open("emoney.txt", "a") as uang:
                    print(
                        "===========================================================",
                        file=uang,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 500000, file=uang)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["total_topup"],
                        end="\n",
                        file=uang,
                    )
                    print(
                        "===========================================================",
                        file=uang,
                    )

                print("\n--- PENGISIAN SALDO E-MONEY ANDA BERHASIL ---\n")
                print("Saldo e-Money : Rp", uang_cust["total_topup"])
                break
            else :
                print("[] PILIHAN TIDAK TERSEDIA")
                print("[] SILAHKAN COBA LAGI\n")
        except ValueError :
            print(" ! MOHON PERHATIKAN INPUTAN ANDA !")

def cara_pembayaran(belimakanminum,jumlah1,totalharga):
    with open("pemilihan menu.txt", "a") as mb:
        print(" +------------------------------------------+")
        print(" |               PILIH MENU                 |", file=mb)
        print(f"|-> Barang: {belimakanminum}               |", file=mb)
        print(f"|-> Jumlah: {jumlah1}                     |", file=mb)
        print(" |                                          |")
        print(f"|-> Total: Rp {totalharga}                 |", file=mb)
        print(" +------------------------------------------+", file=mb)
    print("  Terima kasih, silahkan lakukan pembayaran`\n")

    pajak = totalharga * 0.1
    total_pembayaran = totalharga + pajak
    print(f"-> Total: Rp {total_pembayaran}")
    cara_bayar()
    while True:
        pil_carabayar= int(input("Pilih metode pembayaran (1/2): "))
        if pil_carabayar == 1:
            uang = int(input("Masukkan nominal uang Anda: "))
            harga = totalharga
            pajak = harga * 0.1
            total_pembayaran = harga + pajak
            if uang >= total_pembayaran:
                kembalian = uang - total_pembayaran
                print("\n+---------- TRANSAKSI ANDA BERHASIL -----------+")
                print("\n|               STRUK PEMBELIAN                |")
                print(f" | Uang      : Rp {uang}                        |")
                print(f" | PPN 10%    : Rp {pajak}                      |")
                print(f" | Total     : Rp {total_pembayaran}            |")
                print(f" | Kembalian : Rp {kembalian}                   |")
                print("  +----------------------------------------------+")
                print(" THANk YOU, SILAHKAN DATANG KEMBALI ;)")
                break

            elif uang < total_pembayaran:
                total_kurang = total_pembayaran - uang
                print("\n---------- TRANSAKSI TIDAK BERHASIL -----------")
                print(f"-> Uang Anda kurang sebesar Rp. {total_kurang}  ")
            
            elif uang == total_pembayaran:
                print("")
                break

        elif pil_carabayar == 2:
            saldo = uang_cust["e-Money"]
            harga = totalharga
            pajak = harga * 0.1
            total_pembayaran = harga + pajak
            
            if saldo >= total_pembayaran:
                uang_cust["e-Money"] = saldo - total_pembayaran
                print(" +---------- TRANSAKSI ANDA BERHASIL -----------+")
                print(" |               STRUK PEMBELIAN                |")
                print(f"| e-Money    : Rp {saldo}                      |")
                print(f"| PPN 10%    : Rp {pajak}                      |")
                print(f"| Total      : Rp {total_pembayaran}           |")
                print(f"| Sisa Saldo : Rp {uang_cust['e-Money']}       |")
                print(" +----------------------------------------------+")
            elif saldo < total_pembayaran:
                print("Saldo e-Money Anda kurang")
                tanya = input("Apakah Anda ingin top up saldo e-Money? (y/t): ")
                if tanya.lower == "y":
                    topup_emoney()
                    top_up = int(input("Masukkan jumlah top up saldo e-Money: "))
                    uang_cust["e-Money"] += top_up
                    print(f"Saldo e-Money Anda sekarang: Rp {uang_cust['e-Money']}")
                    if saldo > total_pembayaran :
                            uang_cust["e-Money"] = saldo - total_pembayaran
                            with open("emoney.txt", "a") as mb:
                                print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                                print("|============= STRUK PEMBELIAN =============|", file=mb)
                                print("| e-Money    : Rp                           |", saldo, file=mb)
                                print("| PPN 10%    : Rp                           |", pajak, file=mb)
                                print("|Total      : Rp                            |", total_pembayaran, file=mb)
                                print("| Sisa Saldo : Rp                           |", uang_cust["e-Money"], file=mb)
                                print("|===========================================|", file=mb)
                    else :
                        kurang = total_pembayaran - uang_cust["e-Money"]
                        print("\n----------TRANSAKSI ANDA GAGAL-----------")
                        print("- Saldo e-Money anda kurang sebesar Rp. ", kurang)
                        break

                elif tanya == "t":
                    print("\n---------- SALDO ANDA TIDAK CUKUP ----------")
                    print("--------------- TRANSAKSI GAGAL --------------")
                else:
                    print("\n! INPUT TIDAK SESUAI")
            elif saldo == total_pembayaran:
                
                uang_cust["e-Money"] = saldo - total_pembayaran
                with open("transaksi.txt", "a") as s:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n============= STRUK PEMBELIAN =============",file=s)
                    print(" e-Money    : Rp", saldo, file=s)
                    print(" PPN 10%    : Rp", pajak, file=s)
                    print(" Total      : Rp", total_pembayaran, file=s)
                    print(" Sisa Saldo : Rp", uang_cust["e-Money"], file=s)
                    print("===========================================", file=s)

        else:
            print("[] PILIHAN TIDAK TERSEDIA")
            print("[] SILAHKAN COBA LAGI\n")

    while True:
        lagi = input(">> Apakah Anda ingin kembali ke menu utama (y/t): ")
        if lagi == "y":
            os.system("cls")  # Menghapus layar konsol biar bersih (cuma buat windows)
            menu_customer()
        elif lagi == "t":
            exit()
        else:
            print("[] TOLONG PERHATIKAN INPUT")

def menu_customer():
    while True:
        try :
            operasi_cust()
            pilih = int(input("~ Masukan Menu yang dipilih : "))
            if pilih == 1:
                os.system('cls')
                beli_makanminum()
                while True :
                    kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
                    if kembali == "t":
                        beli_makanminum()
                    elif kembali == "y":
                        os.system('cls')
                        break
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")
            
            elif pilih == 2:
                os.system('cls')
                sortirmenu()
                while True :
                    kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
                    if kembali == "t":
                        sortirmenu()
                    elif kembali == "y":
                        os.system('cls')
                        break
                    else :
                        print("X PILIHAN TIDAK ADA X")

            elif pilih == 3:
                os.system('cls')
                mencarimenu = input("masukkan nama menu: ")
                if mencarimenu in listmakanan:
                    print("menu anda tersedia di data kami")
                else:
                    print("menu tidak tersedia di data kami")

            elif pilih == 4:
                os.system('cls')
                topup_emoney()
                while True :
                    kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
                    if kembali == "t":
                        topup_emoney()
                    elif kembali == "y":
                        os.system('cls')
                        break
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")

            elif pilih == 5:
                os.system('cls')
                while True :
                    print("\n------------------------- E-Money -------------------------\n")
                    print(f' Saldo e-Money anda adalah Rp. {uang_cust["e-Money"]}')
                    print("\n-----------------------------------------------------------\n")
                    kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
                    if kembali == "t":
                        pass
                    elif kembali == "y":
                        os.system('cls')
                        break
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")
                        
            elif pilih == 6:
                os.system('cls')
                print("---------- PROGRAM TELAH SELESAI ----------")
                print("--------------- TERIMA KASIH --------------")
                exit()
            else :
                print("[] PILIHAN TIDAK TERSEDIA")
                print("[] SILAHKAN COBA LAGI\n")
        except ValueError :
            print("[] MOHON MASUKAN INPUT DENGAN BENAR")
        
#MENU UTAMA
def main():
    menu_utama()
    while True :
        try :
            mauapa = int(input("Silahkan pilih 1/2/3\n"))
        except KeyboardInterrupt:
            print ("KEYBOARD INTERRUPT, JANGAN CTRL + C")
            main()
        try:
            if mauapa == 1:
                print ("Silahkan masukkan data admin")
                loginadmin()
            elif mauapa == 2:
                menu_cust()
            elif mauapa == 3:
                print ("Terimakasih sudah menggunakan program ini")
                break
            else :
                print ("Input salah")
        except ValueError:
            print ("INPUT SALAH SILAHKAN INPUT 1/2/3")
            main()
main()