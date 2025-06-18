from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = Word2Vec.load("word2vec_stemmed_skipgram_win2_dim100.model")
girdi_cumlesi = "aşk göz git"

with open("stemmed_tokenler.txt", "r", encoding="utf-8") as file:
    cumleler = [line.strip() for line in file.readlines()]

def ortalama_vektor(cumle, model):
    kelimeler = cumle.split()
    vektorler = [model.wv[k] for k in kelimeler if k in model.wv]
    if not vektorler:
        return np.zeros(model.vector_size)
    return np.mean(vektorler, axis=0)

girdi_vektor = ortalama_vektor(girdi_cumlesi, model)

sonuclar = []
for cumle in cumleler:
    vektor = ortalama_vektor(cumle, model)
    skor = cosine_similarity([girdi_vektor], [vektor])[0][0]
    sonuclar.append((cumle, skor))

en_benzer_5 = sorted(sonuclar, key=lambda x: x[1], reverse=True)[:5]

print("📌 Word2Vec (Skip-Gram, win=2, dim=100) ile en benzer 5 cümle:\n")
for cumle, skor in en_benzer_5:
    print(f"{cumle} --> Benzerlik Skoru: {skor:.4f}")
