from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Retail Sales Insights", page_icon="📊", layout="wide")
DATA_PATH = Path(__file__).parent / "dataset" / "supermarket_sales.csv"

@st.cache_data
def load_data():
    if not DATA_PATH.exists():
        return None
    df = pd.read_csv(DATA_PATH)
    df.columns = [c.strip() for c in df.columns]
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for c in ["Total", "Quantity", "Rating", "gross income", "cogs", "Unit price"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df.dropna(subset=["Date", "Total"])

st.title("Retail Sales Insights")
st.markdown("### 👤 **Ranti Junita Anisah** | NIM: 241051021")
st.caption("Dashboard interaktif untuk mengeksplorasi transaksi supermarket berdasarkan cabang, kategori produk, dan perilaku pelanggan.")

df = load_data()
if df is None:
    st.error("Dataset belum ditemukan. Letakkan file supermarket_sales.csv di folder dataset/. Lihat README.md untuk sumber dan petunjuk.")
    st.stop()

## Sidebar filters
st.sidebar.header("Filter Data")
cities = sorted(df["City"].dropna().unique())
selected_cities = st.sidebar.multiselect("Pilih kota", cities, default=cities)
products = sorted(df["Product line"].dropna().unique())
selected_products = st.sidebar.multiselect("Kategori produk", products, default=products)
date_min, date_max = df["Date"].min().date(), df["Date"].max().date()
date_range = st.sidebar.date_input("Rentang tanggal", value=(date_min, date_max), min_value=date_min, max_value=date_max)

# --- PROSES FILTER DATA (WAJIB ADA SEBELUM KPI) ---
filtered = df[df["City"].isin(selected_cities) & df["Product line"].isin(selected_products)].copy()
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    filtered = filtered[(filtered["Date"].dt.date >= date_range[0]) & (filtered["Date"].dt.date <= date_range[1])]

if filtered.empty:
    st.warning("Tidak ada data untuk kombinasi filter tersebut.")
    st.stop()
# ---------------------------------------------------

# KPI cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Transaksi", f"{len(filtered):,}")
c2.metric("Total Pendapatan", f"${filtered['Total'].sum():,.2f}")
c3.metric("Rata-rata Rating", f"{filtered['Rating'].mean():.2f}/10")
c4.metric("Total Unit Terjual", f"{int(filtered['Quantity'].sum()):,}")
# KPI cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Transaksi", f"{len(filtered):,}")
c2.metric("Total Pendapatan", f"${filtered['Total'].sum():,.2f}")
c3.metric("Rata-rata Rating", f"{filtered['Rating'].mean():.2f}/10")
c4.metric("Total Unit Terjual", f"{int(filtered['Quantity'].sum()):,}")

st.divider()
left, right = st.columns(2)
with left:
    monthly = filtered.assign(Month=filtered["Date"].dt.to_period("M").astype(str)).groupby("Month", as_index=False)["Total"].sum()
    st.subheader("Tren Pendapatan Bulanan")
    st.plotly_chart(px.line(monthly, x="Month", y="Total", markers=True, title="Pendapatan per bulan"), use_container_width=True)
with right:
    by_product = filtered.groupby("Product line", as_index=False)["Total"].sum().sort_values("Total", ascending=False)
    st.subheader("Pendapatan per Kategori")
    st.plotly_chart(px.bar(by_product, x="Product line", y="Total", color="Product line", title="Perbandingan kategori"), use_container_width=True)

left, right = st.columns(2)
with left:
    city_sales = filtered.groupby("City", as_index=False)["Total"].sum()
    st.subheader("Kontribusi Pendapatan per Kota")
    st.plotly_chart(px.pie(city_sales, names="City", values="Total", hole=.45), use_container_width=True)
with right:
    st.subheader("Hubungan Kuantitas dan Pendapatan")
    st.plotly_chart(px.scatter(filtered, x="Quantity", y="Total", color="Product line",
                               hover_data=["City", "Payment", "Rating"],
                               title="Kuantitas vs total transaksi"), use_container_width=True)

st.subheader("Metode Pembayaran")
payment = filtered["Payment"].value_counts().rename_axis("Payment").reset_index(name="Jumlah")
st.plotly_chart(px.bar(payment, x="Payment", y="Jumlah", color="Payment"), use_container_width=True)

# Data-driven observations
top_city = filtered.groupby("City")["Total"].sum().idxmax()
top_product = filtered.groupby("Product line")["Total"].sum().idxmax()
top_payment = filtered["Payment"].value_counts().idxmax()
st.subheader("Insight Sementara")
st.markdown(
    f"- Kota dengan pendapatan tertinggi pada filter aktif adalah **{top_city}**.\n"
    f"- Kategori dengan pendapatan tertinggi adalah **{top_product}**.\n"
    f"- Metode pembayaran yang paling sering digunakan adalah **{top_payment}**.\n"
    "- Temuan ini mengikuti filter yang sedang dipilih; ubah filter untuk membandingkan hasil."
)
with st.expander("Lihat data yang sedang dianalisis"):
    st.dataframe(filtered, use_container_width=True)
st.caption("Catatan: dataset ini merupakan data historis transaksi supermarket, bukan data real-time.")
