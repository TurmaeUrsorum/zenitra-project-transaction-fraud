# Deteksi Fraud dan Segmentasi Pengguna Transaksi Nasabah Bank

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)
![NumPy](https://img.shields.io/badge/numpy-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EB5E28?logo=xgboost&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-11557C?logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/seaborn-4C72B0)

![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)


## 📖 Deskripsi

### **Masalah Bisnis**

Bank memiliki jumlah nasabah dengan pola transaksi yang sangat bervariasi. Tanpa analisis mendalam, sulit untuk:

* Mengidentifikasi kelompok nasabah berdasarkan perilaku transaksi.
* Menawarkan produk perbankan secara tepat sasaran.
* Menekan risiko churn dan meningkatkan loyalitas.
* Mendeteksi aktivitas transaksi abnormal sedini mungkin.

### **Pendekatan Model**

Solusi yang digunakan terdiri dari dua tahap utama:

| Tujuan                                             | Algoritma              | Output                                            |
| -------------------------------------------------- | ---------------------- | ------------------------------------------------- |
| Segmentasi pengguna berdasarkan perilaku transaksi | **K-Means Clustering** | Kelompok/segmen nasabah dengan karakteristik unik |
| Deteksi potensi transaksi fraud                    | **Isolation Forest**   | Skor anomali & label apakah transaksi dicurigai   |

📌 Alur pemodelan:

1. **K-Means** mengelompokkan nasabah berdasarkan fitur seperti frekuensi transaksi, nominal, jenis transaksi, lokasi, merchant, dll.
2. **Isolation Forest** memindai transaksi dan memberi skor anomali untuk mendeteksi aktivitas mencurigakan secara otomatis.
3. **Hasil deteksi fraud dianalisis per segmentasi** untuk mengetahui tipe nasabah mana yang berisiko lebih tinggi.

### **Nilai Tambah**

* **Personalisasi produk finansial** berdasarkan segmen.
* **Targeted marketing** pada cluster nasabah tertentu.
* **Peningkatan risk management** melalui fraud monitoring otomatis.
* **Customer retention** berdasarkan insight perilaku tiap segmen.
* **Business decision support** melalui dashboard komposisi segmen + tingkat risiko fraud.

### **Target Audience**

* Tim Data & Analytics
* Tim Marketing
* Tim Product Banking
* Manajemen Bank
* (Opsional) Tim Risk/Fraud

## **🎯 Business Understanding**

### **Problem Statement**

Bank memiliki data transaksi nasabah yang sangat besar dan beragam, namun belum dimanfaatkan secara optimal untuk memahami perilaku dan risiko nasabah. Tanpa analisis mendalam, bank kesulitan menentukan strategi pemasaran yang tepat, menawarkan produk yang relevan, serta mendeteksi aktivitas transaksi yang tidak wajar secara dini. Diperlukan sebuah model yang mampu:

1. mengelompokkan nasabah berdasarkan pola transaksi mereka untuk segmentasi bisnis, dan
2. mengidentifikasi transaksi abnormal sebagai indikasi potensi fraud.

Dengan demikian, keputusan bisnis dapat dibuat lebih cepat, tepat, dan berbasis data.

### **Objectives**

* [ ] **Tujuan 1:** Menghasilkan label segmen nasabah menggunakan model **K-Means Clustering** berdasarkan pola transaksi (frekuensi, nominal, kategori transaksi, merchant, lokasi, dll.).
* [ ] **Tujuan 2:** Mengidentifikasi transaksi abnormal menggunakan **Isolation Forest** untuk mendeteksi potensi fraud secara otomatis.
* [ ] **Tujuan 3:** Mengevaluasi fitur-fitur transaksi yang paling berpengaruh dalam pembentukan segmen dan skor anomali.
* [ ] **Tujuan 4:** Menyediakan dashboard/visualisasi untuk memonitor:

  * Distribusi segmen nasabah,
  * Skor anomali dan indikator risiko fraud,
  * Perubahan perilaku transaksi dari waktu ke waktu.

### **Success Metrics**

#### **Bisnis Metrics**

##### **1. Peningkatan efektivitas targeting**

* Response rate kampanye naik **> 10%** dengan personalisasi berdasarkan segmen.
* Atau peningkatan konversi ke produk tertentu pada segmen prioritas minimal **> 8%**.

##### **2. Efisiensi biaya marketing**

* Pengurangan biaya promosi karena targeting lebih presisi → **> 15%** efisiensi.

##### **3. Peningkatan engagement dan retensi**

* Frekuensi transaksi naik **> 5%** pada segmen yang diberikan campaign.
* Atau peningkatan rata-rata saldo/aktivitas bagi segmen high-value.

##### **4. Peningkatan efektivitas deteksi risiko**

* Model fraud detection mampu menangkap transaksi abnormal dengan **> 90%** precision (false positive rendah).
* Waktu identifikasi transaksi mencurigakan menurun secara signifikan dibanding manual checking.

## **🗂️ Dataset**
### **Sumber Dataset**
 **Primary Source**: [Bank Transaction Dataset](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)

### Dataset Overview
```python
Shape: (2512, 16)
Missing Values: 0%
Duplicate Rows: 0%
```

### **Dataset Description**
| Feature                 | Type    | Description                              | Missing Values |
| ----------------------- | ------- | ---------------------------------------- | -------------- |
| TransactionID           | object  | ID unik transaksi                        | 0%             |
| AccountID               | object  | ID nasabah                               | 0%             |
| TransactionAmount       | float64 | Nominal transaksi                        | 0%             |
| TransactionDate         | object  | Tanggal transaksi                        | 0%             |
| TransactionType         | object  | Jenis transaksi (misal: debit/kredit)    | 0%             |
| Location                | object  | Lokasi transaksi                         | 0%             |
| DeviceID                | object  | ID perangkat yang digunakan              | 0%             |
| IP Address              | object  | Alamat IP saat transaksi                 | 0%             |
| MerchantID              | object  | ID merchant                              | 0%             |
| Channel                 | object  | Kanal transaksi (ATM, mobile, web, dll.) | 0%             |
| CustomerAge             | int64   | Usia nasabah                             | 0%             |
| CustomerOccupation      | object  | Pekerjaan nasabah                        | 0%             |
| TransactionDuration     | int64   | Durasi proses transaksi                  | 0%             |
| LoginAttempts           | int64   | Jumlah percobaan login sebelum transaksi | 0%             |
| AccountBalance          | float64 | Saldo rekening saat transaksi            | 0%             |
| PreviousTransactionDate | object  | Tanggal transaksi sebelumnya             | 0%             |
| Cluster                 | int64   | Label cluster hasil unsupervised model   | 0%             |


## 🏗️ Struktur Projek
```
data_science_project/
├── conf/                          # Configuration data catalog
│   ├── base/                      # Base configuration
│   │   ├── catalog.yml
│   │   ├── parameters_data_EDA.yml
│   │   └── parameters_model_training.yml
│   ├── dev/                       # Development configuration
│   │   ├── catalog.yml
│   │   ├── parameters_data_EDA.yml
│   │   └── parameters_model_training.yml
│   └── prod/                      # Production configuration
│       ├── catalog.yml
│       ├── parameters_data_EDA.yml
│       └── parameters_model_training.yml
├── data/                          # Data storage
│   ├── 01_raw/                    # data asli atau mentah
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── external_data.csv
│   ├── 02_Intermediate/           # data yang sudah clean
│   │   ├── train_cleaned.csv
│   │   ├── test_cleaned.csv
│   │   └── feature_engineered.csv
│   ├── 03_primary/                # data yang sudah siap untuk preproses
│   └── 04_feature/                # data yang dihasilkan dari feature engineering
|   └── 05_model_input/            # data yang siap untuk model training
│
├── docs/                          # Documentation
|
├── models/                        # Model storage
|                      
├── notebooks/                     # Jupyter notebooks
│   ├── 01_eda.ipynb               # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_interpretation.ipynb
│
├── outputs/                       # Report storage
│
├── src/
│   ├── project_name/
│   │   ├── __init__.py
│   │   ├── pipelines/
│   │   │   ├── data_cleaning/     # pipeline data cleaning/
│   │   │   │   ├── nodes.py       # preprocess, cleaning
│   │   │   │   └── pipeline.py
│   │   │   ├── data_EDA/
│   │   │   │   ├── nodes.py       # EDA, feature engineering
│   │   │   │   └── pipeline.py
│   │   │   ├── data_evaluation/
│   │   │   │   ├── nodes.py       # model evaluation
│   │   │   │   └── pipeline.py
│   │   │   └── data_modeling/
│   │   │   |   ├── nodes.py       # model training
│   │   │   |   └── pipeline.py
│   │   │   └── data_preproses/
│   │   │       ├── nodes.py       # data preproses
│   │   │       └── pipeline.py
│   │   │
│   │   ├── __main__.py            # Project entry point
│   │   └── pipeline_registry.py   # Pipeline registry
│   │   └── setings.py             # Project settings
│   │  
│   │   
│   │       
│   │       
│   │       
│   │
│   └── setup.py                   # Project metadata
│
├── tests/                         # Unit tests
│   ├── pipelines/
|   │   ├── data_cleaning/
│   │   ├── data_EDA/
│   │   ├── data_evaluation/
│   │   ├── data_modeling/
│   │   └── data_preproses/
│   ├── conftest.py
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
│
├── environment.yml                # Conda environment
├── pyproject.toml                 # Project configuration
├── setup.py                       # Package setup
├── .env.example                   # Environment variables template
├── .gitignore
└── README.md
```

## ⚙️ Instalasi dan Setup

### Prerequisites
- Python 3.8+
- pip atau conda (direkomendasikan conda)

### 1. Clone Repository
```bash
git clone https://github.com/TurmaeUrsorum/zenitra-project-transaction-fraud
```

### 2. Setup Environment

**Option A: menggunakan conda (sangat direkomendasikan)**
```bash
conda env create -f environment.yml
conda activate ds-project
```

**Option B: menggunakan pip**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows

# harus convert sendiri ke requirements.txt
pip install -r requirements.txt
```

## 🚀 Penggunaan

### Quick Start

1. Clone repository
2. Setup environment
3. Jalankan `kedro run`

```bash
# semua pipeline dijalankan
kedro run
# run kedro dengan parallel
kedro run --runner ParallelRunner
# run kedro spesifik pipeline
kedro run --pipeline data_EDA
```
## 🔬 Metodologi

### Data Preprocessing
- **Handling Missing Values**: [Technique yang digunakan]
- **Outlier Treatment**: [Method untuk handle outliers]
- **Encoding**: [Label encoding, One-hot encoding, etc.]
- **Scaling**: [Standardization/Normalization method]

### Feature Engineering
- **Created Features**: [feature yang dibuat amount to balance ratio dan multiple login flag ]

## License

```
MIT License

Copyright (c) 2025 TurmaeUrsorum

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```