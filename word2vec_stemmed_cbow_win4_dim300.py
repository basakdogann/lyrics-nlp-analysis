from gensim.models import Word2Vec
import time

# Veri dosyasını oku
with open("stemmed_tokenler.txt", "r", encoding="utf-8") as file:
    metin = file.read()

# Tokenlara böl
sentences = [metin.split()]  # tüm kelimeler tek bir belge gibi eğitiliyor

# Model eğitimi başlasın
start = time.time()

model = Word2Vec(
    sentences,
    vector_size=300,
    window=4,
    sg=0,  # CBOW
    min_count=1,
    workers=4
)

end = time.time()
print(f"\nModel eğitimi tamamlandı. Süre: {round(end - start, 2)} saniye")

# Modeli kaydet
model.save("word2vec_stemmed_cbow_win4_dim300.model")

# Örnek kelime: "ask" için en benzer kelimeler
print("\n'ask' kelimesine en benzer 5 kelime:")
for kelime, benzerlik in model.wv.most_similar("ask", topn=5):
    print(f"{kelime} -> {round(benzerlik, 4)}")
