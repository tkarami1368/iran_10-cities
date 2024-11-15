import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display

# تابع برای نمایش متن فارسی
def farsi(farsi_str):
    return get_display(arabic_reshaper.reshape(farsi_str))

# بارگذاری داده‌های نقشه
shapefile_path = "ne_10m_admin_0_countries.shp"
world_map = gpd.read_file(shapefile_path)

# انتخاب نقشه ایران
iran_map = world_map[world_map['ADMIN'] == 'Iran']

# داده‌های شهرها
data = {
    "City": ["تهران", "مشهد", "اصفهان", "کرج", "شیراز", "تبریز", "قم", "اهواز", "کرمانشاه", "ارومیه"],
    "lat": [35.6892, 36.2605, 32.6525, 35.8400, 29.6103, 38.084, 34.6399, 31.3203, 34.3142, 37.5527],
    "lon": [51.389, 59.6168, 51.6746, 50.9391, 52.5311, 46.2919, 50.8759, 48.6692, 47.065, 45.076],
    "pop": [8780000, 3076000, 1960000, 1600000, 1565000, 1550000, 1270000, 1200000, 946000, 736000],
}
cities = pd.DataFrame(data)

# ترسیم نقشه
fig, ax = plt.subplots(figsize=(10, 10))
iran_map.plot(ax=ax, color="lightgray", edgecolor="black")

# افزودن شهرها
for _, row in cities.iterrows():
    plt.scatter(
        row["lon"], row["lat"], s=row["pop"] / 100000, color="blue", alpha=0.6, edgecolor="k", zorder=5
    )
    plt.text(
        row["lon"] + 0.5,
        row["lat"],
        farsi(row["City"]),
        fontsize=10,
        ha="left",
        color="darkblue",
        zorder=6,
    )

# تنظیمات نهایی
plt.title(farsi("10 شهر بزرگ ایران بر اساس جمعیت"), fontsize=16)
plt.xlabel(farsi("عرض جغرافیایی"), fontsize=12)
plt.ylabel(farsi("طول جغرافیایی"), fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
