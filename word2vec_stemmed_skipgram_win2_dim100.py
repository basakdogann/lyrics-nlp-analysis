from gensim.models import Word2Vec
import time

# 1. Stemmed veriyi satır satır oku (her satır bir belge gibi)
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

# 2. Satırları kelime listelerine ayır
sentences = [line.strip().split() for line in data if line.strip()]

# 3. Zamanlayıcıyı başlat
start_time = time.time()
print("Model eğitiliyor...")

# 4. Skip-gram modeli tanımla ve eğit
model = Word2Vec(
    sentences=sentences,
    vector_size=100,
    window=2,
    sg=1,  # 1 = Skip-gram
    min_count=1,
    workers=4,
    epochs=10
)

# 5. Modeli kaydet
model.save("word2vec_stemmed_skipgram_win2_dim100.model")

# 6. Süreyi yazdır
duration = time.time() - start_time
print(f"Model eğitimi tamamlandı. Süre: {duration:.2f} saniye\n")

# 7. Örnek benzerlik çıktısı
try:
    similar = model.wv.most_similar("ask", topn=5)
    print("'ask' kelimesine en benzer 5 kelime:")
    for word, score in similar:
        print(f"{word} -> {score:.4f}")
except KeyError:
    print("'ask' kelimesi modelde bulunamadı.")
