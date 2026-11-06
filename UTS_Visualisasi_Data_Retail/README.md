# Retail Sales Performance & Customer Insights

**Nama:** Ranti Junita Anisah  
**NIM:** 241051021  
**Mata Kuliah:** Visualisasi Data  
**Universitas:** Universitas Dirgantara Marsekal Suryadarma (UNSURYA)

Project UTS Visualisasi Data menggunakan Python, Pandas, Plotly, dan Streamlit untuk mengeksplorasi data penjualan supermarket.

## 🔗 Tautan Penting
- **Live Dashboard:** [Isi dengan link Streamlit Cloud Anda nanti, contoh: https://ranti-retail.streamlit.app]
- **Dataset Kaggle:** [https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)

## 📊 Latar Belakang & Key Insights
Dataset ini berisi 1.000 transaksi historis dari supermarket di Myanmar. Dashboard ini dibuat untuk membantu manajemen memahami tren penjualan, preferensi pelanggan, dan performa cabang.

**Wawasan Utama (Key Insights):**
1. **Kota Yangon** secara konsisten menyumbang total pendapatan tertinggi dibandingkan Mandalay dan Naypyitaw.
2. **Kategori Food and Beverages** dan **Electronic Accessories** menjadi dua kategori produk dengan penjualan tertinggi.
3. Pelanggan lebih banyak menggunakan metode pembayaran **Ewallet** dan **Cash** dibandingkan Credit Card.
4. Terdapat korelasi positif antara jumlah kuantitas barang yang dibeli dengan total transaksi (semakin banyak barang, semakin besar total belanja).
5. Tingkat kepuasan pelanggan (Rating) relatif stabil di kisaran 6.9 - 7.0 dari skala 10, menunjukkan pengalaman belanja yang cukup baik.

## 🚀 Fitur Dashboard
- **KPI Cards:** 4 indikator utama (Total Transaksi, Total Pendapatan, Rata-rata Rating, Total Unit Terjual).
- **Visualisasi Variatif:** Line Chart (tren bulanan), Bar Chart (perbandingan kategori), Donut Chart (kontribusi kota), Scatter Plot (korelasi kuantitas vs total), dan Bar Chart (metode pembayaran).
- **Interaktivitas:** Filter dinamis berdasarkan Kota, Kategori Produk, dan Rentang Tanggal.
- **Storytelling:** Insight otomatis yang menyesuaikan dengan filter yang dipilih pengguna.

## 💻 Panduan Menjalankan Kode Secara Lokal
Jika ingin menjalankan proyek ini di komputer lokal:
1. Clone repositori ini atau unduh file ZIP-nya.
2. Buka terminal/Command Prompt, lalu masuk ke folder proyek.
3. Install semua kebutuhan library:
   ```bash
   pip install -r requirements.txt