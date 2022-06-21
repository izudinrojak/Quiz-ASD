import re
#nomor1
    
uname = input('Masukkan Username: ')
pola = r'@[\w]+[\d]+\_*'
cocok = re.findall(pola,uname)
if not cocok:
    print('FAILED')
elif cocok[0] != uname:
    print('FAILED')
else:
    print('PASS')

#nomor 2
a = open('teks.txt','r')
teks = a.read()
a.close

def cekEmail(txt):
    pola = r'[\w.-]+@[\w.-]+'
    cek = re.findall(pola, teks)[0]
    print(cek)





























