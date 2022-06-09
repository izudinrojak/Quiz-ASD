import re
#nomor 1
kata = '@grg23_'
def cekUname(kata):
    
    pola = r'@[A-Za-z]+[0-9.\_]+'
    cocok = re.findall(pola, kata)[0]
    if kata == cocok:
        return 'pass'
    elif kata != cocok:     
        return 'failed'
print(cekUname(kata))


#nomor 2
a = open('teks.txt','r')
teks = a.read()
a.close

def cekEmail(txt):
    pola = r'[\w.-]+@[\w.-]+'
    cek = re.findall(pola, teks)[0]
    print(cek)





























