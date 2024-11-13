nama_siswa =str(input('Masukan Nama siswa : '))
jumlah_siswa =int(input('Masukan semester siswa : '))

total_nilai= 0
for a in range(jumlah_siswa): 
   nilai = float(input(f'Masukan Nilai Ujian Siswa per semester -{a + 1 }:'))
   total_nilai += nilai

#    keseluruhan_nilai= total_nilai + jumlah_siswa 
  
   rata_rata = total_nilai / jumlah_siswa
print(f'Rata-rata nilai dari {jumlah_siswa} siswa adalah: {rata_rata: .2F}')
print(f'Jadi keseluruhan nilai berjumlah {total_nilai}:')


if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B'
elif nilai >= 75:
    grade = 'C'
elif nilai >= 60:
    grade = 'D'
elif nilai >= 45:
    grade='E'
print(f'Grade: {grade} ')

if  nilai >= 75:
    print("Selamat Anda Dinyatakan Lulus")
else:
    print("Maaf anda belum Lulus tapi jangan patah semangat belajar")