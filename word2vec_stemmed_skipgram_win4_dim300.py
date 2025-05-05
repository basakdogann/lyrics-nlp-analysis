from gensim.models import Word2Vec
from time import time

# Veri dosyasını oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as f:
    kelimeler = f.read().split()

# Cümlemiş gibi yap: Her 1000 kelime = bir belge (cümle)
sentences = [kelimeler[i:i+1000] for i in range(0, len(kelimeler), 1000)]

# Model parametreleri
params = {
    "vector_size": 300,
    "window": 4,
    "sg": 1,  # skip-gram
    "min_count": 1,
    "workers": 4
}

# Modeli eğit
print("Model eğitiliyor...")
start = time()
model = Word2Vec(sentences, **params)
print(f"Model eğitimi tamamlandı. Süre: {round(time() - start, 2)} saniye")

# Modeli kaydet
model.save("word2vec_stemmed_skipgram_win4_dim300.model")

# Örnek kelime için benzer kelimeleri göster
try:
    benzerler = model.wv.most_similar("ask", topn=5)
    print("\n'ask' kelimesine en benzer 5 kelime:")
    for kelime, skor in benzerler:
        print(f"{kelime} -> {round(skor, 4)}")
except KeyError:
    print("\n'ask' kelimesi modelde bulunamadı.")
