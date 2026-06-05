import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 1. Konfigurasi Halaman & Tema
st.set_page_config(
    page_title="Analisis Konsumsi Listrik Rumah Tangga",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown("""
    <style>
    /* Mengubah warna background utama */
    .stApp {
        background-color: #05101a;
        color: white;
    }
    /* Mengubah warna sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0b1a27;
    }
    /* Mengatur style card metrik */
    .metric-card {
        background-color: #1a2d3d;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #2d4a63;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
    }
    .metric-label {
        font-size: 14px;
        color: #a1b0bc;
        margin-bottom: 5px;
    }
    .metric-icon {
        font-size: 30px;
        color: #f1c40f; /* Warna kuning seperti gambar */
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('household_daily_clean.csv', parse_dates=['datetime'])
    df.set_index('datetime', inplace=True)
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['day_of_week'] = df.index.dayofweek
    df['day_type'] = df['day_of_week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
    return df

try:
    df_daily = load_data()

    with st.sidebar:
        st.title("CC26-PRU468")
        st.write("---")
        
        st.subheader("Please Filter")
        tahun_pilihan = st.multiselect(
            "Select Year",
            options=[2006, 2007, 2008, 2009, 2010],
            default=[2006, 2007, 2008, 2009, 2010]
        )
        
        tipe_hari = st.radio(
            "Select Day Type",
            options=["All", "Weekday", "Weekend"]
        )
        
        st.write("---")

    # Filter Logic
    df_analysis = df_daily.loc['2006':'2010'].copy()
    df_filtered = df_analysis[df_analysis.index.year.isin(tahun_pilihan)]
    if tipe_hari != "All":
        df_filtered = df_filtered[df_filtered['day_type'] == tipe_hari]

    # --- HEADER ---
    st.title("Analisis Konsumsi Listrik Rumah Tangga")
    st.markdown(" ")
    st.write("---")


    avg_val = df_filtered['Global_active_power'].mean()
    max_val = df_filtered['Global_active_power'].max()
    sum_val = df_filtered['Global_active_power'].sum()
    weekday_mean = df_filtered.loc[df_filtered['day_type'] == 'Weekday', 'Global_active_power'].mean()
    weekend_mean = df_filtered.loc[df_filtered['day_type'] == 'Weekend', 'Global_active_power'].mean()
    pct_increase = ((weekend_mean - weekday_mean) / weekday_mean * 100) if pd.notna(weekday_mean) and weekday_mean else None
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown(f'<div class="metric-card"><div class="metric-icon">💰</div><div class="metric-label">Total Consumption (sum kW)</div><div class="metric-value">{sum_val:,.0f}</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-card"><div class="metric-icon">🔥</div><div class="metric-label">Peak (kW)</div><div class="metric-value">{max_val:.2f} kW</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="metric-card"><div class="metric-icon">📈</div><div class="metric-label">Average (kW)</div><div class="metric-value">{avg_val:.3f} kW</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="metric-card"><div class="metric-icon">📅</div><div class="metric-label">Years Selected</div><div class="metric-value">{len(tahun_pilihan)}</div></div>', unsafe_allow_html=True)

    st.write("###")

    # --- CHART SECTION (Disesuaikan dengan notebook) ---
    st.subheader("Visualisasi")

    fig1, ax1 = plt.subplots(figsize=(14, 5))
    fig1.patch.set_facecolor('#1a2d3d')
    ax1.set_facecolor('#1a2d3d')

    ax1.plot(df_filtered.index, df_filtered['Global_active_power'], alpha=0.3, label='Harian Asli', color='gray')
    df_filtered['Global_active_power'].rolling(window=7).mean().plot(
        ax=ax1,
        color='#ff4d4d',
        linewidth=2,
        label='Tren Mingguan (Moving Average)'
    )
    ax1.set_title('Tren Konsumsi Listrik Harian', color='white', fontsize=14)
    ax1.set_ylabel('Global Active Power (kW)', color='white')
    ax1.tick_params(colors='white')
    ax1.grid(True, alpha=0.3, color='#2d4a63')
    ax1.legend(facecolor='#1a2d3d', edgecolor='#2d4a63', labelcolor='white')
    st.pyplot(fig1, clear_figure=True)
    # Insight 1: seasonal insight (below trend)
    st.markdown(
        "**Insight:** Rumah tangga ini memiliki ketergantungan yang sangat tinggi pada musim. "
        "Lonjakan di musim dingin/awal tahun kemungkinan besar dipicu oleh penggunaan alat pemanas (heater) atau sistem penghangat air yang bekerja ekstra keras, "
        "sedangkan di pertengahan tahun konsumsi listrik jauh lebih hemat."
    )

    # Visual 2: Perbandingan rata-rata (stacked vertically)
    st.write("#### Perbandingan Rata-rata: Weekday vs Weekend")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    fig2.patch.set_facecolor('#1a2d3d')
    ax2.set_facecolor('#1a2d3d')

    avg_consumption = df_filtered.groupby('day_type')['Global_active_power'].mean().reindex(['Weekday', 'Weekend'])
    sns.barplot(
        x=avg_consumption.index,
        y=avg_consumption.values,
        hue=avg_consumption.index,
        palette='Set2',
        legend=False,
        ax=ax2,
    )

    for i, val in enumerate(avg_consumption.values):
        ax2.text(i, val + 0.02, f'{val:.3f} kW', ha='center', fontweight='bold', color='white')

    ax2.set_title('Perbandingan Rata-rata Konsumsi Listrik: Weekday vs Weekend', color='white', fontsize=12)
    ax2.set_ylabel('Rata-rata Global Active Power (kW)', color='white')
    ax2.tick_params(colors='white')
    ax2.grid(axis='y', color='#2d4a63', linestyle='--', alpha=0.7)
    st.pyplot(fig2, clear_figure=True)

    # Insight 2: weekday vs weekend
    if pct_increase is not None:
        st.markdown(
            f"**Insight:** Rata-rata pada weekday = {weekday_mean:.3f} kW, weekend = {weekend_mean:.3f} kW — "
            f"kenaikan sekitar {pct_increase:.2f}% di akhir pekan."
        )
    else:
        st.info("Insight weekday vs weekend belum bisa dihitung karena data weekday tidak tersedia pada filter saat ini.")

    # Visual 3: Distribusi (stacked vertically)
    st.write("#### Distribusi Konsumsi Harian")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    fig3.patch.set_facecolor('#1a2d3d')
    ax3.set_facecolor('#1a2d3d')

    sns.boxplot(
        data=df_filtered,
        x='day_type',
        y='Global_active_power',
        hue='day_type',
        palette='Set2',
        legend=False,
        ax=ax3,
    )

    ax3.set_title('Distribusi Konsumsi Listrik Harian: Weekday vs Weekend', color='white', fontsize=12)
    ax3.set_ylabel('Global Active Power (kW)', color='white')
    ax3.tick_params(colors='white')
    ax3.grid(axis='y', color='#2d4a63', linestyle='--', alpha=0.5)
    st.pyplot(fig3, clear_figure=True)

    # Insight 3: distribution
    q1 = df_filtered['Global_active_power'].quantile(0.25)
    q3 = df_filtered['Global_active_power'].quantile(0.75)
    iqr = q3 - q1
    st.markdown(
        f"**Insight:** Distribusi konsumsi harian memperlihatkan variasi yang cukup lebar dengan IQR sebesar {iqr:.3f} kW. "
        "Weekend cenderung bergeser lebih tinggi dan lebih mudah memunculkan lonjakan konsumsi."
    )

    # Kesimpulan
    st.header("Kesimpulan")
    st.markdown(
        "- Konsumsi listrik menunjukkan pola musiman: puncak di awal tahun, turun di pertengahan tahun.\n"
        "- Rata-rata konsumsi pada akhir pekan lebih tinggi dibanding hari kerja (weekday), meningkatkan risiko lonjakan beban.\n"
        "- Distribusi akhir pekan lebih variatif (IQR lebih besar) dan menampilkan lebih banyak outlier/puncak ekstrem.\n"
        "Rekomendasi: evaluasi penggunaan alat pemanas/alat besar pada akhir pekan untuk mengurangi puncak beban dan biaya."
    )

except Exception as e:
    st.error(f"Error: {e}")
