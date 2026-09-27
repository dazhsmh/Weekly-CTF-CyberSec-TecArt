# Week0-CyberSec-TecArt  
Homework 00 bertujuan untuk memastikan setiap peserta telah memiliki lingkungan
kerja dan tools dasar yang diperlukan untuk mengikuti pembelajaran serta kompetisi
Cyber Security, khususnya Capture The Flag (CTF)

## Tools Umum  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/tools-umum.png" width="300">

Instalasi tools umum yang telah diinstall:  
- WSL (Windows Subsytem for Linux) Distro Kali Linux  
- Git dan Github  
- Python

## Pengujian WSL  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/create-readme.png" width="500">
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/nano-identitas.png" width="500">  

Pengujian WSL dilakukan sepenuhnya melalui Command Line Interface (CLI).
Langkah - langkah yang dilakukan:
1. Membuat sebuah folder dengan nama Week0-CyberSec-TecArt dengan command ```mkdir [nama_direktori]```.
2. Masuk ke dalam folder tersebut dengan command ```cd [direktori]```.
3. Membuat file baru dengan nama README.md dengan command ```nano [nama_file]```.
4. Lalu menuliskan informasi berikut pada file tersebut:  
- NIM
- Nama
- Divisi

## Pengujian Python  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/create-py.png" width="500">
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/nano-py.png" width="500">  

Pengujian python dengan membuat program sederhana dilakukan dengan langkah - langkah berikut:
1. Membuat program menggunakan ```nano [nama program]``` dengan ekstensi file .py
2. Menuliskan kode program python
3. Menjalankan program menggunakan command ```python3 [nama_program.py]```

# Challenge  
Kerjakan challenge “Undo” pada platform CYLAB Academy:
https://learn.cylabacademy.org/library/766  
Dokumentasikan langkah-langkah penyelesaian challenge dalam write-up.  

## [-] Pengerjaan Challenge Undo  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/launch.png" width="500">  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/nc_soal.png" width="500">  

- Tekan tombol Launch Instance untuk memulai.  
- Hubungkan server soal dengan command ```nc [ip_address] [port]```  

Berikut 5 step yang muncul untuk menyelesaikan challenge ini.  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/challenge_undo.png" width="500">  

### --- Step 1 ---
```
Current flag: KTZvNHFycnE4LWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it:
```
Untuk mendecode string yang didecode dengan base64, gunakan command ```base64 -d```  

### --- Step 2 ---
```
Current flag: )6o4qrrq8-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
Hint: Reversed the text.
Enter the Linux command to reverse it:
```
Untuk reverse sebuah text, gunakan command ```rev```  

### --- Step 3 ---
```
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-8qrrq4o6)
Hint: Replaced underscores with dashes.
Enter the Linux command to reverse it:
```
Untuk mengganti seluruh dash menjadi underscore pada text, gunakan command ```tr "-" "_"```  

### --- Step 4 ---
```
Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_8qrrq4o6)
Hint: Replaced curly braces with parentheses.
Enter the Linux command to reverse it:
```
Untuk mengganti seluruh kurung menjadi kurawal pada text, gunakan command ```tr "()" "{}"```  

### --- Step 5 ---
```
Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_8qrrq4o6}
Hint: Applied ROT13 to letters.
Enter the Linux command to reverse it:
```
Untuk mendekripsi/mengenkripsi text dengan sandi ROT13, gunakan command ```tr "A-Za-z" "N-ZA-Mn-za-m"``` dimana huruf A-Z berubah menjadi N-Z dan A-M (Bergeser 13 huruf)  

Setelah mengerjakan seluruh step, kita akan mendapatkan sebuah flag. Copy flag tersebut lalu submit pada website untuk menyelesaikan challenge ini.  

Referensi:  
https://www.linuxsec.org/2018/09/base64-terminal.html  
https://www.geeksforgeeks.org/linux-unix/rev-command-in-linux-with-examples/  
https://www.tecmint.com/tr-command-examples-in-linux/  
https://medium.com/@marshal_demi/using-rot13-and-tr-command-e67c2bd607ed  

