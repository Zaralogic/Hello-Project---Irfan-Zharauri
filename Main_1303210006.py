file_input = input('Masukkan nama file teks ') # meminta kepada penggunan memasukkan nama file sesuai dengan yang dimilikinya

hasil_akhir = open(file_input,'r') # mengakses file teks dengan mode akses read

# inisialisasi dict info_akhir untuk menampung informasi klub
info_akhir = {}

# inisialisasi dict info_klub dan list info_klub_awal untuk menampung data klub yang terdapat dalam teks
info_klub = {} 
info_klub_awal = []

for teks in hasil_akhir: # looping untuk mengakses dan membaca setiap baris pada file teks
    club1, score1, score2, club2 = teks.split()
    klub1 = club1.title() #nama klub pertama
    klub2 = club2.title() #nama klub kedua 
    skor1 = int(score1) #skor dari klub pertama yang telah di casting
    skor2 = int(score2) #skor dari klub kedua yang telah di casting
    
    info_klub_awal.append([klub1, skor1, skor2, klub2]) 

# fungsi untuk menghitung banyak data yang terdapat dalam teks
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# inisialisasi x sebagai jumlah banyak data yang terdapat dalam teks
x = file_len(file_input)

# looping untuk memasukkan setiap angka yang terlooping sebagai ganti key dari dict info_klub dengan valuenya dari list info_klub_awal
for i in range(x):
    info_klub[i] = info_klub_awal[i]

# mencari total pertandingan
info_totalpertandingan = {} #dict kosong untuk menampung jumlah total pertandingan beserta dengan nama klubnya

for a in info_klub.values(): 
    if a[0] not in info_totalpertandingan: 
        info_totalpertandingan[a[0]] = 1
    else:
        info_totalpertandingan[a[0]] += 1
        
    if a[3] not in info_totalpertandingan:
        info_totalpertandingan[a[3]] = 1
    else:
        info_totalpertandingan[a[3]] += 1

for b, totalpertandingan in info_totalpertandingan.items(): # looping untuk menambah value pada dict info_akhir dengan mengambilnya dari dict info_totalpertandingan
    info_akhir[b] = [totalpertandingan]

# mencari WIN,DRAW,LOSE
total_win = {} # dict kosong untuk menampung jumlah total menang
total_draw = {} # dict kosong untuk menampung jumlah total seri
total_lose = {} # dict kosong untuk menampung jumlah total kalah

for b in info_klub.values():
    if b[1] == b[2]:
        if b[0] not in total_win:
            total_win[b[0]] = 0
        else:
            total_win[b[0]] += 0
            
        if b[3] not in total_win:
            total_win[b[3]] = 0
        else:
            total_win[b[3]] += 0

        if b[0] not in total_draw:
            total_draw[b[0]] = 1
        else:
            total_draw[b[0]] += 1

        if b[3] not in total_draw:
            total_draw[b[3]] = 1
        else:
            total_draw[b[3]] += 1

        if b[0] not in total_lose:
            total_lose[b[0]] = 0
        else:
            total_lose[b[0]] += 0
            
        if b[3] not in total_lose:
            total_lose[b[3]] = 0
        else:
            total_lose[b[3]] += 0

    elif b[1] > b[2]:
        if b[0] not in total_win:
            total_win[b[0]] = 1
        else:
            total_win[b[0]] += 1
            
        if b[3] not in total_win:
            total_win[b[3]] = 0
        else:
            total_win[b[3]] += 0

        if b[0] not in total_draw:
            total_draw[b[0]] = 0
        else:
            total_draw[b[0]] += 0

        if b[3] not in total_draw:
            total_draw[b[3]] = 0
        else:
            total_draw[b[3]] += 0

        if b[0] not in total_lose:
            total_lose[b[0]] = 0
        else:
            total_lose[b[0]] += 0
            
        if b[3] not in total_lose:
            total_lose[b[3]] = 1
        else:
            total_lose[b[3]] += 1

    else:
        if b[0] not in total_win:
            total_win[b[0]] = 0
        else:
            total_win[b[0]] += 0
            
        if b[3] not in total_win:
            total_win[b[3]] = 1
        else:
            total_win[b[3]] += 1

        if b[0] not in total_draw:
            total_draw[b[0]] = 0
        else:
            total_draw[b[0]] += 0

        if b[3] not in total_draw:
            total_draw[b[3]] = 0
        else:
            total_draw[b[3]] += 0

        if b[0] not in total_lose:
            total_lose[b[0]] = 1
        else:
            total_lose[b[0]] += 1
            
        if b[3] not in total_lose:
            total_lose[b[3]] = 0
        else:
            total_lose[b[3]] += 0
    

