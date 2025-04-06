# H1D023112-PraktikumKB-Pertemuan3
Tugas Pertemuan 3 Praktikum Kecerdasan Buatan
1. Struktur Data Utama:
   - Program menggunakan list kosong daftar_buku untuk menyimpan data buku
   - Setiap buku akan disimpan dalam bentuk dictionary di dalam list ini
     
2. Fungsi tambah_buku():
   - Fungsi ini meminta input dari pengguna berupa:
     - Judul buku
     - Nama penulis
     - Tahun terbit
   - Ada penanganan error untuk tahun (memastikan input berupa angka)
   - Data buku disimpan dalam dictionary dan ditambahkan ke daftar_buku

3. Fungsi tampilkan_buku():
   - Memeriksa apakah ada buku yang tersimpan
   - Jika ada, menampilkan semua buku dalam format tabel sederhana
   - Menggunakan enumerate untuk memberikan nomor urut pada setiap buku

4. Fungsi main():
   - Ini adalah fungsi utama yang menjalankan program
   - Menampilkan menu dengan 3 pilihan:
     1. Tambah buku baru
     2. Lihat semua buku
     3. Keluar dari program
   - Menggunakan perulangan while agar program terus berjalan sampai user memilih keluar

5. Cara Kerja Program:
   - Program akan menampilkan menu utama
   - User memilih opsi dengan memasukkan angka 1-3
   - Berdasarkan pilihan user:
     - Pilihan 1: Menjalankan fungsi tambah_buku()
     - Pilihan 2: Menjalankan fungsi tampilkan_buku()
     - Pilihan 3: Keluar dari program
     - Pilihan lain: Menampilkan pesan error
    
6. Konsep yang Digunakan:
   - Struktur Data:
     - List untuk menyimpan kumpulan buku
     - Dictionary untuk menyimpan detail setiap buku
   - Struktur Kontrol:
     - Perulangan while untuk menu utama
     - Percabangan if-elif-else untuk pilihan menu
     - try-except untuk penanganan error
   - Fungsi: Pemisahan logika program ke dalam fungsi-fungsi terpisah

7. Keunggulan Program:
   - Sederhana dan mudah dipahami
   - Tidak memerlukan library tambahan
   - Memiliki penanganan error dasar
   - Menggunakan struktur data yang efisien
   - Menu yang interaktif dan user-friendly
