# Program Order Restoran
## Deskripsi Program
> Program order restoran ini dibuat untuk memudahkan pembeli atau pengguna untuk membeli makanan dengan mudah dan efisien dan juga untuk membantu admin untuk dapat memonitor menu makanan dan mengganti isinya dengan mudah. Program ini diharapkan dapat membantu pembeli dan admin untuk memudahkan berbelanja/mengganti menu. Program ini dibuat menggunakan bahasa pemrograman Python

## Struktur Project
> 1. file PADASPRO.py adalah keseluruhan kode dari program order restoran ini
> 2. file akunuser.json adalah file json yang menyimpan semua user , password dan saldonya
> 3. barangg.json adalah file json untuk menyimpan list menu makanan
> 4. emoney.txt adalah file txt yang akan dicetak ketika user sudah selesai membayar menggunakan emoney
> 5. pemilihan menu.txt adalah file txt yang dicetak ketika user selesai belanja dan membayar menggunakan cash

## Fitur
> beberapa fitur dan dictionary yang digunakan program ini adalah PrettyTable, os dan pwinput
> - PrettyTable prettytable adalah sebuah pustaka yang digunakan untuk menampilkan data dalam sebuah tabel
> - Modul os digunakan untuk membersihkan terminal yang digunakan untuk menginput agar terlihat lebih rapi
> - modul pwinput adalah sebbuah modul yang jika digunakan akan membuat tulisan yang kita input menjadi bintang "*"

Fitur yang disediakan untuk user dan admin adalah
- User
> - pembuatan akun : user dapat membuat akun baru
> - memesan makanan : user bisa memesan makanan
> - emoney : user bisa top up emoney dan membayar dengan emoney
> - fitur sorting : fitur yang disediakan program ini yang jika digunakan akan mencetak tabel dan isinya diurutkan berdasarkan huruf
> - fitur mencari menu : sebuah fitur yang disediakan untuk mencari apakah sebuah makanan ada di dalam daftar menu

- Admin
> - CRUD : menambah,membaca,mengupdate dan menghapus menu yang diinginkan

## Fungsionalitas
> - Registrasi user baru. User yang belum memiliki akun bisa membuat akun baru dan kebudian membuat akun baru
> - Login dan Logout (Exit). User dapat melakukan login menggunakan username dan password dan menggunakan fitur fitur untuk user
> - Pembelian makanan 
