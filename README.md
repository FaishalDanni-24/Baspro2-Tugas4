# Perkalian Matriks 5x5
Kode berikut adalah implementasi untuk perkalian matriks A dan B dengan ukuran 5x5.

# Penjelesan Kode
- Pertama, diinisialisasi list dan diberikan input nilai ke matriks A dan B.
- Kedua, diinisialisasi sebuah list kosong C untuk menyimpan hasil matriks perkalian.

Untuk melakukan perkalian digunakan 3 for loop :
- loop i : mengakses setiap baris dalam matriks A dan append kolom baru untuk Matriks C.
- loop j : mengakses setiap kolom dalam matriks B dan append nilai baru ke Matriks C.
- loop k : menghitung perkalian matriks.

# Contoh
```python
# Matriks A
matriksA = [
    [1,2,3,4,5],
    [3,2,5,4,6],
    [7,9,1,0,1],
    [0,2,4,6,8],
    [1,3,5,7,9]
]

# Matriks B
matriksB = [
    [6,7,8,9,10],
    [1,6,2,1,3],
    [0,0,4,1,9],
    [2,10,5,8,0],
    [6,9,0,3,10]
]
```
## Hasil
Berikut ini adalah hasil perkalian matriks dari contoh Matriks A dan Matriks B:
```python
[46, 104, 44, 61, 93]
[64, 127, 68, 84, 141]
[57, 112, 78, 76, 116]
[62, 144, 50, 78, 122]
[77, 176, 69, 100, 154]
```
