totharga=[]
varianku=[]
def pembuka() :
    print("\t\t\t\t\t\t\t\t\t\t\t\tASSALAMU'ALAIKUM\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t\t SELAMAT DATANG")
    print("\t\t\t\t\t\t\t=======================================\t KERIPIK NAFISA ==========================================")
    print("\t\t\t\t\t\t\t__________________________________________________________________________________________________")

def menu() :
    print("""
    \t\t\t\t\t\t\t=======================================\t MENU KERIPIK \t==========================================
    \t\t\t\t\t\t\t==================================================================================================
    \t\t\t\t\t\t\t| \tKODE\t | \tDAFTAR KERIPIK\t\t | \tJUMLAH (Bks)\t | \tHARGA\t\t |
    \t\t\t\t\t\t\t==================================================================================================
    \t\t\t\t\t\t\t| \t1\t | \tKERIPIK UBI\t\t | \t1\t\t | \tRp. 35.000\t |
    \t\t\t\t\t\t\t| \t2\t | \tKERIPIK PISANG\t\t | \t1\t\t | \tRp. 35.000\t |
    \t\t\t\t\t\t\t| \t3\t | \tKERIPIK UBI PEDAS MANIS\t | \t1\t\t | \tRp. 40.000\t |
    \t\t\t\t\t\t\t| \t4\t | \tKERIPIK KELADI BULAT\t | \t1\t\t | \tRp. 60.000\t |
    \t\t\t\t\t\t\t| \t5\t | \tKERIPIK STIK KELADI\t | \t1\t\t | \tRp. 75.000\t |
    \t\t\t\t\t\t\t==================================================================================================
    """)

def tambahan () :
    print(""" 
    \t\t\t\t\t\t\t\t ========================\tTAMBAHAN VARIAN RASA \t==========================
    \t\t\t\t\t\t\t\t =================================================================================
    \t\t\t\t\t\t\t\t | \tKODE\t | \t\tVARIAN RASA\t\t | \tHARGA\t\t |
    \t\t\t\t\t\t\t\t =================================================================================
    \t\t\t\t\t\t\t\t | \t1\t | \t\tJAGUNG MANIS\t\t | \tRp. 5.000\t |
    \t\t\t\t\t\t\t\t | \t2\t | \t\tJAGUNG BAKAR\t\t | \tRp. 5.000\t |
    \t\t\t\t\t\t\t\t | \t3\t | \t\tBALADO\t\t\t | \tRp. 5.000\t |
    \t\t\t\t\t\t\t\t =================================================================================
    """)

def identitas () :
    print("\t\t\t\t\t\tIdentitas Pembeli")
    nama = input("Masukkan Nama Pembeli : ")
    print("\t\t\t\t\t\tNama \t\t:", nama)
    email = input("Masukkan Alamat Email Pembeli Tanpa Mengetik @gmail.com : ")
    print("\t\t\t\t\t\tEmail \t\t:", email,"@gmail.com")
    wa = int(input("Masukkan Nomor Whatsapp Pembeli dalam 12 Digit : "))
    print("\t\t\t\t\t\tNo Whatsappp \t:", wa)

def menupilihan():
    print("\n\t\t\t\t\t\t=================================================================================================================")
    print("\t\t\t\t\t\t-----------------------------------------------STRUK PEMBELIAN---------------------------------------------------")
    print("\t\t\t\t\t\t=================================================================================================================")
    identitas()
    import time;
    localtime = time.asctime( time.localtime(time.time()) )
    print ("\t\t\t\t\t\tWaktu Transaksi :", localtime)

def listbeli():
    print("""\t\t\t\t\t\t==================================================================================================================
    \t\t\t\t\t\t| \tPEMBELIAN KERIPIK\t | \tJUMLAH PEMBELIAN\t | \tTAMBAHAN VARIAN RASA\t |    HARGA\t |
    \t\t\t\t\t\t==================================================================================================================
    """)

def varianrasa() :
    tambahanvarian = int(input("Masukkan Tambahan Varian Rasa Yang Diinginkan : "))
    if tambahanvarian == 1 :
        varian = "JAGUNG MANIS"
        tbeli = beli+5000
    elif tambahanvarian == 2 :
        varian = "JAGUNG BAKAR"
        tbeli = beli+5000
    elif tambahanvarian == 3 :
        varian = "BALADO"
        tbeli = beli+5000
    else :
        varian = "     -      "
        tbeli = beli
    varianku.append(varian)
    totharga.append(tbeli)

pembuka()
menu()
tambahan()
menupilihan()
listbeli()
tekan = "y"
while tekan == "y":
    kode = int(input("Masukkan Kode Untuk Memesan Makanan Pada Pilihan Menu Keripik: "))
    if kode == 1 :
        keripik = "UBI             "
        jumlah = int(input("Masukkan Jumlah Keripik per Bks Dalam Memesan Keripik: "))
        beli = jumlah*35000
        varianrasa()

    elif kode == 2 :
        keripik = "PISANG           "
        jumlah = int(input("Masukkan Jumlah Keripik per Bks Dalam Memesan Keripik : "))
        beli = jumlah*35000
        varianrasa()

    elif kode == 3 :
        keripik = "UBI PEDAS MANIS"
        jumlah = int(input("Masukkan Jumlah Keripik per Bks Dalam Memesan Keripik : "))
        beli = jumlah*40000
        varianrasa()

    elif kode == 4 :
        keripik = "KELADI BULAT   "
        jumlah = int(input("Masukkan Jumlah Keripik per Bks Dalam Memesan Keripik : "))
        beli = jumlah*60000
        varianrasa()

    elif kode == 5 :
        keripik = "STIK KELADI    "
        jumlah = int(input("Masukkan Jumlah Keripik per Bks Dalam Memesan Keripik : "))
        beli = jumlah*75000
        varianrasa()

    else :
       break
    print ("\t\t\t\t\t\t| \t",keripik,"\t | \t\t",jumlah,"\t\t | \t", varianku[-1],"\t\t | ","Rp.",totharga[-1],"\t |")    
    tekan=input("Tekan Y untuk melakukan pembelian keripik lagi dan tekan N langsung ke Struk Pembayaran?")

uang = int(input("Silahkan Melakukan Pembayaran Uang : "))
totalpembelian = sum(totharga)
if totalpembelian > 100000 :
    diskon = 10000
    harganya = totalpembelian-diskon
else :
    diskon = 0
    harganya = totalpembelian

print("\t\t\t\t\t\t------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\tTotal Pembelian\t\t\t\t\t\t\t\t\t\t\t    Rp.", totalpembelian)
print("\t\t\t\t\t\tDiskon\t\t\t\t\t\t\t\t\t\t\t\t    Rp.", diskon)
print("\t\t\t\t\t\t------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\tHarga Total\t\t\t\t\t\t\t\t\t\t\t    Rp.", harganya)
print("\t\t\t\t\t\tUang Dibayar\t\t\t\t\t\t\t\t\t\t\t    Rp.", uang)
kembalian = uang-harganya
print("\t\t\t\t\t\tUang Kembalian\t\t\t\t\t\t\t\t\t\t\t    Rp.", kembalian) 
print("\t\t\t\t\t\t------------------------------------------TERIMA KASIH TELAH MELAKUKAN PEMBELIAN----------------------------------")