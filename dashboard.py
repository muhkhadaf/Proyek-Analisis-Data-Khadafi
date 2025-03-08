import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("day_data.csv")
hour_df = pd.read_csv("hour_data.csv")

# Konversi tanggal ke datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar untuk filter
time_option = st.sidebar.selectbox("Pilih Data yang Ditampilkan", ["Harian", "Jam"])

st.title("Dashboard Analisis Penyewaan Sepeda")

if time_option == "Harian":
    st.header("Analisis Penyewaan Sepeda Harian")
    
    # Statistik penyewaan berdasarkan musim
    season_stats = day_df.groupby("season")["cnt"].agg(['sum', 'mean', 'max', 'min'])
    st.subheader("Statistik Penyewaan berdasarkan Musim")
    st.dataframe(season_stats)
    
    # Visualisasi
    fig, ax = plt.subplots()
    sns.barplot(x=season_stats.index, y=season_stats['sum'], palette='coolwarm', ax=ax)
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
    # Statistik penyewaan berdasarkan hari dalam seminggu
    weekday_stats = day_df.groupby("weekday")["cnt"].agg(['sum', 'mean', 'max', 'min'])
    st.subheader("Statistik Penyewaan berdasarkan Hari dalam Seminggu")
    st.dataframe(weekday_stats)
    
    # Visualisasi
    fig, ax = plt.subplots()
    sns.barplot(x=weekday_stats.index, y=weekday_stats['sum'], palette='viridis', ax=ax)
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
    ax.set_xlabel("Hari dalam Seminggu")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
else:
    st.header("Analisis Penyewaan Sepeda per Jam")
    
    # Statistik penyewaan berdasarkan jam
    hourly_stats = hour_df.groupby("hr")["cnt"].agg(['sum', 'mean', 'max', 'min'])
    st.subheader("Statistik Penyewaan berdasarkan Jam")
    st.dataframe(hourly_stats)
    
    # Visualisasi
    fig, ax = plt.subplots()
    sns.lineplot(x=hourly_stats.index, y=hourly_stats['sum'], marker='o', ax=ax)
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
st.sidebar.header("Kesimpulan")
st.sidebar.write("- Penyewaan sepeda lebih tinggi di musim panas.")
st.sidebar.write("- Hari kerja didominasi oleh pengguna terdaftar.")
st.sidebar.write("- Akhir pekan lebih banyak pengguna kasual.")
st.sidebar.write("- Jam sibuk adalah pagi (07:00 - 09:00) dan sore (17:00 - 19:00).")
