# Tugas 2 - Data Lifecycle Management
## Smart Agriculture Dataset

### Identitas
- Nama: Btari Adiella Duhita Salsabila
- NPM: 23082010150
- Kelas: Big Data & IoT paralel B

### Deskripsi Proyek
Proyek ini membahas implementasi data lifecycle management menggunakan Smart Agriculture Dataset dari Kaggle. Analisis dilakukan menggunakan Jupyter Notebook/Google Colab dan divisualisasikan melalui dashboard interaktif menggunakan Streamlit.

### Dataset
- Nama dataset: Smart Agriculture Dataset
- Sumber: Kaggle
- File data mentah: `data/raw/cropdata_updated.csv`

### Struktur Repository
repo_github/
├── README.md
├── data/
│   └── raw/
│       └── cropdata_updated.csv
├── Data_Lifecycle_Smart_Agriculture.ipynb
├── dashboard/
│   └── streamlit_app.py
├── outputs/
│   ├── cleaned_data.csv
│   ├── data_quality_score.csv
│   ├── dashboard_screenshot.png
│   └── analysis_report.pdf

### Tahapan Pengerjaan

#### 1. Data Acquisition
Dataset diunduh dari Kaggle dan disimpan ke folder `data/raw/`.

#### 2. Data Understanding
Tahap ini dilakukan dengan:
- melihat beberapa baris awal data
- memeriksa jumlah data dan kolom
- memeriksa tipe data
- menghitung statistik deskriptif
- memeriksa missing values

#### 3. Data Cleaning
Tahapan cleaning meliputi:
- standarisasi nama kolom
- pemeriksaan missing value
- penghapusan duplikasi
- penghapusan outlier dengan metode IQR
- pembuatan kolom `record_time` sintetis karena dataset tidak memiliki timestamp asli

#### 4. Data Analysis
Analisis dilakukan menggunakan:
- statistik deskriptif
- heatmap korelasi
- time series trend
- data quality score

#### 5. Dashboard
Dashboard dibuat menggunakan Streamlit dan memuat:
- time series trend
- gauge meter
- heatmap korelasi
- alert system
- preview data

### Hasil Utama
- Dataset tidak memiliki missing value pada seluruh kolom.
- Variabel `temp` dan `humidity` memiliki korelasi negatif yang kuat.
- Dashboard berhasil menampilkan visualisasi utama sesuai kebutuhan tugas.
- Data hasil cleaning disimpan dan digunakan untuk dashboard.

### Data Quality Score
- Accuracy: 1.0000
- Completeness: 1.0000
- Timeliness: 0.0443

### Catatan
Kolom `record_time` dibuat secara sintetis untuk kebutuhan visualisasi tren dan perhitungan timeliness karena dataset tidak memiliki timestamp pengukuran asli.

### Cara Menjalankan Dashboard
Buka terminal pada folder `dashboard`, lalu jalankan:

```bash
python -m streamlit run streamlit_app.py