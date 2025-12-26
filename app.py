import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Awal
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="centered"
)

sns.set(style="whitegrid")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    return df

df = load_data()

# Judul 
st.title("🚲 Bike Sharing Data Analysis Dashboard")
st.write(
    "Dashboard ini menampilkan hasil Exploratory Data Analysis (EDA) "
    "pada Bike Sharing Dataset untuk memahami pola penyewaan sepeda."
)

# Ringkasan Data
st.subheader("Ringkasan Dataset")
st.write(f"Jumlah data: **{df.shape[0]} baris** dan **{df.shape[1]} kolom**")
st.dataframe(df.head())

# Pertanyaan Bisnis 1
st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")

fig1, ax1 = plt.subplots()
sns.boxplot(x="weathersit", y="cnt", data=df, ax=ax1)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Penyewaan Sepeda")
ax1.set_title("Jumlah Penyewaan Sepeda berdasarkan Kondisi Cuaca")

st.pyplot(fig1)

st.markdown(
    """
**Insight:**  
Jumlah penyewaan sepeda cenderung lebih tinggi pada kondisi cuaca cerah.
Sebaliknya, saat cuaca memburuk, jumlah penyewaan mengalami penurunan.
"""
)

# Pertanyaan Bisnis 2
st.subheader("Perbandingan Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan")

fig2, ax2 = plt.subplots()
sns.barplot(x="workingday", y="cnt", data=df, ax=ax2)
ax2.set_xlabel("Jenis Hari (0 = Libur, 1 = Hari Kerja)")
ax2.set_ylabel("Jumlah Penyewaan Sepeda")
ax2.set_title("Perbandingan Penyewaan Sepeda")

st.pyplot(fig2)

st.markdown(
    """
**Insight:**  
Jumlah penyewaan sepeda pada hari kerja relatif lebih stabil dan cenderung
lebih tinggi dibandingkan akhir pekan.
"""
)

# Kesimpulan
st.subheader("Kesimpulan")
st.markdown(
    """
Berdasarkan analisis yang dilakukan, kondisi cuaca dan jenis hari
merupakan faktor penting yang memengaruhi jumlah penyewaan sepeda.
Hasil ini dapat digunakan sebagai dasar pengambilan keputusan
dalam pengelolaan layanan bike sharing.
"""
)
