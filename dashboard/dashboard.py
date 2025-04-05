import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("dashboard/airquality.csv", parse_dates=['datetime'])
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO']

# Title
st.title("Dashboard Kualitas Udara Kota Beijing")

# Sidebar
st.sidebar.header("Navigasi")

menu = st.sidebar.radio("Pilih Visualisasi: ", [
    "Korelasi Polutan dengan Temperatur Suhu",
    "Tren Polusi"
])

if menu == "Korelasi Polutan dengan Temperatur Suhu":
    st.header("Korelasi Polutan dengan Temperatur Suhu")
    st.write("Menampilkan korelasi antara polutan (PM2.5, PM10, SO2, NO2, CO) dengan Temperatur Suhu.")
    correlation_matrix = df[["PM2.5", "PM10", "SO2", "NO2", "CO", "TEMP"]].corr()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    ax.set_title("Korelasi Polutan dengan Suhu")
    st.pyplot(fig)

    st.markdown("""
    ### Kesimpulan
    ##### Hubungan Antar Polutan
    1. **PM2.5 dan PM10** memiliki korelasi sangat tinggi (**0.89**) yang menunjukkan bahwa jika kadar PM2.5 meningkat, PM10 juga cenderung meningkat.  
    2. **CO** berkorelasi kuat dengan PM2.5 (**0.79**) dan PM10 (**0.71**) karena berasal dari sumber serupa seperti kendaraan dan industri.  
    3. **NO2** berkorelasi cukup tinggi dengan PM2.5 (**0.66**) dan PM10 (**0.66**) yang juga berasal dari emisi kendaraan.  
    4. **SO2** memiliki korelasi sedang dengan PM2.5 (**0.51**) dan PM10 (**0.50**) karena kemungkinan berasal dari sumber emisi yang berbeda.
    
    ##### Pengaruh Suhu (TEMP) terhadap Polutan
    Suhu berkorelasi negatif dengan semua polutan yang dibuktikan dengan korelasi setiap polutan berikut ini:

    PM2.5 (-0.11) dan PM10 (-0.08) 

    SO2 (-0.36), NO2 (-0.28), dan CO (-0.32) 

    Dari korelasi tersebut dapat disimpulkan ketika suhu meningkat, kadar polutan cenderung menurun.
    Hal tersebut dapat terjadi karena suhu yang lebih tinggi sering dikaitkan dengan atmosfer yang lebih aktif, sehingga polutan lebih cepat terdilusi atau terdorong ke lapisan atmosfer yang lebih tinggi.                
    """)

elif menu == "Tren Polusi":
    st.header("Korelasi Polutan dengan Temperatur Suhu")
    st.write("Menampilkan tren setiap polutan (PM2.5, PM10, SO2, NO2, CO) dari dataset.")