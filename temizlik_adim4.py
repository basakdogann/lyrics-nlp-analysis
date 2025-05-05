import html
import re

# 1. Dosyayı oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as file:
    metin = file.read()

# 2. HTML karakterlerini çöz (örn. &amp; → &)
metin = html.unescape(metin)

# 3. Özel karakterleri temizle (örn. “…” gibi)
metin = re.sub(r"[^\w\sçğıöşüÇĞİÖŞÜ]", "", metin)

# 4. Fazla boşlukları tek boşluğa indir
metin = re.sub(r"\s+", " ", metin).strip()

# 5. Örnek çıktı göster
print("Temizlenmiş metinden örnek:")
print(metin[:300])  # İlk 300 karakteri yazdır

# 6. Yeni dosyaya yaz
with open("temizlenmis_korpus.txt", "w", encoding="utf-8") as f:
    f.write(metin)