### [-] Pengerjaan Challenge IntroToBurp (Kategori Web)  
Link: https://learn.cylabacademy.org/library/419  
1. Start instance lalu buka website target untuk mulai menganalisa.  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/web1.png" width="500">
2. Saya menggunakan software Burp Suite yang telah terinstall di laptop saya untuk melakukan proses analisa.  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/web2.png" width="500">
3. Website target berisikan form registrasi. Setelah mengisi form tersebut halaman dialihkan ke form otp.  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/web3.png" width="500">
4. Setelah itu saya membuka Burp Suite lalu pergi ke dashboard Proxy dan menghidupkan mode Intercept. Gunakan web browser dari Burp Suite untuk menganalisa website target. Disaat saya mengisi lalu mengirim form otp, website mengirimkan sebuah request yang berisikan nilai otp dengan metode POST.  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/web4.png" width="500">
5. Saya mencoba request tersebut di mode repeater lalu mencoba menghapus "otp=1234" untuk melihat responsenya. Flag berhasil di dapatkan dan challenge berhasil diselesaikan.  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/web5.png" width="500">

### [-] Pengerjaan Challenge Information (Kategori Forensics)  
Link: https://learn.cylabacademy.org/library/186  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/forensic-1.png" width="500">  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/forensic-2.png" width="500">


Download file foto cat.jpg untuk dianalisis. Tampilan foto saat dibuka tampak normal. Saya telah menginstall tool Exiftool untuk digunakan menganalisis gambar. Gunakan command ```exiftool [nama_file]``` untuk menganalisis. 
```
ExifTool Version Number         : 13.55
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2026:09:08 22:38:56+08:00
File Access Date/Time           : 2026:09:08 22:45:57+08:00
File Inode Change Date/Time     : 2026:09:08 22:45:56+08:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/forensic-3.png" width="500">

Terlihat seluruh detail file foto. Karena nampak ada yang janggal dengan licensenya, saya menggunakan command ```echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d``` untuk mencoba mendecode teks tersebut dengan base64. Benar saja teks tersebut merupakan flag tersembunyi. Challenge pun terselesaikan.  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/forensic-4.png" width="500">  


### [-] Pengerjaan Challenge The Numbers (Kategori Cryptography)  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/crypto-2.png" width="500">  

Sebelum mengerjakan challenge, pada WSL saya mempelajari cara membuat Python Virtual Environment (venv) lalu menginstall library pycryptodome. Setelah library diinstall saya menjalankan kode berikut:  
```
from Crypto . Cipher import AES
from Crypto . Random import get_random_bytes
key = get_random_bytes (16)
data = b" Hello PyCryptodome !"
cipher = AES . new ( key , AES . MODE_EAX )
ciphertext , tag = cipher . encrypt_and_digest ( data )
print (" Ciphertext :", ciphertext .hex () )
cipher = AES . new ( key , AES . MODE_EAX , nonce = cipher . nonce )
plaintext = cipher . decrypt ( ciphertext )
print (" Plaintext :", plaintext . decode () )

```

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/crypto-1.png" width="500">  

Program dapat dijalankan tanpa error dan menghasilkan Plaintext: Hello
PyCryptodome!.  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/crypto-3.png" width="500">  

Link: https://learn.cylabacademy.org/library/68  
Pada challenge ini, saya mendapatkan sebuah gambar yang berisikan kumpulan angka unik disertai tanda kurung kurawal buka dan tutup. Hint pada challenge ini yaitu format flagnya adalah PICOCTF{}. Karena format flag dan nomor sama sama memiliki kurung kurawal, saya mencoba mencocoklogikan antara nomor yang di dapat dengan format flag.  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/crypto-4.png" width="500">  

```
16 = P
9 = I
3 = C
15 = O
3 = C
20 = T
6 = F
```
Dari pola tersebut didapatkan bahwa nomor tersebut telah diterjemahkan dengan sandi A1Z26. Kita hanya perlu menerjemahkannya kembali ke text semula. Di linux kita dapat menggunakan command ``` echo "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }" | perl -pe 's/(\d+)/chr($1+96)/ge; s/\s//g' ``` untuk menerjemahkan kembali teks itu dalam sandi A1Z26. Flag pun berhasil didapatkan. Challenge selesai.  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/crypto-5.png" width="500">  

Referensi:  
https://mutiinsani.medium.com/virtual-environment-pada-python-b1f49816ee51  
https://www.scribd.com/document/523257737/codes  

### [-] Pengerjaan Challenge Icibos Tekart 0 (Kategori Reverse Engineering dan Binary Exploitation)  
Link: https://tecartlab.sanca.site/challenges#Icibos%20Tekart%200-12  
Install program lalu coba jalankan dan analisis. Saya juga menggunakan software Binary Ninja untuk meganalisis program ini. Saat menjalankan program, muncul text dimana kita bisa menginput kata ajaib. 

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/program1-1.png" width="500">  
<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/program1-2.png" width="500">  

```
Belajar Reverse Engineering
Masukan kata ajaib:
```
Untuk mencari kata ajaib tersebut, saya membuka program ini di software Binary Ninja. Gunakan tampilan linear dan High Level IL untuk membaca kode programnya.

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/program1-3.png" width="500">  

```
00401166    int32_t main()

