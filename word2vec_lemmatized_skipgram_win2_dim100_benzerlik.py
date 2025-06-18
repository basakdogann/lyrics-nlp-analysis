from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Modeli yükle
model = Word2Vec.load("models/word2vec_lemmatized_cbow_win4_dim100.model")

# 2. Giriş cümlesi
giris_cumlesi = "aşk göz git"
giris_tokens = giris_cumlesi.split()

# 3. Giriş cümlesi için ortalama vektör hesapla
giris_vektorler = []
for kelime in giris_tokens:
    if kelime in model.wv:
        giris_vektorler.append(model.wv[kelime])
if not giris_vektorler:
    raise ValueError("Hiçbir kelime modele ait değil.")
giris_ort = np.mean(giris_vektorler, axis=0).reshape(1, -1)

# 4. Korpus cümlelerini yükle
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as f:
    metin = f.read()
cümleler = metin.split("\n")

# 5. Her cümle için ortalama vektör hesapla
sonuclar = []
for cumle in cümleler:
    tokens = cumle.split()
    vektorler = [model.wv[t] for t in tokens if t in model.wv]
    if vektorler:
        ort = np.mean(vektorler, axis=0).reshape(1, -1)
        skor = cosine_similarity(giris_ort, ort)[0][0]
        sonuclar.append((cumle, skor))

# 6. En yüksek 5 sonucu al ve yazdır
en_benzer_5 = sorted(sonuclar, key=lambda x: x[1], reverse=True)[:5]
print("\n📌 Word2Vec (Skip-Gram, win=2, dim=100) ile en benzer 5 cümle:\n")
for cumle, skor in en_benzer_5:
    print(f"{cumle[:120]}... --> Benzerlik Skoru: {skor:.4f}")
