import pandas as pd
import math
def safe_subtract(total, *args):
    if total is None:
        return 0
    total_value = total
    for a in args:
        total_value -= a if a is not None else 0
    return total_value

def safe_divide(a, b):
    if a is None or b in (None, 0):
        return 0
    return a / b

# ========================================================== #
# ==================== Fungsi Universal ==================== #
# ========================================================== #
harga_sewa_per_jam = 70000000

def harga_sewa_pesawat(input_operasi, jh_keseluruhan, harga_sewa_per_jam):
    if input_operasi == "Kondisi Tertentu/Khusus (Operasi 24 Jam)":
        jam_terbang = 6
    else:
        jam_terbang = 3
    jumlah_alutsista_pesawat = jam_terbang * jh_keseluruhan * harga_sewa_per_jam
    return jam_terbang, jumlah_alutsista_pesawat


# Fungsi Biaya Uang Harian
def hitung_uang_harian(uang_harian: int, jumlah_hari: int, jumlah_personel: int) -> int:
    return jumlah_hari * jumlah_personel * uang_harian

# Fungsi Biaya Penginapan
def biaya_penginapan(harga_penginapan, jumlah_hari_penginapan, jumlah_personel):
    jumlah_biaya_penginapan = jumlah_hari_penginapan * jumlah_personel * harga_penginapan
    # print(f"jumlah personel: {jumlah_personel}")
    # print(f"jumlah hari penginapan: {jumlah_hari_penginapan}")
    # print(f"jumlah harga penginapan: {harga_penginapan}")
    # print(f"Jumlah biaya penginapan untuk {provinsi}: Rp {jumlah_biaya_penginapan:,}")
    return jumlah_biaya_penginapan

# Fungsi Biaya Tiket
def biaya_tiket_pelaksanaan(biaya_tiket, pp, jumlah_personel):
    jumlah_biaya_tiket_pelaksanaan = jumlah_personel * pp * biaya_tiket
    # print(f"Jumlah biaya tiket untuk {provinsi}: Rp {jumlah_biaya_tiket_pelaksanaan:,}")
    return jumlah_biaya_tiket_pelaksanaan

# Fungsi Biaya Taxi
def biaya_taksi(jumlah_personel: int, harga_taksi_flat: int) -> int:
    return jumlah_personel * harga_taksi_flat

# Fungsi Pelaporan
def pencetakan_dan_penggandaan_laporan(jumlah_paket, jumlah_kali_paket, harga_pencetakan_dan_penggandaan_laporan):
    return jumlah_paket * jumlah_kali_paket * harga_pencetakan_dan_penggandaan_laporan

# ========================================================= #
# ==================== Fungsi Jasa OMC ==================== #
# ========================================================= #
# Fungsi Biaya Bahan Semai
def harga_bahan_semai_NaCl(jumlah_kg: float, harga_per_kg: float, jh_keseluruhan: int) -> float:
    total_harga = jumlah_kg * harga_per_kg * jh_keseluruhan
    return total_harga

# Fungsi Biaya Penggantian Avtur Pesawat
def penggantian_avtur_pesawat(jumlah_liter, harga_avtur_per_liter, jam_mobdemob):
    jumlah_penggantian_avtur = jumlah_liter * harga_avtur_per_liter * jam_mobdemob
    # print(f"Total biaya penggantian avtur Mob - Demob: Rp {jumlah_penggantian_avtur:,}")
    return jumlah_penggantian_avtur

# Fungsi Hitung Biaya Alutsista Pesawat Selama Operasi
def alutsista_pesawat_selama_operasi(input_operasi, jh_keseluruhan, jumlah_liter, harga_avtur_per_liter):
    if input_operasi == "Kondisi Tertentu/Khusus (Operasi 24 Jam)":
        jam_terbang = 6
    else:
        jam_terbang = 3
    jumlah_alutsista_pesawat = jam_terbang * jh_keseluruhan * jumlah_liter * harga_avtur_per_liter
    return jam_terbang, jumlah_alutsista_pesawat

# Biaya Modifikasi dan Inspeksi Pesawat
def modifikasi_dan_inspeksi_pesawat(harga_paket_modifikasi_inspeksi, jumlah_paket, jumlah_kali_paket): 
    return harga_paket_modifikasi_inspeksi * jumlah_paket * jumlah_kali_paket