00401178        char const* const p = "iniString"
00401186        puts(str: "Belajar Reverse Engineering")
0040119a        printf(format: "Masukan kata ajaib: ")
004011b5        char r[0xc8]
004011b5        fgets(buf: &r, n: 0xc8, fp: __bss_start)
004011d3        r[strcspn(&r, "\n")] = 0
004011db        int isCorrect = 1
004011db        
0040121b        for (int i = 0; i s<= 8; i += 1)
0040120a            if (p[sx.q(i)] != r[sx.q(i)])
0040120c                isCorrect = 0
0040120c        
00401221        if (isCorrect == 0)
00401267            puts(str: "password salah!")
00401221        else if (strlen(&r) != 9)
00401267            puts(str: "password salah!")
00401236        else
00401242            puts(str: "password benar!")
00401256            printf(format: "tecart{1ntr0_to_R3vEr1n9}")
00401256        
00401272        return 0
```
Pada main function, terdapat deklarasi variabel p = "iniString" dengan tipe data char. Lalu di bawahnya terlihat ada program untuk menginput variabel r serta perulangan dan percabangan. Sepertinya kode program perulangan digunakan untuk menampilkan huruf yang disimpan dalam array p & r. Kondisi percabangan menunjukkan jika seluruh karakter dari variabel r sama dengan karakter variabel p, maka password benar. Maka kata ajaib yang dimaksud adalah "IniString". Setelah memasukkan kata tersebut di dalam program, saya berhasil mendapatkan flag dan menyelesaikan challenge ini.  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/program1-4.png" width="500">  

### [-] Pengerjaan Challenge Icibos Tekart 1 (Kategori Reverse Engineering dan Binary Exploitation)  
Link: https://tecartlab.sanca.site/challenges#Icibos%20Tekart%201-13  
Install program lalu coba jalankan dan analisis. Saya juga menggunakan software Binary Ninja untuk meganalisis program ini. Saat menjalankan program, muncul text dimana kita bisa menginput kata ajaib. (Lagi)

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/program2-1.png" width="500">  

```
Belajar Reverse Engineering
Masukan kata ajaib:
```
Untuk mencari kata ajaib tersebut, saya membuka program ini di software Binary Ninja. Gunakan tampilan linear dan High Level IL untuk membaca kode programnya.

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/program2-2.png" width="500">  

```
004012b8    int32_t main()

004012cd        char p[0xc]
004012cd        __builtin_strcpy(dest: &p, src: "bukanString")
004012e8        puts(str: "Belajar reversing lagi")
004012fc        printf(format: "Masukan kata ajaib: ")
00401317        char r[0xc8]
00401317        fgets(buf: &r, n: 0xc8, fp: stdin)
00401335        r[strcspn(&r, "\n")] = 0
0040133d        int isCorrect = 1
0040133d        
0040137a        for (int i = 0; i s<= 0xa; i += 1)
00401369            if (p[sx.q(i)] != r[sx.q(i)])
0040136b                isCorrect = 0
0040136b        
00401380        if (isCorrect == 0)
004013b2            puts(str: "password salah!")
00401380        else if (strlen(&r) != 0xb)
004013b2            puts(str: "password salah!")
00401395        else
004013a1            win(&r)
004013a1        
004013bd        return 0
```
Pada main function, terdapat deklarasi variabel p dan r dengan tipe data char. Lalu di bawahnya terlihat ada program untuk menginput variabel r serta perulangan dan percabangan. Sepertinya kode program perulangan digunakan untuk menampilkan huruf yang disimpan dalam array p & r. Terdapat pula kode ```__builtin_strcpy(dest: &p, src: "bukanString")``` yang menyalin string ke memory variabel p. Kondisi percabangan menunjukkan jika seluruh karakter dari variabel r sama dengan karakter variabel p, lalu panjang string tepat 11, maka password benar. Maka kata ajaib yang dimaksud adalah "bukanString". Setelah memasukkan kata tersebut di dalam program, saya berhasil mendapatkan flag dan menyelesaikan challenge ini.  

<img src="https://github.com/dazhsmh/Weekly-CTF-CyberSec-TecArt/blob/main/week0/img/program2-3.png" width="500">  


