def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("="*10)
        print(f"nama : {kontak['nama']}")
        print(f"email : {kontak['email']}")
        print(f"telepon : {kontak['telepon']}")

def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon : ")
    kontak = {
        "Nama" : nama,
        "Email" : email,
        "telepon" : telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("no telepon yang akan di hapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    if index == -1:
        print("Data Tidak Ditemukan")
    else:
        del daftar_kontak[index]
        print("berhasil menghapus data kontak")

    del daftar_kontak 
#ini appnya seblum di masukan elif ke 3
#program managemen kontak
import function
#list of dictionary

daftar_kontak = []

daftar_kontak.append({
    "nama" : "macan putih",
    "email" : "jokokendil13@gmail.com",
    "telepon" : "0812003"
})

#menu program
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. tambah kontak")
    print("3. hapus kontak")
    print("4. cari kontak")
    print("0. keluar program")

    menu = input("pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)


print("program selesai berjalan, sampai jumpa lagi")