# Fungsi Biaya Sewa Kendaraan
def biaya_sewa_kendaraan(jh_keseluruhan, jumlah_unit_kendaraan_keseluruhan, sewa_kendaraan):
    total_biaya_sewa_kendaraan = jh_keseluruhan * jumlah_unit_kendaraan_keseluruhan * sewa_kendaraan
    # print(f"Biaya sewa kendaraan {total_biaya_sewa_kendaraan:,}")
    return total_biaya_sewa_kendaraan

# Fungsi Biaya Peralatan dan Pendukung Lapangan
def peralatan_dan_pendukung_lapangan(jumlah_hari, jumlah_paket, harga_peralatan_dan_pendukung_lapangan):
    total_biaya_peralatan_dan_pendukung = jumlah_hari * jumlah_paket * harga_peralatan_dan_pendukung_lapangan
    # print(f"Total biaya peralatan dan pendukung lapangan: Rp {total_biaya_peralatan_dan_pendukung:,}")
    return total_biaya_peralatan_dan_pendukung

# Fungsi Biaya Sewa Gedung
def sewa_gedung(jumlah_hari, jumlah_paket, harga_paket_sewa_gedung):
    total_biaya_sewa_gedung = jumlah_hari * jumlah_paket * harga_paket_sewa_gedung
    # print(f"Total biaya sewa gedung: Rp {total_biaya_sewa_gedung:,}")
    return total_biaya_sewa_gedung

# Fungsi Biaya Ekspedisi
def biaya_ekspedisi(total_berat, biaya_per_kg, jumlah_hari_pp):
    total_biaya = total_berat * biaya_per_kg * jumlah_hari_pp
    # print("Biaya Ekspedisi:", total_biaya)
    return total_biaya

# Fungsi Biaya Dukungan Teknis Operasional di Lapangan
def dukungan_teknis_operasional_di_lapangan(uang_harian, jumlah_hari, jumlah_orang):
    jumlah_uang_harian_dukungan_teknis = jumlah_hari * jumlah_orang * uang_harian
    # print(f"Total uang harian Dukungan Teknis untuk {provinsi}: Rp {jumlah_uang_harian_dukungan_teknis:,}")
    return jumlah_uang_harian_dukungan_teknis

# Fungsi Biaya Air Mobil Pemadam Kebakaran dan Cuci Pesawat
def air_mobil_pk_cuci_pesawat(jumlah_paket, jumlah_hari, harga_air_cuci_pesawat):
    jumlah_biaya_air_mobil_pk_cuci_pesawat = jumlah_paket * jumlah_hari * harga_air_cuci_pesawat
    # print(f"Total biaya Air Mobil Pemadam Kebakaran dan Cuci Pesawat untuk {provinsi}: Rp {jumlah_biaya_air_mobil_pk_cuci_pesawat:,}")
    return jumlah_biaya_air_mobil_pk_cuci_pesawat

# Fungsi Biaya Ground Handling
def groundhandling(jumlah_paket, jumlah_hari, harga_groundhandling):
    jumlah_biaya_groundhandling = jumlah_hari * harga_groundhandling
    # print(f"Total biaya Ground Handling untuk {provinsi}: Rp {jumlah_biaya_groundhandling:,}")
    return jumlah_biaya_groundhandling

# ============================================================ #
# ==================== Fungsi Jasa Survey ==================== #
# ============================================================ #
def perolehan_data_cuaca_historis(jumlah_paket, jumlah_kali_paket, harga_perolehan_data_cuaca_historis):
    total_harga = jumlah_paket * jumlah_kali_paket * harga_perolehan_data_cuaca_historis
    return total_harga

# Fungsi Jasa Konsultasi Meteorologi dan Klimatologi
def jasa_konsultasi_meteorologi_klimatologi(jumlah_lokasi, jumlah_kali_lokasi, harga_jasa_konsultasi_meteorologi_klimatologi):
    return jumlah_lokasi * jumlah_kali_lokasi * harga_jasa_konsultasi_meteorologi_klimatologi

# Fungsi Jasa Konsultasi Kegiatan Perekayasaan
def jasa_konsultasi_kegiatan_perekayasaan(jumlah_kegiatan, harga_jasa_konsultasi_kegiatan_perekayasaan):
    return jumlah_kegiatan * harga_jasa_konsultasi_kegiatan_perekayasaan

