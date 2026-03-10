import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Smart Agriculture Dashboard", layout="wide")

base_dir = Path(__file__).resolve().parents[1]
file_path = base_dir / "outputs" / "cleaned_data.csv"

df = pd.read_csv(file_path)
df["record_time"] = pd.to_datetime(df["record_time"])

st.title("Smart Agriculture Dashboard")
st.write("Dashboard monitoring sensor pertanian berbasis dataset Smart Agriculture")

# =========================
# PILIH SENSOR UNTUK TREND
# =========================
sensor = st.selectbox("Pilih sensor untuk time series", ["moi", "temp", "humidity"])

# Biar grafik tidak terlalu padat, agregasi per hari
trend_df = (
    df.set_index("record_time")[sensor]
    .resample("D")
    .mean()
    .reset_index()
)

st.subheader("1. Time Series Trend")
fig_line = px.line(
    trend_df,
    x="record_time",
    y=sensor,
    title=f"Rata-rata Harian {sensor.upper()}",
)
st.plotly_chart(fig_line, use_container_width=True)

# =========================
# GAUGE METER
# =========================
st.subheader("2. Gauge Meter")

latest_humidity = float(df["humidity"].iloc[-1])

fig_gauge = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=latest_humidity,
        title={"text": "Humidity Saat Ini"},
        gauge={
            "axis": {"range": [0, 100]},
            "steps": [
                {"range": [0, 30], "color": "red"},
                {"range": [30, 60], "color": "yellow"},
                {"range": [60, 100], "color": "green"},
            ],
        },
    )
)
st.plotly_chart(fig_gauge, use_container_width=True)

# =========================
# HEATMAP KORELASI
# =========================
st.subheader("3. Heatmap Korelasi")

corr_cols = ["moi", "temp", "humidity", "result"]
corr = df[corr_cols].corr()

fig_heat = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Korelasi Antar Sensor"
)
st.plotly_chart(fig_heat, use_container_width=True)

# =========================
# ALERT SYSTEM
# =========================
st.subheader("4. Alert System")

threshold = st.slider("Tentukan threshold minimum MOI", 0, 100, 30)

latest_moi = float(df["moi"].iloc[-1])

if latest_moi < threshold:
    st.error(f"ALERT: MOI saat ini {latest_moi:.2f}, di bawah threshold {threshold}")
else:
    st.success(f"MOI saat ini {latest_moi:.2f}, masih aman di atas threshold {threshold}")

# =========================
# TABEL PREVIEW
# =========================
st.subheader("Preview Data")
st.dataframe(df.head(20))