print("---------------Selamat Datang Di Python Store---------------")
nama_barang = input("Masukan Nama Barang      :")
harga = int(input  ("Masukan Harga Barang     :"))
qty = int(input    ("Masukan Qty              :"))

subtotal = harga * qty
diskon = 0.05 * subtotal
total_bayar = subtotal - diskon

print(f"Subtotal                    = Rp. {subtotal :10}")
print(f"Diskon 5%                   = Rp. {diskon :10.0f}")
print(f"Total Yang Harus Dibayar    = Rp. {total_bayar: 10.0f}")
besar_bayar = int(input(f"Besar Bayar                 = Rp.     "))
kembalian = int (besar_bayar - total_bayar)
print(f"Kembalian                   = Rp. {kembalian}")

print("-"*50)

print("Rincian Pesanan          :")
print(f"{qty} {nama_barang}      Rp. {subtotal :10}")
print("Rincian Kembalian        :")
lembar50 = kembalian // 50000
print(f"Rp. 50.000               : {lembar50} Lembar")
kembalian = kembalian % 50000
lembar20 = kembalian // 20000
print(f"Rp. 20.000               : {lembar20} Lembar")
kembalian = kembalian % 20000
lembar10 = kembalian // 10000
print(f"Rp. 10.000               : {lembar10} Lembar")
kembalian = kembalian % 10000
lembar5 = kembalian // 5000
print(f"Rp. 5.000                : {lembar5} Lembar")
kembalian = kembalian % 5000
lembar2 = kembalian // 2000
print(f"Rp. 2.000                : {lembar2} Lembar")
kembalian = kembalian % 2000
lembar1 = kembalian // 1000
print(f"Rp. 1.000                : {lembar1} Lembar")

print("--------TERIMA KASIH TELAH BERBELANJA DI Pyhton Store--------")