for c, totalwin in total_win.items(): # looping untuk menambah value pada dict info_akhir dengan mengambilnya data dari dict total_win
    info_akhir[c] += [totalwin]

for d, totaldraw in total_draw.items(): # looping untuk menambah value pada dict info_akhir dengan mengambilnya data dari dict total_draw
    info_akhir[d] += [totaldraw]

for e, totallose in total_lose.items(): # looping untuk menambah value pada dict info_akhir dengan mengambilnya data dari dict total_lose
    info_akhir[e] += [totallose]

# mencari GF(Gol memasukkan), GA(Gol kemasukan), GD(Selisih gol)
info_GF = {} # dict kosong untuk menampung informasi Gol memasukkan pada setiap klub
info_GA = {} # dict kosong untuk menampung informasi Gol kemasukkan pada setiap klub

for z in info_klub.values():
    if z[0] not in info_GF:
        info_GF[z[0]] = [z[1]]
    else:
        info_GF[z[0]] += [z[1]]

    if z[3] not in info_GF:
        info_GF[z[3]] = [z[2]]
    else:
        info_GF[z[3]] += [z[2]]

for y in info_klub.values():
    if y[0] not in info_GA:
        info_GA[y[0]] = [y[2]]
    else:
        info_GA[y[0]] += [y[2]]

    if y[3] not in info_GA:
        info_GA[y[3]] = [y[1]]
    else:
        info_GA[y[3]] += [y[1]]

for f, totalGF in info_GF.items(): # looping untuk menambah value pada dict info_akhir dengan mengambilnya data dari dict info_GF
    totalGFakhir = totalGF[0] + totalGF[1] 
    info_akhir[f] += [totalGFakhir]

for g, totalGA in info_GA.items(): # looping untuk menambah value pada dict info_akhir dengan mengambilnya data dari dict info_GA
    totalGAakhir = totalGA[0] + totalGA[1]
    info_akhir[g] += [totalGAakhir]

for h, totalGD in info_akhir.items(): # looping mencari total selisih gol yang diambil dari informasi GF dan GA yang sebelumnya telah diinput terlebih dahulu
    totalGDakhir = totalGD[4] - totalGD[5]
    info_akhir[h] += [totalGDakhir]

# mencari Total Points
total_winforpoints = {} # dict kosong untuk menampung informasi point menang pada setiap klub
total_drawforpoints = {} # dict kosong untuk menampung informasi point draw pada setiap klub
total_loseforpoints = {} # dict kosong untuk menampung informasi point kalah pada setiap klub
total_points = {} # dict kosong untuk menampung informasi total point setalah dikalkulasikan pada setiap klub

