import datetime
import tabulate  # untuk membuat tabel yang rapi
from colorama import Fore, Style  # untuk memberikan warna pada output

# Struktur data: List untuk menyimpan dictionary buku
daftar_buku = []

def tambah_buku():
    """Fungsi untuk menambah buku baru"""
    print("\n=== Tambah Buku Baru ===")
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    
    # Penanganan error untuk input tahun
    while True:
        try:
            tahun = int(input("Masukkan tahun terbit: "))
            break
        except:
            print("Error: Mohon masukkan angka yang valid!")
    
    # Menyimpan data buku dalam dictionary
    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun
    }
    
    # Menambahkan buku ke dalam list
    daftar_buku.append(buku)
    print("\nBuku berhasil ditambahkan!")

def tampilkan_buku():
    """Fungsi untuk menampilkan semua buku"""
    if len(daftar_buku) == 0:
        print("\nBelum ada buku yang tersimpan!")
        return
    
    print("\n=== Daftar Buku ===")
    print("No. | Judul | Penulis | Tahun")
    print("-" * 40)
    
    for idx, buku in enumerate(daftar_buku, 1):
        print(f"{idx}. | {buku['judul']} | {buku['penulis']} | {buku['tahun']}")

def main():
    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Keluar")
        
        pilihan = input("\nPilih menu (1-3): ")
        
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            tampilkan_buku()
        elif pilihan == "3":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