# Fungsi Sistem Teleburning
# jumlah_unit berupa inputan dari user
def sistem_teleburning(jumlah_unit, jumlah_kali_paket, harga_sistem_teleburning):
    jumlah_unit_sistem_teleburning = jumlah_unit
    harga_sistem_teleburning = jumlah_unit_sistem_teleburning * jumlah_kali_paket * harga_sistem_teleburning
    return harga_sistem_teleburning

# Fungsi Gas
def gas(jumlah_paket, jumlah_kali_paket, harga_gas):
    return jumlah_paket * jumlah_kali_paket * harga_gas

# Fungsi Balon Pibal
def balon_pibal(jumlah_paket, jumlah_kali_paket, harga_balon_pibal):
    return jumlah_paket * jumlah_kali_paket * harga_balon_pibal

# Fungsi Bahan Semai Flare untuk Komisioning Instalasi Menara GBG
# sesuaikan jumlah_hari
def bahan_semai_flare(jumlah_unit_sistem_teleburning, jumlah_hari, harga_bahan_semai_flare):
    jumlah_pcs = 2*jumlah_unit_sistem_teleburning
    harga_bahan_semai_flare = jumlah_pcs * jumlah_hari * harga_bahan_semai_flare
    return jumlah_pcs, harga_bahan_semai_flare

# Fungsi Perijinan Bahan Semai Flare untuk Komisioning Instalasi Menara GBG
harga_perijinan_bahan_semai_flare = 200000000 # pindah ke jasa_survey.py
def perijinan_bahan_semai_flare(jumlah_paket, jumlah_kali_paket, harga_perijinan_bahan_semai_flare):
    return jumlah_paket * jumlah_kali_paket * harga_perijinan_bahan_semai_flare

# biaya_sewa_kendaraan_survey_lokasi = biaya_sewa_kendaraan(jh_keseluruhan+3, jumlah_unit_kendaraan_keseluruhan, sewa_kendaraan) # pindah ke jasa_survey.py

# =============================================================== #
# ==================== Fungsi Jasa OMC Darat ==================== #
# =============================================================== #
# Fungsi Tenaga Lokal
def tenaga_lokal(jumlah_personel, jumlah_hari, harga_tenaga_lokal):
    return jumlah_personel * jumlah_hari * harga_tenaga_lokal

def bahan_semai_flare_darat(jumlah_hari, harga_bahan_semai_flare_darat):
    jumlah_pcs=1*jumlah_hari
    total_harga_bahan_semai_flare_darat = jumlah_pcs * jumlah_hari * harga_bahan_semai_flare_darat
    return jumlah_pcs, total_harga_bahan_semai_flare_darat

# =============================================================== #
# ==================== Fungsi Jasa OMC Nirawak ==================== #
# =============================================================== #
# Fungsi Bahan Semai Berbasis Nirawak
def bahan_semai_berbasis_nirawak(jumlah_unit_pesawat_nirawak, jumlah_hari, harga_bahan_semai_berbasis_nirawak):
    jumlah_pcs=4*jumlah_unit_pesawat_nirawak
    total_harga_bahan_semai_berbasis_nirawak = jumlah_pcs * jumlah_hari * harga_bahan_semai_berbasis_nirawak
    return jumlah_pcs, total_harga_bahan_semai_berbasis_nirawak

# Fungsi sewa pesawat nirawak
def sewa_pesawat_nirawak(jumlah_unit_pesawat_nirawak, jumlah_hari, harga_sewa_pesawat_nirawak):
    return jumlah_unit_pesawat_nirawak * jumlah_hari * harga_sewa_pesawat_nirawak

# Fungsi perijinan bahan semai flare # sama kaya di jasa_survey.py

# ========== Kebutuhan Operasional Lapangan ========== #
# Fungsi Sewa Kendaraan # sama kaya di jasa_survey.py

# Fungsi Peralatan dan Pendukung Lapangan Jasa OMC Darat
harga_peralatan_dan_pendukung_lapangan_omc_darat = 4275000 # pindah ke jasa_omc_darat.py
def peralatan_dan_pendukung_lapangan_omc_darat(jumlah_hari, jumlah_paket, harga_peralatan_dan_pendukung_lapangan_omc_darat):
    return jumlah_hari * jumlah_paket * harga_peralatan_dan_pendukung_lapangan_omc_darat

# ========== C. Hasil Layanan Operasional Modifikasi Cuaca Berbasis Wahana Penyemaian Awan dari Darat ========== #
# Fungsi Laporan Kegiatan Pelaksanaan Operasi Modifikasi Cuaca # sama kaya di atas
