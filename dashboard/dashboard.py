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
    st.header("Tren Polusi Berdasarkan Rentang Tahun dan Bulan")
    st.write("Menampilkan tren setiap polutan (PM2.5, PM10, SO2, NO2, CO) dari dataset.")

    df["year"] = df["datetime"].dt.year
    df["month"] = df["datetime"].dt.month

    tahun_tersedia = sorted(df["year"].unique())
    tahun_awal, tahun_akhir = st.select_slider(
        label="Pilih Rentang Tahun",
        options=tahun_tersedia,
        value=(tahun_tersedia[0], tahun_tersedia[-1])
    )

    # Pilihan bulan
    bulan_dict = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
        7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    bulan_terpilih = st.multiselect(
        "Pilih Bulan",
        options=range(1, 13),
        format_func=lambda x: bulan_dict[x],
        default=list(range(1, 13))
    )

    # Filter dataframe berdasarkan pilihan
    filtered_df = df[
        (df["year"] >= tahun_awal) & (df["year"] <= tahun_akhir) &
        (df["month"].isin(bulan_terpilih))
    ]

    # Agregasi rata-rata polusi
    monthly_avg = filtered_df.groupby(["year", "month"])[["PM2.5", "PM10", "SO2", "NO2", "CO"]].mean().reset_index()

    pollutant = st.selectbox("Pilih Polutan", ["PM2.5", "PM10", "SO2", "NO2", "CO"])

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=monthly_avg, x="month", y=pollutant, hue="year", marker="o", palette="tab10", ax=ax)
    ax.set_title(f"Tren {pollutant} per Bulan ({tahun_awal} - {tahun_akhir})")
    ax.set_xlabel("Bulan")
    ax.set_ylabel(f"Konsentrasi {pollutant}")
    ax.set_xticks(range(1, 13))
    ax.grid(True)
    ax.set_xticklabels([bulan_dict[i] for i in range(1, 13)], rotation=45)
    st.pyplot(fig)
    st.markdown("""
    ### Kesimpulan
    Dari analisis tren tahunan, terlihat bahwa polusi udara mengalami peningkatan 
    serta penurunan yang berarti bersifat fluktuatif sepanjang tahun.

    Jika tren polusi meningkat, ini menunjukkan bahwa kualitas udara semakin 
    memburuk, kemungkinan yang menyebabkan peningkatan polusi ini adalah 
    peningkatan jumlah kendaraan, aktivitas industri, atau faktor lingkungan lainnya.

    Jika tren polusi menurun, ini bisa menjadi indikasi bahwa kebijakan pengendalian 
    polusi berhasil diterapkan. Berikut ini adalah penjelasan mengenai tren dari 
    setiap polutan.

    1. PM2.5 dan PM10 menunjukkan penurunan yang konsisten dari tahun ke tahun, 
    terutama setelah tahun 2014. Hal ini menunjukkan adanya perbaikan kualitas 
    udara secara bertahap, yang kemungkinan besar akibat regulasi lingkungan yang 
    lebih ketat dan upaya pengurangan emisi oleh pemerintah.
    
    2. Konsentrasi SO2 mengalami penurunan tajam dari tahun ke tahun, terutama 
    setelah 2013 di mana ini kemungkinan menunjukan keberhasilan kebijakan 
    pemerintah dalam mengurangi penggunaan bahan bakar berbasis sulfur, 
    seperti batu bara.

    3. Konsentrasi NO2 sedikit fluktuatif namun cenderung stabil atau menurun 
    secara perlahan.

    4. Konsentrasi CO menunjukkan penurunan bertahap, yang kemungkinan disebabkan 
    dengan perbaikan efisiensi kendaraan dan pengurangan emisi industri.

    5. Polutan cenderung lebih tinggi pada musim dingin (Desember-Februari), 
    zat polutan seperti PM2.5, PM10, dan CO meningkat disebabkan pemanasan 
    berbasis batu bara, peningkatan aktivitas transportasi, dan fenomena inversi
    suhu yang menjebak polusi di permukaan tanah.

    6. Konsentrasi polutan menurun pada musim panas (Juni-Agustus) yang disebabkan 
    karena curah hujan yang lebih tinggi dan peningkatan sirkulasi atmosfer, 
    yang membantu menyebarkan atau membersihkan polusi udara.
    
    Rata-rata konsentrasi polutan udara di kota Beijing mengalami penurunan 
    signifikan secara tahunan, terutama PM2.5, PM10, dan SO2, 
    dari tahun 2013 hingga 2017. Secara musiman, tingkat polusi tertinggi terjadi 
    pada musim dingin, sedangkan tingkat terendah terjadi pada musim panas, 
    menandakan pengaruh besar dari faktor cuaca dan aktivitas manusia terhadap 
    kualitas udara.
    """)