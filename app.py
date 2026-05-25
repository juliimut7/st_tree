#dinamis tree
import streamlit as st

class KategoriNode:
    def __init__(self, nama_kategori):
        self.nama = nama_kategori
        self.sub_kategori = [] #ini adalah 'anak' atau 'cabang' dr kategori

    def tambahkan_sub(self, node_kategori):
        self.sub_kategori.append(node_kategori)
        return node_kategori #mengembalikan node agar mudah disambung
    
    def tampilkan_tree(self, level=0):
        #mengatur spasi agar terlihat bertingkat
        indentasi = "   " *  level
        simbol = "╰┈➤ " if level > 0 else "+ "

        print(f"{indentasi} {simbol} {self.nama}")

        for sub in self.sub_kategori:
            sub.tampilkan_tree(level + 1)

    def cari_node(self, target_nama):
        #mencari node spesifik untuk menambahkan anak dibwhnya
        if self.nama.lower() == target_nama.lower():
            return self
    
        for sub in self.sub_kategori:
            hasil = sub.cari_node(target_nama)
            if hasil:
                return hasil
            
            return None
        
    def cari_jalur(self, target, path=""):
        #mencari jalur lengkap (breadcrumb) seperti studi kasus sblmny
        jalur_saat_ini = path + " > " + self.nama if path else self.nama

        if self.nama.lower() == target.lower():
            return jalur_saat_ini
        
        for sub in self.sub_kategori:
            hasil = sub.cari_jalur(target,jalur_saat_ini)
            if hasil:
                return hasil
            
        return None

# ==========================
# PROGRAM UTAMA (INTERAKSI)
# ==========================

def jalankan_program():
    print("=== SELAMAT DATANG DIPEMBUAT STRUKTUR KATEGORI ===")
    nama_root = input("Masukan nama kategori utama (root): ")
    if not nama_root:
        nama_root = "toko saya"

    root = KategoriNode(nama_root)

    while True:
        print("\n" + "-"*40)
        print("MENU PILIHAN: ")
        print("1. Lihat struktur kategori")
        print("2. Tambah sub kategori baru")
        print("3. Cari jalur kategori")
        print("4. Keluar")
        print("="*40)

        pilihan = input("pilih menu (1/2/3/4): ")
        if pilihan == '1':
            print("\n --- STRUKTUR SAAT INI ---")
            root.tampilkan_tree()

        elif pilihan == '2':
            induk_nama = input("\n masukan nama kategori induk tempat anda ingin menambahkan cabang: ")
            induk_node = root.cari_node(induk_nama)

            if induk_node:
                anak_nama = input(f"masukkan nama sub kategori baru dibawah '{induk_node.nama}': ")
                induk_node.tambahkan_sub(KategoriNode(anak_nama))
                print(f"berhasil menambahkan '{anak_nama}' dibawah '{induk_node.nama}'. ")
            else:
                print(f"kategori '{induk_nama}' tdk ditemukan")

        elif pilihan == '3':
            target_cari = input("\nmasukann nama kategori yg ingin dicari jalurnya: ")
            hasil = root.cari_jalur(target_cari)

            if hasil:
                print(f"dittemukan {hasil}")
            else:
                print(f"kategori '{target_cari}' tdk ditemukan dlm sistem")

        elif pilihan == '4':
            print("\n sudah keluar, terima kasih")
            break
        
        else:
            print("\npilihan tdk valid")

#menjalankan
if __name__ == "__main__":
    jalankan_program()