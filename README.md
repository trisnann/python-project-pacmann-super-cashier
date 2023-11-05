# Python Project Super Cashier
## JPP Data Science - Trisna Nurhayati
### A. Latar Belakang
Super cashier merupakan kasir self-service yang tujuannya dibuat untuk mengefektifkan proses bisnis dan menjangkau Customer dari luar kota.
### B. Requirement yang Dibutuhkan
Berikut beberapa fitur yang akan dibangun :
<br>a. Membuat ID Transaksi dengan membuat objek dari class: trnscrt_123 = Transation()
<br>b. Fitur untuk memasukkan data pesanan berupa nama item, jumlah item, dan harga per item
<br>c. Fitur untuk menampilkan daftar pesanan yang sudan diinput dalam bentuk tabel
<br>d. Fitur untuk mengubah nama item yang telah ditambahkan jika Customer salah input nama item
<br>e. Fitur untuk mengubah jumlah item yang telah ditambahkan jika Customer salah input jumlah item
<br>f. Fitur untuk mengubah harga per item yang telah ditambahkan jika Customer salah input harga per item
<br>g. Fitur untuk menghapus salah satu item yang telah ditambahkan
<br>h. Fitur untuk menghapus seluruh pesanan yang telah diinputkan
<br>i. Fitur untuk memastikan data yang diinputkan sudah benar
<br>j. Fitur untuk menghitung jumlah biaya yang perlu dibayar oleh Customer 
### C. Flowchart
Berikut alur program pembuatan self service cashier
![Alt text](flowchat.png)
### D. Penjelasan functions
#### a. init()
Berfungsi sebagai inisiasi untuk class class Transation()
![Alt text](init().png)
#### b. add_item 
 Berfungsi untuk memasukkan data pesanan berupa nama item, jumlah item, dan harga per item
![Alt text](add_item.png)
#### c. show_order 
Berfungsi untuk menampilkan daftar pesanan yang sudan diinput dalam bentuk tabel
![Alt text](show_order.png)
#### d. update_item_name 
Berfungsi untuk mengubah nama item yang telah ditambahkan
![Alt text](update_item_name.png)
#### e. update_item_qty 
Berfungsi untuk mengubah jumlah item yang telah ditambahkan
![Alt text](update_item_qty.png)
#### f. update_item_price 
Berfungsi untuk mengubah harga per item yang telah ditambahkan
![Alt text](update_item_price.png)
#### g. delete_item 
Berfungsi untuk menghapus salah satu item yang telah ditambahkan
![Alt text](delete_item.png)
#### h. reset_transaction 
Berfungsi untuk menghapus seluruh pesanan yang telah diinputkan
![Alt text](reset_transaction.png)
#### i. check_order 
Berfungsi untuk memastikan data yang diinputkan sudah benar
![Alt text](check_order.png)
#### j. total_price 
Berfungsi untuk menghitung jumlah biaya yang perlu dibayar oleh Customer
![Alt text](total_price.png)
### E. Demonstrasi Test Case
![Alt text](test-case-0.png)
#### Test Case 1
![Alt text](test-case-1.png)
#### Test Case 2
![Alt text](test-case-2.png)
Menambahkan item lagi
![Alt text](test-case-2-1.png)
Mengubah nama item
![Alt text](test-case-2-2.png)
Mengubah jumlah item
![Alt text](test-case-2-3.png)
Mengubah harga per item
![Alt text](test-case-2-4.png)
#### Test Case 3
![Alt text](test-case-3.png)
Menambahkan item lagi
![Alt text](test-case-3-1.png)
Pengecekan data pesanan
![Alt text](test-case-3-2.png)
#### Test Case 4
![Alt text](test-case-4.png)
### F. Future Work
a. Dalam sistem sudah tersedia data berikut:
<br> - Nama barang, sehingga kesalahan input nama item dapat dihindari
<br> - Jumlah barang, untuk mengetahui ketersediaan barang sehingga jika habis ada peringatan
<br> - Harga barang, sehingga kesalahan input harga barang dapat dihindari
<br>b. Menambahkan sistem membership untuk memperoleh keuntungan lebih dari diskon yang telah tersedia
<br>c. Menambahkan input data alamat, ongkos kirim untuk customer yang berasal dari luar kota atau yang memilih delivery
### Terima kasih atas bimbingannya untuk seluruh tim Pacmann khususnya Kak Shandy selaku instruktur live class dan mentoring, Kak Erlando selaku instruktur mentoring dan Kak Aliya selaku student consultant
