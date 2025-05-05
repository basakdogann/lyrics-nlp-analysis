from gensim.models import Word2Vec
import time

# Stemmed veri dosyasını oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Cümleleri oluştur
sentences = [text.split()]  # tüm kelimeleri tek bir cümlede birleştiriyoruz

# Model eğitimi
print("Model eğitiliyor...")
start_time = time.time()
model = Word2Vec(
    sentences,
    vector_size=100,
    window=2,
    sg=0,  # CBOW
    min_count=1,
    workers=4
)
duration = time.time() - start_time
print(f"Model eğitimi tamamlandı. Süre: {duration:.2f} saniye")

# Modeli kaydet
model.save("word2vec_stemmed_cbow_win2_dim100.model")

# Örnek kelime: "ask" varsa en benzerlerini getir
try:
    print("\n'ask' kelimesine en benzer 5 kelime:")
    for word, score in model.wv.most_similar("ask", topn=5):
        print(f"{word} -> {score:.4f}")
except KeyError:
    print("'ask' kelimesi modelde bulunamadı.")
