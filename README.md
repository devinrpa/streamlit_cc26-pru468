# Analisis Konsumsi Listrik Rumah Tangga

## Project Overview
Proyek ini menampilkan dashboard interaktif berbasis Streamlit untuk menganalisis konsumsi listrik rumah tangga. Analisis mencakup tren harian, perbandingan weekday vs weekend, dan distribusi konsumsi.

## Dataset
Dataset yang digunakan: `household_daily_clean.csv` 

## Setup Environment - Anaconda
Jika menggunakan Anaconda/Miniconda, jalankan:

```bash
conda create --name capstone python=3.10 -y
conda activate capstone
pip install -r requirements.txt
```

## Setup Environment - Shell / Terminal
Perintah alternatif (venv atau pipenv):

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.\.venv\Scripts\Activate  # Windows PowerShell
pip install -r requirements.txt
```

Atau jika pakai `pipenv`:

```bash
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App
Jalankan aplikasi dengan perintah:

```bash
streamlit run dashboard.py
```
