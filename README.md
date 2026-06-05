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
- Jangan commit folder `.venv` ke GitHub. Tambahkan file `.gitignore` jika perlu.

Jika mau, saya bisa juga membuat `.gitignore` dan commit semuanya ke repo GitHub untukmu — mau saya buatkan?
