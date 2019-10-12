def nilai(n1,n2):
    hasil = n1+n2
    if 80 <= hasil <= 100:
        print("nilai anda adalah A")
    elif 70 <= hasil < 80:
        print("nilai anda adalah B")
    elif 60 <= hasil < 70:
        print("nilai anda adalah C")
    elif 50 <= hasil < 60:
        print("nilai anda adalah D, Silahkan Mengulang kembali")
    else:
        print("anda GAGAL")