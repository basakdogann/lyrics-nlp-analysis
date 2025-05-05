from gensim.models import Word2Vec
import time

# Veriyi yükle
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as f:
    text = f.read()

sentences = [text.split()]  # Tek belge gibi

# Model eğitimi
start = time.time()
model = Word2Vec(
    sentences,
    vector_size=300,
    window=2,
    sg=0,  # CBOW
    min_count=1,
    workers=4
)
end = time.time()

# Modeli kaydet
model.save("word2vec_stemmed_cbow_win2_dim300.model")

print("Model eğitiliyor...")
print(f"Model eğitimi tamamlandı. Süre: {round(end - start, 2)} saniye\n")

# Benzer kelimeleri yazdır
try:
    print("'ask' kelimesine en benzer 5 kelime:")
    for word, score in model.wv.most_similar("ask", topn=5):
        print(f"{word} -> {round(score, 4)}")
except KeyError:
    print("'ask' kelimesi modelde bulunamadı.")
