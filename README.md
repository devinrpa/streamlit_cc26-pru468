# Analisis Konsumsi Listrik Rumah Tangga

Proyek ini menampilkan dashboard Streamlit yang melakukan analisis deskriptif terhadap konsumsi listrik rumah tangga.

## Ringkasan
- Aplikasi utama: `dashboard.py`
- Dataset: `household_daily_clean.csv` (sudah termasuk di repo jika ukurannya kecil)

## Setup (Windows PowerShell)
1. Buat virtual environment dan aktifkan:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Perbarui pip dan install dependency:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Jalankan aplikasi Streamlit:

```powershell
streamlit run dashboard.py
```

Aplikasi akan tersedia di `http://localhost:8501` secara default.

## Struktur Repository (direkomendasikan)
- `dashboard.py` — aplikasi Streamlit utama
- `requirements.txt` — daftar paket Python yang dibutuhkan
- `household_daily_clean.csv` — file data (opsional jika file besar)
- `README.md` — dokumentasi ini
- `.gitignore` — file untuk mengecualikan `.venv` dan file sementara

## Deploy ke Streamlit Cloud
1. Push repository ke GitHub.
2. Buka https://share.streamlit.io dan login dengan GitHub.
3. Klik **New app** → pilih repository, branch, lalu set file ke `dashboard.py` → Deploy.

Catatan:
- Jika dataset terlalu besar (>~50 MB) atau bersifat privat, simpan di penyimpanan eksternal (Google Drive, S3) dan ubah `load_data()` pada `dashboard.py` untuk membaca dari URL.
- Jangan commit folder `.venv` ke GitHub. Tambahkan file `.gitignore` jika perlu.

Jika mau, saya bisa juga membuat `.gitignore` dan commit semuanya ke repo GitHub untukmu — mau saya buatkan?