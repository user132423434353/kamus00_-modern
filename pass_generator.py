import random


sandi = rtygdcgefuwyhg7vreruvguvgrg634891p93748$%%&I(iuiicevf)
panjang = int(input("berapa panjang karakter untuk kata sandi?"))
hasil = ""

for i in range(panjang):
    hasil += random.choice(sandi)
print("Kata sandi yg dihasilkan adalah",hasil)