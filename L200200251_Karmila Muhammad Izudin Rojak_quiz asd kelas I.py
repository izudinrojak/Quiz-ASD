import re
#nomor 1

pola  = r'@[A-Za-z]+[0-9.\_]+'
uname = input('Masukkan Username: ')
cocok = re.findall(a, uname)
if cocok:
    if uname == cocok[0]:
        print('PASS')
    elif uname != cocok[0]:
        print('FAILED')
else:
    print('FAILED')


#nomor 2
a = open('teks.txt','r')
teks = a.read()
a.close

def cekEmail(txt):
    pola = r'[\w.-]+@[\w.-]+'
    cek = re.findall(pola, teks)[0]
    print(cek)





























