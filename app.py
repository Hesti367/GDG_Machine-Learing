import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi visual
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (8, 5)

# Judul Dashboard
st.title("Analisis Data Bike Sharing")
st.subheader("Hesti Sisila Wati")

st.markdown("""
**Pertanyaan Bisnis**
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Apakah terdapat perbedaan jumlah penyewaan sepeda antara hari kerja dan akhir pekan?
""")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    df.drop(columns=['instant'], inplace=True)
    return df

df = load_data()
st.success("Dataset berhasil dimuat")

# Preview Data
st.subheader("📄 Preview Dataset")
st.dataframe(df.head())

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.dataframe(df[['temp', 'hum', 'windspeed', 'cnt']].describe())

# Visualisasi 1: Cuaca vs Penyewaan
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")

fig1, ax1 = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=df, ax=ax1)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig1)

st.markdown("""
**Insight**  
Jumlah penyewaan sepeda paling tinggi terjadi saat kondisi cuaca cerah.  
Ketika cuaca memburuk seperti hujan atau salju, jumlah penyewaan menurun cukup signifikan.
""")

# Visualisasi 2: Hari Kerja vs Akhir Pekan
st.subheader("Hari Kerja vs Akhir Pekan")

fig2, ax2 = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=df, ax=ax2)
ax2.set_xlabel("Hari Kerja (1 = Ya, 0 = Tidak)")
ax2.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig2)

st.markdown("""
**Insight**  
Penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan akhir pekan.  
Hal ini menunjukkan sepeda banyak digunakan sebagai sarana transportasi harian.
""")

# Visualisasi Tambahan: Suhu vs Penyewaan
st.subheader("Hubungan Suhu dengan Jumlah Penyewaan")

fig3, ax3 = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=df, ax=ax3)
ax3.set_xlabel("Suhu")
ax3.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig3)

st.markdown("""
**Insight**  
Semakin tinggi suhu, jumlah penyewaan sepeda cenderung meningkat.
""")

# Kesimpulan
st.subheader("Kesimpulan")

st.markdown("""
- Kondisi cuaca berpengaruh signifikan terhadap jumlah penyewaan sepeda.
- Penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan akhir pekan.
- Faktor lingkungan seperti suhu turut memengaruhi minat masyarakat dalam menggunakan sepeda.
""")
