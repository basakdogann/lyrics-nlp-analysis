from gensim.models import Word2Vec
import time

# Veriyi oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as file:
    tokens = file.read().split()

# Gensim modeli için her kelime ayrı bir cümle gibi ele alınmalı
sentences = [tokens]

# Eğitim başlat
print("Model eğitiliyor...")
start_time = time.time()

model = Word2Vec(
    sentences,
    vector_size=100,
    window=2,
    sg=1,  # 1 = Skip-gram
    min_count=1,
    workers=4,
    epochs=10
)

# Modeli kaydet
model.save("word2vec_lemmatized_skipgram_win2_dim100.model")

end_time = time.time()
print(f"Model eğitimi tamamlandı. Süre: {round(end_time - start_time, 2)} saniye\n")

# Örnek benzer kelimeleri yazdır
anahtar_kelime = "ask"
if anahtar_kelime in model.wv:
    print(f"'{anahtar_kelime}' kelimesine en benzer 5 kelime:")
    for kelime, benzerlik in model.wv.most_similar(anahtar_kelime, topn=5):
        print(f"{kelime} -> {round(benzerlik, 4)}")
else:
    print(f"'{anahtar_kelime}' kelimesi modelde bulunamadı.")
