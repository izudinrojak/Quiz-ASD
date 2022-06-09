import re
#nomor 1

pola1 = r'@[A-Za-z]+[0-9.\_]+'
pola2 = r'@[A-Za-z]+[0-9]+.\_'
pola3 = r'@[A-Za-z]+.\_'
uname = input('Masukkan Username: ')
cocok1 = re.findall(pola1, uname)
cocok2 = re.findall(pola2, uname)
cocok3 = re.findall(pola3, uname)
if cocok3:
    if uname == cocok3[0]:
        print('FAILED')
elif cocok2:
    print('PASS')
elif cocok1:
    if uname == cocok1[0]:
        print('PASS')
    elif uname != cocok1[0]:
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





























