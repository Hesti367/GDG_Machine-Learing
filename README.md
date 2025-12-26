# Proyek Analisis Data: Bike Sharing Dataset

Proyek ini bertujuan untuk melakukan analisis data secara end-to-end menggunakan Bike Sharing Dataset. Analisis dilakukan untuk memahami pola, tren, serta faktor-faktor yang memengaruhi jumlah penyewaan sepeda, sehingga dapat menghasilkan insight yang mendukung pengambilan keputusan berbasis data.

## Informasi Proyek
- Nama: Hesti Sisila Wati  
- Dataset: Bike Sharing Dataset (UCI Machine Learning Repository)  
- Jenis Analisis: Exploratory Data Analysis (EDA) dan analisis pendukung menggunakan Machine Learning sederhana

## Deskripsi Dataset
Dataset Bike Sharing berisi data penyewaan sepeda harian yang mencakup informasi kondisi cuaca, suhu, kelembapan, kecepatan angin, hari kerja, serta jumlah penyewaan sepeda oleh pengguna terdaftar dan kasual.

## Pertanyaan Bisnis
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Apakah terdapat perbedaan jumlah penyewaan sepeda antara hari kerja dan akhir pekan?

## Tahapan Analisis
1. Data Wrangling  
   Dataset dikumpulkan dari UCI Machine Learning Repository dan dimuat ke dalam lingkungan analisis menggunakan Python. Data kemudian diperiksa untuk memastikan struktur dan formatnya sesuai.

2. Assessing Data  
   Dilakukan pengecekan terhadap missing value, duplikasi data, serta tipe data setiap kolom. Hasil pengecekan menunjukkan bahwa dataset bersih dan tidak memerlukan penanganan data yang kompleks.

3. Exploratory Data Analysis (EDA)  
   Analisis statistik deskriptif digunakan untuk memahami karakteristik data numerik seperti suhu, kelembapan, dan jumlah penyewaan sepeda. Selain itu, eksplorasi visual dilakukan untuk melihat pola dan hubungan antar variabel.

4. Visualisasi Data  
   Visualisasi digunakan untuk mendukung analisis, antara lain:
   - Perbandingan jumlah penyewaan sepeda berdasarkan kondisi cuaca
   - Perbandingan jumlah penyewaan antara hari kerja dan akhir pekan

5. Analisis Lanjutan (Opsional)  
   Model regresi linear sederhana diterapkan untuk melihat hubungan antara variabel lingkungan (suhu, kelembapan, dan kecepatan angin) terhadap jumlah penyewaan sepeda. Model ini digunakan sebagai pendukung insight, bukan sebagai fokus utama analisis.

## Insight Utama
- Kondisi cuaca memiliki pengaruh yang signifikan terhadap jumlah penyewaan sepeda, di mana cuaca cerah cenderung menghasilkan jumlah penyewaan yang lebih tinggi.
- Terdapat perbedaan pola penyewaan antara hari kerja dan akhir pekan.
- Faktor lingkungan seperti suhu dan kelembapan berkontribusi terhadap variasi jumlah penyewaan sepeda.

## Kesimpulan
Berdasarkan hasil analisis, dapat disimpulkan bahwa kondisi cuaca dan jenis hari (hari kerja atau akhir pekan) merupakan faktor penting yang memengaruhi jumlah penyewaan sepeda. Insight ini dapat digunakan sebagai dasar dalam perencanaan operasional dan pengambilan keputusan pada layanan bike sharing.

## Cara Menjalankan Proyek
1. Install seluruh dependensi: pip install -r requirements.txt
2. Jalankan notebook untuk melihat proses analisis: ML_Hesti_Sisila_Wati.ipynb
3. Jalankan dashboard Streamlit: streamlit run app.py
