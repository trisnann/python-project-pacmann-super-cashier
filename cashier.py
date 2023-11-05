#!/usr/bin/env python
# coding: utf-8

# In[1206]:


import random
from tabulate import tabulate

class Transaction:
    # inisialisasi attribut
    def __init__ (self):
        '''
        method untuk menginisialisasi dict_order, sebuah dict yang akan menampung data order
        '''
        self.dict_order = dict ()
    
    # menambahkan item yang akan dibeli
    def add_item(self, nama_item, jumlah_item, harga_item):
        '''
        method untuk menambahkan barang yang akan dipesan
        '''
        self.dict_order.update({nama_item: [jumlah_item, harga_item]})
        
        # memastikan jenis data yang diinputkan benar untuk jumlah item dan harga item
        try:
            self.jumlah_item = int(jumlah_item)
            self.harga_item = int(harga_item)
            
        except:
            raise Exception("Tolong masukan angka untuk harga dan jumlah barang")
        
    # menampilkan data pesanan dalam tabel
    def show_order(self):
        '''
        method untuk menampilkan data pesanan berupa nama item, jumlah item, harga per item dan total harga per item dalam bentuk tabel
        '''
        
        table_data = [["No.", "Nama Item", "Jumlah Item", "Harga per Item", "Total Harga"]]
        
        no = 0
        for key, value in self.dict_order.items():
            no += 1
            table_data.append([no, key, value[0], value[1], value[0] * value[1]])
        print("\nBerikut daftar pesanan Anda\n")
        print(tabulate(table_data, headers = "firstrow", tablefmt="github"))

    # jika membatalkan/salah membeli salah satu item
    def delete_item(self, nama_item):
        '''
        method untuk menghapus salah satu item belanja yang sudah diinput
        '''
        try:
            self.dict_order.pop(nama_item)
            print(f"{nama_item} berhasil dihapus dari daftar pesanan")
        
        except:
            print(f"{nama_item} tidak terdapat dalam pesanan")
           
    # jika ada kesalahan memasukan informasi item 
    # update nama item
    def update_item_name(self, nama_item, update_nama_item):
        '''
        method untuk mengganti nama item yang sudah diinput
        '''
        self.dict_order[update_nama_item] = self.dict_order[nama_item]
        del self.dict_order[nama_item]
    
    # update jumlah item
    def update_item_qty(self, nama_item, update_jumlah_item):
        '''
        method untuk mengganti jumlah item yang sudah diinput
        '''
        self.dict_order[nama_item][0] = update_jumlah_item
    
    # update harga item
    def update_item_price(self, nama_item, update_harga_item):
        '''
        method untuk mengganti harga per item yang sudah diinput
        '''
        self.dict_order[nama_item][1] = update_harga_item
     
    # jika batal berbelanja
    def reset_transaction(self):
        '''
        method untuk menghapus seluruh pesanan yang sudah diinput
        '''
        self.dict_order.clear()
        print("Semua item berhasil dihapus.\nAnda tidak memiliki daftar pesanan.")

    # check order
    def check_order(self):
        '''
        method untuk memastikan data pesanan yang diinput sudah benar dan sesuai
        '''
        for key, value in self.dict_order.items():
            if type(key) == str and all(type(val) == int for val in value):
                return ("Data pesanan yang diinputkan sudah benar")
            else:
                return ("Terdapat kesalahan data yang diinputkan")
    
    # menghitung total belanjaan
    def total_price(self):
        '''
        method untuk menghitung total belanja yang akan dibayarkan dan potongannya/diskon jika memenuhi ketentuan, yaitu:
        diskon 5% jika belanja > 200.000
        diskon 8% jika belanja > 300.000
        diskon 10% jika belanja > 500.000
        '''
        total_price = sum([jumlah_item * harga_item for jumlah_item, harga_item in self.dict_order.values()])
        
        if total_price > 500000:
                total_price = round(total_price - (total_price * 0.10), 2)
                print(f"\nSelamat Anda memdapatkan diskon sebesar 10% karena berbelanja lebih dari Rp 500.000\nTotal belanja yang harus dibayarkan setelah diskon sebesar {total_price}")
            
        elif total_price > 300000:
                total_price = round(total_price - (total_price * 0.08), 2)
                print(f"\nSelamat Anda memdapatkan diskon sebesar 8% karena berbelanja lebih dari Rp 300.000\nTotal belanja yang harus dibayarkan setelah diskon sebesar {total_price}")
            
        elif total_price > 200000:
            total_price = round(total_price - (total_price * 0.05), 2)
            print(f"\nSelamat Anda memdapatkan diskon sebesar 5% karena berbelanja lebih dari Rp 200.000\nTotal belanja yang harus dibayarkan setelah diskon sebesar {total_price}")

        else:
            print(f"\nTotal belanja yang harus dibayarkan sebesar {total_price}")
# %%
