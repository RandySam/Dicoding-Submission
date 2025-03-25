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
    "Tren Polusi Harian",
])

if menu == "Tren Polusi Harian":
    min_date = df['datetime'].min()
    max_date = df['datetime'].max()

    start_date= st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=(min_date)
    )

    daily_df = df[df["datetime"].dt.date == start_date]

    pollutant_type = st.selectbox(
        label='Pilih Jenis Polutan',
        options = pollutants
    )

    fig, ax = plt.subplots(figsize=(12, 5))
    if pollutant_type == 'PM2.5':
        fig, ax = plt.subplots(figsize=(12, 5))
        if not daily_df.empty:
            st.subheader(f"Tren Polutan {pollutant_type} pada {start_date}")

            # Plot tren polutan dalam sehari      
            sns.lineplot(x=daily_df["datetime"].dt.hour, y=daily_df["PM2.5"], label="PM2.5", color="red")
            plt.xlabel("Jam")
            plt.ylabel(f"Konsentrasi {pollutant_type}")
            plt.title(f"Polutan {pollutant_type} pada {start_date} (Per Jam)")
            plt.xticks(range(0, 24))
            plt.legend()
            plt.grid(True)
        

    elif pollutant_type == 'PM10':
        if not daily_df.empty:
            st.subheader(f"Tren Polutan {pollutant_type} pada {start_date}")

            # Plot tren polutan dalam sehari      
            sns.lineplot(x=daily_df["datetime"].dt.hour, y=daily_df["PM10"], label="PM10", color="blue")
            plt.xlabel("Jam")
            plt.ylabel(f"Konsentrasi {pollutant_type}")
            plt.title(f"Polutan {pollutant_type} pada {start_date} (Per Jam)")
            plt.xticks(range(0, 24))
            plt.legend()
            plt.grid(True)
    
    
    elif pollutant_type == 'SO2':
        if not daily_df.empty:
            st.subheader(f"Tren Polutan {pollutant_type} pada {start_date}")

            # Plot tren polutan dalam sehari     
            sns.lineplot(x=daily_df["datetime"].dt.hour, y=daily_df["SO2"], label="SO2", color="green")
            plt.xlabel("Jam")
            plt.ylabel(f"Konsentrasi {pollutant_type}")
            plt.title(f"Polutan {pollutant_type} pada {start_date} (Per Jam)")
            plt.xticks(range(0, 24))
            plt.legend()
            plt.grid(True)
    
    
    elif pollutant_type == 'NO2':
        if not daily_df.empty:
            st.subheader(f"Tren Polutan {pollutant_type} pada {start_date}")

            # Plot tren polutan dalam sehari      
            sns.lineplot(x=daily_df["datetime"].dt.hour, y=daily_df["NO2"], label="NO2", color="purple")
            plt.xlabel("Jam")
            plt.ylabel(f"Konsentrasi {pollutant_type}")
            plt.title(f"Polutan {pollutant_type} pada {start_date} (Per Jam)")
            plt.xticks(range(0, 24))
            plt.legend()
            plt.grid(True)
            

    elif pollutant_type == 'CO':
        if not daily_df.empty:
            st.subheader(f"Tren Polutan {pollutant_type} pada {start_date}")

            # Plot tren polutan dalam sehari       
            sns.lineplot(x=daily_df["datetime"].dt.hour, y=daily_df["CO"], label="CO", color="orange")
            plt.xlabel("Jam")
            plt.ylabel(f"Konsentrasi {pollutant_type}")
            plt.title(f"Polutan {pollutant_type} pada {start_date} (Per Jam)")
            plt.xticks(range(0, 24))
            plt.legend()
            plt.grid(True)
st.pyplot(fig)