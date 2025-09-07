import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 3])  # Kolom kiri kecil, kolom kanan besar
with col1:
    st.image("app/assets/logo.png", width=150)  # Logo di kiri atas
with col2:
    st.write("")  # Kolom kanan kosong atau bisa isi konten lain

# === Page Setup ===
jasa_omc = st.Page(
    page="views/jasa_omc.py",
    title="Jasa Operasi Modifikasi Cuaca",
    icon="🌧️",
    default=True
)
kelayakan = st.Page(
    page="views/jasa_kelayakan.py",
    title="Jasa Studi Kelayakan Operasi Modifikasi Cuaca",
    icon="📑"
)
survey = st.Page(
    page="views/jasa_survey.py",
    title="Jasa Survey Lokasi & Commissioning",
    icon="📍"
)
omc_darat = st.Page(
    page="views/jasa_omc_darat.py",
    title="Jasa OMC Wahana Darat",
    icon="🚚"
)

supervisi = st.Page(
    page="views/supervisi.py",
    title="Supervisi Pelaksanaan OMC",
    icon="🛠️"
)

# === Navigation ===
pg = st.navigation({
    "Layanan Modifikasi Cuaca": [jasa_omc, kelayakan, survey, omc_darat,  supervisi]
})

# === Sidebar ===
with st.sidebar:
    st.markdown("### Informasi Modifikasi Cuaca")
    st.markdown("[Dasbor Historis Kegiatan OMC (2014-2025)](http://belgaman.infy.uk/omc/statistik)")
    st.markdown("[Sarana dan Prasarana Modifikasi Cuaca](https://link.bmkg.go.id/d-sm-)")

pg.run()
