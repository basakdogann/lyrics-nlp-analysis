from gensim.models import Word2Vec
import time

# Veriyi oku
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()

sentences = [line.split() for line in data]

# Model eğitimi
start = time.time()
model = Word2Vec(
    sentences,
    vector_size=300,
    window=2,
    min_count=1,
    sg=1,  # Skip-Gram
    workers=4
)
end = time.time()

# Kaydet
model.save("word2vec_lemmatized_skipgram_win2_dim300.model")
print(f"Model eğitimi tamamlandı. Süre: {round(end - start, 2)} saniye")

# Örnek kelimeyle benzerlik testi
try:
    benzerler = model.wv.most_similar("ask", topn=5)
    print("\n'ask' kelimesine en benzer 5 kelime:")
    for kelime, skor in benzerler:
        print(f"{kelime} -> {round(skor, 4)}")
except KeyError:
    print("\n'ask' kelimesi modelde bulunamadı.")