for x in info_klub.values():
    if x[1] == x[2]:
        if x[0] not in total_winforpoints:
            total_winforpoints[x[0]] = 0
        else:
            total_winforpoints[x[0]] += 0

        if x[3] not in total_winforpoints:
            total_winforpoints[x[3]] = 0
        else:
            total_winforpoints[x[3]] += 0

        if x[0] not in total_drawforpoints:
            total_drawforpoints[x[0]] = 1
        else:
            total_drawforpoints[x[0]] += 1

        if x[3] not in total_drawforpoints:
            total_drawforpoints[x[3]] = 1
        else:
            total_drawforpoints[x[3]] += 1

        if x[0] not in total_loseforpoints:
            total_loseforpoints[x[0]] = 0
        else:
            total_loseforpoints[x[0]] += 0

        if x[3] not in total_loseforpoints:
            total_loseforpoints[x[3]] = 0
        else:
            total_loseforpoints[x[3]] += 0

    elif x[1] > x[2]:
        if x[0] not in total_winforpoints:
            total_winforpoints[x[0]] = 3
        else:
            total_winforpoints[x[0]] += 3

        if x[3] not in total_winforpoints:
            total_winforpoints[x[3]] = 0
        else:
            total_winforpoints[x[3]] += 0

        if x[0] not in total_drawforpoints:
            total_drawforpoints[x[0]] = 0
        else:
            total_drawforpoints[x[0]] += 0

        if x[3] not in total_drawforpoints:
            total_drawforpoints[x[3]] = 0
        else:
            total_drawforpoints[x[3]] += 0

        if x[0] not in total_loseforpoints:
            total_loseforpoints[x[0]] = 0
        else:
            total_loseforpoints[x[0]] += 0

        if x[3] not in total_loseforpoints:
            total_loseforpoints[x[3]] = 0
        else:
            total_loseforpoints[x[3]] += 0

    else:
        if x[0] not in total_winforpoints:
            total_winforpoints[x[0]] = 0
        else:
            total_winforpoints[x[0]] += 0

        if x[3] not in total_winforpoints:
            total_winforpoints[x[3]] = 3
        else:
            total_winforpoints[x[3]] += 3

        if x[0] not in total_drawforpoints:
            total_drawforpoints[x[0]] = 0
        else:
            total_drawforpoints[x[0]] += 0

        if x[3] not in total_drawforpoints:
            total_drawforpoints[x[3]] = 0
        else:
            total_drawforpoints[x[3]] += 0

        if x[0] not in total_loseforpoints:
            total_loseforpoints[x[0]] = 0
        else:
            total_loseforpoints[x[0]] += 0

        if x[3] not in total_loseforpoints:
            total_loseforpoints[x[3]] = 0
        else:
            total_loseforpoints[x[3]] += 0

for ab, totalwinpoints in total_winforpoints.items(): 
    total_points[ab] = [totalwinpoints]

for ac, totaldrawpoints in total_drawforpoints.items():
    total_points[ac] += [totaldrawpoints]

for ad, totallosepoints in total_loseforpoints.items():
    total_points[ad] += [totallosepoints]

for g, totalpoints in total_points.items(): # looping untuk menambah value pada dict info_akhir dengan mengambilnya data dari dict total_point
    totalpointsakhir = totalpoints[0] + totalpoints[1] + totalpoints[2]
    info_akhir[g] += [totalpointsakhir]
        
# memanggil fungsi klasemen_liga_inggris
def klasemen_liga_inggris(klasemen_sementara): # membuat fungsi untuk membuat tabel klasemen liga inggris
    print("\nClub Name\tMP\tWin\tDraw\tLose\tGF\tGA\tGD\tPoints\n") # judul dari setiap informasi yang terdapat dalam tabel klasemen
    urutan_klasemen = dict(sorted(klasemen_sementara.items())) # mengurutkan nama klub dalam dict berdasarkan abjad 
    urutan_klasemen1 = dict(sorted(urutan_klasemen.items(), key = lambda x : x[1][-1], reverse = True)) # mengurutkan klub berdasarkan total points yang dikumpulkan
    for namaklub, infoklub in urutan_klasemen1.items():
        print(namaklub.replace('_', ' '), end='\t')
        if len(namaklub) <= 7: 
            namaklub = " " + namaklub
            print(end='\t')
        for value in infoklub:
            print(value, end='\t')
        print()

# main program
klasemen_liga_inggris(info_akhir)
hasil_akhir.close()
