from google.colab import files
uploaded = files.upload()
EXCEL_PATH = "Excel_Tugas Modul 2.xlsx"
import os
os.makedirs("visualization", exist_ok=True)
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(EXCEL_PATH)
print("===== Preview Data =====")
print(df.head())
print("\nKolom yang tersedia:")
print(df.columns.tolist())
COL_X  = "Aplikasi ini memiliki tampilan yang sederhana dan mudah dipahami"
COL_Y  = "Saya merasa yakin bahwa data pribadi saya dalam aplikasi ini aman"
COL_Z1 = "Fitur-fitur yang tersedia di dalam aplikasi ini telah memenuhi kebutuhan saya dalam membayar pajak kendaraan"
COL_Z2 = "Saya merasa puas dengan pengalaman saya menggunakan aplikasi ini"
COL_Z3 = "Saya bersedia merekomendasikan aplikasi ini kepada orang lain"
COL_USIA   = "Usia"
COL_GENDER = "Jenis Kelamin"
COL_JOB    = "Pekerjaan"
X  = pd.to_numeric(df[COL_X],  errors="coerce")
Y  = pd.to_numeric(df[COL_Y],  errors="coerce")
Z1 = pd.to_numeric(df[COL_Z1], errors="coerce")
Z2 = pd.to_numeric(df[COL_Z2], errors="coerce")
Z3 = pd.to_numeric(df[COL_Z3], errors="coerce")
Z_total = Z1 + Z2 + Z3
data_scores = pd.DataFrame({
    "X_kemudahan": X,
    "Y_keamanan": Y,
    "Z1_fitur": Z1,
    "Z2_pengalaman": Z2,
    "Z3_rekomendasi": Z3,
    "Z_total": Z_total
})

print("\n===== Preview Variabel Skor =====")
print(data_scores.head())
print("\n===== Statistik Deskriptif (X, Y, Z_total) =====")
desc_main = data_scores[["X_kemudahan", "Y_keamanan", "Z_total"]].describe()
print(desc_main)
def summary_with_mode(series, name):
    print(f"\n--- {name} ---")
    print(f"Mean   : {series.mean():.2f}")
    print(f"Median : {series.median():.2f}")
    print(f"Min    : {series.min()}")
    print(f"Max    : {series.max()}")
    mode_vals = series.mode()
    if len(mode_vals) > 0:
        print(f"Mode   : {list(mode_vals.values)}")
    else:
        print("Mode   : (tidak terdefinisi)")

summary_with_mode(X,  "X (Kemudahan Penggunaan)")
summary_with_mode(Y,  "Y (Keamanan Data)")
summary_with_mode(Z_total, "Z_total (Kepuasan Fitur)")
print("\n===== Ringkasan Demografi =====")

def freq_table(col, name):
    print(f"\n--- {name} ---")
    counts = df[col].value_counts(dropna=False)
    perc = df[col].value_counts(normalize=True, dropna=False) * 100
    freq_df = pd.DataFrame({
        "Frekuensi": counts,
        "Persentase (%)": perc.round(1)
    })
    print(freq_df)

freq_table(COL_GENDER, "Jenis Kelamin")
freq_table(COL_USIA,   "Usia")
freq_table(COL_JOB,    "Pekerjaan")
VIS_DIR = "visualization"
os.makedirs(VIS_DIR, exist_ok=True)
def plot_hist(series, title, xlabel, filename, bins=5):
    plt.figure()
    plt.hist(series.dropna(), bins=bins, edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Frekuensi")
    save_path = os.path.join(VIS_DIR, filename)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {save_path}")

print("\n===== Membuat histogram dan menyimpan ke folder visualization/ =====")

plot_hist(X,  "Histogram Kemudahan Penggunaan (X)", "Skor X",  "hist_X.png",  bins=5)
plot_hist(Y,  "Histogram Keamanan Data (Y)",        "Skor Y",  "hist_Y.png",  bins=5)
plot_hist(Z_total, "Histogram Kepuasan Fitur (Z_total)", "Skor Z total", "hist_Z.png", bins=7)

print("\nSelesai! Analisis deskriptif sudah dijalankan dan visualisasi disimpan.")
