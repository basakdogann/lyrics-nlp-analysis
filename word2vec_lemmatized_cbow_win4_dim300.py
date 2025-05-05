import time
from gensim.models import Word2Vec

# 1. Eğitim verisini yükle
with open("lemmatize_tokenler.txt", "r", encoding="utf-8") as file:
    tokens = file.read().split()

# 2. Her 1000 kelimeyi bir belge gibi ele alalım
windowed_sentences = [tokens[i:i+1000] for i in range(0, len(tokens), 1000)]

# 3. Model eğitimi
print("Model eğitiliyor...")
start = time.time()

model = Word2Vec(
    sentences=windowed_sentences,
    vector_size=300,
    window=4,
    sg=0,  # CBOW
    min_count=1,
    workers=4,
    epochs=10
)

end = time.time()
print(f"Model eğitimi tamamlandı. Süre: {round(end - start, 2)} saniye")

# 4. Modeli kaydet
model.save("word2vec_lemmatized_cbow_win4_dim300.model")

# 5. Örnek benzer kelimeleri yazdır
print("\n'ask' kelimesine en benzer 5 kelime:")
try:
    for word, score in model.wv.most_similar("ask", topn=5):
        print(f"{word} -> {round(score, 4)}")
except KeyError:
    print("'ask' kelimesi modelde bulunamadı.")
