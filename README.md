# Dokumentasi Proyek Enkripsi Diskrit

Proyek ini terdiri dari dua program Python yang mengimplementasikan algoritma enkripsi dan dekripsi:

1. **RSA (Rivest–Shamir–Adleman)**: Digunakan untuk mengenkripsi dan mendekripsi nama menjadi blok ASCII.
2. **ElGamal**: Digunakan untuk mengenkripsi pesan berbasis karakter ASCII dengan parameter kunci publik tertentu.

Kedua program menghasilkan laporan perhitungan secara lengkap dalam format `.docx`.

---

## 📁 Struktur File

```
├── rsa_enkripsi.py          # Kode Python untuk enkripsi & dekripsi RSA
├── elgamal_enkripsi.py      # Kode Python untuk enkripsi ElGamal
├── [NIM-Klean]_DISKRIT [Kelas-Klean]_Tugas3.docx  # Output RSA
├── [NIM-Klean]_DISKRIT [Kelas-Klean]_Tugas4.docx  # Output ElGamal
```

---

## 🛠️ Cara Menjalankan

### ✅ Persyaratan
- Python 3.x
- Paket tambahan:
  - `python-docx`
  - `tabulate` (khusus untuk ElGamal)

### 🔧 Instalasi Paket

```bash
pip install python-docx tabulate
```

### 💻 Menjalankan Program di Windows/macOS

**RSA**
```bash
python rsa_enkripsi.py
```
Input: Nama yang akan dienkripsi.

**ElGamal**
```bash
python elgamal_enkripsi.py
```
Input: Pesan (teks) yang ingin dienkripsi.

Output dari kedua program adalah file `.docx` berisi laporan lengkap proses enkripsi dan dekripsi.

---

## 🔐 Penjelasan Teknis

### 🔸 RSA Encryption & Decryption
- **Kunci Publik (e, n)**: Digunakan untuk enkripsi.
- **Kunci Privat (d, n)**: Digunakan untuk dekripsi.
- Nama dikonversi ke ASCII, lalu dibagi menjadi blok-blok 3 digit.
- Setiap blok dienkripsi dengan formula: `c = m^e mod n`.
- Dekripsi dilakukan dengan: `m = c^d mod n`.
- Semua langkah ditulis secara eksplisit ke file `.docx`, termasuk pemangkatan modular.

### 🔸 ElGamal Encryption
- Menggunakan parameter:
  - `p = 2579`
  - `α (alpha) = 2`
  - `β (beta) = 949`
- Untuk setiap karakter:
  - Dipilih angka acak `k`.
  - Hitung: `γ = α^k mod p` dan `δ = (β^k * m) mod p`.
- Proses modular exponentiation disertai langkah-langkah rinci.
- Output disimpan dalam `.docx` bersama tabel ASCII dan hasil enkripsi.

---

## 📝 Output File
Setiap program menghasilkan file Word dengan struktur:

- **Informasi kunci**
- **Tabel ASCII (untuk RSA dan ElGamal)**
- **Langkah perhitungan modular exponentiation**
- **Hasil akhir enkripsi (dan dekripsi untuk RSA)**

Contoh nama file output:
```
[NIM-Klean]_DISKRIT [Kelas-Klean]_Tugas3.docx
[NIM-Klean]_DISKRIT [Kelas-Klean]_Tugas4.docx
```


