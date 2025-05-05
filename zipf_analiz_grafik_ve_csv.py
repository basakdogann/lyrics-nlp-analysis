import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Dosya yolları
lemmatized_path = "lemmatize_tokenler.txt"
stemmed_path = "stemmed_tokenler.txt"

# Dosyaları oku
with open(lemmatized_path, "r", encoding="utf-8") as f:
    lemmatized_words = f.read().split()

with open(stemmed_path, "r", encoding="utf-8") as f:
    stemmed_words = f.read().split()

# Veri boyutlarını yazdır
print(f"Lemmatize Boyutu: {os.path.getsize(lemmatized_path)/(1024*1024):.2f} MB")
print(f"Stemmed Boyutu: {os.path.getsize(stemmed_path)/(1024*1024):.2f} MB")

# CSV kayıt
pd.DataFrame({"tokens": lemmatized_words}).to_csv("lemmatize_tokenler.csv", index=False)
pd.DataFrame({"tokens": stemmed_words}).to_csv("stemmed_tokenler.csv", index=False)

# En sık geçen 50 kelime
lemma_counts = Counter(lemmatized_words)
stem_counts = Counter(stemmed_words)

top_lemma = pd.DataFrame(lemma_counts.most_common(50), columns=["word", "frequency"])
top_stem = pd.DataFrame(stem_counts.most_common(50), columns=["word", "frequency"])

# Grafik 1 - Lemmatize edilmiş kelimeler
plt.figure(figsize=(10, 5))
sns.lineplot(x=range(1, 51), y=top_lemma["frequency"], marker="o", color="blue")
plt.title("Zipf Grafiği - Lemmatize Kelimeler")
plt.xlabel("Kelime Sırası (Rank)")
plt.ylabel("Frekans")
plt.grid(True)
plt.tight_layout()
plt.savefig("zipf_lemmatize.png")
plt.show()

# Grafik 2 - Stemmed kelimeler
plt.figure(figsize=(10, 5))
sns.lineplot(x=range(1, 51), y=top_stem["frequency"], marker="o", color="green")
plt.title("Zipf Grafiği - Stemmed Kelimeler")
plt.xlabel("Kelime Sırası (Rank)")
plt.ylabel("Frekans")
plt.grid(True)
plt.tight_layout()
plt.savefig("zipf_stemmed.png")
plt.show()
