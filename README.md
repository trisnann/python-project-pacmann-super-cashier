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
![flowchat](https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/1795fc0c-9a5b-4d97-a7b5-a59d2e9ea811)
### D. Penjelasan functions
#### a. init()
Berfungsi sebagai inisiasi untuk class class Transation()
<br>
<img width="398" alt="init()" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/96cbc06c-b615-4b02-81b4-8dda101f0290">
#### b. add_item 
Berfungsi untuk memasukkan data pesanan berupa nama item, jumlah item, dan harga per item
<img width="596" alt="add_item" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/acdc12d9-8761-4ba1-940c-b5bda090868b">
#### c. show_order 
Berfungsi untuk menampilkan daftar pesanan yang sudan diinput dalam bentuk tabel
<img width="626" alt="show_order" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/1f140f17-0535-445c-9537-debd51069fb6">
#### d. update_item_name 
Berfungsi untuk mengubah nama item yang telah ditambahkan
<img width="490" alt="update_item_name" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/f132590a-8d30-4a09-8868-ba36e7419dbe">
#### e. update_item_qty 
Berfungsi untuk mengubah jumlah item yang telah ditambahkan
<img width="435" alt="update_item_qty" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/58760cc5-e439-4406-87eb-fd8f91a8f12d">
#### f. update_item_price 
Berfungsi untuk mengubah harga per item yang telah ditambahkan
<img width="455" alt="update_item_price" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/99446a16-de2f-47b7-9507-501970a3ad32">
#### g. delete_item 
Berfungsi untuk menghapus salah satu item yang telah ditambahkan
<img width="505" alt="delete_item" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/af541ce3-13aa-4b3b-b77a-ed93d148ac57">
#### h. reset_transaction 
Berfungsi untuk menghapus seluruh pesanan yang telah diinputkan
<img width="571" alt="reset_transaction" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/573523c6-84c5-40bd-906b-41a4e2ce4955">
#### i. check_order 
Berfungsi untuk memastikan data yang diinputkan sudah benar
<img width="563" alt="check_order" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/0542c2fe-f99e-4ef7-bb61-55fe09140ab0">
#### j. total_price 
Berfungsi untuk menghitung jumlah biaya yang perlu dibayar oleh Customer
<img width="739" alt="total_price" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/96fb332e-da5a-49b1-9483-b0e9d764ec00">
### E. Demonstrasi Test Case
<img width="641" alt="test-case-0" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/8783ad76-d3ac-4d81-ba85-bf9af0822f27">
### Test Case 1
<img width="639" alt="test-case-1" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/74b0d914-6204-4563-b3d2-d621b86801c4">
### Test Case 2
<img width="558" alt="test-case-2" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/f7f1b955-8101-400e-b2ad-3d2be0bba1ea">
<br>Menambahkan item lagi
<img width="556" alt="test-case-2-1" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/212d9fbf-abe9-4d31-b0b7-2359f2cd8f01">
<br>Mengubah nama item
<img width="551" alt="test-case-2-2" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/f2d6d05f-d65b-44ed-ba05-2240afd5447b">
<br>Mengubah jumlah item
<img width="561" alt="test-case-2-3" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/8f038f20-7053-4b6b-902a-a121a4d3b02d">
<br>Mengubah harga per item
<img width="597" alt="test-case-2-4" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/618355ee-41b3-4fd4-ad8d-709cc9471667">
### Test Case 3
<img width="643" alt="test-case-3" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/8fc52a90-8cdd-4a7a-900e-ff804a931187">
<br>Menambahkan item lagi
<img width="544" alt="test-case-3-1" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/6978b908-bf2d-48dc-8d23-fdeb03c2a6cd">
<br>Pengecekan data pesanan
<img width="567" alt="test-case-3-2" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/ba6d8eba-b91d-4c03-9f8b-ccba1c7c14ff">
### Test Case 4
<img width="637" alt="test-case-4" src="https://github.com/trisnann/python-project-pacmann-super-cashier/assets/149927711/76f1cbf9-eeb9-4f54-96e7-17dfb502aed6">
### F. Future Work
a. Dalam sistem sudah tersedia data berikut:
<br> - Nama barang, sehingga kesalahan input nama item dapat dihindari
<br> - Jumlah barang, untuk mengetahui ketersediaan barang sehingga jika habis ada peringatan
<br> - Harga barang, sehingga kesalahan input harga barang dapat dihindari
<br>b. Menambahkan sistem membership untuk memperoleh keuntungan lebih dari diskon yang telah tersedia
<br>c. Menambahkan input data alamat, ongkos kirim untuk customer yang berasal dari luar kota atau yang memilih delivery
<br>
Terima kasih atas bimbingannya untuk seluruh tim Pacmann khususnya Kak Shandy selaku instruktur live class dan mentoring, Kak Erlando selaku instruktur mentoring dan Kak Aliya selaku student consultant
